function solution(n) {
  // function recursion(n) {
  //     if (n === 1) {
  //         answer++
  //         return
  //     }
  //     if (n === 2) {
  //         answer += 2
  //         return
  //     }
  //     recursion(n - 1)
  //     recursion(n - 2)
  // }
  // recursion(n)
  const arr = [0, 1, 2];
  for (let i = 3; i < n + 1; i++) {
    arr.push((arr[i - 1] + arr[i - 2]) % 1234567);
  }

  return arr[n];
}
