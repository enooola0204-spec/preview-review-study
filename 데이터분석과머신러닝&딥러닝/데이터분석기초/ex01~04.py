############################
###2222222222222222222222222장-1가 최선입니다......................
############################

# 1. 다음 벡터를 생성하고 내적 계산
#    - v1 = [1, 2, 3, 4], v2 = [5, 6, 7, 8]
#    - np.dot() 또는 @ 연산자 사용
#    - 결과 출력 및 수동 검증

import numpy as np

# 1. v1 과 v2를 만든다

v1 = np.array([1, 2, 3, 4])
v2 = np.array([5, 6, 7, 8])

# 2. np.dot() 또는 @ 연산자를 사용한다.
answer1 = np.dot(v1, v2)
answer2 = v1 @ v2

# 2-1. 여기서 문제가 발생할수있는 상황 
# ==> v1 과 v2를 v1 = [1,2,3,4] 이런식으로 파이썬 리스트를 생성하면 계산이 안된다.


# 3. 결과 출력 
print(f"dot을 활용 한 결과 값 : {answer1}")
print("@을 활용 한 결과 값 : ", answer2)

# 4. 수동 검증
print("수동검증 = 1x5 + 2x6 + 3x7 + 4x8 ==> ",  1*5 + 2*6 + 3*7 + 4*8)

###########################################################################3
# 2. 행렬 곱셈 수행
#    - 2×3 행렬 A와 3×2 행렬 B 생성
#    - A @ B 계산 (결과: 2×2 행렬)

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8], [9, 10], [11, 12]])

answer3 = np.dot(a, b)
print(answer3)

print("수동 검증 : [ 1*7 + 2*9 + 3*11 ] => "," [ 1*8 + 2*10 + 3*12 ] => ")
print("수동 검증 : [ 4*7 + 5*9 + 6*11 ] => "," [ 4*8 + 5*10 + 6*12 ] => ")

#######################################################################
# 3. 벡터 노름
print("\n[3] 벡터 노름 계산")
print("-" * 60)

c = np.array([3, 4, 5])
print("벡터 c =", c)

# -----------------------------
# L1 노름 직접 계산해보기
# 절댓값을 모두 더하기
# -----------------------------

l1_sum = 0  # 합을 저장할 변수

for i in range(len(c)):   # 벡터 길이만큼 반복
    value = abs(c[i])     # 절댓값 구하기
    l1_sum += value       # 계속 더하기

print("L1 노름 (for문으로 계산) =", l1_sum)

# numpy로 계산한 값도 비교
l1_norm = np.linalg.norm(c, ord=1)
print("L1 노름 (numpy) =", l1_norm)


# -----------------------------
# L2 노름 직접 계산
# sqrt(x**2 + y**2 + z**2)
# -----------------------------

square_sum = 0  # 제곱값 합

for i in range(len(c)):
    square_sum += c[i] ** 2   # 각 원소 제곱해서 더하기

l2_manual = np.sqrt(square_sum)

print("L2 노름 (for문으로 계산) =", l2_manual)

# numpy 계산
l2_norm = np.linalg.norm(c, ord=2)
print("L2 노름 (numpy) =", l2_norm)


# -----------------------------
# L 노름 직접 계산
# 절댓값 중 최대값 찾기
# -----------------------------

max_value = 0

for i in range(len(c)):
    value = abs(c[i])
    
    # 지금까지 최대값보다 크면 갱신
    if value > max_value:
        max_value = value

print("L∞ 노름 (for문으로 계산) =", max_value)

linf_norm = np.linalg.norm(c, ord=np.inf)
print("L∞ 노름 (numpy) =", linf_norm)


#######################################################################

# 4. 조건부 인덱싱
print("\n[4] 조건부 인덱싱")
print("-" * 60)

data = np.array([1, 5, 3, 8, 2, 9, 4, 7, 6])
print("원본 배열:", data)


# 5보다 큰 값 찾기

greater_than_5 = []

for i in range(len(data)):
    if data[i] > 5:
        greater_than_5.append(data[i])

print("5보다 큰 값:", greater_than_5)


# 3 이상 7 이하 값 찾기

between_3_7 = []

for i in range(len(data)):
    if data[i] >= 3 and data[i] <= 7:
        between_3_7.append(data[i])

print("3 이상 7 이하 값:", between_3_7)


# 짝수 찾기

even = []

for i in range(len(data)):
    if data[i] % 2 == 0:
        even.append(data[i])

print("짝수:", even)


print("="*60)
print("모든 계산 완료")
print("="*60)