import matplotlib.pyplot as plt
import matplotlib.ticker
from load_csv import load


def millions(x, pos):
    return f'{x * 1e-6:.0f}M'  # or use :.1f for 1 decimal place


def main():
    data = load("./population_total.csv")
    df1 = (data[data['country'] == 'Turkey'])
    df2 = (data[data['country'] == 'France'])
    print("df1:", df1, "\n--------df2:", df2)
    pop1 = [float(y[:-1]) for y in ((df1.iloc[0].values[1:252]))]
    pop2 = [float(y[:-1]) for y in df2.iloc[0].values[1:252]]
    years1 = [int(y) for y in df1.iloc[0].keys()[1:252]]
    years2 = [int(y) for y in df2.iloc[0].keys()[1:252]]
    plt.plot(years1, [x*1000000 for x in pop1])
    plt.plot(years2, [x*1000000 for x in pop2])
    plt.legend(['Turkey', 'France'], loc=4)
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.title("Population Projections")
    formatter = matplotlib.ticker.FuncFormatter(millions)
    plt.gca().yaxis.set_major_formatter(formatter)
    plt.show()


if __name__ == "__main__":
    main()
