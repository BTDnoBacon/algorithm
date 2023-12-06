# Union_Find 알고리즘 Python

def solution(k, room_number):
    answer = []
    room_dict = {}

    def find_empty_room(number):
        # 빈 방인 경우
        if number not in room_dict:
            room_dict[number] = number + 1
            return number
        # 이미 배정된 방인 경우, 재귀적으로 연결된 다음 빈 방을 찾음
        empty = find_empty_room(room_dict[number])
        room_dict[number] = empty + 1
        return empty

    for number in room_number:
        empty_room = find_empty_room(number)
        answer.append(empty_room)

    return answer
