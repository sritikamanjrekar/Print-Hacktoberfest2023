//import 'package:flutter/material.dart';

void main() 
{ 
   var n1 = 111; 
   var n2 = 222; 
   var res = 0; 
   var divres = 0.0; 
   
   res = n1+n2; 
   print("Addition: ${res}"); 
   res = n1-n2;
   print("Subtraction: ${res}"); 
   res = n1*n2; 
   print("Multiplication: ${res}"); 
   divres = n1/n2; 
   print("Division: ${res}"); 
   
   res = n1~/n2; 
   print("Division returning Integer: ${res}"); 
   res = n1%n2; 
   print("Remainder: ${res}"); 
   
   n1++; 
   print("Increment: ${n1}"); 
   n2--; 
   print("Decrement: ${n2}"); 
}

//https://www.tutorialspoint.com/compile_dart_online.php
