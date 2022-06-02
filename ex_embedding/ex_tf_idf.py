import pandas as pd
from math import log
# TF-IDF(Term Frequency- Inverse Document Frequency)
# TF(d, t) : 특정 문서 D 에서의 특정 단어 T의 등장 횟수
# DF(t) : 특정 단어 t가 등장한 문서의 수
# IDF(d, t) : DF(t)에 반비례하는 수

docs = ['먹고 싶은 사과'
        ,'먹고 싶은 바나나'
        ,'길고 노란 바나나 바나나'
        ,'저는 과일이 좋아요'
]

# 출현 단어
vocab = list(set(w for doc in docs for w in doc.split() ))
vocab.sort()
N = len(docs) # 총문서 수
print(vocab)
print(N)
def tf(t, d):
        return d.count(t)
def idf(t):
        df = 0
        for doc in docs:
                df += t in doc
        return log(N/df + 1)

def tfidf(t, d):
        return tf(t, d) * idf(t)

result = []
for i in range(N):
        result.append([])
        d = docs[i]
        for j in range(len(vocab)):
                t = vocab[j]
                result[-1].append(tfidf(t, d))
tfidf_ = pd.DataFrame(result, columns=vocab)
import numpy as np
# 코사인 유사도 벡터의 방향(각)
def cos_sim(x, y):
        return np.dot(x, y)/ (np.linalg.norm(x) * np.linalg.norm(y))

print('tf-idf:', tfidf_)
doc_list = tfidf_.values.tolist()
while True:
        num = int(input('가까운 문서 찾기 문서 번호 입력: '))
        for i in range(len(doc_list)):
                if i != num:
                        print(i, ': 번째 문서 유사도: ', cos_sim(doc_list[num],doc_list[i]))

