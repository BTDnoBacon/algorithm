function solution(s)
{
    var answer = 0;

    left = []
    for (x of s) {
        if (left.length === 0 || left[left.length-1] !== x) {

            left.push(x)
            continue
        }
        if (left[left.length-1] === x) {
            left.pop()
        }
        while (left.length > 1) {
            temp = left.pop()
            if (left[-1] === temp) {
                left.pop()
                continue
            } else {
                left.push(temp)
                break
            }
        }
    }
    if (left.length === 0) {
        answer = 1
    }
    return answer;
}