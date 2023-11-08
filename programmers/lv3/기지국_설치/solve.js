// function solution(n, stations, w) {
//   var answer = 0;

//   stations.forEach((item, idx) => {
//     if (idx === 0) {
//       answer += Math.ceil((item - w - 1) / (2 * w + 1));
//       console.log(answer, idx);
//     } else {
//       answer += Math.ceil((item - stations[idx - 1] - 2 * w) / (2 * w + 1));
//       console.log(answer, idx);
//     }
//     if (idx === stations.length - 1) {
//       answer += Math.ceil((n - item - w) / (2 * w + 1));
//       console.log(answer, idx);
//     }
//   });
//   if (stations.length === 0) {
//     // 모든 지역에 새로운 기지국 설치
//     return Math.ceil(n / (2 * w + 1));
//   }

//   return answer;
// }

function solution(n, stations, w) {
  let answer = 0;
  let lastCovered = 0;

  stations.forEach((station, idx) => {
    // 기지국의 왼쪽 커버 범위 계산
    let leftCover = station - w;
    // 아직 커버되지 않은 왼쪽 영역에 필요한 기지국 수 계산
    if (leftCover > lastCovered + 1) {
      answer += Math.ceil((leftCover - (lastCovered + 1)) / (2 * w + 1));
    }
    // 기지국의 오른쪽 커버 범위 업데이트
    lastCovered = station + w;
  });

  // 마지막 기지국 오른쪽 영역에 필요한 기지국 수 계산
  if (lastCovered < n) {
    answer += Math.ceil((n - lastCovered) / (2 * w + 1));
  }

  return answer;
}

console.log(solution(11, [4, 11], 1));
console.log(solution(16, [9], 2));
