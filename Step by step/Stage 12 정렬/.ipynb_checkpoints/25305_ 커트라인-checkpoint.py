# k번째로 큰 수를 구하는 문제
#--------------------------------------------------------------------------------------------
# My Code
N, k = map(int, input().split())
score = list(map(int, input().split()))
    
score.sort(reverse=True)    
score
print(score[k-1])
    

#--------------------------------------------------------------------------------------------
# Googling Code
    
    
