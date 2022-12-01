from textblob import TextBlob

positive_words = ""
neutral_words = ""
negative_words = ""

text = input("Type here: ")

words = text.split(" ")

for word in words:
    if TextBlob(word).polarity > 0:
        positive_words += word + " "
    if TextBlob(word).polarity == 0:
        neutral_words += word + " "
    if TextBlob(word).polarity < 0:
        negative_words += word + " "

if positive_words == "":
    positive_words += "None"
if neutral_words == "":
    neutral_words += "None"
if negative_words == "":
    negative_words += "None"

print(f" \n Negative Words: {negative_words} \n Neutral Words: {neutral_words} \n Positive Words: {positive_words}")