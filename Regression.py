import numpy as np

perch_length = np.array([8.4, 13.7, 15.0, 16.2, 17.4, 18.0, 18.7, 19.0, 19.6, 20.0, 21.0,
       21.0, 21.0, 21.3, 22.0, 22.0, 22.0, 22.0, 22.0, 22.5, 22.5, 22.7,
       23.0, 23.5, 24.0, 24.0, 24.6, 25.0, 25.6, 26.5, 27.3, 27.5, 27.5,
       27.5, 28.0, 28.7, 30.0, 32.8, 34.5, 35.0, 36.5, 36.0, 37.0, 37.0,
       39.0, 39.0, 39.0, 40.0, 40.0, 40.0, 40.0, 42.0, 43.0, 43.0, 43.5,
       44.0])
perch_weight = np.array([5.9, 32.0, 40.0, 51.5, 70.0, 100.0, 78.0, 80.0, 85.0, 85.0, 110.0,
       115.0, 125.0, 130.0, 120.0, 120.0, 130.0, 135.0, 110.0, 130.0,
       150.0, 145.0, 150.0, 170.0, 225.0, 145.0, 188.0, 180.0, 197.0,
       218.0, 300.0, 260.0, 265.0, 250.0, 250.0, 300.0, 320.0, 514.0,
       556.0, 840.0, 685.0, 700.0, 700.0, 690.0, 900.0, 650.0, 820.0,
       850.0, 900.0, 1015.0, 820.0, 1100.0, 1000.0, 1100.0, 1000.0,
       1000.0])

import matplotlib.pyplot as plt

plt.scatter(perch_length, perch_weight)
plt.xlabel('length')
plt.ylabel('weight')
plt.show()

""" 
    train_test_split에서 train input/target, test input/target 을 한번에 얻어온다. 
    data의 두개의 성질을 넣고, random seed (random_state=42)를 설정해준다.
"""
from sklearn.model_selection import train_test_split
train_input, test_input, train_target, test_target = train_test_split(perch_length, perch_weight, random_state=42)

""" 
넘파이는 배열의 크기에 -1을 넣으면 자동으로 배열의 크기가 들어가게 된다. 
"""
train_input = train_input.reshape(-1, 1)
test_input = test_input.reshape(-1, 1)

from sklearn.neighbors import KNeighborsRegressor # k-최근접 이웃회귀알고리즘 클래스
knr = KNeighborsRegressor()

"""
과대적합: 훈련세트의 점수가 테스트 세트의 점수에 비해서 상대적으로 너무 높은 경우.
과소적합: 훈련세트 점수와 테스트세트 점수가 둘다 너무 낮거나, 테스트세트 점수가 더 높은 경우. 
이웃 알고리즘으로 모델을 더 복잡하게 만드는 방법은 이웃의 개수 k를 줄이는 것이다. 
이웃을 개수를 줄이면 훈련 세트는 있는 국지적인 패턴에 민감해지고, 이웃의 개수를 늘이면 데이터 전반에 있는 
패턴을 따를 것이다. k-최근접 이웃 알고리즘의 기본 k값은 5 이다. 
"""
knr.n_neighbors = 3

# k-최근접 이웃 회귀 모델을 훈련합니다.
knr.fit(train_input, train_target)
print(knr.score(test_input, test_target)) # coefficient of determination

from sklearn.metrics import mean_absolute_error

# 테스트 세트에 대한 예측을 만듭니다.
test_prediction = knr.predict(test_input)

# 테스트 세트에 대한 평균 절대값 오차를 계산합니다.
mae = mean_absolute_error(test_target, test_prediction)
print(mae)

print(knr.score(train_input, train_target))
train_predict = knr.predict(train_input)
mae_train = mean_absolute_error(train_target, train_predict)
print(mae_train)



