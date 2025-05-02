import matplotlib.pyplot as plt
from load_csv import load


def main():
    data_life = load("./life_expectancy_years.csv")
    di = load("./income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    val_income = []
    val_life = []
    for i in range(0, 195):
        country = di['country'].iloc[i]
        data = (di[di['country'] == country])
        val_income.append(data.iloc[0].values[101])
        data = (data_life[data_life['country'] == country])
        val_life.append(data.iloc[0].values[101])
    plt.plot(val_income, val_life, 'bo')
    plt.xscale('log')
    plt.xticks([300, 1000, 10000], ['300', '1k', '10k'])
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life expectancy")
    plt.title("1900")
    plt.show()


if __name__ == "__main__":
    main()
