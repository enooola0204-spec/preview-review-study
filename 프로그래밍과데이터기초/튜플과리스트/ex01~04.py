import math

# 공통 좌표 데이터
points = [(1, 2), (3, 4), (-1, 5), (2, -3), (0, 0), (4, 1), (-2, -2)]


# 1️⃣ 원점 기준 거리 ≤ 3 인 좌표 (x^2 + y^2 ≤ 9)
within_distance = [
    (x, y)
    for x, y in points
    if x**2 + y**2 <= 9
]
print(within_distance)


# 2️⃣ y좌표 반전 (대칭 이동)
reflected = [(x, -y) for x, y in points]
print(reflected)


# 3️⃣ 1사분면 좌표 개수 (x > 0, y > 0)
first_quadrant = [
    (x, y)
    for x, y in points
    if x > 0 and y > 0
]
print(len(first_quadrant))


# 4️⃣ 원점으로부터 거리 계산
distances = [
    math.sqrt(x**2 + y**2)
    for x, y in points
]
print(distances)