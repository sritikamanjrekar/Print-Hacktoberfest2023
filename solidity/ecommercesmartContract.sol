//SPDX-License-Identifier:UNLICNSED

pragma solidity ^0.5.0;

contract ecommerce{

    struct Product{
        string title;
        string des;
        address payable seller;
        uint ProductID;
        uint Price;
        address buyer;
        bool delivered;

    }

    uint public count=1;

    event registered(string title,uint ProductID,address seller);
    event buyer(uint ProductID,address buyer);
    event delivered(uint ProductID);


       Product[] public products;
       function reigisterproduct(string memory _title,string memory _des,uint _price) public{
           require(_price>0,"Price should be greater than Zero");
           Product memory tempproduct;
           tempproduct.title=_title;
           tempproduct.des=_des;
           tempproduct.Price=_price*10**18;
           tempproduct.seller=msg.sender;
           tempproduct.ProductID=count;

           products.push(tempproduct);
           count++;
           emit registered(_title,tempproduct.ProductID,msg.sender);

}

function buy(uint _productid) payable public{
    require(products[_productid-1].Price==msg.value,"Please pay exact amount");
    require(products[_productid-1].seller!=msg.sender,"Seller cannnot be the Buyer");
    products[_productid-1].buyer=msg.sender;
    emit buyer(_productid,msg.sender);

}

function delivery(uint _productid) public{
     require(products[_productid-1].buyer==msg.sender,"Only Buyer can confirm this");
     products[_productid-1].delivered=true;
     products[_productid-1].seller.transfer(products[_productid-1].Price);
     emit delivered(_productid);

}



}