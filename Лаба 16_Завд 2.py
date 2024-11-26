import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

nltk.download('wordnet')
nltk.download('omw-1.4')
    
try:
    with open("лаба 16.txt", encoding='utf-8') as File:
        text = File.read()

except FileNotFoundError:
    print("Файл не знайдено.")
    exit(0)

try:
    with open("txt.txt", "w", encoding='utf-8') as File1:
        # Токенізація по словам
        sentences = nltk.sent_tokenize(text)
        File1.write("Токеніцація:\n")
        for sentence in sentences:
            words = word_tokenize(sentence)
            File1.write(" ".join(words) + "\n")

        # Лемматизація та стеммінг
        words1 = word_tokenize(text)
        ps = PorterStemmer()
        File1.write("\nСтемінг:\n")
        for w in words1:
            rootWord = ps.stem(w)
            File1.write(rootWord + " ")
        File1.write("\n")

        wordnet_lemmatizer = WordNetLemmatizer()
        File1.write("\nЛемматизація:\n")
        for w in words1:
            lemma = wordnet_lemmatizer.lemmatize(w)
            File1.write(lemma + " ")
        File1.write("\n")

        # Видалення стоп-слів та пунктуації
        stop_words = set(stopwords.words("english"))
        words = [word for word in word_tokenize(text.lower()) if word.isalpha()]
        without_stop_words = [word for word in words if word not in stop_words]
        File1.write("\nТекст після видалення пунктуації та стоп-слів:\n")
        File1.write(" ".join(without_stop_words) + "\n")
except FileNotFoundError:
    print("Файл для запису не створено.")
    exit(0)
