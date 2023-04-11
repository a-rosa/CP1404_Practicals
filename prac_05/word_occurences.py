"""
Word Occurences
estimate: 30 mins
Actual: 40 mins
"""

text = input("Text: ").lower()
words = text.split()
word_occurences = {}
# initialize the longest width to the width to the first word for comparison
width = len(words[0])
for word in words:
    if word in word_occurences:
        word_occurences[word] += 1 # add one to the value of the key
    else:
        word_occurences[word] = 1
        if len(word) > width:
            width = len(word)

word_occurences = sorted(word_occurences.items())
for entry in word_occurences:
    print(f"{entry[0]:{width}} : {entry[1]}")