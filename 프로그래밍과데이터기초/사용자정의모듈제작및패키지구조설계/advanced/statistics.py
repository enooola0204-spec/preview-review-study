# 테스트 데이터
test_data = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]


# 📌 평균
def mean(arr: list) -> float:
    return sum(arr) / len(arr)


# 📌 중앙값
def median(arr: list) -> float:
    arr_sorted = sorted(arr)
    n = len(arr_sorted)

    if n % 2 == 1:  # 홀수
        return arr_sorted[n // 2]
    else:  # 짝수
        return (arr_sorted[n // 2 - 1] + arr_sorted[n // 2]) / 2


# 📌 표준편차
def standard_deviation(arr: list) -> float:
    avg = mean(arr)
    variance = sum((x - avg) ** 2 for x in arr) / len(arr)
    return variance ** 0.5


# ✅ 실행
print("평균:", mean(test_data))
print("중앙값:", median(test_data))
print("표준편차:", standard_deviation(test_data))