"""
Module for testing, verification, and manual licensing
"""
import sys
import time
import json
import hashlib
from ipfs_module import read_ipfs_new
from cryptolib import AESCipher
from gps_wuling import get_gps
from auto_map import HEADER0, HEADER1, HEADER2, HEADER3, FOOTER1
from contract_sender import call_data
from abi_code import TRACK_ABI


def update_map(ipfs_period, gps_data):
    file_str = HEADER0 + str(ipfs_period) + HEADER1 + gps_data[-1] + HEADER2 + gps_data[-1] + HEADER3 + "\n"
    for i in range(len(gps_data)):
        file_str += "                new google.maps.LatLng("+gps_data[i]+"),\n"
    file_str += FOOTER1

    with open("auto_map.html", "w", encoding="utf-8") as fw:
        fw.write(file_str)


mode = int(sys.argv[1])

if mode == 1:  # read ipfs
    data = read_ipfs_new(sys.argv[2])
    print(data)

elif mode == 0:
    """
    Get tracking recap from blockchain
    params: network, sc_adr, time_index
    network: celo or polygon
    s_adr: 0x2807fe5aff1b0EE81108D8295631a61fDA80037f  0xeCE741E83a69ee075ECdd223e2AE6B26805B4D30
    celo: 28787476 28787477
    polygon: 28786120 28786121
    """
    call_data(sys.argv[2], sys.argv[3], TRACK_ABI, int(sys.argv[4]))

elif mode == 2:
    """
    Get IPFS data
    params: ipfs
    """
    dt = read_ipfs_new(sys.argv[2])
    data = json.loads(dt)
    print(data)
elif mode == 20:
    """
    Get tracking recap from blockchain
    and read all of the IPFS URL
    params: network, sc_adr, time_index
    """
    dt = call_data(sys.argv[2], sys.argv[3], TRACK_ABI, int(sys.argv[4]), True)
    print(dt)
    print(dt[1])
    dt2 = read_ipfs_new(dt[1])
    print(dt2)
    data = json.loads(dt2)
    print(data)
    list_url = data["data"].split(";")
    print(list_url)
    for url in list_url:
        buf = json.loads(read_ipfs_new(url))
        print(buf["index"])
        # print(read_ipfs_new(url))
    # print(data)

elif mode == 40:
    """
    Get tracking recap from blockchain, download all ipfs urls
    and generate the password for each IPFS url
    params: network, sc_adr, time_index, secret-key
    """
    dt = call_data(sys.argv[2], sys.argv[3], TRACK_ABI, int(sys.argv[4]), True)
    print(dt)
    print(dt[1])
    dt2 = read_ipfs_new(dt[1])
    print(dt2)
    data = json.loads(dt2)
    print(data)
    list_url = data["data"].split(";")
    print(list_url)
    for url in list_url:
        buf = json.loads(read_ipfs_new(url))
        print(buf["index"])
        _pwd = sys.argv[5]
        pwd_plain = _pwd + "_" + buf["index"]
        pwd = hashlib.sha256(pwd_plain.encode('utf-8')).hexdigest()
        # print(pwd)
        aes2 = AESCipher(pwd, True)
        dec_data = aes2.decrypt(buf["data"])
        # print(data["data"])
        print(dec_data)
    # print(data)

elif mode == 4:
    """
    Get and decrypt IPFS data
    params: ipfs, pwd, time_index
    """
    dt = read_ipfs_new(sys.argv[2])
    data = json.loads(dt)
    _pwd = sys.argv[3]
    pwd_plain = _pwd + "_" + sys.argv[4]
    print(data)
    print(pwd_plain)
    pwd = hashlib.sha256(pwd_plain.encode('utf-8')).hexdigest()
    print(pwd)
    aes2 = AESCipher(pwd)
    dec_data = aes2.decrypt(data["data"])
    print(data["data"])
    print(dec_data)

elif mode == 3:  # reload web
    # read ipfs, decrypt file
    # ROUND = 20
    SAMPLE = 10
    ctr = 0
    IPFS_PERIOD = 6
    last_index = int(sys.argv[2])
    # while ctr < ROUND:

    while True:
        time.sleep(IPFS_PERIOD)

        gps_data, last_index = get_gps(SAMPLE, last_index)
        print(gps_data)
        print(last_index)

        update_map(IPFS_PERIOD, gps_data)
        # file_str = HEADER0 +str(IPFS_PERIOD)+ HEADER1 + gps_data[-1] + HEADER2 + gps_data[-1] + HEADER3 + "\n"
        # for i in range(len(gps_data)):
        #     file_str += "                new google.maps.LatLng("+gps_data[i]+"),\n"
        # file_str += FOOTER1
        # with open("auto_map.html", "w", encoding="utf-8") as fw:
        #         fw.write(file_str)

    # gmap1 = gmplot.GoogleMapPlotter(latitude_list[-1], longitude_list[-1], 13, title="BIoV Tracker", apikey="AIzaSyDpnuP0pRGFFN9agYXHWrpRWuAHG79ai5E")
    # lastlat = [latitude_list[-1]]
    # lastlon = [longitude_list[-1]]
    # gmap1.scatter(lastlat, lastlon, size=40, marker=True)
    # gmap1.plot(latitude_list, longitude_list,  'cornflowerblue', edge_width=2.5)
    # # gmap1.draw("/home/biov/templates/automap.html")
    # gmap1.draw("automap.html")
    # # self.browser.page().settings().setAttribute(QWebEngineSettings.LocalContentCanAccessRemoteUrls, True)
    # # self.browser.setUrl(QUrl.fromLocalFile("/home/biov/Downloads/code_map/map.html"))
    # # return "/home/biov/templates/automap.html"
    # return "automap.html"

# fda0bf409c08d2426ed59753200cabe1f0c9f2447c96673428de41f6c2edaf1a
# fda0bf409c08d2426ed59753200cabe1f0c9f2447c96673428de41f6c2edaf1a

# QmUYL8BDk7VnAZGDsBvhTiDAkDja9bpbjJEu9YRXowtB8j
# data = read_ipfs_new("QmV8r3YEKJiTbBPe54Sc8LiCYfyeihGCurWySPSpP6vg4X")

sys.exit()
