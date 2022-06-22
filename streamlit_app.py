import pandas as pd
import streamlit as sl

sl.title('First Streamlit App!')

sl.header('A header')

sl.text('Some text 🥑')

sl.header('🥭 Another Header 🥝')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
sl.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
sl.dataframe(my_fruit_list)