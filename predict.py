import csv


def estimatePrice(thetas, mileage):
    return thetas[0] + (thetas[1] * mileage)


def getThetas():
    t = []
    try:
        with open("thetas.csv", "r") as file:
            for row in csv.reader(file, quoting=csv.QUOTE_NONNUMERIC):
                for cell in row:
                    t.append(cell)
    except FileNotFoundError:
        t = [0, 0]
    return t


def printEstimate(t):
    try:
        m = float(input("Insert mileage: "))
        if m > -1:
            p = estimatePrice(t, float(m))
            p = 0 if p < 0 else p
        print(f"{p:.2f}")
    except ValueError:
        print("Error")


if __name__ == '__main__':
    t = getThetas()
    printEstimate(t)
