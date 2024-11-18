"use strict";

const fs = require("fs");

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
 * Complete the 'pickingNumbers' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts INTEGER_ARRAY a as parameter.
 */

function pickingNumbers(a) {
  const aSorted = a.sort();
  console.log(aSorted);
  const subArrays = [];
  let numbersCounter = 0;
  let sliceSince = 0;

  for (let i = 0; i < aSorted.length; i++) {
    console.log(i, aSorted[i]);
    if (aSorted[i] == 3) {
      i = 1;

      console.log("i=1");
    }
  }

  /*
    for( let i = 0 ; i < aSorted.length ; i++ ){
        console.log(i)
        console.log(aSorted[i],aSorted[i+1])
         if(Math.abs(aSorted[i]-aSorted[i+1])<=1){
             console.log('enter')
             
             if(aSorted[i]!=aSorted[i+1]){
                 numbersCounter+=1
                 console.log('countr',numbersCounter)
             }
             
             if(sliceSince = 0){
                 sliceSince = i
             }
             
             if(numbersCounter > 1){
                 console.log('slice')
                 subArrays.push(aSorted.slice(sliceSince,i+1))
                 sliceSince = i
                 numbersCounter = 0
             }
             
             if(i = aSorted.length){
                  subArrays.push(aSorted.slice(i-1,i+i))
             }
             
         }
    }
    */
  console.log(subArrays);
}

function main() {
  const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

  const n = parseInt(readLine().trim(), 10);

  const a = readLine()
    .replace(/\s+$/g, "")
    .split(" ")
    .map((aTemp) => parseInt(aTemp, 10));

  const result = pickingNumbers(a);

  ws.write(result + "\n");

  ws.end();
}
