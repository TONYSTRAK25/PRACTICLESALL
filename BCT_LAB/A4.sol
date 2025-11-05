// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract StudentData {
    
    struct Student {
        uint256 id;
        string name;
        uint8 age;
    }

    Student[] public students;

    function addStudent(uint256 _id, string memory _name, uint8 _age) public {
        students.push(Student(_id, _name, _age));
    }

    function getStudent(uint256 index) public view returns (uint256, string memory, uint8) {
        require(index < students.length, "Invalid index");
        Student memory s = students[index];
        return (s.id, s.name, s.age);
    }

    fallback() external payable {
    }

    receive() external payable {}
}
