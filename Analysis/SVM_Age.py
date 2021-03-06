# #Analysis with Age using Support Vector Machine
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

# Initializing Training and Target data array
trainData =[]
trainTarget=[]
fileName="Facebook posts.csv"
# Openning the data set file
file = open(fileName, "r",encoding="utf8")
# Reading the data set file
data = csv.reader(file)
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
    trainTarget.append(int(col[4]))

# Creating input feature vector using TfidfVectorizer
vectorizer=TfidfVectorizer(use_idf=True, token_pattern='[^ \n,".\':()ঃ‘?’।“”!;a-zA-Z0-9#০১২৩৪৫৬৭৮৯*&_><+=%$-`~|^·]+') #০১২৩৪৫৬৭৮৯
trainData=vectorizer.fit_transform(trainData)
features=vectorizer.get_feature_names()

# Initializing the Support Vector Machine model
model = svm.SVC(kernel='linear', C=1, gamma=1)

# Analyzing with 5 iteration
for i in range(5):
    x_train, x_test, y_train, y_test = train_test_split(trainData, trainTarget, test_size=0.3)

    # Fitting Support Vector Machine model with trainData and trainTarget
    model.fit(x_train, y_train)
    predicted2 = model.predict(x_test)
    count2 = 0
    for i in range(len(predicted2)):
        if (predicted2[i]-y_test[i])==0:
            count2 += 1
    print(float(count2)/float(len(predicted2)))

# Accuracy:
# 0.125
# 0.125
# 0.25
# 0.25
# 0.125

# Decision:
# Due to lack of data set it was difficult for us to classify with our classifier. Further, SVM is a binary classifier. So we need to train with more data set and set age range like 18-21, 22 - 25 etc.