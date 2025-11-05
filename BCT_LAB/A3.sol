// SPDX-License-Identifier: Bhide License
pragma solidity ^0.8.0;

contract Bank {
    mapping(address => uint256) private balances;

    function createAccount() public {
        balances[msg.sender] = 0;
    }

    function deposit(uint256 amount) public payable {
        balances[msg.sender] += amount;
    }

    function withdraw(uint256 amount) public {
        require(balances[msg.sender] >= amount, "Insufficient balance");
        balances[msg.sender] -= amount;
    }

    

    function getBalance() public view returns (uint256) {
        return balances[msg.sender];
    }
}