import TextBlob
#class Editor():
    # def __init__(self):
    #     pass
    # def predict(self, text, words=9):
    #     blob = TextBlob(text)
    #     return blob.ngrams(words)
    # def get_words(self, text):
    #     blob = TextBlob(text)
    #     return blob.words
    #
    #
blob = TextBlob("This is a test")
test = blob.ngrams(5)
print(test)