def solution(number, k):
    stack = []
    l = len(number)
    for i in range(len(number)) :
        while k>0 and stack and stack[-1]<number[i] :
            stack.pop()
            k -= 1
        stack.append(number[i])
    return ''.join(stack[:l-k])