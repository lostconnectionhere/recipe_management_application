import sqlite3
import pandas as pd

connection = sqlite3.connect('recipes_database')
cursor = connection.cursor()

cursor.execute('''
                CREATE TABLE IF NOT EXISTS recipes
                ([recipe_id] INTEGER PRIMARY KEY, [recipe_name] VARCHAR(30))
''')

cursor.execute('''
                CREATE TABLE IF NOT EXISTS contributers
                ([recipe_id] INTEGER PRIMARY KEY, [contributer_name] VARCHAR(30))
''')

cursor.execute('''
                INSERT INTO recipes (recipe_id, recipe_name) VALUES
                (1,'Pasta Carbonara'),
                (2,'Pumpkin Soup'),
                (3,'Green Curry with Rice'),
                (4,'Korean Chicken Wings'),
                (5,'Pratha')
''')

cursor.execute('''
                INSERT INTO contributers (recipe_id, contributer_name) VALUES
                (1,'Roz, S'),
                (2,'Nasrin, F'),
                (3,'Anna, F'),
                (4,'Julia, G'),
                (5,'Tom, S')
''')

connection.commit()

cursor.execute('''
                SELECT
                a.recipe_name,
                b.contributer_name
                FROM recipes a
                LEFT JOIN contributers b ON a.recipe_id = b.recipe_id
                ''')

df = pd.DataFrame(cursor.fetchall(), columns=['recipe_name','contributer_name'])
print (df)