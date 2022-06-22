import pandas as pd
import streamlit as sl

sl.title('First Streamlit App!')

sl.header('A header')

sl.text('Some text 🥑')

sl.header('🥭 Another Header 🥝')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

sl.dataframe(my_fruit_list)