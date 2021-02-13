"""  마켓과 머신러닝 """

""" 생선 분류 문제 """
"""도미테이터 준비하기"""
bream_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0,
                31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0,
                35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0]
bream_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0,
                500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0,
                700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0]

import matplotlib.pyplot as plt

plt.scatter(bream_length, bream_weight)
plt.xlabel('length')  # x축은 길이
plt.ylabel('weight')  # y 축은 무게
plt.show()

""" ### 빙어 데이터 준비하기 """
smelt_length = [8.8, 10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
smelt_weight = [5.7, 7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]

plt.scatter(bream_length, bream_weight)
plt.scatter(smelt_length, smelt_weight)
plt.xlabel('length')  # x축은 길이
plt.ylabel('weight')  # y 축은 무게
plt.show()
plt.clf()

"""## 첫 번째 머신러닝 프로그램"""

length = bream_length + smelt_length
weight = bream_weight + smelt_length
fish_data = [[l, w] for l, w in zip(length, weight)]

fish_target = [1] * 35 + [0] * 14

from sklearn.neighbors import KNeighborsClassifier

kn = KNeighborsClassifier()
kn.fit(fish_data, fish_target)
kn.score(fish_data, fish_target)

"""## k-최근점 이웃 알고리즘 """
plt.scatter(bream_length, bream_weight)
plt.scatter(smelt_length, smelt_weight)
plt.scatter(30, 600, marker='^')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()

rtn = kn.predict([[30, 600]])
print(rtn)
print(kn._fit_X)
print(kn._y)

kn49 = KNeighborsClassifier(n_neighbors=18)
kn49.fit(fish_data, fish_target)
s = kn49.score(fish_data, fish_target)
print(f"s = {s}")

print(f"35/49 = {35/49}")

for n in range(5, 49):
    kn.n_neighbors = n
    score = kn.score(fish_data, fish_target)
    if score < 1:
        print(n, score)
        break
