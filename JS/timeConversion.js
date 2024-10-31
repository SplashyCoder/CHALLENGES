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
 * Complete the 'timeConversion' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts STRING s as parameter.
 */

function timeConversion(s) {
  let newS = [];
  for (let i = 0; i < s.length; i++) {
    newS.push(s[i]);
  }
  let hourZone = s[s.length - 2];

  const [first, second, ...rest] = newS;
  let hour = Number(first + second);

  const transform = (hourZone, hour, newS) => {
    if (hourZone == "P" && hour != 12) {
      let newHour = hour + 12;
      newS.shift();
      newS.shift();
      newS.unshift(newHour);
      newS.pop();
      newS.pop();
      let answ = newS.toString();
      let noComas = answ.replaceAll(",", "");
      return noComas;
    }
    if ((hourZone == "P" && hour == 12) || (hourZone == "A" && hour != 12)) {
      newS.pop();
      newS.pop();
      let answ = newS.toString();
      let noComas = answ.replaceAll(",", "");
      return noComas;
    }
    if (hourZone == "A" && hour == 12) {
      let newHour = "00";
      newS.shift();
      newS.shift();
      newS.unshift(newHour);
      newS.pop();
      newS.pop();
      let answ = newS.toString();
      let noComas = answ.replaceAll(",", "");
      return noComas;
    }
  };
  return transform(hourZone, hour, newS);
}

function main() {
  const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

  const s = readLine();

  const result = timeConversion(s);

  ws.write(result + "\n");

  ws.end();
}
