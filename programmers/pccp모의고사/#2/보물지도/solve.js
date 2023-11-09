const dx = [1, -1, 0, 0];
const dy = [0, 0, 1, -1];

function solution(n, m, hole) {
  const matrix = Array.from({ length: n + 1 }, () => Array(m + 1).fill(0));
  const visited = Array.from({ length: n + 1 }, () =>
    Array.from({ length: m + 1 }, () => Array(2).fill(0))
  );

  hole.forEach((item) => {
    const [a, b] = item;
    matrix[a][b] = 1;
  });

  const queue = [[1, 1, 0]];
  while (queue.length > 0) {
    const [x, y, check] = queue.shift();
    if (x === m && y === n) {
      return visited[x][y][check];
    }
    for (let i = 0; i < 4; i++) {
      const nx = x + dx[i];
      const ny = y + dy[i];
      if (
        0 < nx &&
        nx < n + 1 &&
        0 < ny &&
        ny < m + 1 &&
        visited[nx][ny][check] === 0
      ) {
        if (matrix[nx][ny] === 0) {
          queue.push([nx, ny, check]);
          visited[nx][ny][check] += visited[nx][ny][check] + 1;
        }
        if (check === 0 && matrix[nx][ny] === 1) {
          queue.push([nx, ny, 1]);
          visited[nx][ny][1] = visited[nx][ny][check];
        }
      }
    }
    console.log(visited);
  }

  return -1;
}

solution(4, 4, [
  [2, 3],
  [3, 3],
]);
