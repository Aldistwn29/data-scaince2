import numpy as np
import pandas as pd

raw_data = pd.read_csv('dataset_statistic.csv', sep=";")

# menghitung rerata dan median 'Pendapatan' dan 'Harga'
print(raw_data[['Pendapatan', 'Harga']].agg(['mean', 'median']))

# menghitung mean dan median Pendapatan, Harga dari setiap produk
print(raw_data[['Pendapatan', 'Harga', 'Produk']].groupby('Produk').agg(['mean', 'median']))