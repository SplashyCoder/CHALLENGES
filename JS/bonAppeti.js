"use strict";

process.stdin.resume();
process.stdin.setEncoding("utf-8");

let inputString = "";
let currentLine = 0;

process.stdin.on("data", function (inputStdin) {
  inputString += inputStdin;
});

process.stdin.on("end", function () {
  inputString = inputString.split("\n");

  main();
});

function readLine() {
  return inputString[currentLine++];
}

/*
 * Complete the 'bonAppetit' function below.
 *
 * The function accepts following parameters:
 *  1. INTEGER_ARRAY bill
 *  2. INTEGER k
 *  3. INTEGER b
 */

function bonAppetit(bill, k, b) {
  const arrStart = bill.slice(0, k);
  const arrEnd = bill.slice(k + 1);

  const arrSum = (arr) => {
    let counter = 0;
    for (let i = 0; i < arr.length; i++) {
      counter += arr[i];
      //console.log(counter)
    }
    return counter;
  };

  const arrStartSum = arrSum(arrStart);
  const arrEndSum = arrSum(arrEnd);

  //console.log(bill, arrStart, arrEnd)
  //console.log(arrStartSum, arrEndSum)
  //console.log(arrStartSum + arrEndSum)
  if ((arrEndSum + arrStartSum) / 2 == b) {
    console.log("Bon Appetit");
  } else {
    console.log(Math.abs((arrEndSum + arrStartSum) / 2 - b));
  }
}

function main() {
  const firstMultipleInput = readLine().replace(/\s+$/g, "").split(" ");

  const n = parseInt(firstMultipleInput[0], 10);

  const k = parseInt(firstMultipleInput[1], 10);

  const bill = readLine()
    .replace(/\s+$/g, "")
    .split(" ")
    .map((billTemp) => parseInt(billTemp, 10));

  const b = parseInt(readLine().trim(), 10);

  bonAppetit(bill, k, b);
}
