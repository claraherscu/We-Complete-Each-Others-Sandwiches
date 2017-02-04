# in this file we implement the A-Priori algorithm, in order to find the
# frequent itemsets from the recipes, taking the weights into account.

import json


# a function to augment the ratings so that higher ratings have a bigger
# effect on the weights of the recipes. given a rating, the function returns
# the augmented rating (float)
def augment_rating(rating):
    return rating ** 2


# load the data into the variables:
with open('C:\\Users\\Daniel\\PycharmProjects\\SpiceItUp\\XXX.json', 'r') as json_file:
    raw_recipes = json.load(json_file) # list of dictionaries from the crawler

# calculate the recipe weights:
recipes = []
for recipe in raw_recipes:
    recipe_dict = {}
    recipe_dict['name'] = recipe['recipe_name']
    recipe_dict['ingredients'] = set(recipe['recipe_ingredient_list'])
    recipe_dict['categories'] = recipe['categories']
    recipe_dict['url'] = recipe['url']
    recipe_dict['image link'] = recipe['recipe_image_link']
    recipe_dict['weight'] = augment_rating(recipe['recipe_rating']) * recipe['recipe_review_count'] ### TODO: deal with "default"
    recipes.append(recipe_dict)

# calculate the weight total:
w_tot = 0
for recipe in recipes:
    w_tot += recipe['weight']

# create a set of all the ingredients:
full_ingredient_set = set()
for recipe in recipes:
    full_ingredient_set = full_ingredient_set.union(recipe['ingredients'])


# the function for calculating the support of an itemset. given a set of
# ingredients, the function returns the set's support.
def support(ingredient_set):
    sup = 0
    for recipe in recipes:
        if recipe['ingredients'].issuperset(ingredient_set):
            sup += recipe['weight']
    return sup / w_tot


# A-Priori algorithm:
S = 0.01 ### The support threshold
frequent_ingredients_1 = {}
for ingredient in full_ingredient_set:
    s = support(set(ingredient))
    if s > S:
        frequent_ingredients_1[ingredient] = (ingredient, s)

frequent_ingredients_2 = []
for item1 in frequent_ingredients_1:
    for item2 in frequent_ingredients_1:
        if (item1 != item2):
            s = support({item1[0], item2[0]})
            if s > S:
                frequent_ingredients_2.append(({item1[0], item2[0]}, s))

frequent_ingredients_3 = []
for item1 in frequent_ingredients_2:
    for item2 in frequent_ingredients_2:
        temp_set = item1[0].intersection(item2[0])
        if len(temp_set) == 3:
            s = support(temp_set)
            if s > S: ### TODO: do we decrease S?
                frequent_ingredients_3.append((temp_set, s))

frequent_ingredients_4 = []
for item1 in frequent_ingredients_3:
    for item2 in frequent_ingredients_3:
        temp_set = item1[0].intersection(item2[0])
        if len(temp_set) == 4:
            s = support(temp_set)
            if s > S: ### TODO: do we decrease S?
                frequent_ingredients_4.append((temp_set, s))


# the function for calculating an association rule's confidence. Given an
# itemset (X) and an ingredient (Y), the function returns the confidence of the
# association rule X->Y
def confidence(itemset, item):
    return support(itemset[0].add(item)) / support(itemset)


# find the association rules, each rule is a tuple that contains a set, an ingredient and a confidence
C = 0.5 ### the confidence threshold
association_rules = []
for frequent_itemset in frequent_ingredients_4:
    for ingredient in frequent_itemset[0]:
        conf = confidence(frequent_itemset.remove(ingredient), ingredient)
        if conf > C:
            association_rules.append((frequent_itemset.remove(ingredient), ingredient, frequent_itemset[1], conf))
for frequent_itemset in frequent_ingredients_3:
    for ingredient in frequent_itemset[0]:
        conf = confidence(frequent_itemset.remove(ingredient), ingredient)
        if conf > C:
            association_rules.append((frequent_itemset.remove(ingredient), ingredient, frequent_itemset[1], conf))
for frequent_itemset in frequent_ingredients_2:
    for ingredient in frequent_itemset[0]:
        conf = confidence(frequent_itemset.remove(ingredient), ingredient)
        if conf > C:
            association_rules.append((frequent_itemset.remove(ingredient), ingredient, frequent_itemset[1], conf))


# the function that calculates the interest of an association rule. Given an
# itemset (X) and an ingredient (Y), the function returns the interest of the
# association rule X->Y
def interest(itemset_A, item):
    return confidence(itemset_A, item) - frequent_ingredients_1[item][1]


# remove the association rules with bad interest:
I = 0
final_association_rules = []
for rule in association_rules:
    i = interest(rule[0], rule[1])
    if i > I:
        final_association_rules.append((rule[0], rule[1], rule[2], rule[3], i))

### the final association rule object is (X, Y, support, confidence, interest)
# Save the json that contains the association rules. It is a dictionary that
# has keys that are the ordered ingredients in X, and the value is a list of lists,
# where each inner list has 2 values: Y and the interest.
rule_dictionary = {}
for rule in final_association_rules:
    key = sorted(list(rule[0]))
    rule_dictionary[key] = []
for rule in final_association_rules:
    key = sorted(list(rule[0]))
    rule_dictionary[key].append([rule[1], rule[4]])

# save the final json with the association rulezzzzz!!
with open('C:\\Users\\Daniel\\PycharmProjects\\SpiceItUp\\association_rules.json', 'w') as json_file:
    json.dump(rule_dictionary, json_file)
