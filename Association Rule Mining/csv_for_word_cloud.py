import json
import operator

with open('C:\\Users\\Daniel\\PycharmProjects\\SpiceItUp\\jsons\\recipes.json', 'r') as json_file:
    recipes = json.load(json_file)
with open('C:\\Users\\Daniel\\PycharmProjects\\SpiceItUp\\jsons\\appetizer_recipes.json', 'r') as json_file:
    appetizer_recipes = json.load(json_file)
with open('C:\\Users\\Daniel\\PycharmProjects\\SpiceItUp\\jsons\\desert_recipes.json', 'r') as json_file:
    desert_recipes = json.load(json_file)
with open('C:\\Users\\Daniel\\PycharmProjects\\SpiceItUp\\jsons\\drink_recipes.json', 'r') as json_file:
    drink_recipes = json.load(json_file)
with open('C:\\Users\\Daniel\\PycharmProjects\\SpiceItUp\\jsons\\easy_recipes.json', 'r') as json_file:
    easy_recipes = json.load(json_file)
with open('C:\\Users\\Daniel\\PycharmProjects\\SpiceItUp\\jsons\\italian_recipes.json', 'r') as json_file:
    italian_recipes = json.load(json_file)
with open('C:\\Users\\Daniel\\PycharmProjects\\SpiceItUp\\jsons\\meat_and_poultry_recipes.json', 'r') as json_file:
    meat_and_poultry_recipes = json.load(json_file)
with open('C:\\Users\\Daniel\\PycharmProjects\\SpiceItUp\\jsons\\salad_recipes.json', 'r') as json_file:
    salad_recipes = json.load(json_file)
with open('C:\\Users\\Daniel\\PycharmProjects\\SpiceItUp\\jsons\\soups_stews_chili_recipes.json', 'r') as json_file:
    soups_stews_chili_recipes = json.load(json_file)

recipes_ingredients = {}
for recipe in recipes:
    for ingredient in recipe['filtered_ingredient_list']:
        recipes_ingredients[ingredient] = 0
for recipe in recipes:
    for ingredient in recipe['filtered_ingredient_list']:
        recipes_ingredients[ingredient] += 1
filtered_ingredients = recipes_ingredients.items()
sorted_ingredients = sorted(filtered_ingredients, key = operator.itemgetter(1), reverse=True)
sorted_recipes_ingredients = sorted_ingredients[0:99]

appetizer_recipes_ingredients = {}
for recipe in appetizer_recipes:
    for ingredient in recipe['filtered_ingredient_list']:
        appetizer_recipes_ingredients[ingredient] = 0
for recipe in appetizer_recipes:
    for ingredient in recipe['filtered_ingredient_list']:
        appetizer_recipes_ingredients[ingredient] += 1
filtered_ingredients = appetizer_recipes_ingredients.items()
sorted_ingredients = sorted(filtered_ingredients, key = operator.itemgetter(1), reverse=True)
sorted_appetizer_recipes_ingredients = sorted_ingredients[0:99]

desert_recipes_ingredients = {}
for recipe in desert_recipes:
    for ingredient in recipe['filtered_ingredient_list']:
        desert_recipes_ingredients[ingredient] = 0
for recipe in desert_recipes:
    for ingredient in recipe['filtered_ingredient_list']:
        desert_recipes_ingredients[ingredient] += 1
filtered_ingredients = desert_recipes_ingredients.items()
sorted_ingredients = sorted(filtered_ingredients, key = operator.itemgetter(1), reverse=True)
sorted_desert_recipes_ingredients = sorted_ingredients[0:99]

drink_recipes_ingredients = {}
for recipe in drink_recipes:
    for ingredient in recipe['filtered_ingredient_list']:
        drink_recipes_ingredients[ingredient] = 0
for recipe in drink_recipes:
    for ingredient in recipe['filtered_ingredient_list']:
        drink_recipes_ingredients[ingredient] += 1
filtered_ingredients = drink_recipes_ingredients.items()
sorted_ingredients = sorted(filtered_ingredients, key = operator.itemgetter(1), reverse=True)
sorted_drink_recipes_ingredients = sorted_ingredients[0:99]

easy_recipes_ingredients = {}
for recipe in easy_recipes:
    for ingredient in recipe['filtered_ingredient_list']:
        easy_recipes_ingredients[ingredient] = 0
for recipe in easy_recipes:
    for ingredient in recipe['filtered_ingredient_list']:
        easy_recipes_ingredients[ingredient] += 1
filtered_ingredients = easy_recipes_ingredients.items()
sorted_ingredients = sorted(filtered_ingredients, key = operator.itemgetter(1), reverse=True)
sorted_easy_recipes_ingredients = sorted_ingredients[0:99]

italian_recipes_ingredients = {}
for recipe in italian_recipes:
    for ingredient in recipe['filtered_ingredient_list']:
        italian_recipes_ingredients[ingredient] = 0
for recipe in italian_recipes:
    for ingredient in recipe['filtered_ingredient_list']:
        italian_recipes_ingredients[ingredient] += 1
filtered_ingredients = italian_recipes_ingredients.items()
sorted_ingredients = sorted(filtered_ingredients, key = operator.itemgetter(1), reverse=True)
sorted_italian_recipes_ingredients = sorted_ingredients[0:99]

meat_and_poultry_recipes_ingredients = {}
for recipe in meat_and_poultry_recipes:
    for ingredient in recipe['filtered_ingredient_list']:
        meat_and_poultry_recipes_ingredients[ingredient] = 0
for recipe in meat_and_poultry_recipes:
    for ingredient in recipe['filtered_ingredient_list']:
        meat_and_poultry_recipes_ingredients[ingredient] += 1
filtered_ingredients = meat_and_poultry_recipes_ingredients.items()
sorted_ingredients = sorted(filtered_ingredients, key = operator.itemgetter(1), reverse=True)
sorted_meat_and_poultry_recipes_ingredients = sorted_ingredients[0:99]

salad_recipes_ingredients = {}
for recipe in salad_recipes:
    for ingredient in recipe['filtered_ingredient_list']:
        salad_recipes_ingredients[ingredient] = 0
for recipe in salad_recipes:
    for ingredient in recipe['filtered_ingredient_list']:
        salad_recipes_ingredients[ingredient] += 1
filtered_ingredients = salad_recipes_ingredients.items()
sorted_ingredients = sorted(filtered_ingredients, key = operator.itemgetter(1), reverse=True)
sorted_salad_recipes_ingredients = sorted_ingredients[0:99]

soups_stews_chili_recipes_ingredients = {}
for recipe in soups_stews_chili_recipes:
    for ingredient in recipe['filtered_ingredient_list']:
        soups_stews_chili_recipes_ingredients[ingredient] = 0
for recipe in soups_stews_chili_recipes:
    for ingredient in recipe['filtered_ingredient_list']:
        soups_stews_chili_recipes_ingredients[ingredient] += 1
filtered_ingredients = soups_stews_chili_recipes_ingredients.items()
sorted_ingredients = sorted(filtered_ingredients, key = operator.itemgetter(1), reverse=True)
sorted_soups_stews_chili_recipes_ingredients = sorted_ingredients[0:99]



# save the csvs
# with open('C:\\Users\\Daniel\\PycharmProjects\\SpiceItUp\\csv for wordclouds\\ingredients.csv', 'w') as csv_file:
#     for item in sorted_recipes_ingredients:
#         csv_file.write(str(item[1]) + "," + item[0] + "\n")
# with open('C:\\Users\\Daniel\\PycharmProjects\\SpiceItUp\\csv for wordclouds\\appetizer_ingredients.csv', 'w') as csv_file:
#     for item in sorted_appetizer_recipes_ingredients:
#         csv_file.write(str(item[1]) + "," + item[0] + "\n")
# with open('C:\\Users\\Daniel\\PycharmProjects\\SpiceItUp\\csv for wordclouds\\desert_ingredients.csv', 'w') as csv_file:
#     for item in sorted_desert_recipes_ingredients:
#         csv_file.write(str(item[1]) + "," + item[0] + "\n")
# with open('C:\\Users\\Daniel\\PycharmProjects\\SpiceItUp\\csv for wordclouds\\drink_ingredients.csv', 'w') as csv_file:
#     for item in sorted_drink_recipes_ingredients:
#         csv_file.write(str(item[1]) + "," + item[0] + "\n")
# with open('C:\\Users\\Daniel\\PycharmProjects\\SpiceItUp\\csv for wordclouds\\easy_ingredients.csv', 'w') as csv_file:
#     for item in sorted_easy_recipes_ingredients:
#         csv_file.write(str(item[1]) + "," + item[0] + "\n")
# with open('C:\\Users\\Daniel\\PycharmProjects\\SpiceItUp\\csv for wordclouds\\italian_ingredients.csv', 'w') as csv_file:
#     for item in sorted_italian_recipes_ingredients:
#         csv_file.write(str(item[1]) + "," + item[0] + "\n")
# with open('C:\\Users\\Daniel\\PycharmProjects\\SpiceItUp\\csv for wordclouds\\meat_and_poultry_ingredients.csv', 'w') as csv_file:
#     for item in sorted_meat_and_poultry_recipes_ingredients:
#         csv_file.write(str(item[1]) + "," + item[0] + "\n")
# with open('C:\\Users\\Daniel\\PycharmProjects\\SpiceItUp\\csv for wordclouds\\salad_ingredients.csv', 'w') as csv_file:
#     for item in sorted_salad_recipes_ingredients:
#         csv_file.write(str(item[1]) + "," + item[0] + "\n")
# with open('C:\\Users\\Daniel\\PycharmProjects\\SpiceItUp\\csv for wordclouds\\soups_stews_chili_ingredients.csv', 'w') as csv_file:
#     for item in sorted_soups_stews_chili_recipes_ingredients:
#         csv_file.write(str(item[1]) + "," + item[0] + "\n")

with open('C:\\Users\\Daniel\\PycharmProjects\\SpiceItUp\\csv for wordclouds\\all_ingredients.txt', 'w') as csv_file:
    for item in sorted_recipes_ingredients:
        for i in range(item[1]):
            x = str(item[0]).replace(' ','_')
            csv_file.write(x + "\n")
with open('C:\\Users\\Daniel\\PycharmProjects\\SpiceItUp\\csv for wordclouds\\drink_ingredients.txt', 'w') as csv_file:
    for item in sorted_drink_recipes_ingredients:
        for i in range(item[1]):
            x = str(item[0]).replace(' ','_')
            csv_file.write(x + "\n")
with open('C:\\Users\\Daniel\\PycharmProjects\\SpiceItUp\\csv for wordclouds\\appetizer_ingredients.txt', 'w') as csv_file:
    for item in sorted_appetizer_recipes_ingredients:
        for i in range(item[1]):
            x = str(item[0]).replace(' ','_')
            csv_file.write(x + "\n")
with open('C:\\Users\\Daniel\\PycharmProjects\\SpiceItUp\\csv for wordclouds\\desert_ingredients.txt', 'w') as csv_file:
    for item in sorted_desert_recipes_ingredients:
        for i in range(item[1]):
            x = str(item[0]).replace(' ','_')
            csv_file.write(x + "\n")
with open('C:\\Users\\Daniel\\PycharmProjects\\SpiceItUp\\csv for wordclouds\\easy_ingredients.txt', 'w') as csv_file:
    for item in sorted_easy_recipes_ingredients:
        for i in range(item[1]):
            x = str(item[0]).replace(' ','_')
            csv_file.write(x + "\n")
with open('C:\\Users\\Daniel\\PycharmProjects\\SpiceItUp\\csv for wordclouds\\italian_ingredients.txt', 'w') as csv_file:
    for item in sorted_italian_recipes_ingredients:
        for i in range(item[1]):
            x = str(item[0]).replace(' ','_')
            csv_file.write(x + "\n")
with open('C:\\Users\\Daniel\\PycharmProjects\\SpiceItUp\\csv for wordclouds\\meat_and_poultry_ingredients.txt', 'w') as csv_file:
    for item in sorted_meat_and_poultry_recipes_ingredients:
        for i in range(item[1]):
            x = str(item[0]).replace(' ','_')
            csv_file.write(x + "\n")
with open('C:\\Users\\Daniel\\PycharmProjects\\SpiceItUp\\csv for wordclouds\\salad_ingredients.txt', 'w') as csv_file:
    for item in sorted_salad_recipes_ingredients:
        for i in range(item[1]):
            x = str(item[0]).replace(' ','_')
            csv_file.write(x + "\n")
with open('C:\\Users\\Daniel\\PycharmProjects\\SpiceItUp\\csv for wordclouds\\soups_stews_chili_ingredients.txt', 'w') as csv_file:
    for item in sorted_soups_stews_chili_recipes_ingredients:
        for i in range(item[1]):
            x = str(item[0]).replace(' ','_')
            csv_file.write(x + "\n")
