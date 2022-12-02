import sqlite3

connection = sqlite3.connect('recipes.db')
cursor = connection.cursor()

cursor.execute("CREATE TABLE Recipes (recipe_name text, cooking_time integer, country_of_origin text)")

recipe_list =[
    ('Bahn Mi', 25, 'Vietnam'),
    ('Mushroom Risotto', 30, 'Italy'),
    ('Brown Beans with Chicken', 30, 'Surinam'),
    ('Danish Frikadell', 20, 'Denmark'),
    ('Chicken Satay', 30, 'Indonesian'),
    ('Korean Oven Chicken Wings', 60, 'Korea')    
]

cursor.executemany("INSERT INTO Recipes VALUES (?,?,?)", recipe_list)

#print rows of Recipes table 
for row in cursor.execute("SELECT * FROM Recipes"):
    print(row)

#print specific rows
# cursor.execute("SELECT * FROM Recipes WHERE country_of_origin=:x", {'x': 'Korea'})
# recipe_search = cursor.fetchall
# print(recipe_search)

cursor.execute("CREATE TABLE Diet (recipe_name text, type_of_diet text, allergies text)")
cursor.execute("INSERT INTO Diet VALUES (?,?,?)", ('Bahn Mi', 'Non-vegetarian', 'peanuts shellfish gluten'))
print("--------------------------------------------")
#print rows of Diet table 
for row in cursor.execute("SELECT * FROM Diet"):
    print(row)
connection.close()