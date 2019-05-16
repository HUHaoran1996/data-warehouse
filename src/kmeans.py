import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def main():
    data = pd.read_csv("olap_export.txt", sep = "\t", engine='python', names=['country', 'education', '<=50K', '>50K'])
    data = data.fillna(0)
    data['all'] = data['<=50K'] + data['>50K']

    data['<=50K'] = data['<=50K'] / data['all']
    data['>50K'] = data['>50K'] / data['all']
    data = data.drop(['education'], axis=1)
    data = data.drop(['all'], axis=1)

    dataX = pd.DataFrame(data,columns = ['<=50K', '>50K'])
    #print(dataX)

    estimator = KMeans(n_clusters=5)
    estimator.fit(dataX)

    data['labels'] = estimator.labels_

    class_1 = ""
    class_2 = ""
    class_3 = ""
    class_4 = ""
    class_5 = ""

    for index, row in data.iterrows():
        if (row["labels"] == 0):
            if (class_1 != ""):
                class_1 += ", "
            class_1 += row["country"]
        elif (row["labels"] == 1):
            if (class_2 != ""):
                class_2 += ", "
            class_2 += row["country"]
        elif (row["labels"] == 2):
            if (class_3 != ""):
                class_3 += ", "
            class_3 += row["country"]
        elif (row["labels"] == 3):
            if (class_4 != ""):
                class_4 += ", "
            class_4 += row["country"]
        else:
            if (class_5 != ""):
                class_5 += ", "
            class_5 += row["country"]

    print("Country in class 1: " + class_1)
    print("Country in class 2: " + class_2)
    print("Country in class 3: " + class_3)
    print("Country in class 4: " + class_4)
    print("Country in class 5: " + class_5)

    x0 = data.loc[(data['labels'] == 0)]
    x1 = data.loc[(data['labels'] == 1)]
    x2 = data.loc[(data['labels'] == 2)]
    x3 = data.loc[(data['labels'] == 3)]
    x4 = data.loc[(data['labels'] == 4)]

    plt.scatter(x0['<=50K'], x0['>50K'], c="red", marker='o', label='label1')
    plt.scatter(x1['<=50K'], x1['>50K'], c="green", marker='*', label='label2')
    plt.scatter(x2['<=50K'], x2['>50K'], c="blue", marker='+', label='label3')
    plt.scatter(x3['<=50K'], x3['>50K'], c="yellow", marker='o', label='label4')
    plt.scatter(x4['<=50K'], x4['>50K'], c="black", marker='+', label='label5')

    plt.xlabel('ratio <= 50K')
    plt.ylabel('ratio > 50K')
    plt.legend(loc=2)
    plt.show()

if __name__ == '__main__':
    main()