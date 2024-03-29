"""
문제를 풀고 난 후, 구글링을 해봤을 때 나랑 똑같이 생각한 사람이 있어서 신기했다 !!!
근데 글을 읽어보니 이중반복문을 사용하면 시간복잡도가 높아져서 좋지 않은 풀이라고 했다...
문제에서 n의 범위값을 5000으로 제한했기 때문에 푸는데 지장은 없었다고 한다.
우수 코드 찾아서 넣어둔다...
"""
#----------------------------------------------------------------------------------------------------
# My_Code
N = int(input())

cnt = []
for i in range(N//3+1) :
    for j in range(N//5+1) :
        if 5*j + 3*i == N :
            cnt.append(i+j)

if len(cnt) == 0 : 
    print("-1")
else :
    print(min(cnt))

#----------------------------------------------------------------------------------------------------
# Excellent Code
n = int(input())

# count = 0으로 초깃값 잡아주는거 기본수학1에서 자주 했었는데 !
count = 0

while n >= 0:  # n>=0보다 크거나 같다면 계속 실행
    if n % 5 == 0:  # n이 5로나누어 떨어지면
        count += (n // 5)  # n을 5로 나눈 몫을 count에 더해준다
        print(count)  # count 출력
        break  # 반복문 빠져나온다. else문 실행 x
    n -= 3 # n이 5로 나누어 떨지지 않으면 3만큼 빼준다.
    count += 1 #개수에 한번 더해준다.
else: #n이 0보다 작고 위의 while문에서 반복문을 break로 빠져나오지 못했다면(itreable이 소진되었을 경우)
    print(-1) #-1출력
