// SPDX-License-Identifier

 pragma solidity 0.8.17; 

  contract NameJohn{
   address public John;
   
   function getName() public view returns (string memory){
       return "My name is John Fawole, I am Contributing in Hacktober Open Source Project";
   }
  }