// function solution(menu, order, k) {
//   var answer = 0;
//   const waiting = Array.from({ length: order.length * 100 + 1 }, (_, idx) =>
//     idx / k < order.length ? Math.floor(idx / k) + 1 : order.length
//   );
//   let start_idx = 0;
//   order.forEach((item) => {
//     const time = menu[item];
//     start_idx += time;
//     for (let i = start_idx; i < waiting.length; i++) {
//       waiting[i]--;
//     }
//   });
//   answer = Math.max(...waiting);

//   return answer;
// }

function solution(menu, order, k) {
  let cur_time = 0;
  let cur_person = 0;
  let order_end = menu[order[0]];
  let cur_waiting = 0;
  let max_waiting = 0;
  const people_invite_arr = Array.from(
    { length: order.length },
    (_, idx) => idx * k
  );
  let people_invite = 0;

  while (cur_person < order.length) {
    if (cur_time === order_end) {
      cur_waiting--;
      cur_person++;
    }
    if (
      people_invite < order.length &&
      people_invite_arr[people_invite] === cur_time
    ) {
      cur_waiting++;
      people_invite++;
    }
    if (cur_person < people_invite && order_end <= cur_time) {
      order_end = cur_time + menu[order[cur_person]];
    }

    max_waiting = Math.max(max_waiting, cur_waiting);
    cur_time++;
  }

  return max_waiting;
}

solution([5, 12, 30], [1, 2, 0, 1], 10);
solution([5], [0, 0, 0, 0, 0], 5);
