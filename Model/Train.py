from Model import Data_load as dl

from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers import Dense, GRU, Embedding
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam

import numpy as np
import os
import re


def preprocessing(text):
    text = re.sub('\n', '. ', text)
    text = text.lower()
    text = re.sub(r'[^a-z]', ' ', text)
    return text


def label_cleansing(text):
    text = re.sub('Dataset', '', text)
    text = re.sub('.txt', '', text)
    text = re.sub('/', '', text)
    text = re.sub(r'[^a-z]', '', text)
    return text


def one_hot_encoder(y):
    list_label = list(set(y))
    label = np.zeros([len(y), len(list_label)])
    for i in range(len(y)):
        label[i][list_label.index(y[i])] = 1
    return label


def fit(x_train_tokens, y_train, max_tokens=5000, embedding_size=8, num_words=10000, summary=False):

    model = Sequential()
    model.add(Embedding(input_dim=num_words,
                        output_dim=embedding_size,
                        input_length=max_tokens,
                        name='layer_embedding'))
    # model.add(GRU(units=16, return_sequences=True))
    # model.add(GRU(units=8, return_sequences=True))
    model.add(GRU(units=4))
    model.add(Dense(5, activation='softmax'))
    optimizer = Adam(lr=1e-3)
    model.compile(loss='binary_crossentropy',
                  optimizer=optimizer,
                  metrics=['accuracy'])
    y_train = np.array(y_train)
    if summary:
        print(model.summary())
    model.fit(x_train_tokens, y_train, epochs=15)
    return model


def train():

    data = []
    data += dl.load_data(os.path.join(os.getcwd(), 'Dataset/business/*.txt'))
    data += dl.load_data(os.path.join(os.getcwd(), 'Dataset/entertainment/*.txt'))
    data += dl.load_data(os.path.join(os.getcwd(), 'Dataset/politics/*.txt'))
    data += dl.load_data(os.path.join(os.getcwd(), 'Dataset/sport/*.txt'))
    data += dl.load_data(os.path.join(os.getcwd(), 'Dataset/tech/*.txt'))

    x_train = []
    y_train = []

    for i in range(len(data)):
        x_train.append(preprocessing(data[i][0]))
        y_train.append(label_cleansing(data[i][1]))

    num_words = 100
    max_tokens = 100
    embedding_size = 256

    tokenizer = Tokenizer(num_words=num_words)
    tokenizer.fit_on_texts(x_train)

    x_train_tokens = tokenizer.texts_to_sequences(x_train)
    x_train_tokens = pad_sequences(x_train_tokens, maxlen=max_tokens, padding='pre', truncating='pre')
    y_train = one_hot_encoder(y_train)

    model = fit(x_train_tokens, y_train, max_tokens=max_tokens,
                embedding_size=embedding_size,
                num_words=num_words,
                summary=True)
