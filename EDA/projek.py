# tugasnya

# Saya sedang rapat dan bahan ini ditunggu dalam pembahasan cabang supermarket kita. Berikut ya detailnya:

# 1. Median price yang dibayar customer dari masing-masing metode pembayaran.
# 2. Tentukan metode pembayaran yang memiliki basket size (rataan median price) terbesar.
# 3. Ubah freight_value menjadi shipping_cost dan cari shipping_cost termahal dari data penjualan tersebut menggunakan sort.
# 4. Untuk setiap product_category_name, berapa rata-rata weight produk tersebut dan standar deviasi mana yang terkecil dari weight tersebut,
# 5. Buat histogram quantity penjualan dari dataset tersebut untuk melihat persebaran quantity penjualan tersebut dengan bins = 5 dan figsize= (4,5)

# catatan pada point 4, hasil dari analisinya akan di gunakan oleh kepala cabang untuk menyusun strategi free ongkir

# import library yg di gunakan
import pandas as pd
import matplotlib.pyplot as plt

# memangil data set dan di simpan pada variabel order_df
order_df = pd.read_csv('order.csv')

# mencari median price menyandingkannya dengan metode pembayara
median_price = order_df['price'].groupby(order_df['payment_type']).median()
print(median_price)

# menggubah nama kolom freight_value dengan shipping_cost
order_df.rename(columns={'freight_value': 'shipping_cost'}, inplace=True)
# mencari penjualan termahal dari shipping_cost dengan sort
sort_value = order_df.sort_values(by='shipping_cost', ascending=0)
print(sort_value)
print(sort_value['shipping_cost'])

# mencari rata-rata dari product_name menyandingkan dengan product_weight_gram
print('\n mean \n')
mean_value = order_df['product_weight_gram'].groupby(order_df['product_category_name']).mean()
print(mean_value)
# mencari standar deviasi dari product_name menyandingkan dengan product_weight_gram
print('\n Standar Deviansi \n')
std_value = order_df['product_weight_gram'].groupby(order_df['product_category_name']).std()
print(std_value)

# membuat visualisasi pada columns columns
order_df[['quantity']].hist(figsize=(4, 5), bins=5)
plt.show()