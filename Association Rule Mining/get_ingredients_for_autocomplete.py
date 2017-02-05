import json
import operator

with open('C:\\Users\\Daniel\\PycharmProjects\\SpiceItUp\\jsons\\recipes.json', 'r') as json_file:
    recipes = json.load(json_file)

ingredients = {}
for recipe in recipes:
    for ingredient in recipe['filtered_ingredient_list']:
        ingredients[ingredient] = 0
for recipe in recipes:
    for ingredient in recipe['filtered_ingredient_list']:
        ingredients[ingredient] += 1

# filtered_ingredients = [x[0] for x in ingredients.items() if x[1] > 700]
filtered_ingredients = [x for x in ingredients.items() if x[1] > 50]
# sorted_ingredients = sorted(filtered_ingredients, key=lambda x: len(x.split()))#, reverse=True)
# for item in sorted_ingredients:
#     print(item)
for item in filtered_ingredients:
    if "chocolate" in item[0]:
        print(item)
# print(len(sorted_ingredients))
# print("pineapple" in sorted_ingredients)


# save to a json
# with open('C:\\Users\\Daniel\\PycharmProjects\\SpiceItUp\\autocomplete.json', 'w') as json_file:
#     json.dump(sorted_ingredients, json_file)


