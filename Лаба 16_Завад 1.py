import nltk
import matplotlib.pyplot as plt
from collections import Counter #словник, який дозволяє рахувати кількість незмінюваних об'єктів (напр. рядки)
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

try:
    with open('shakespeare-hamlet.txt', 'r', encoding='utf-8') as File:
        text = File.read()

except FileNotFoundError:
    print("Файл не знайдено!")
    exit(0)


def count_words(text):
    sentences = nltk.sent_tokenize(text) #токенізація по реченням
    k_words = 0

    for sentence in sentences:
        words = nltk.word_tokenize(sentence)
        #words - список зі словами
        k_words += len(words)

    print("Кількість слів у тексті:", k_words)
    return k_words

def most_used_words(text):
    text1 = text.split() #cписок зі словами
    cnt = Counter(text1) #підрахунок слів
    cort = cnt.most_common(10)

    x = [cort[el][0] for el in range(len(cort))] #слова
    y = [cort[el][1] for el in range(len(cort))] #к-ть повторень у тексті
    
    plt.bar(x, y)
    plt.title("10 найбільш вживаних слів у тексті")
    plt.xlabel("Слова") #підписи по осям
    plt.ylabel("Зустрічаються разів у тексті")
    plt.show()

def delete_stop_words(text):
    # Список стоп-слів англійською
    stop_words = set(stopwords.words("english"))
    # Вхідне речення
    words = word_tokenize(text.lower())
    words = [word for word in words if word.isalpha()]

    # Видалення стоп-слів
    without_stop_words = [word for word in words if word.lower() not in stop_words]
    most_used_words(" ".join(without_stop_words))

count_words(text)
most_used_words(text)
delete_stop_words(text)
