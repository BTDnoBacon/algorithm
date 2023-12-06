// UnionFInd 알고리즘

function solution(k, room_number) {
  const answer = [];
  const roomMap = new Map(); // 방 번호를 키로 하고, 다음 빈 방 번호를 값으로 저장

  const findEmptyRoom = (number) => {
    if (!roomMap.has(number)) {
      // 빈 방인 경우
      roomMap.set(number, number + 1); // 다음 방 번호를 맵핑
      return number;
    }
    // 이미 배정된 방인 경우, 연결된 다음 빈 방을 찾음
    const nextEmptyRoom = findEmptyRoom(roomMap.get(number));
    roomMap.set(number, nextEmptyRoom + 1); // 현재 방과 다음 빈 방을 연결
    return nextEmptyRoom;
  };

  for (const number of room_number) {
    const emptyRoom = findEmptyRoom(number); // 빈 방 찾기
    answer.push(emptyRoom); // 결과 배열에 추가
    console.log(roomMap);
  }

  return answer;
}

solution(10, [1, 3, 4, 1, 3, 1]);
