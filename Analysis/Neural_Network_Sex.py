#Analysis with Sex using Neural Network
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm, datasets
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.datasets import load_files
from sklearn.naive_bayes import MultinomialNB
from sklearn.cross_validation import train_test_split
from sklearn import metrics
from numpy import array
import numpy as np
from sklearn import datasets, linear_model
import csv
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score
from sklearn import metrics
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn.datasets import make_multilabel_classification
from sklearn.multiclass import OneVsRestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn import linear_model
from sklearn.neural_network import MLPClassifier

# Initializing Training and Target data array
trainData =[]
trainTarget=[]
fileName="Facebook posts.csv"
# Openning the data set file
file = open(fileName, "r",encoding="utf8")
data = csv.reader(file)
# Reading the data set file
count =0
for col in data:
    if count==0:
        count=1
        continue
    count+=1
    if count==185:
        break
    post=col[5]+" "+col[6]+" "+col[7]+" "+col[8]+" "+col[9]+" "+col[10]+" "+col[11]+" "+col[12]+" "+col[13]+" "+col[14]
    trainData.append(post)
    t=""
    
    if col[3]=='Female':
        t+="0"
    else:
        t+="1"
    trainTarget.append(int(t))

# Creating input feature vector using TfidfVectorizer
vectorizer=TfidfVectorizer(use_idf=True,  max_features=6000 ,token_pattern='[^ \n,".\':()ঃ‘?’।“”!;a-zA-Z0-9#০১২৩৪৫৬৭৮৯*&_><+=%$-`~|^·]+') #০১২৩৪৫৬৭৮৯
trainData=vectorizer.fit_transform(trainData)
features=vectorizer.get_feature_names()
trainData=trainData.toarray()

# Initializing the Neural Network model
clf = MLPClassifier(hidden_layer_sizes=(3000, ), activation='identity',  max_iter=200)
# Fitting Neural Network model with trainData and trainTarget
clf.fit(trainData,trainTarget)

# print(trainData.shape)

# Analyzing with 5 iteration
for i in range(5):
    x_train, x_test, y_train, y_test = train_test_split(trainData, trainTarget, test_size=0.3)
    acuracy= clf.score(x_test,y_test)
    print("Accuracy is: ",acuracy,"\n")
print("------------------\n")
# Accuracy is:  1.0
clf = MLPClassifier(hidden_layer_sizes=(3000, ), activation='relu',  max_iter=200)
clf.fit(trainData,trainTarget)

print(trainData.shape)

# Analyzing with 5 iteration
for i in range(5):
    x_train, x_test, y_train, y_test = train_test_split(trainData, trainTarget, test_size=0.3)
    acuracy= clf.score(x_test,y_test)
    print("Accuracy is: ",acuracy,"\n")
print("------------------\n")
# Accuracy is:  1.0
clf = MLPClassifier(hidden_layer_sizes=(3000, ), activation='tanh',  max_iter=200)
clf.fit(trainData,trainTarget)

print(trainData.shape)

# Analyzing with 5 iteration
for i in range(5):
    x_train, x_test, y_train, y_test = train_test_split(trainData, trainTarget, test_size=0.3)
    acuracy= clf.score(x_test,y_test)
    print("Accuracy is: ",acuracy,"\n")
print("------------------\n")
# Accuracy is:  1.0 logistic
clf = MLPClassifier(hidden_layer_sizes=(3000, ), activation='logistic',  max_iter=200)
clf.fit(trainData,trainTarget)

print(trainData.shape)

# Analyzing with 5 iteration
for i in range(5):
    x_train, x_test, y_train, y_test = train_test_split(trainData, trainTarget, test_size=0.3)
    acuracy= clf.score(x_test,y_test)
    print("Accuracy is: ",acuracy,"\n")
print("------------------\n")

# Accuracy is:  1.0

# Accuracy is:  1.0

# Accuracy is:  1.0

# Accuracy is:  1.0

# Accuracy is:  1.0

# Decision: Due to lack of data set our model overfitted

