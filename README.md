# dialog-sample

# mecab導入
`brew install mecab mecab-ipadic`

## 導入確認
ターミナルでmecabと打って何か文章を入力すると形態素解析してくれる。

# 追加辞書(mecab-ipadic-neologd)の導入
初期の辞書ではどうしても登録語が少ないので、思った通りに出力してくれません。

ということで追加辞書はgit上にあるのでクローンしてきましょう。
辞書のアップデートがあるのでわかりやすい場所に置いておきましょう

`git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git`

クローンしたら、mecab-ipadic-neologdに入って以下のコマンドでインストールします。
-aオプションで全ての追加辞書をインストールしますがある程度の空き容量が必要です。(1GB以上)全部入れなくても良い場合は-aを外してください。
(sudoでしないと怒られたのでsudoつけてます)

`sudo ./bin/install-mecab-ipadic-neologd -n -a`

インストール途中でyes or noを聞かれるので`yes`と答えてください。

この-d以降の階層に追加されています。
追加辞書を使う際には指定してあげるのでメモっておきましょう。

`mecab -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd`

追加辞書のインストール先を忘れた場合は以下を叩けば出てきます。

`echo `mecab-config --dicdir`"/mecab-ipadic-neologd"`

***

追加前
```
西野かな
西野	名詞,固有名詞,人名,姓,*,*,西野,ニシノ,ニシノ
か	助詞,副助詞／並立助詞／終助詞,*,*,*,*,か,カ,カ
な	助詞,終助詞,*,*,*,*,な,ナ,ナ
EOS
```

追加後
```
西野かな
西野	名詞,固有名詞,人名,姓,*,*,西野,ニシノ,ニシノ
かな	名詞,固有名詞,人名,名,*,*,かな,カナ,カナ
```

# Pythonでmecabを使う
Python上でmecabを動かせるようにします。筆者の環境はPython3.6.7です。
pip経由で入れることができます。

`pip install mecab-python3`

ipythonあたりでimport Mecabと打って確認しときましょう。

## Pythonでの簡単な使用例として追加辞書との簡単な比較
```python
demo_mecab.py
import MeCab

wakati = MeCab.Tagger('-Owakati')    #分かち書き
neo_wakati = MeCab.Tagger('-Owakati -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd') #追加辞書を適用
word = input("分かち書き：")

wakati = wakati.parse(word).strip()
neo_wakati = neo_wakati.parse(word).strip()

print('通常辞書：' + wakati)
print('追加辞書：' + neo_wakati)
```
