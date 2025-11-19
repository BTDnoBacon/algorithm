function solution(n, q, ans) {
    let count = 0;
    
    function combination(arr, start, selected) {
        if (selected.length === 5) {
            if (isValid(selected)) {
                count++;
            }
            return;
        }
        
        for (let i = start; i <= n; i++) {
            selected.push(i);
            combination(arr, i + 1, selected);
            selected.pop();
        }
    }
    
    function isValid(selected) {
        for (let i = 0; i < q.length; i++) {
            let matchCount = 0;
            for (let num of q[i]) {
                if (selected.includes(num)) {
                    matchCount++;
                }
            }
            if (matchCount !== ans[i]) {
                return false;
            }
        }
        return true;
    }
    
    combination([], 1, []);
    return count;
}