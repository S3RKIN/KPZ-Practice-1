#Завдання1:
import string
import re
from collections import defaultdict

def get_text_info(filepath):
    # Відкриваємо файл з текстом
    with open(filepath, 'r') as f:
        # Читаємо весь текст з файлу
        text = f.read()

    # Видаляємо цифри, пропуски та розділові знаки з тексту
    text = text.translate(str.maketrans('', '', string.digits + string.punctuation))
    text = text.lower()

    # Розділяємо текст на слова та підраховуємо кількість входжень кожного слова
    word_counts = defaultdict(int)
    for word in re.findall(r'\b\w+\b', text):
        word_counts[word] += 1

    # Виводимо на екран список слів та їхню частотність
    for word, count in word_counts.items():
        print(f'{word} - {count}')

#Завдання2:
import csv
import urllib.request
import os


def download_csv(urlpath):
    # Створення папки, якщо її ще немає
    if not os.path.exists('source_data'):
        os.makedirs('source_data')

    # Завантаження CSV файлу
    urllib.request.urlretrieve(urlpath, 'source_data/username.csv')

    # Видалення останнього рядка
    with open('source_data/username.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        data = [row for row in csvreader][:-1]
    
    # Збереження файлу без останнього рядка
    with open('source_data/username.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(data)

    print('Completed!')
