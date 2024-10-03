import sys
import time
import asyncio
import hashlib
import json
from ipfs_module import create_ipfs
from gps_wuling import get_gps
from cryptolib import AESCipher
from contract_sender import call_tracking
from abi_code import TRACK_ABI
from auto_map import HEADER0, HEADER1, HEADER2, HEADER3, FOOTER1

ACCOUNT_NAME = "Car_001"
SK_GENESIS = sys.argv[1]
IPFS_PERIOD = 6  # 6 seconds
BC_PERIOD = 10  # 10 X of IPFS PERIOD = 1 minute
CTR_BC = 0
RUN = True
SAMPLE = 12
LAST_INDEX = 0
TIME_INDEX = 0
ipfs_db = {}

BC_NET = "celo"
P_C_ADR = "0xeCE741E83a69ee075ECdd223e2AE6B26805B4D30"
C_C_ADR = "0x2807fe5aff1b0EE81108D8295631a61fDA80037f"
U_ADR = "0x9073e1dc12f0f44E1af024D00e047990Dd7a9e76"
U_KEY = "2df21f58103f990a96eab0409b102f850cef477b295d5e2d943279377606e644"

MAIN_CTR = 0
log_time = []
TTS_BC = False

TEST_ROUND = 21  # 20


def read_ipfs_db():
    """
    reload the recorded ipfs data from local disk
    """
    lines = []
    with open("ipfs.track", "r", encoding="utf-8") as fr:
        lines = fr.readlines()

    for line in lines:
        buf = line.split(":")
        v = buf[1][:-1]
        k = buf[0].split("_")[0]
        ipfs_db[k] = v
    print(ipfs_db)


read_ipfs_db()


async def update_map(gps_data):
    """
    Update auto_map.html using the recent GPS data
    """
    file_str = HEADER0 + str(IPFS_PERIOD) + HEADER1 + gps_data[-1] + HEADER2 + gps_data[-1] + HEADER3 + "\n"
    for i in range(len(gps_data)):
        file_str += "                new google.maps.LatLng("+gps_data[i]+"),\n"
    file_str += FOOTER1

    with open("auto_map.html", "w", encoding="utf-8") as fw:
        fw.write(file_str)


async def get_gps_data():
    """
    Generate gps data in asyncronous manner
    """
    global LAST_INDEX
    gps_data, LAST_INDEX = get_gps(SAMPLE, LAST_INDEX)
    await update_map(gps_data)
    buffer = "\n".join(gps_data)
    # print(buffer)
    return buffer


async def gen_pwd():
    """
    Generate password for each data segment
    """
    global TIME_INDEX
    TIME_INDEX = str(int(time.time() // IPFS_PERIOD))
    pwd_plain = SK_GENESIS + "_" + TIME_INDEX
    print(pwd_plain)
    pwd_hash = hashlib.sha256(pwd_plain.encode('utf-8')).hexdigest()
    print(pwd_hash)
    return pwd_hash


async def enc_aes(str_loc_data, gps_pwd):
    """
    Generate password for each data segment
    """
    # print(str_loc_data)
    print(gps_pwd)
    aes = AESCipher(gps_pwd)
    enc_data = aes.encrypt(str_loc_data)
    # print(enc_data)
    final_data = {
        "index": TIME_INDEX,
        "periode": str(IPFS_PERIOD),
        "name": ACCOUNT_NAME,
        "data": enc_data,
    }
    submit_data = json.dumps(final_data, indent=4)
    # print(submit_data)
    return submit_data


async def submit_ipfs(format_name, submit_data, is_bundle=False):
    """
    Generate password for each data segment
    """
    print(submit_data)
    hashval = create_ipfs(format_name, submit_data)
    print(hashval)

    if is_bundle:
        return hashval
    else:
        ipfs_db[TIME_INDEX] = hashval
        with open("ipfs.track", "a", encoding="utf-8") as fw:
            fw.write(TIME_INDEX + "_" + str(IPFS_PERIOD) + ".track" + ":" + hashval + "\n")


async def send_bc(bc_index, ipfs_url):
    """
    Generate password for each data segment
    """
    param_function = []
    param_function.append(bc_index)
    param_function.append(ipfs_url)
    if BC_NET == "celo":
        trx_hash = call_tracking("celo", C_C_ADR, TRACK_ABI, U_ADR, U_KEY, param_function)
    elif BC_NET == "polygon":
        trx_hash = call_tracking("polygon", P_C_ADR, TRACK_ABI, U_ADR, U_KEY, param_function)
    return trx_hash


async def gen_ipfs():
    """
    Generate IPFS url
    """
    global last, CTR_BC
    print("::gen_ipfs::")
    loc_data = await get_gps_data()
    pwd = await gen_pwd()

    # print(loc_data, pwd)
    submit_data = await enc_aes(loc_data, pwd)

    format_name = TIME_INDEX + "_" + str(IPFS_PERIOD) + ".track"
    await asyncio.gather(
        submit_ipfs(format_name, submit_data)
    )
    CTR_BC += 1


async def gen_trx_bc(time_x=0):
    """
    Generate IPFS url
    t_index : timestamp // IPFS_PERIOD
    """
    global TTS_BC
    print("::trx_bc::", TTS_BC)
    if not TTS_BC:
        return
    else:
        TTS_BC = False
    print("sending to BC")
    if time_x == 0:
        t_index = int(time.time()) // IPFS_PERIOD
    else:
        t_index = time_x
    bc_index = t_index // BC_PERIOD

    start_index = t_index - BC_PERIOD
    print(t_index, start_index, BC_PERIOD)
    ipfs_list = []
    for i in range(start_index, t_index):
        if str(i) in ipfs_db:
            ipfs_list.append(ipfs_db[str(i)])

    print("====================")
    print(ipfs_list)
    print("====================")

    bundle_data = {
        "index": str(bc_index),
        "periode": str(BC_PERIOD),
        "name": ACCOUNT_NAME,
        "data": ";".join(ipfs_list),
    }
    submit_data = json.dumps(bundle_data, indent=4)
    format_name = str(bc_index) + "_" + str(BC_PERIOD) + "_" + str(IPFS_PERIOD) + ".bundle"
    print(str(bc_index), format_name)

    url = await submit_ipfs(format_name, submit_data, True)
    trx_hash = await send_bc(bc_index, url)
    print(url, trx_hash)


async def main_loop():
    """
    The main loop
    """
    global MAIN_CTR, CTR_BC, RUN, log_time, TTS_BC
    while RUN:
        print(MAIN_CTR, CTR_BC, TTS_BC)
        # asyncio.run(gen_trx_bc(287845955))
        # exit()
        await asyncio.gather(
            asyncio.sleep(IPFS_PERIOD),
            gen_ipfs(),
            gen_trx_bc()
        )
        # time.sleep(IPFS_PERIOD)  # discarded
        MAIN_CTR += 1
        log_time.append([MAIN_CTR, time.time()])
        if MAIN_CTR > TEST_ROUND:
            RUN = False

        if CTR_BC >= BC_PERIOD:
            CTR_BC = 0
            TTS_BC = True
    print(log_time)


asyncio.run(main_loop())
