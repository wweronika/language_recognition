from textParser import TextParser
from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import ModelCheckpoint, TensorBoard

class TrainingEnvironment:

    def __init__(self):
        self.statistics = []
        self.languages = []
        self.textParser = TextParser()
        self.languages = ['en', 'fr', 'de', 'it']

    def getPages(self, n):
        for i in range(n):
            self.pages.append(self.textParser.readRandomWiki())
            print(i)

    def getDataset(self, n):
        for i in range(n):
            text = self.textParser.readRandomWiki()
            self.statistics.append(self.textParser.getNormalizedStats(text))
            print(i)
        dataset = np.array(self.statistics)
        print(dataset)
        return dataset

    def initialiseNetwork(self):

        network = Sequential()
        network.add(Dense(200, input_dim=26, activation='sigmoid'))
        network.add(Dense(150, activation='sigmoid'))
        network.add(Dense(100, activation='sigmoid'))
        network.add(Dense(100, activation='sigmoid'))
        network.add(Dense(len(self.languages), activation='softmax'))

        network.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

        return network

tEnv = TrainingEnvironment()
tEnv.getDataset(20)
