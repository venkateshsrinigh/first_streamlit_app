import streamlit

streamlit.title('My Parents New Heathly Diner')

sreamlit.header('Breakfast Favorites')
sreamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
sreamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
sreamlit.text('🐔 Hard-Boiled Free-Range Egg')
sreamlit.text('🥑🍞 Avacado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
