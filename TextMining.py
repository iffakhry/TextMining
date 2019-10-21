# import nltk
# import nltk
import string
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
# nltk.download()

kalimat = "[MOJOK.co] Manfaat jogging setiap pagi yang pertama adalah meredakan stres. Olahraga itu seperti kode bagi tubuh untuk memproduksi hormon endorfin, agen perangsang rasa bahagia. Dilakukan di pagi hari, ketika udara masih bersih, sejuk, jalanan lengang, gunung terlihat jelas di sebelah utara, manfaat jogging bisa kamu rasakan secara maksimal."
#
# tokens = nltk.tokenize.word_tokenize(kalimat)
# print(tokens)
# case_folding = kalimat.lower()
# print(case_folding)

# case_folding = kalimat.translate(str.maketrans('','',string.punctuation)).lower()
# tokens = nltk.tokenize.word_tokenize(case_folding)
# kemunculan = nltk.FreqDist(tokens)
# print(kemunculan.most_common())



kalimat = kalimat.translate(str.maketrans('', '', string.punctuation)).lower()

# katadasar = stemmer.stem(kalimat)
#
# print(katadasar)

#stopword
tokens = word_tokenize(kalimat)
listStopword = set(stopwords.words('indonesian'))

#stemming
factory = StemmerFactory()
stemmer = factory.create_stemmer()

removed = []
for t in tokens:
    if t not in listStopword:
        katadasar = stemmer.stem(t)
        removed.append(katadasar)

print(removed)