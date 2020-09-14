from textParser import TextParser
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import Adam
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

DATASET_SIZE = 500

class TrainingEnvironment:

    def __init__(self):
        self.statistics = []
        self.languages = []
        self.datasetSize = DATASET_SIZE
        self.textParser = TextParser()
        # self.network = self.initialiseNetwork()

    def getDataset(self):
        file_d = open("data.csv", "w+")
        file_l = open("languages.csv", "w+")

        # # first row in file_d is letters
        # for letter in string.ascii_lowercase:
        #     file_d.write(letter + ",")
        # file_d.write("\n")

        for i in range(self.datasetSize):

            # get new Wiki text and its language
            dataPair = self.textParser.readRandomWiki()
            language = dataPair[0]
            text = dataPair[1]
            self.languages.append(language)
            letterCount = self.textParser.getNormalizedStats(text)
            self.statistics.append(letterCount)

            # save to file
            values = list(letterCount.values())
            file_l.write(str(self.textParser.languages.index(language)) + "\n")
            for j in range(len(values)):
                if j == len(values) - 1:
                    file_d.write(str(values[j]))
                else:
                    file_d.write(str(values[j])+",")
            file_d.write("\n")
            print(i)

    def loadData(self, file_l, file_d):
        langs = np.genfromtxt(file_l, delimiter=",", dtype="int")
        data = np.genfromtxt(file_d, delimiter=",", dtype="float")
        # print(np.shape(data))
        # print(langs)
        return data, langs


    def initialiseNetwork(self):

        network = Sequential()
        # network.add(Dense(200, input_dim=26, activation='sigmoid'))
        network.add(Dense(500,input_dim=26, kernel_initializer="glorot_uniform", activation="sigmoid"))
        network.add(Dropout(0.5))
        network.add(Dense(300, kernel_initializer="glorot_uniform", activation="sigmoid"))
        network.add(Dropout(0.5))
        network.add(Dense(100, kernel_initializer="glorot_uniform", activation="sigmoid"))
        network.add(Dropout(0.5))
        network.add(Dense(1, activation='linear'))

        opt = Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-08, decay=0.0)
        network.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])

        return network

    # data - x, languages - y
    def trainNetwork(self, X, Y):
        pass
        # self.network.fit(X, Y, epochs=30, batch_size=1)

    def knn(self, X, Y, test_size):
        neigh = KNeighborsClassifier(n_neighbors=3)
        neigh.fit(data[test_size:], langs[test_size:])
        predictions = neigh.predict(data[:test_size])
        print(predictions)
        print(langs[:test_size] - predictions)
        errors = 0
        for entry in langs[:test_size] - predictions:
            if entry != 0:
                errors += 1
        accuracy = (len(predictions) - errors) / len(predictions) * 100
        print(str(accuracy)+"%")

tEnv = TrainingEnvironment()
# tEnv.getDataset()
data, langs = tEnv.loadData("languages.csv", "data.csv")
# tEnv.trainNetwork(data, langs)
tEnv.knn(data, langs, 100)

