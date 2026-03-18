


#============================
# sum = 0
# for i in range(h1):
#     sum += h1[i]

# print("h1 : " + sum/len(h1))
# #============================
# sum = 0
# for i in range(h2):
#     sum += h2[i]

# print("h2 : "+ sum/len(h2))
# #============================
def av(arr):
# 1. 더한 값을 저장하는 변수를 만든다.
    sum = 0
    for i in range(len(arr)):
        # 2. 리스트 안에 모든 값을 더한다
        sum += arr[i]
    # 3. 더한 값을 저장하는 변수를 리스트의 길이로 나눈다.
    return sum / len(arr)


# print(mean(h2))
test_data = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]

def median(a:list):
    n = len(a)
    # if 홀수면 ~~~
    # a[(n+1)/2] 
    if(n % 2 == 1):
        return a[(n+1) // 2]        
    # else << 짝수면 ~~~
    # (a[(n/2)] + a[(n/2)+1]) / 2
    else:
        return (a[(n // 2)] + a[(n//2) + 1]) / 2
        

print(median(test_data))

def median(arr):
    # 1. 리스트 정렬을 한다.
    arr2 = sorted(arr)
    n = len(arr2)

    # 2. 홀수인지 짝수인지 비교한다.
    if(n %2 != 0):
        # 3. 홀수라면 n/2+1 값을 리턴한다.
        return arr2[n // 2]
    else:
        # 4. 짝수라면 list(n/2 + n/2+1) 값에 나누기 2를 한다.
        return (arr2[n // 2 - 1] + arr2[(n // 2)]) / 2
    
#표준편차 (네이버 공식 검색)

def SD(arr:list):
    # 1. 평균 계산: 모든 자료의 합을 자료의 개수로 나눕니다.
    average = av(arr)
    # 2. 편차 제곱합: 각 데이터에서 평균을 뺀 후(편차) 제곱하고, 이 값들을 모두 더합니다.
    # 2-1. 새로운 리스트 생성후 값을 더한다.
    sum = 0
    for i in arr:
        sum += (i - average) ** 2
    # 3. 분산 계산: 제곱합을 데이터 개수(또는 표본 )로 나누어 분산을 구합니다.
    var = sum / len(arr)
    # 4. 제곱근: 분산에 루트()를 씌워 최종 표준편차를 구합니다.
    return var ** 0.5

print(SD(test_data))