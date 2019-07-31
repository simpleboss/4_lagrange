# 프로그램 명: lagrange
# 제한시간: 1 초
# 양의 정수는 많아야 4 개의 제곱수의 합으로 표현가능하다는 것이 1770 년에 Joseph-Louis Lagrange 에 의해서 처음 발표되었다.
# 이는 Lagrange's Four-Square 이론으로 얄려져 있다.
#
# 우리가 관심있는 것은 양의 정수가 주어질 때 제곱수의 합으로 만들수 있는 종류가 몇 개가 되는 지를 구하는 것이 문제이다. 제곱수는 최대 4 개까지 사용가능한다.
#
# 단, 42 + 32 과 32 + 42 은 같은 표현으로 본다.
#
# 예를 들어 , n 이 25 인 경우 3 가지 표현이 가능한다.
#
# 12 + 22 + 22 + 42
# 32 + 42
# 52
# 물론 0 이 되는 답은 없다.
# 입력
# 215 이하인 양의 정수가 입력으로 주어진다.
# 출력
# 가능한 가짓수를 출력한다.
# 입출력 예
# 입력
#
# 1
#
# 출력
#
# 1
#
# 입력
#
# 25
#
# 출력
#
# 3
#
# 입력
#
# 2003
#
# 출력
#
# 48
#
# 입력
#
# 211
#
# 출력
#
# 7
#
# 입력
#
# 20007
#
# 출력
#
# 738
# 요구 사항
# 4 중 반복문을 사용하면 시간초과 오류가 날수 있으니 3 중 반복문으로 구현해 보세요.
# 출처: Japan 2003,Aizu
# [질/답] [제출 현황] [푼 후(1)]
# [ 채 점 ] [홈으로]  [뒤 로]

input_number = int(input())

count_result = 0
i = 1
while i**2 <= input_number:
    if i**2 == input_number:
        count_result += 1
        break
    save_1 = i**2
    j = i
    while save_1 + j**2 <= input_number:
        if save_1 + j**2 == input_number:
            count_result += 1
            break
        save_2 = save_1 + j**2
        k = j
        while save_2 + k**2 <= input_number:
            if save_2 + k**2 == input_number:
                count_result += 1
                break
            save_3 = save_2 + k**2
            l = k
            while save_3 + l**2 <= input_number:
                if save_3 + l**2 == input_number:
                    count_result += 1
                    break
                l += 1
            k += 1
        j += 1
    i += 1

print(count_result)

