import pandas as pd
import ast
import csv
import nltk
import re
import fasttext
from sklearn.metrics import f1_score

nltk.download("punkt")

def returntestscore():
    df = pd.read_csv('Aboutlabeled.csv')

    df[['Article', 'Line']] = df['ID'].str.split(pat='.', n=1, expand=True).values
    del df['ID']

    df['Offsets'] = df['Offsets'].apply(lambda s: ast.literal_eval(s))

    df['Labels'] = df['Offsets'].apply(lambda l: ' '.join(list(set(['__label__' + i['label'] for i in l]))))

    df.loc[df['Label'] == 'None', 'Labels'] = '__label__None'

    df['Text'] = df['Text'].apply(lambda x: re.sub(r'[^a-zA-Z0-9\s]', '',' '.join(nltk.word_tokenize(x.lower()))))

    df['FastText'] = df['Labels'] + ' ' + df['Text']

    df.head(13625)[['FastText']].to_csv('pb.train.txt', header=None, index=None, quoting=csv.QUOTE_NONE, quotechar="",  escapechar="\\")
    df.tail(3028)[['FastText']].to_csv('pb.valid.txt', header=None, index=None, quoting=csv.QUOTE_NONE, quotechar="",  escapechar="\\")

    ################## Final Model ###################################
    model = fasttext.train_supervised(input="pb.train.txt", lr=	0.7468864248632575, epoch=27, wordNgrams=4, loss='ova')

    valid = pd.read_csv("pb.valid.txt", header=None, sep='\t', names=['text'])
    valid['text'] = valid['text'].str.split(' ').apply(lambda l: ' '.join([i for i in l if '__label__' not in i]))

    predictions = []
    for i in range(valid.shape[0]):
        pred = model.predict(valid['text'][i], k=-1, threshold=0.018211034677959557)
        predictions.append((list(pred[0]).__len__() == 1) & ('__label__None' in list(pred[0])))

    predictions = ['None' if i else 'About' for i in predictions]

    actuals = df.tail(3028).copy()
    actuals['predictions'] = predictions

    y_true = actuals['Label'].copy()
    y_pred = actuals['predictions'].copy()

    score = f1_score(y_true, y_pred, average=None)[0]
    
    return score
