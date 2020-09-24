from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
import re
import string
import nltk
from lxml import html
import time
from bs4 import BeautifulSoup
import requests
import sys
from nltk import classify
from nltk import NaiveBayesClassifier

# print("I got argument " + sys.argv[1])

# url = "https://www.theguardian.com/us-news/2020/aug/27/kenosha-community-jacob-blake-shooting"
# url = "https://www.bbc.com/news/world-us-canada-53934109"
# url = "https://www.dailymail.co.uk/news/article-8580091/Muslim-leaders-condemn-minute-lockdown-announcement.html"

# ---------parser ---------------
url = "https://www.bbc.com/sport/football/53802028"
# url = sys.argv[1]

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
scraped = []
if "www.theguardian.com" in url:
    print("Site for analysis - The Guardian")
    # article = soup.find('div', class_='article-body-commercial-selector')
    paragraphs = soup.find_all('p', class_='css-38z03z')
elif "www.bbc.com" in url:
    print("Site for analysis - BBC")
    # quote = soup.find('div', class_='story-body__inner')
    # scraped = []
    # article = soup.find('div', class_='story-body__inner')
    article = soup.find('div', class_='story-body')
    paragraphs = article.find_all('p')
elif "thesun.co.uk" in url:
    print("Site for analysis - The Sun")
    # quote = soup.find('div', class_='story-body__inner')
    # scraped = []
    article = soup.find('div', class_='article__content')
    paragraphs = article.find_all('p')
elif "www.dailymail.co.uk" in url:
    print("Site for analysis - DailyMail")
    # article = soup.find('div', class_='article-text')
    # article = soup.find_all('p', class_='mol-para-with-font')
    paragraphs = soup.find_all('p', class_='mol-para-with-font')
# paragraphs = article.find_all('p')
for paragraph in paragraphs:
    scraped.append(paragraph.text)
parsed = ' '.join(scraped)

# print(parsed)

# ----------- end parser -----------------

# ----------- text preprocessing -----------------

stop_words = list(set(stopwords.words('english')))

# pos_train = open('tempMyscripts/poswords.txt', encoding='utf-8').read()
# neg_train = open('tempMyscripts/negwords.txt', encoding='utf-8').read()
pos_train = open('tempMyscripts/positiveReviews.txt', encoding='utf-8').read()
neg_train = open('tempMyscripts/negativeReviews.txt', encoding='utf-8').read()
parsed_text = parsed


def parsedPrep(text):
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(r'\d', '', text)
    work_data = re.sub(r"[–”“’]", "", text).lower()
    return work_data


def listPrep(text):
    ####################
    # text = text.translate(str.maketrans('', '', string.punctuation))
    # text = re.sub(r'\d', '', text)
    # work_data = re.sub(r"[–”“’]", "", text).lower()
    # sent_tok = sent_tokenize(work_data)

    ##################
    lower_case = text.lower()
    sent_tok = sent_tokenize(lower_case)
    # ###filtered_sentence = [w for w in sent_tok if not w in stop_words]
    return sent_tok


def dictPrep(words):
    return dict([(word, True) for word in words.split() if word not in stop_words])


posids = listPrep(pos_train)
pos_feats = [(dictPrep(f), 'positive') for f in posids]

negids = listPrep(neg_train)
neg_feats = [(dictPrep(f), 'negative') for f in negids]

trainfeats = pos_feats + neg_feats

parsed_text = parsedPrep(parsed)
test_set = dictPrep(parsed_text)

# print(neg_feats)

# ----------- end preprocessing -----------------

# ----------- text analys -----------------
print("---------------------------------------------------------------")
print("NLTK Naive Bayes Classifier:")
classifier = NaiveBayesClassifier.train(trainfeats)

print("Accuracy is: ", classify.accuracy(classifier, trainfeats))
print(classifier.show_most_informative_features(20))

# print(test_set)
print(classifier.classify(test_set))
print("---------------------------------------------------------------\n")
# print("With accuracy:", classifier.classify(test_set).accuracy())
# print(nltk.classify.accuracy(classifier, test_set))
