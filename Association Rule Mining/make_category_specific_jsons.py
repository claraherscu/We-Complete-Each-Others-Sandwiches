import json
import operator

with open('C:\\Users\\Daniel\\PycharmProjects\\SpiceItUp\\recipes.json', 'r') as json_file:
    recipes = json.load(json_file)

desserts = []
appetizers = []
salads = []
meat_and_poultry = []
easy = []
soups_stews_chili = []
italian = []
drinks = []

for recipe in recipes:
    if "desserts" in recipe['categories']:
        desserts.append(recipe)
    if "appetizers and snacks" in recipe['categories']:
        appetizers.append(recipe)
    if "salad" in recipe['categories']:
        salads.append(recipe)
    if "meat and poultry" in recipe['categories']:
        meat_and_poultry.append(recipe)
    if "easy" in recipe['categories']:
        easy.append(recipe)
    if "soups, stews and chili" in recipe['categories']:
        soups_stews_chili.append(recipe)
    if "italian" in recipe['categories']:
        italian.append(recipe)
    if "drinks" in recipe['categories']:
        drinks.append(recipe)


# save the jsons
with open('C:\\Users\\Daniel\\PycharmProjects\\SpiceItUp\\desert_recipes.json', 'w') as json_file:
    json.dump(desserts, json_file)
with open('C:\\Users\\Daniel\\PycharmProjects\\SpiceItUp\\appetizer_recipes.json', 'w') as json_file:
    json.dump(appetizers, json_file)
with open('C:\\Users\\Daniel\\PycharmProjects\\SpiceItUp\\salad_recipes.json', 'w') as json_file:
    json.dump(salads, json_file)
with open('C:\\Users\\Daniel\\PycharmProjects\\SpiceItUp\\meat_and_poultry_recipes.json', 'w') as json_file:
    json.dump(meat_and_poultry, json_file)
with open('C:\\Users\\Daniel\\PycharmProjects\\SpiceItUp\\easy_recipes.json', 'w') as json_file:
    json.dump(easy, json_file)
with open('C:\\Users\\Daniel\\PycharmProjects\\SpiceItUp\\soups_stews_chili_recipes.json', 'w') as json_file:
    json.dump(soups_stews_chili, json_file)
with open('C:\\Users\\Daniel\\PycharmProjects\\SpiceItUp\\italian_recipes.json', 'w') as json_file:
    json.dump(italian, json_file)
with open('C:\\Users\\Daniel\\PycharmProjects\\SpiceItUp\\drink_recipes.json', 'w') as json_file:
    json.dump(drinks, json_file)


