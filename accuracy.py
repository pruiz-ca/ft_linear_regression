import pandas as pd
from predict import estimatePrice, getThetas


def explainedVariance(data, t):
    var = 0
    for row in data.iterrows():
        predicted = estimatePrice(t, row[1][0])
        var += (row[1][1] - predicted) ** 2
    return var


def totalVariance(data, t):
    var = 0
    mean = data['price'].mean()
    for row in data.iterrows():
        var += (row[1][1] - mean) ** 2
    return var


def calculateAccuracy(*args):
    if (len(args) == 2):
        t = [args[0], args[1]]
    else:
        t = getThetas()
    data = pd.read_csv("datasets/data.csv", sep=',', header=0)
    rss = explainedVariance(data, t)
    tss = totalVariance(data, t)
    r_squared = 1 - (rss / tss)
    r_squared = 0 if r_squared < 0 else r_squared
    return r_squared


if __name__ == "__main__":
    acc = calculateAccuracy() * 100
    print(f"Accuracy of prediction model is {acc:.1f}%")
