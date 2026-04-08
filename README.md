# IowaHousePrices

Single-neuron linear regression model that predicts Iowa home sale prices from square footage.

## Overview

This project uses Keras to build the simplest possible neural network — a single Dense neuron — to fit a linear regression line through Iowa housing data. It reads square footage and sale price pairs from a CSV file, trains for 30 epochs, plots the data alongside the predicted regression line, and then prints a price estimate for a given square footage value (default: 2000 sq ft).

The goal is a minimal, readable example of how Keras can be used for numerical regression on tabular data.

## How to Run

1. Install dependencies:

   ```bash
   pip install keras matplotlib pandas
   ```

2. Run the script:

   ```bash
   python main.py
   ```

   The script reads `prices.csv` from the current directory, trains the model, displays a scatter plot with the regression line, and prints a predicted price for 2000 square feet.

## Dependencies

- Python 3.x
- [Keras](https://keras.io/)
- [pandas](https://pandas.pydata.org/)
- [matplotlib](https://matplotlib.org/)

The `prices.csv` file must be present in the same directory as `main.py`. It requires two columns: `SquareFeet` and `SalePrice`.

## License

MIT License
