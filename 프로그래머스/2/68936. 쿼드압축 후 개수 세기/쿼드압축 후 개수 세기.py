def solution(arr):
    result = [0, 0]
    l = len(arr)
    def compression(a, b, l) :
        start = arr[a][b]
        for i in range(a, a+l) :
            for j in range(b, b+l) :
                if start != arr[i][j] :
                    l = l//2
                    compression(a, b, l)
                    compression(a+l, b, l)
                    compression(a, b+l, l)
                    compression(a+l, b+l, l)
                    return 
        result[start] += 1
    compression(0, 0, l)
    return result