# 정렬을 활용하는 문제
#--------------------------------------------------------------------------------------------
# My Code
import sys
N = int(sys.stdin.readline())
number_list = []
total = 0

for i in range(N) :
    number = int(sys.stdin.readline())
    total += number
    number_list.append(number)
    
    
number_list.sort()
number_list


# 산술평균 ⭕
print(round(total/N))

# 중앙값 ⭕
center = (1+N)/2
print(number_list[int((1+N)/2)-1])

# 최빈값 ❌
    # count_list : 개수 담을 리스트
count_list = []
    # final : 중복되지 않고 들어있는 숫자 오름차순으로 정리
final = sorted(list(set(number_list)))


for i in final :
    count = number_list.count(i)
    count_list.append(count)
    

for i in range(len(count_list)) :
    for j in range(len(count_list)) :
        while i < j : 
            if count_list[i] == count_list[i+1] :
            
                print(final[i+1])
                break
        
    
            else :
                max_index = count_list.index(max(count_list))
                print(final[max_index])


# 범위 ⭕
print(number_list[N-1]-number_list[0])    



#--------------------------------------------------------------------------------------------
# Googling Code
## 최빈값 ❌❌
"""
number_list : [-1, 0, 0]
count_list : [(0, 2), (-1, 1)]
"""
from collections import Counter
count_list = Counter(number_list).most_common()
count_list
len(count_list)
# 최빈값 2개 이상
"""
> 정렬 순서 
    - 최빈값이 높은 숫자부터
    - 최빈값이 여러개면 큰 작은 숫자부터 정렬된다. 
> 첫번째 두번째 인덱스만 비교하면 된다.
(왜냐하면 최빈값이 1개면 젤 처음 숫자 입력하면 되고, 최빈값이 아무리 많아도 두번째로 작은 수를 출력하니까)
"""
if len(count_list) > 1 and count_list[0][1] == count_list[1][1] :
    print(count_list[1][0])
else :
    print(count_list[0][0])
