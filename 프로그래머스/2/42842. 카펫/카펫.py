import math
def solution(brown, yellow):
    answer = []
    n = brown+yellow

    a=1
    b=((n+4-yellow)//2)
    c=n
    
    if b**2 - 4*a*c > 0:
        x1 = (b + math.sqrt(b**2 - 4*a*c)) / 2*a
        x2 = (b - math.sqrt(b**2 - 4*a*c)) / 2*a
        answer.append(x1)
        answer.append(x2)
    elif b**2 - 4*a*c == 0:
        x1 = (+b - math.sqrt(b**2 - 4*a*c)) / 2*a
        answer.append(x1)
        answer.append(x1)
    return answer