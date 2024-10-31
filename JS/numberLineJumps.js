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

function kangaroo(x1, v1, x2, v2) {
  let position1 = x1;
  let position2 = x2;

  if (x1 == x2 && v1 != v2) {
    return "NO";
  }

  if (x1 < x2 && v1 < v2) {
    return "NO";
  }
  let p1 = x1;
  let p2 = x2;

  for (let i = 0; i < 9999; i++) {
    p1 = p1 + v1;
    p2 = p2 + v2;

    if (p1 == p2) {
      return "YES";
    }
  }
  return "NO";
}

function main() {
  const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

  const firstMultipleInput = readLine().replace(/\s+$/g, "").split(" ");

  const x1 = parseInt(firstMultipleInput[0], 10);

  const v1 = parseInt(firstMultipleInput[1], 10);

  const x2 = parseInt(firstMultipleInput[2], 10);

  const v2 = parseInt(firstMultipleInput[3], 10);

  const result = kangaroo(x1, v1, x2, v2);

  ws.write(result + "\n");

  ws.end();
}
