import csv
import pandas as pd
import matplotlib.pyplot as plt
from sys import argv
from predict import estimatePrice
from accuracy import calculateAccuracy

global update_interval

iterations = 5000		# 1100
learningRate = 0.1		# 0.1 - 0.01
max_epsilon = 0.06		# 0.06
update_interval = 1


def normalizeData(data):
    data_norm = (data - data.min()) / (data.max() - data.min())
    return data_norm


def gradientDescent(t0, t1, data, learningRate):
    tmp0 = tmp1 = 0
    sum0 = sum1 = 0

    for i in range(len(data)):
        sum0 += (t0 + t1 * data.iloc[i].km) - data.iloc[i].price
        sum1 += (((t0 + t1 * data.iloc[i].km) -
                 data.iloc[i].price) * data.iloc[i].km)
    tmp0 = sum0 * learningRate / len(data)
    tmp1 = sum1 * learningRate / len(data)

    return t0 - tmp0, t1 - tmp1


def calcEpsilon(t0, old_t0):
    epsilon = t0 - old_t0
    return epsilon < max_epsilon and epsilon > -max_epsilon


def denormalizeThetas(data, t0n, t1n):
    price_diff = data['price'].max() - data['price'].min()
    mileage_diff = data['km'].max() - data['km'].min()
    t1 = t1n * price_diff / mileage_diff
    t0 = (t0n * price_diff + data['price'].min()) - (t1 * data['km'].min())
    return t0, t1


def saveThetas(t0, t1):
    with open("thetas.csv", "w") as wfile:
        csv.writer(wfile, delimiter=',').writerow([t0, t1])


def createGraph():
    plt.suptitle("ft_linear_regression", fontsize='16', fontweight='bold')
    plt.xlabel("Mileage", fontweight='bold')
    plt.ylabel("Price", fontweight='bold')
    plt.xlim([data['km'].min() - 10000, data['km'].max() + 10000])
    plt.ylim([data['price'].min() - 500, data['price'].max() + 500])
    plt.scatter(data.km, data.price, color="black")


def updateGraph(km_min, km_max, t0, t1, e):
    if e % update_interval == 0:
        acc = calculateAccuracy(t0, t1) * 100
        plt.title(f"epoch = {e}, m = {t1:.3f}, b = {t0:.0f}, acc = {acc:.2f}% auto = {auto_mode}")
        x_values = [km_min, km_max]
        y_values = [t0 + (t1 * km_min), t0 + (t1 * km_max)]
        reg_line = plt.plot(x_values, y_values, color="red")
        plt.pause(0.0001)
        reg_line.pop(0).remove()
        print(f"\rIteration {i}: "
              f"m = {t1:.3f}, "
              f"b = {t0:.3f}, "
              f"acc = {acc:.2f}%, "
              f"auto = {auto_mode}",
              end=''
              )


def saveGraph(km_min, km_max, t0, t1, e):
    acc = calculateAccuracy(t0, t1) * 100
    plt.title(f"epoch = {e}, m = {t1:.3f}, b = {t0:.0f}, acc = {acc:.2f}% auto = {auto_mode}")
    x_values = [km_min, km_max]
    y_values = [t0 + (t1 * km_min), t0 + (t1 * km_max)]
    plt.plot(x_values, y_values, color="red")
    plt.savefig("result.png")
    plt.show()


if __name__ == "__main__":
    old_t0 = 0
    t0n = t1n = 0
    try:
        data = pd.read_csv(argv[1], sep=',', header=0)
    except (FileNotFoundError, IndexError):
        print("Using default dataset")
        data = pd.read_csv("datasets/data.csv", sep=',', header=0)

    data_n = normalizeData(data)
    km_min = int(data['km'].min())
    km_max = int(data['km'].max()) + 1
    auto_mode = True if len(argv) > 1 and argv[len(argv) - 1] == "auto" else False

    createGraph()
    for i in range(iterations + 1):
        t0n, t1n = gradientDescent(t0n, t1n, data_n, learningRate)
        t0, t1 = denormalizeThetas(data, t0n, t1n)
        updateGraph(km_min, km_max, t0, t1, i)
        if auto_mode and calcEpsilon(t0, old_t0):
            break
        old_t0 = t0
        update_interval += 1 if (i + 1) % 75 == 0 else 0

    print(f"Iteration {i}: m = {t1:.3f}, b = {t0:.3f}")
    print(f"Finished at iteration {i}")
    saveGraph(km_min, km_max, t0, t1, i)
    saveThetas(t0, t1)
