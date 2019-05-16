import pandas as pd
import matplotlib.pyplot as plt

def main():
    data = pd.read_csv("olap_export.txt", sep = "\t", engine='python', names=['country', 'education', '<=50K', '>50K'])
    data = data.fillna(0)
    data['all'] = data['<=50K'] + data['>50K']

    data['<=50K'] = data['<=50K'] / data['all']
    data['>50K'] = data['>50K'] / data['all']
    print(data)
    data.plot.scatter(x='<=50K', y='>50K', c = "red", marker='o');
    plt.xlabel('ratio <= 50K')
    plt.ylabel('ratio > 50K')
    plt.show()


if __name__ == '__main__':
    main()