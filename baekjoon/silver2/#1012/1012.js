// let input = require('fs').readFileSync('input.txt').toString().split('\n')
let input = require('fs').readFileSync('/dev/stdin').toString().split('\n')

var dx = [-1, 1, 0, 0]
var dy = [0, 0, -1, 1]


function solution() {
    let NMK = input[idx++].split(' ')
    let N = Number(NMK[0])
    let M = Number(NMK[1])
    let K = NMK[2]
    let area = Array.from(Array(N), ()=> Array(M).fill(0))
    let visited = Array.from(Array(N), ()=> Array(M).fill(0))
    

    for (let i = 0; i < K; i++) {
        let dummy = input[idx++].split(' ')
        area[Number(dummy[0])][Number(dummy[1])] = 1
    }
    function dfs(x, y) {
        visited[x][y] = 1
        for (let i = 0; i < 4; i++) {
            let nx = x + dx[i]
            let ny = y + dy[i]
            if (nx < 0 || nx > N-1 || ny < 0 || ny > M-1) {
                continue
            }
            if (visited[nx][ny] === 0 && area[nx][ny] == 1) {
                dfs(nx, ny)
            }
        }
    }
    // console.log(area)
    let cnt = 0
    for (let i = 0; i < N; i++) {
        for (let j = 0; j< M; j++){
            if (area[i][j] == 1 && visited[i][j] == 0){
                dfs(i, j)
                cnt = cnt + 1
            }
        }
    }
    
    console.log(cnt)
}


var idx = 1
T = Number(input[0])
for (let tc=0; tc< T;tc++) {
    solution()
}