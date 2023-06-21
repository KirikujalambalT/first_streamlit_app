import streamlit
streamlit.title('My New Coding Challenge')
streamlit.header('My skills')
streamlit.text('Python')
streamlit.text('SQL')
streamlit.text('Power BI')
streamlit.text('Tableau')            
streamlit.title('My New Healthy Diner')
streamlit.header('My Breakfast menu')
streamlit.text('🥣Omega 3 & Blueberry oatmeal')
streamlit.text('🥗Kale, Spinach and Rocket smoothie')
streamlit.text('🐔Hard-boiled Free range Egg')  
streamlit.text('🥑🍞Avacado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
# Display the table on the page.
streamlit.dataframe(my_fruit_list)
