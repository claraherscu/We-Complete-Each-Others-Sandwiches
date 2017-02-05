import json
import operator

# load the data into the variables:
with open('C:\\Users\\Daniel\\PycharmProjects\\SpiceItUp\\allRecipesRecipes_2.json', 'r') as json_file:
    all_recipes = json.load(json_file) # list of dictionaries from the crawler
with open('C:\\Users\\Daniel\\PycharmProjects\\SpiceItUp\\foodNetworkRecipes_2.json', 'r') as json_file:
    food_network = json.load(json_file) # list of dictionaries from the crawler

categories = {}
for recipe in all_recipes:
    for category in recipe['categories']:
        categories[category] = 0
for recipe in food_network:
    for category in recipe['categories']:
        categories[category] = 0

for recipe in all_recipes:
    for category in recipe['categories']:
        categories[category] += 1
for recipe in food_network:
    for category in recipe['categories']:
        categories[category] += 1

sorted_items = sorted(categories.items(), key = operator.itemgetter(1), reverse=True)
for item in sorted_items:
    print(item)


# join the recipes together:
all_of_the_recipes = all_recipes + food_network

# fix the json:
for recipe in all_of_the_recipes:

    # make categories lower case:
    recipe['categories'] = [x.lower() for x in recipe['categories']]

    # fix the ratings of foodNetwork:
    if recipe['recipe_rating'] == "default":
        recipe['recipe_rating'] = 10
        recipe['recipe_review_count'] = 0

    # join the similar categories:
    if "dessert" in recipe['categories']:
        recipe['categories'].append('desserts')
    if "appetizer" in recipe['categories']:
        recipe['categories'].append('appetizers and snacks')
    if "chicken" in recipe['categories'] or "beef" in recipe['categories']:
        recipe['categories'].append('meat and poultry')
    if "quick and easy" in recipe['categories']:
        recipe['categories'].append('easy')
    if "soup" in recipe['categories']:
        recipe['categories'].append('soups, stews and chili')
    if "beverages" in recipe['categories']:
        recipe['categories'].append('drinks')

with open('C:\\Users\\Daniel\\PycharmProjects\\SpiceItUp\\recipes.json', 'w') as json_file:
    json.dump(all_of_the_recipes, json_file) # list of dictionaries from the crawler
