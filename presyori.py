# サンプルのツイートリスト
tweets = [
    "これは普通のツイートです。",
    "エロティックな内容のツイート。",
    "宗教に関する議論をしている。",
    "この方法で稼げるらしい。",
    "美しい風景の写真。",
    "えろ"
]

# フィルタリングする不適切なキーワード
inappropriate_keywords = ["エロ", "宗教", "稼げる"]

# 不適切な内容を含むツイートをフィルタリング
filtered_tweets = [tweet for tweet in tweets if not any(keyword in tweet for keyword in inappropriate_keywords)]

print(filtered_tweets)
