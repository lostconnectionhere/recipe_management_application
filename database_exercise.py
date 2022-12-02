import sqlite3

connection = sqlite3.connect('recipes.db')

recipe_list =[
    ('Bahn Mi', 25, 'Vietnam'),
    ('Mushroom Risotto', 30, 'Italy'),
    ('Brown Beans with Chicken', 30, 'Surinam'),
    ('Danish Frikadell', 20, 'Denmark'),
    ('Chicken Satay', 30, 'Indonesian'),
    ('Korean Oven Chicken Wings', 60, 'Korea')    
]

connection.close()