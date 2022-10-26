import 'dart:math';

import 'package:flutter/material.dart';

class Calculator extends StatefulWidget {
  const Calculator({super.key});

  @override
  State<Calculator> createState() => _CalculatorState();
}

class _CalculatorState extends State<Calculator> {
  Widget numButton(String btnText, Color btnColor, Color txtColor) {
    return ElevatedButton(
      onPressed: () => {calculate(btnText)},
      style: ElevatedButton.styleFrom(
        fixedSize: const Size(70, 70),
        shape: const CircleBorder(),
        backgroundColor: btnColor,
      ),
      child: Text(
        btnText,
        style: TextStyle(fontSize: 25, color: txtColor),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.black,
      appBar: AppBar(
        title: const Text("Calculator"),
        backgroundColor: Colors.black,
      ),
      body: Padding(
        padding: const EdgeInsets.symmetric(horizontal: 5),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.end,
          children: [
            Row(
              mainAxisAlignment: MainAxisAlignment.end,
              children: [
                Padding(
                  padding: const EdgeInsets.all(10.0),
                  child: Text(
                    text,
                    textAlign: TextAlign.left,
                    style: const TextStyle(color: Colors.white, fontSize: 80),
                  ),
                ),
              ],
            ),
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: [
                numButton("C", Colors.grey, Colors.white),
                numButton("+/-", Colors.grey, Colors.white),
                numButton("%", Colors.grey, Colors.white),
                numButton("/", Colors.orange, Colors.white),
              ],
            ),
            const SizedBox(
              height: 10,
            ),
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: [
                numButton("7", Colors.grey[850]!, Colors.white),
                numButton("8", Colors.grey[850]!, Colors.white),
                numButton("9", Colors.grey[850]!, Colors.white),
                numButton("X", Colors.orange, Colors.white),
              ],
            ),
            const SizedBox(
              height: 10,
            ),
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: [
                numButton("4", Colors.grey[850]!, Colors.white),
                numButton("5", Colors.grey[850]!, Colors.white),
                numButton("6", Colors.grey[850]!, Colors.white),
                numButton("-", Colors.orange, Colors.white),
              ],
            ),
            const SizedBox(
              height: 10,
            ),
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: [
                numButton("1", Colors.grey[850]!, Colors.white),
                numButton("2", Colors.grey[850]!, Colors.white),
                numButton("3", Colors.grey[850]!, Colors.white),
                numButton("+", Colors.orange, Colors.white),
              ],
            ),
            const SizedBox(
              height: 10,
            ),
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: [
                numButton("0", Colors.grey[850]!, Colors.white),
                numButton("^", Colors.grey[850]!, Colors.white),
                numButton(".", Colors.grey[850]!, Colors.white),
                numButton("=", Colors.orange, Colors.white),
              ],
            ),
            const SizedBox(
              height: 1,
            ),
          ],
        ),
      ),
    );
  }

  // logic
  double firstNumber = 0;
  double secondNumber = 0;
  String result = "";
  String text = "";
  String operation = "";
  String temp = "";

  void calculate(String btnText) {
    if (btnText == "C") {
      result = "";
      firstNumber = 0;
      secondNumber = 0;
    } else if (btnText == "+" ||
        btnText == "-" ||
        btnText == "X" ||
        btnText == "/" ||
        btnText == "^" ||
        btnText == "%") {
      firstNumber = double.parse(text);
      // print(firstNumber);
      result = ("$result$btnText").toString();
      temp = result;
      // print(result);
      operation = btnText;
    } else if (btnText == "=") {
      // secondNumber = int.parse(text);
      // secondNumber = double.parse(text.substring(text.length - 1));
      int length = temp.length;
      secondNumber = double.parse(text.substring(length));
      // var listName = text.split("");
      // print(listName);
      // secondNumber = double.parse(listName[listName.length - 1]);
      // print(secondNumber);

      if (operation == "+") {
        result = (firstNumber + secondNumber).toString();
      }
      if (operation == "-") {
        result = (firstNumber - secondNumber).toString();
        // print(result);
      }
      if (operation == "X") {
        result = (firstNumber * secondNumber).toString();
      }
      if (operation == "/") {
        result = (firstNumber / secondNumber).toString();
      }
      if (operation == "^") {
        result = (pow(firstNumber, secondNumber)).toString();
      }
      if (operation == "%") {
        result = ((firstNumber * secondNumber) / 100).toString();
      }
    } else {
      result = ("$text$btnText").toString();
      // print(result);
    }

    setState(() {
      text = result;
    });
  }
}
