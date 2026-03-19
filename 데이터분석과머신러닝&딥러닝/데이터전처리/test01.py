import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. **결측값 분석**
#    - Titanic 데이터의 결측값 시각화
#    - 각 열별 결측값 개수와 비율 계산
#    - Age 열: 177개 결측 (19.9%)
#    - Cabin 열: 687개 결측 (77.1%)

df = sns.load_dataset('titanic')
isnull = df.isnull().sum()
print(isnull)

print(isnull/len(df)*100)


# 2. **전략 1: 삭제(Deletion)**
#    - `df.dropna(subset=['age'])` 사용
df_age_cleaned = df.dropna(subset=['age'])
#    - 891행 → 714행 (177행 삭제)
print(f"원본 데이터 행 개수: {len(titanic)}")
print(f"age 결측값 삭제 후 행 개수: {len(titanic_dropped)}")
print(f"삭제된 행 개수: {len(titanic) - len(titanic_dropped)}")
#    - 데이터 손실률: 19.9%
print(f"데이터 손실률: {((len(titanic) - len(titanic_dropped)) / len(titanic)) * 100:.2f}%")
#    - 장점: 데이터 품질 유지
#    - 단점: 정보 손실
print("-" * 60)



# 3. **전략 2: 대체(Imputation) - 통계값 사용**
#    - 평균값 대체: `age.fillna(age.mean())`
#    - 중앙값 대체: `age.fillna(age.median())`
#    - 최빈값 대체: `age.fillna(age.mode()[0])`
#    - 장점: 데이터 크기 유지
#    - 단점: 분포 왜곡 가능

# 4. **전략 3: 고급 대체 - 그룹별 대체**
#    - 성별-좌석등급별 평균값으로 대체
#    - `groupby(['sex', 'pclass']).transform(lambda x: x.fillna(x.mean()))`
#    - 더 정교한 대체 가능
#    - 각 그룹별 평균값 출력

# 5. **결과 비교**
#    - 각 전략별 결측값 개수 확인
#    - 분포 변화 시각화
#    - 통계값 비교