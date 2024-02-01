# Tolong tampilkan data persebaran dari product_weight_gram penjualan cabang tadi ya,” ujar Andra kembali.
import pandas as pd

order_df = pd.read_csv('order.csv')

# Standar variasi product_weight_gram
print(order_df.loc[:, "product_weight_gram"].std())

# Variansi product_weight_gram
print(order_df.loc[:, "product_weight_gram"].var())