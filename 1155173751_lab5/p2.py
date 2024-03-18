import csv
import numpy as np
import matplotlib.pyplot as plt

def load_csv_data(file_name: str) -> tuple[list, list]:
    dates = []
    closed_prices = []

    with open(file_name, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip the header row

        for row in csv_reader:
            date = row[0]
            closed_price = float(row[1])

            dates.append(date)
            closed_prices.append(closed_price)

    return dates, closed_prices
  

def compute_sma20(closed_prices: list) -> list:
    sma20 = [None] * 19
    for i in range(19, len(closed_prices)):
        prices_slice = closed_prices[i - 19 : i + 1]
        sma = np.mean(prices_slice)
        sma20.append(sma)
    return sma20


def compute_std20(closed_prices: list) -> list:
    std20 = [None] * 19
    for i in range(19, len(closed_prices)):
        prices_slice = closed_prices[i - 19 : i + 1]
        std = np.std(prices_slice)
        std20.append(std)
    return std20


def compute_bollinger_band(closed_prices: np.ndarray) -> tuple[list, list]:
    sma20 = compute_sma20(closed_prices)
    std20 = compute_std20(closed_prices)
    upper_bb = [None] * 19  # Replace the first 19 days' values with None
    lower_bb = [None] * 19  # Replace the first 19 days' values with None

    for i in range(19, len(closed_prices)):
        upper_band = sma20[i] + (2 * std20[i])
        lower_band = sma20[i] - (2 * std20[i])
        upper_bb.append(upper_band)
        lower_bb.append(lower_band)

    return upper_bb, lower_bb


dates, closed_prices = load_csv_data("HSBC2023.csv")
closed_prices = np.array(closed_prices)
sma20 = compute_sma20(closed_prices)
upper_bb, lower_bb = compute_bollinger_band(closed_prices)

plt.figure(figsize=(10, 6))

plt.plot(dates, closed_prices, color='blue', label='Closed Price')
plt.plot(dates, sma20, color='green', label='SMA-20')
plt.plot(dates, upper_bb, color='purple', label='Upper Bollinger Band')
plt.plot(dates, lower_bb, color='orange', label='Lower Bollinger Band')

plt.xticks(rotation=45)
plt.xticks(dates[::20])
plt.legend()
plt.tight_layout()
plt.savefig("HSBC2023.png")
