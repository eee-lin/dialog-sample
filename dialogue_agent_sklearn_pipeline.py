from os.path import dirname, join, normpath

import MeCab
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
#追加
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC

class DialogueAgent:
    def __init__(self):
        self.tagger = MeCab.Tagger()

    def _tokenize(self, text):
      node = self.tagger.parseToNode(text)

      tokens = []
      while node:
          if node.surface != ' ':
            tokens.append(node.surface)

          node = node.next
      return tokens

    def train(self, texts, labels):
      # vectorizer, classifierをpipelineにまとめる
      pipeline = Pipeline([
        ('vectorizer', CountVectorizer(tokenizer=self._tokenize)),
        ('classifier', SVC()),
      ])
      # pipeline.fit()の内部で、vectorizer.fit(), vectorizer.transform()とclassifier.fit()が呼ばれる
      pipeline.fit(texts, labels)
      self.pipeline = pipeline

    def predict(self,texts):
      # pipeline.predict()の内部で、vectorizer.transform()とclassifier.predict()が呼ばれる
      return self.pipeline.predict(texts)

if __name__ == '__main__':
    BASE_DIR = normpath(dirname(__file__))
    # 実行時、このスクリプトと同じディレクトリに学習データ(training_data.csv)を入れる
    training_data = pd.read_csv(join(BASE_DIR, 'dialogue_agent_data/training_data.csv'))

    dialogue_agent = DialogueAgent()
    dialogue_agent.train(training_data['text'], training_data['label'])

    # 実行時、このスクリプトと同じディレクトリに返答分リストreplies.csvを入れる
    with open(join(BASE_DIR, 'dialogue_agent_data/replies.csv')) as f:
        replies = f.read().split('\n')
    print("入力してください：")
    while True:
        input_text = input()#'好きな食べ物は？'
        predictions = dialogue_agent.predict([input_text])
        # .predict()はクラスIDの配列を返すため、その0番目を取り出す
        predicted_class_id = predictions[0]
        print(replies[predicted_class_id])
    