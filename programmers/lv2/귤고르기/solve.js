function solution(k, tangerine) {
  var answer = 0;
  const typeTangerineCount = {};

  // 각 귤의 개수를 계산합니다.
  tangerine.forEach((num) => {
    if (!typeTangerineCount[num]) {
      typeTangerineCount[num] = 0;
    }
    typeTangerineCount[num]++;
  });

  // 귤의 개수만 추출하여 정렬합니다.
  const arr = Object.values(typeTangerineCount).sort((a, b) => b - a);

  let idx = 0;
  while (k > 0 && idx < arr.length) {
    k -= arr[idx];
    answer++;
    idx++;
  }
  return answer;
}
