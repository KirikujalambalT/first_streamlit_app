import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
            
streamlit.title('My New Healthy Diner')
streamlit.header('My Breakfast menu')
streamlit.text('🥣Omega 3 & Blueberry oatmeal')
streamlit.text('🥗Kale, Spinach and Rocket smoothie')
streamlit.text('🐔Hard-boiled Free range Egg')  
streamlit.text('🥑🍞Avacado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
# Display the table on the page.
streamlit.dataframe(fruits_to_show)

#create the repeatable code block(called function)
def get_fruityvice_data(this_fruit_choice):
            fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
            fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
            return fruityvice_normalized

#New section to display fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")
try:
            fruit_choice = streamlit.text_input('What fruit would you like information about?')
            if not fruit_choice:
                        streamlit.error("Please select a fruit to get a information")
            else:
                        back_from_function = get_fruityvice_data(fruit_choice)
                        streamlit.dataframe(back_from_function)
except URLError as e:
            streamlit.error()                        

#streamlit.write('The user entered ', fruit_choice)
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
# take the json version of response and normalize it
#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# Output it the screen as a table
#streamlit.dataframe(fruityvice_normalized)

#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#my_cur = my_cnx.cursor()
#my_cur.execute("SELECT * from fruit_load_list")
#my_data_rows = my_cur.fetchall()

#streamlit.header("The fruit load list contains:")
#snowflake related functions
def get_fruit_load_list():
            with my_cnx.cursor() as my_cur:
                        my_cur.execute("SELECT * from fruit_load_list")
                        return my_cur.fetchall()

#streamlit.stop()

#Allow the end user to add fruit to the list
def insert_row_snowflake(new_fruit):
            with my_cnx.cursor() as my_cur:
                        my_cur.execute("insert into fruit_load_list values ('" + new_fruit + "')")
                        return "Thanks for adding " + new_fruit
                        
add_my_fruit = streamlit.text_input('What fruit would you like add?')
if streamlit.button('Add a Fruit to the List'):
            my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
            back_from_function = insert_row_snowflake(add_my_fruit)
            streamlit.text(back_from_function)

#add a button to load the fruit 
streamlit.header("View Our Fruit List - Add Your Favorites")
if streamlit.button('Get Fruit List'):
            my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
            my_data_rows = get_fruit_load_list()
            my_cnx.close()
            streamlit.dataframe(my_data_rows)
            
#streamlit.write('Thanks for adding', add_fruit)










