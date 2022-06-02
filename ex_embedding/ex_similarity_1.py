import matplotlib.pyplot as plt
import numpy as np

# 유클리드 거리 (점과 점사이의 거리)
def euclidean(x, y):
    return np.sqrt(np.sum((x - y) **2))
doc1 = np.array([1, 0])
doc2 = np.array([0, 6])
doc3 = np.array([1, 2])

plt.scatter([doc1[0], doc2[0], doc3[0]], [doc1[1], doc2[1], doc3[1]])
plt.show()

print('1과 3의 거리 : ', euclidean(doc1, doc3))
print('2와 3의 거리 : ', euclidean(doc2, doc3))

# 코사인 유사도 벡터의 방향(각)
def cos_sim(x,y):
    return np.dot(x,y)/(np.linalg.norm(x)*np.linalg.norm(y))

print('코사인 유사도 1과 3의 거리 : ', cos_sim(doc1, doc3))
print('코사인 유사도 2와 3의 거리 : ', cos_sim(doc2, doc3))