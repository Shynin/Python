from textblob.classifiers import NaiveBayesClassifier
import paralleldots
from textblob import TextBlob
import sys
# from script import trainfeats
from script import parsed

# print("\nI am second")

# print(parsed)
# TextBlob

###########################
# с обучением
# classifier = classifiers.NaiveBayesClassifier(trainfeats)
# print(classifier.accuracy(trainfeats))
# print(classifier.show_informative_features(5))
# print((TextBlob(test_feats, classifier=classifier)).classify())

###########################
testimonial = TextBlob(parsed)
print("---------------------------------------------------------------")
print("Text Blob Sentiment Analyzer:")
print(testimonial.sentiment)
print(testimonial.sentiment.polarity)
print("---------------------------------------------------------------")


###########################
paralleldots
paralleldots.set_api_key('DpcUTBWJTRFgJoG5nGVC5DChMv5r0A5ar4SGZptF7Mc')
paralleldots.get_api_key()
print("Parallel Dots")
print(paralleldots.sentiment(parsed))
