import matplotlib.pyplot as plt
from load_csv import load
import pandas as pd


def main():
    data_table = load("./life_expectancy_years.csv")
    campus = data_table[data_table['country'] == 'Turkey']
    print(campus)
    years = list(campus.iloc[0].keys()[1:])
    #casting into numeric data
    years = [int(y) for y in years]
    age = campus.iloc[0].values[1:]
    age = [int(a) for a in age]
    plt.figure(1)
    plt.plot(years, age)
    #set ticks
    tick_years = list(range(min(years), max(years)+1, 40))
    plt.xticks(tick_years)
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.title("Turkey Life expectancy Projections")
    plt.show()


if __name__=="__main__":
    main()
