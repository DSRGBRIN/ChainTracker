// SPDX-License-Identifier: GPL-3.0
pragma solidity > 0.7.2;

contract BC_Track{
    string public Name;
    string public Info;
    address public Owner;
    address public Vehicle;

    struct _data{
        bool stat;
        string url; 
    }
    mapping(uint => _data) public data;  // hour:ipfs link

    modifier onlyOwner() {
        require(msg.sender == Owner, "Not the owner");
        _;
    }

    constructor(string memory _name, string memory _info) {
        Owner = msg.sender;
        Name = _name;
        Info = _info;
    }
    
    function updateVhc(address _vehicle) public onlyOwner {    
        Vehicle = _vehicle;
    }

    function track(uint _hour, string memory _url) public onlyOwner {    
        require(data[_hour].stat == false,"Data is present"); 
        data[_hour].url = _url;
        data[_hour].stat = true;
    }

}