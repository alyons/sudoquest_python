let currentExp = 0;

let headers = ["Level", "XP Required", "Total XP"];
let longestString = Math.max(headers[0].length, headers[1].length, headers[2].length);
let rows = [];

// console.log(`Longest String Length: ${longestString}`);

const padString = (text, padChar = " ") => {
  let out = text;
  while(out.length < longestString) {
    out += padChar;
  }
  return out;
};

let totalExp = [];

for(let i = 1; i < 100; i++) {
  totalExp.push(currentExp);
  currentExp += i * 500;  
}

for(let l = -1; l < 34; l++) {
  if (l == -1) {
    rows.push(`|${padString(headers[0])}|${padString(headers[1])}|${padString(headers[2])}|${padString(headers[0])}|${padString(headers[1])}|${padString(headers[2])}|${padString(headers[0])}|${padString(headers[1])}|${padString(headers[2])}|`);
  } else if (l == 0) {
    rows.push("|:---------:|:---------:|:---------:|:---------:|:---------:|:---------:|:---------:|:---------:|:---------:|")  
  } else {
    rows.push(`|${padString(l + "")}|${padString((l * 500) + "")}|${padString(totalExp[l-1] + "")}|${padString((l + 33) + "")}|${padString(((l + 33) * 500) + "")}|${padString(totalExp[l+32] + "")}|${padString((l + 66) + "")}|${padString(((l + 66) * 500) + "")}|${padString(totalExp[l+65] + "")}|`);
  }
}

// rows.forEach(r => {
//   console.log(r);
// });


for(let i = 1; i < 100; i += 4) {
  console.log(i);
}