import os

from os import path
from wordcloud import WordCloud

import matplotlib.pyplot as plt

import nltk
import string
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# remove whitespace from text
def remove_whitespace(text):
    return  " ".join(text.split())

# remove stopwords function
def remove_stopwords(text):
    filtered_text=""
    word=""
    stop_words = set(stopwords.words("indonesian"))
    word_tokens = word_tokenize(text)
    filtered_text = [word for word in word_tokens if word not in stop_words]
    # filtered_text += " "+ word for word in word_tokens if word not in stop_words
    return filtered_text

# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# Read the whole text.
text = open(path.join(d, 'PidatoPresiden.txt')).read()

#menghapus tanda baca, dan ubah ke lowercase
text = text.translate(str.maketrans('', '', string.punctuation)).lower()

#menghilangkan stopword/kata yang tidak perlu
# removed = remove_stopwords(text)
# print(removed)

#stopword
tokens = word_tokenize(text)
stop_words = set(stopwords.words('indonesian'))
new_stopwords = ["hormati", "wakil", "presiden", "negara", "republik", "indonesia", "'", "salam", "om","shanti","namo", "buddhaya", "alaikum", "warahmatullahi","wabarakatuh", "prof", "dr","kh", "jusuf", "kalla", "ma", "ruf", "amin"]

new_stopwords_list = stop_words.union(new_stopwords)
listStopword = set(new_stopwords_list)

#stemming
factory = StemmerFactory()
stemmer = factory.create_stemmer()

removed = []
katakata = ""
for t in tokens:
    if t not in listStopword:
        # katadasar = stemmer.stem(t)
        # removed.append(katadasar)
        katakata+=" "+t

# print(removed)
print("Cleaning Result: ")
print(katakata)

# tokenize
tokens = nltk.tokenize.word_tokenize(katakata)
kemunculan = nltk.FreqDist(tokens)
print("Tokenize: ")
print(kemunculan.most_common())

# Generate a word cloud image
wordcloud = WordCloud().generate(katakata)

# Display the generated image:
# the matplotlib way:

# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis("off")

# lower max_font_size
wordcloud = WordCloud(max_font_size=40, background_color="white").generate(katakata)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()