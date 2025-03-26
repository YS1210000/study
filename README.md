# study
https://www.acmicpc.net/user/yschoihschoi


# 문제집
https://www.acmicpc.net/workbook/view/8708

https://covenant.tistory.com/224

https://covenant.tistory.com/145

https://school.programmers.co.kr/learn/challenges?order=recent


# 주의
약수 구하기 문제 -> 자기 자신도 약수

유클리드 호제법 ->
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
