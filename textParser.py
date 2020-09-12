import wikipedia
import string

class TextParser:

    def __init__(self):
        pass

    def readWiki(self, topic):
        page = wikipedia.page(topic)
        return page.content

    def readRandomWiki(self):
        while True:
            try:
                random_topic = wikipedia.random(1)
                page = wikipedia.page(random_topic)
                return page.content
            except wikipedia.exceptions.DisambiguationError as e:
                continue
            except wikipedia.exceptions.PageError as e:
                continue


    def getLetterStats(self, text):
        alphabet = string.ascii_lowercase
        letterCount = {}

        for c in alphabet:
            letterCount[c] = 0

        for char in text:
            if char.isalpha():
                c = char.lower()
                if c in alphabet:
                    letterCount[c] += 1
        print(letterCount)
        return letterCount

    # get fractional letter count
    def getNormalizedStats(self, text):
        letterCount = self.getLetterStats(text)
        nLetters = sum(letterCount.values())
        print(nLetters)
        for key in letterCount.keys():
            letterCount[key] = letterCount[key] / nLetters
        print(letterCount)
        return letterCount


textParser = TextParser()
# textParser.readRandomWiki()
textParser.getNormalizedStats("acdfff")