# app.py untuk Streamlit Dashboard

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
products_df = pd.read_csv('olist_products_dataset.csv')
order_items_df = pd.read_csv('olist_order_items_dataset.csv')

# Menggabungkan dataset
merged_df = pd.merge(order_items_df, products_df, on='product_id')

# Pertanyaan 1: Produk dengan jumlah penjualan tertinggi
sales_by_category = merged_df.groupby('product_category_name')['order_item_id'].count().reset_index().sort_values(by='order_item_id', ascending=False)

# Pertanyaan 2: Rata-rata harga produk per kategori
avg_price_by_category = merged_df.groupby('product_category_name')['price'].mean().reset_index().sort_values(by='price', ascending=False)

# Streamlit App
st.title('E-commerce Data Analysis')

# Tampilkan pertanyaan 1
st.subheader('Jumlah Penjualan per Kategori Produk')
st.bar_chart(sales_by_category.set_index('product_category_name'))

# Tampilkan pertanyaan 2
st.subheader('Rata-rata Harga Produk per Kategori')
st.bar_chart(avg_price_by_category.set_index('product_category_name'))
