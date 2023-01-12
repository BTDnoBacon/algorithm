const fs = require('fs');
const input = fs.readFileSync("./example.txt").toString().trim().split(/\s/);
const inputOne = input.slice(0,3);
const inputTwo = input.slice(3, );

var N = inputOne[0]
var K = inputOne[1]
var M = inputOne[2]
var L = []

var P = -1

for (let i = 0; i < N; i++) {
    let kimbab = inputTwo[i]
    let a = kimbab - K
    let b = K*2
    if (kimbab > b ) {
        L.push(kimbab-b)
    }
    if (a>0 && kimbab <b) {
        L.push(kimbab-K)
    }
}
console.log(L)

if (L.length == 0) {
    return console.log(P)
}

var left = 1
var right = Math.max(...L)

while (left <= right) {
    let c = left + right
    let mid = Math.floor(c/2)
    let sum = 0
    L.forEach((item)=> {
        sum += Math.floor(item/mid)
    })
    if (sum < M) {
        right = mid - 1
    } else {
        left = mid + 1
        P = mid
    }
}
console.log(P)