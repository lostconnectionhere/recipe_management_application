import sqlite3

connection = sqlite3.connect('recipes.db')
cursor = connection.cursor()

cursor.execute("CREATE TABLE Recipes (recipe_name text, cooking_time integer, country_of_origin text")

recipe_list =[
    ('Bahn Mi', 25, 'Vietnam'),
    ('Mushroom Risotto', 30, 'Italy'),
    ('Brown Beans with Chicken', 30, 'Surinam'),
    ('Danish Frikadell', 20, 'Denmark'),
    ('Chicken Satay', 30, 'Indonesian'),
    ('Korean Oven Chicken Wings', 60, 'Korea')    
]

cursor.executemany("insert into Recipes values (?,?,?)", recipe_list)

connection.close()