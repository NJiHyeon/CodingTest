## 정렬 : 배열의 원소를 순서대로 나열하는 알고리즘
### 🔎 Fuction
#### **`map`**
- `map(int, input().split())` 
    - 입력값을 몇 개 받을지 알고, 그 값들을 공백으로 분리
    - 대부분 input()을 받는 형식이고 for문으로 반복하면서 받을 수도 있음
- `list(map(int, input().split()))` 
    - 숫자 입력값을 받아야 하는데 for문으로 받지 않을 때
    - 한꺼번에 받고 공백으로 분리 후, 리스트에 저장
    - 따로 따로 입력 받아서 append할 때 [] 묶어서 넣는 방법도 있음.
- `list(map(int, str(input())))` 
    - 문자의 각 자리값을 리스트로 받고 싶을 때
- `list(input())` , `list(sys.stdin.readline())`
    - 숫자의 각 자리수를 리스트로 받고 싶을 때
    - list안에 int를 넣으면 안된다. 


#### **`sys`**
- `list_name.append(int(sys.stdin.readline()))`
    - 범위가 커지면 시간초과가 발생할 수 있으므로 input() 대신 사용하면 유용
    - `sys.stdin.readline().split()` : 개수(숫자)를 받을 때
    - `sys.stdin.readline().strip()` : for문을 이용하여 입력을 받을 때 공백 삭제

#### **`sort`**
- `list_name.sort()` 
    - 리스트 객체 자체를 정렬해주는 함수로 리스트에만 사용 가능
    - 기본적으로 리스트를 오름차순으로 정렬해주는 기능
    - 숫자, 소문자 문자, 대소문자 문자 리스트 모두 가능
    
- `reverse = False, True`
    - 리스트 정렬 방식을 지정해 줄 수 있는 옵션
    - True로하면 내림차순, False로하면 오름차순

- `sorted`와 비교
    - sorted는 새로운 정렬된 리스트를 반환하는 함수로 원본 리스트 값은 유지되고, 정렬된 새로운 리스트에 저장된다. (`a2=sorted(a1)`)
    - sort 함수는 원본 리스트 값이 정렬된 값으로 수정되어 출력되서 정렬된 값(새로운 변수)는 리턴되지 않는다.(`a1.sort()`)
    
- 인자
    - `reverse = False, True`
        - 리스트 정렬 방식을 지정해 줄 수 있는 옵션
        - True로하면 내림차순, False로하면 오름차순
    - `key=lambda x : x[1]`
        - 특정 값을 기준으로 정렬하고 싶을 때
        - key=lambda x : (x[1], x[0])


#### **`반올림, 내림, 올림`**
- 반올림
    - `round(3.1415)`, `round(3.1415, 2)`, `round(3.1415, -1)`
- 올림
    - math 모듈 사용
    - `math.ceil(3.14)`, `math.ceil(-3.14)`
- 내림
    - math 모듈 사용
    - `math.floor(3.14)`, `math.floor(-3.14)` : 무조건 아래만 향해 내림한다. 
    - `math.trunc(-3.14)` : 내림을 하더라도 0으로 향한다.(int()와 같이 결과를 반환)


#### **`index`**
- `list_name.index(max(list_name))` : 리스트에서 최댓값의 인덱스 찾기
- `list_name.index(min(list_name))` : 리스트에서 최솟값의 인덱스 찾기


#### **`dict`**
- `dict = {set_list[i] : i for i in range(len(set_list))}`
- 개수를 비교하는 문제에서 if, for문을 쓰면서 하나씩 비교하면 시간초과가 발생하므로 딕셔너리를 이용해서 비교 


----------------------------------
### 💡 Problem type
- 정렬 종류
    - 버블 정렬 : 현재 값과 다음 인덱스의 값을 비교해서, 다음 인덱스 값이 현재 값보다 작으면 두 값을 서로 교환
        - `for i in range(N) :`
        - `    for j in range(N - i - 1) :`
        - `        if len(word_list[j]) > len(word_list[j+1]) :`
        - `            word_list[j], word_list[j+1] = word_list[j+1], word_list[j]`
    - 삽입 정렬 : 이전 인덱스의 값과 현재 인덱스의 값을 비교해 작은 값을 앞으로 옮긴다. 
    - ⚠ 안정 정렬 : 값이 같은 원소의 전후관계가 바뀌지 않는 정렬 알고리즘
        - `list.sort(key = lambda x : (x[0]))` # (age, name)에서 age만 비교
    - 카운팅 정렬
    - 병합 정렬, 힘 정렬 ...

- 입력 받는 여러가지 방법들
    - `int(input())`로 받아서 sort()후 for문으로 print [2750번](https://www.acmicpc.net/problem/2750)
    - `int(sys.stdin.readline())`로 받아서 sort()후 for문으로 print [2751번](https://www.acmicpc.net/problem/2751)
    - `int(sys.stdin.readline())`와 배열 생성의 조합 [10989번](https://www.acmicpc.net/problem/10989)
       - 배열에는 각 숫자의 개수가 들어가게 된다.
       - 숫자의 수만큼 출력해 주도록 한다. 

- 최빈값 
    - 코드
        - `from collections import Counter`
        - `count_list = Counter(list_name).most_common()`
    - 정렬 순서 
        - 최빈값이 높은 숫자부터
        - 최빈값이 여러개면 큰 작은 숫자부터 정렬된다. 
        - ex) [(-2, 2), (-1, 2), (-3, 1)]

----------------------------------
### ✨Caution
- 정렬 문제를 풀 때 거의 대부분 `list_name.sort()`를 사용하는데, 이것은 리스트에서만 사용할 수 있으므로 먼저 빈 리스트를 선언해두면 유용하다.  
- 범위가 크므로 sys로 대부분 입력 받는걸 생각
- 입력을 받을 때 변수를 여러개 만들어서 넣고 넣고 하면 에러 발생 확률 높아지므로 한번에 만들도록
- 빈 리스트도 필요없더라도 꼭 만들어놓기 (까먹는것보다 나음)


----------------------------------
### 📌 Question to be solved again
- [10989번](https://www.acmicpc.net/problem/10989)
- [2108번-최빈값](https://www.acmicpc.net/problem/2108)
- [1191번](https://www.acmicpc.net/problem/1181)
- [18870번](https://www.acmicpc.net/problem/18870)
- [10814번](https://www.acmicpc.net/problem/10814)