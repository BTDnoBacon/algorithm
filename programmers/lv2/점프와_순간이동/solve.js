// function solution(n) {
//   const location = Array.from({ length: n + 1 }, (_, idx) => idx);

//   location.forEach((item, idx) => {
//     if (idx > 0) {
//       location[idx + 1] = Math.min(item + 1, location[idx + 1]);
//     }
//     if (idx * 2 < location.length) {
//       location[idx * 2] = Math.min(item, location[idx * 2]);
//     }
//   });
//   console.log(location[n]);

//   return location[n];
// }

// function solution(n) {
//   const visited = Array.from({ length: n + 1 }).fill(0);
//   const queue = [1];
//   visited[1] = 1;
//   while (queue.length > 0) {
//     let num = queue.shift();
//     if (num * 2 < n + 1 && visited[num * 2] === 0) {
//       queue.push(num * 2);
//       visited[num * 2] = visited[num];
//     }
//     if (num + 1 < n + 1 && visited[num + 1] === 0) {
//       queue.push(num + 1);
//       visited[num + 1] = visited[num] + 1;
//     }
//   }
//   return visited[n];
// }

function solution(n) {
  let answer = 0;
  while (n > 0) {
    if (n % 2 > 0) {
      n = n - 1;
      answer++;
    } else {
      n /= 2;
    }
  }
  // console.log(answer);
  return answer;
}

solution(5000);
