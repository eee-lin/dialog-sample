```python
from sklearn.svm import SVC

# 学習データの特徴ベクトル(2次元配列)
training_data = [
    [],
    [],
]

training_labels = [0,1,...] #学習データのクラスID(1次元配列)

# sklearn.svm.SVCをインスタンス化
classifier = SVC()
# fit()メソッドを呼ぶことで、学習が行われる。引数は学習データ
classifier.fit(training_data, training_labels)

test_data = [
    [],
    [],
]
#ユーザー入力の特徴ベクトル
predictions = classifier.predict(test_data) 
#学習された識別器インスタンスclassifierのpredict()メソットを呼ぶことで予測を行う。
#引数は2次元配列 返り値predictionsは1次元配列
```