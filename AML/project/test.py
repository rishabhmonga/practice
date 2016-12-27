from pprint import pprint
import pandas as pd
import numpy as np
import seaborn
from PIL import Image

seaborn.set()
from wordcloud import WordCloud
import matplotlib.pyplot as plt

from sklearn.datasets import fetch_20newsgroups

newsgroups = fetch_20newsgroups()
len(newsgroups.data)

dir(newsgroups)

df = pd.DataFrame(newsgroups.data, columns=['data'])

df['target'] = newsgroups.target

df['target_name'] = df['target'].apply(lambda x: newsgroups.target_names[x])

df.head()

df.groupby(df.target_name).size().reset_index(name='Size').plot(x='target_name', y='Size', kind='bar')


def get_cloud(text, mapping=False):
    if mapping is True:
        wordcloud = WordCloud(max_font_size=40).generate_from_frequencies(text.items())
    else:
        wordcloud = WordCloud(max_font_size=40).generate(text)
    plt.figure()
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()


for tn in df.target_name.unique():
    print(tn)
    text = ""
    for d in df[df.target_name == tn].iterrows():
        text += d[1].data
    get_cloud(text)
    break

model = make_pipeline(
        TfidfVectorizer(ngram_range=(1,3), stop_words='english'),
        AdaBoostClassifier(n_estimators=100),
    ).fit(newsgroups_train.data, newsgroups_train.target)
prediction = model.predict(newsgroups_test.data)

print 'macro f1:', f1_score(newsgroups_test.target, prediction, average='macro')
print(classification_report(newsgroups_test.target, prediction, target_names=newsgroups_test.target_names))
cm = confusion_matrix(newsgroups_test.target, prediction)
df_cm = pd.DataFrame(cm, index = newsgroups_test.target_names, columns=newsgroups_test.target_names)
plt.figure(figsize = (10,7))
seaborn.heatmap(df_cm, annot=True,fmt='g')