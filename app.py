from flask import Flask, jsonify, request
from http import HTTPStatus

app = Flask(__name__)

recipes = [
    {
        'id': 1,
        'name': 'Pasta Funghi',
        'description': 'A creamy pasta funghi that is easy to make.'
    },
    {
        'id': 2,
        'name': 'Puff Pastry with Goat Cheese',
        'description': 'Soft Goat cheese wrapped in puff pastry with honey and walnuts.'
    }
]


@app.route('/recipes', methods=['GET'])
def get_recipes():
    return jsonify({'data': recipes})


@app.route('/recipes/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    recipe = next((recipe for recipe in recipes if recipe['id'] == recipe_id), None)

    if recipe:
        return jsonify(recipe)

    return jsonify({'message': 'recipe not found'}), HTTPStatus.NOT_FOUND


@app.route('/recipes', methods=['POST'])
def create_recipe():
    data = request.get_json()

    name = data.get('name')
    description = data.get('description')

    recipe = {
        'id': len(recipes) + 1,
        'name': name,
        'description': description
    }

    recipes.append(recipe)

    return jsonify(recipe), HTTPStatus.CREATED


@app.route('/recipes/<int:recipe_id>', methods=['PUT'])
def update_recipe(recipe_id):
    recipe = next((recipe for recipe in recipes if recipe['id'] == recipe_id), None)

    if not recipe:
        return jsonify({'message': 'recipe not found'}), HTTPStatus.NOT_FOUND

    data = request.get_json()

    recipe.update(
        {
            'name': data.get('name'),
            'description': data.get('description')
        }
    )

    return jsonify(recipe)


if __name__ == '__main__':
    app.run()