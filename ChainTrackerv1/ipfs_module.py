"""
module for IPFS operations
"""
import sys
import json
import requests  # type: ignore

API_KEY = "2O36yUDHVTBHJga57QT6CYeUu6k"
API_KEY_SCR = "60c6a4a188b428f5036716c3c72638d5"

API_KEY2 = "4ae814529fcf43ddb3eec654d77c5578"
API_KEY_SCR2 = "1557d72acb6c4e62a68f8e6faac886d8"


def create_ipfs(name="vid", data="-"):
    """
    create a new IPFS recrod with name and vid
    vid type: store serialized context
    vdt type: store serialized vector data
    """
    print("generating IPFS")
    files = {name: data}
    # response = requests.post('https://ipfs.infura.io:5001/api/v0/add',
    # files=files, auth= (API_KEY, API_KEY_SCR) )
    response = requests.post('https://secure-nft.infura-ipfs.io:5001/api/v0/add',
                             files=files, auth=(API_KEY2, API_KEY_SCR2), timeout=10)
    # print(response.text)
    dt = json.loads(response.text)
    
    # print(data)
    print("IPFS generated")
    print(dt)
    for k in dt:
        print(k, dt[k])
    return dt['Hash']


def pin_data(hashstr):
    """
    Manually pin IPFS URL
    """
    params = {('arg', hashstr)}
    response = requests.post('https://ipfs.infura.io:5001/api/v0/pin/add',
                             params=params, auth=(API_KEY, API_KEY_SCR), timeout=10)
    print(response.json())


def read_ipfs_new(hashstr):
    """ 
    Read the IPFS URL using infura service
    """
    url = "https://super-nft.infura-ipfs.io/ipfs/"+hashstr
    response = requests.get(url, allow_redirects=True, timeout=10)
    # print(response.text)
    return response.text


def read_ipfs(hashstr):
    """
    Read the IPFS URL using ipfs.io service
    """
    # url = "https://ipfs.io/ipfs/"+hashstr
    url = "https://ipfs.infura.io:5001/api/v0/get?arg="+hashstr
    response = requests.get(url, allow_redirects=True, timeout=10)
    # print(response.text)
    return response.text


def list_ipfs():
    """
    list IPFS url, not recommended!!
    """
    # params = { ('arg', hashstr), }
    response = requests.post('https://ipfs.infura.io:5001/api/v0/pin/ls',
                             auth=(API_KEY, API_KEY_SCR), timeout=10)
    # response = requests.post('https://ipfs.infura.io:5001/api/v0/pin/ls',
    #   params=params, auth= (API_KEY, API_KEY_SCR)  )
    print(response.json())


def test_1():
    """
    for testing only
    """
    if sys.argv[1] == "1":
        # files = { 'file': 'C:\Users\akbar\OneDrive\Documents\_Keltian\2023\PPRM_PB\mytext.txt' }
        files = {'file': 'E:/mytext.txt'}
        response = requests.post('https://ipfs.infura.io:5001/api/v0/add',
                                 files=files, auth=(API_KEY, API_KEY_SCR), timeout=10)
        # response = requests.post('https://secure-nft.infura-ipfs.io/api/v0/add',
        #   files=files, auth= (API_KEY, API_KEY_SCR) )
        print(response.text)
    elif sys.argv[1] == "2":
        params = (('arg', 'QmQEad5bCsxipkJps3fiKR5MZLZgxmgwNagkYTXXd4o69o'))
        # response = requests.post('https://ipfs.infura.io:5001/api/v0/dag/get',
        #   params=params, auth= (API_KEY, API_KEY_SCR) )
        # response = requests.post('https://ipfs.infura.io:5001/api/v0/block/stat',
        #   params=params, auth= (API_KEY, API_KEY_SCR) )
        response = requests.post('https://ipfs.infura.io:5001/api/v0/block/get',
                                 params=params, auth=(API_KEY, API_KEY_SCR), timeout=10)
        # response = requests.post('https://ipfs.infura.io:5001/api/v0/get',
        #   params=params, auth= (API_KEY, API_KEY_SCR) )
        # response = requests.post('https://ipfs.infura.io:5001/api/v0/cat',
        #   params=params, auth= (API_KEY, API_KEY_SCR) )
        print(response.text)

    else:
        # hashval = sys.argv[1]
        # import requests
        params = {
            ('arg', 'QmQEad5bCsxipkJps3fiKR5MZLZgxmgwNagkYTXXd4o69o'),
            }
        response = requests.post('https://ipfs.infura.io:5001/api/v0/pin/add',
                                 params=params, auth=(API_KEY, API_KEY_SCR), timeout=10)
        print(response.json())


if __name__ == "__main__":
    # readIPFS('QmQEad5bCsxipkJps3fiKR5MZLZgxmgwNagkYTXXd4o69o')
    list_ipfs()

    # hv = cerateIPFS("vid","aloha")
    # print("hv:",hv)
    # read_ipfs(hv)
