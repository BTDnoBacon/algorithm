import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n = int(input())


def hanoi(n, from_fix, to, ass): # n개의 블럭을 / 출발기둥 , 도착기둥 , 보조기둥 으로 옮기는 함수

    # 1방에 가능 할 때 이동 과정 찍고 함수 종료
    if n==1:
        print(from_fix, to)
        return

    hanoi(n-1, from_fix, ass, to) # n개의 블럭 옮기는 과정을 쪼개면, n-1개를 from부터 ass까지 옮기기
    print(from_fix, to) # 1개 남은거 from부터 to에 갖다놓기
    hanoi(n-1, ass, to, from_fix) #ass에 있는 n-1개 블럭 to에 갖다놓기


print(2**n-1) # n 입력 받았을 때 이동 횟수
hanoi(3, 1, 3, 2) # 3개 블럭 1번 기둥에서 3번기둥까지//2번을 보조로 출력