import sys
from script import parsed_text
from collections import Counter
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

tokenized_words = parsed_text.split()

# print("\nI am third")
print("\n---------------------------------------------------------------")
print("Custom Sentiment Analyser:")

lemmatized_words = []

for word in tokenized_words:
    lemma = lemmatizer.lemmatize(word)
    lemmatized_words.append(lemma)

# print(lemmatized_words)
# print(tokenized_words)

emotion_list = []
value_list = []
values = 0
counter = 0
Lvalue_list = []
Lvalues = 0
Lcounter = 0

# with open('tempMyscripts/emotions.txt', 'r') as file:
#     for line in file:
#         clear_line = line.replace('\n', '').strip()
#         word, emotion = clear_line.split(':')

#         if word in tokenized_words:
#             emotion_list.append(emotion)

with open('tempMyscripts/valEmotionsWords.txt', 'r') as file:
    for line in file:
        clear_line = line.replace('\n', '').strip()
        word, value = clear_line.split(':')

        if word in tokenized_words:
            value_list.append(value)
            counter += 1
            values += float(value)
        if word in lemmatized_words:
            Lvalue_list.append(value)
            Lcounter += 1
            Lvalues += float(value)


w = Counter(value_list)
# total = w['negative'] * 0.42

# print("values: ", values)
# print("counter: ", counter)
# print("emotion: ", values/counter)
print("Matched summ value: ", Lvalues)
print("Word matches: ", Lcounter)
print("Avarage emotion mark: ", Lvalues/Lcounter)
print("---------------------------------------------------------------")
# print(w)
