# in this file we implement the A-Priori algorithm, in order to find the
# frequent itemsets from the recipes, taking the weights into account.

import json
import time
import math
import pickle

# TODO: maybe not using weights will be better, and all recipes will be the same?

# a function to augment the ratings so that higher ratings have a bigger
# effect on the weights of the recipes. given a rating, the function returns
# the augmented rating (float)
def augment_rating(rating):
    return rating ** 1.5


# load the data into the variables:
with open('C:\\Users\\Daniel\\PycharmProjects\\SpiceItUp\\jsons\\recipes.json', 'r') as json_file:
    raw_recipes = json.load(json_file) # list of dictionaries from the crawler

# calculate the recipe weights:
print("calculating recipe weights!")
recipes = []
for recipe in raw_recipes:
    recipe_dict = {}
    recipe_dict['name'] = recipe['recipe_name']
    recipe_dict['ingredients'] = set(recipe['filtered_ingredient_list'])
    recipe_dict['categories'] = recipe['categories']
    recipe_dict['url'] = recipe['url']
    recipe_dict['image link'] = recipe['recipe_image_link']
    recipe_dict['weight'] = augment_rating(recipe['recipe_rating']) * (1 + math.log(recipe['recipe_review_count']+1, 2))
    recipes.append(recipe_dict)

# calculate the weight total:
w_tot = 0
for recipe in recipes:
    w_tot += recipe['weight']

# create a set of all the ingredients (all that appear above 20 times):
print("creating the full ingredient set")

ingredient_dictionary = {}
for recipe in recipes:
    for ingredient in recipe['ingredients']:
        ingredient_dictionary[ingredient] = 0
for recipe in recipes:
    for ingredient in recipe['ingredients']:
        ingredient_dictionary[ingredient] += 1
filtered_ingredients = [x[0] for x in ingredient_dictionary.items() if x[1] > 20]
full_ingredient_set = set(filtered_ingredients)


# the function for calculating the support of an itemset. given a set of
# ingredients, the function returns the set's support. Also, return the top
# recipe details for the given ingredient set.
def support(ingredient_set):
    sup = 0
    top_weight = 0
    top_weight_links = []
    for recipe in recipes:
        if recipe['ingredients'].issuperset(ingredient_set):
            sup += recipe['weight']
            if recipe['weight'] > top_weight:
                top_weight_links = [recipe['name'], recipe['url'], recipe['image link']]
    return float(sup) / float(w_tot), top_weight_links


# A-Priori algorithm:
S = 0.005 ### The support threshold
print("starting A-Priori algorithm!")
frequent_ingredients_1 = {}
print("there are " + str(len(full_ingredient_set)) + " items to go over")
tic = time.clock()
i = 0
for ingredient in full_ingredient_set:
    i += 1
    (s, temp) = support({ingredient})
    if s > S:
        frequent_ingredients_1[ingredient] = (ingredient, s)
        print("new frequent ingredient: " + ingredient)
    if i%1000 == 0:
        print("went over " + str(i) + " items so far")
toc = time.clock()
print("finished support of frequent itemsets of size 1 in " + str(toc-tic) + " seconds")

S = S / 2.0
frequent_ingredients_2 = {}
print("there are " + str(len(frequent_ingredients_1)**2) + " items to go over")
tic = time.clock()
for item1 in frequent_ingredients_1:
    for item2 in frequent_ingredients_1:
        if (item1 != item2):
            (s, links) = support({item1, item2})
            if s > S:
                key = ' '.join(sorted([item1,item2]))
                frequent_ingredients_2[key] = ({item1, item2}, s, links)
toc = time.clock()
print("finished support of frequent itemsets of size 2 in " + str(toc-tic) + " seconds")

S = S / 2.0
frequent_ingredients_3 = {}
print("there are " + str(len(frequent_ingredients_2)**2) + " items to go over")
tic = time.clock()
for item1 in frequent_ingredients_2.values():
    for item2 in frequent_ingredients_2.values():
        temp_set = item1[0].union(item2[0])
        if len(temp_set) == 3:
            (s, links) = support(temp_set)
            if s > S:
                key = ' '.join(sorted(list(temp_set)))
                frequent_ingredients_3[key] = (temp_set, s, links)
toc = time.clock()
print("finished support of frequent itemsets of size 3 in " + str(toc-tic) + " seconds")

S = S / 2.0
frequent_ingredients_4 = {}
print("there are " + str(len(frequent_ingredients_3)**2) + " items to go over")
tic = time.clock()
for item1 in frequent_ingredients_3.values():
    for item2 in frequent_ingredients_3.values():
        temp_set = item1[0].union(item2[0])
        if len(temp_set) == 4:
            (s, links) = support(temp_set)
            if s > S:
                key = ' '.join(sorted(list(temp_set)))
                frequent_ingredients_4[key] = (temp_set, s, links)
toc = time.clock()
print("finished support of frequent itemsets of size 4 in " + str(toc-tic) + " seconds")

# save the itemsets to a file:
with open('C:\\Users\\Daniel\\PycharmProjects\\SpiceItUp\\itemsets\\itemsets_size_1.pickle', 'wb') as f:
    pickle.dump(frequent_ingredients_1, f)
with open('C:\\Users\\Daniel\\PycharmProjects\\SpiceItUp\\itemsets\\itemsets_size_2.pickle', 'wb') as f:
    pickle.dump(frequent_ingredients_2, f)
with open('C:\\Users\\Daniel\\PycharmProjects\\SpiceItUp\\itemsets\\itemsets_size_3.pickle', 'wb') as f:
    pickle.dump(frequent_ingredients_3, f)
with open('C:\\Users\\Daniel\\PycharmProjects\\SpiceItUp\\itemsets\\itemsets_size_4.pickle', 'wb') as f:
    pickle.dump(frequent_ingredients_4, f)


# the function for calculating an association rule's confidence. Given an
# itemset (X) and an ingredient (Y), the function returns the confidence of the
# association rule X->Y
def confidence(itemset, item):
    joined = itemset.union({item})

    try:
        if len(joined) == 4:
            key = ' '.join(sorted(list(joined)))
            support_x_and_y = frequent_ingredients_4[key][1]
            key = ' '.join(sorted(list(itemset)))
            support_x = frequent_ingredients_3[key][1]
        elif len(joined) == 3:
            key = ' '.join(sorted(list(joined)))
            support_x_and_y = frequent_ingredients_3[key][1]
            key = ' '.join(sorted(list(itemset)))
            support_x = frequent_ingredients_2[key][1]
        elif len(joined) == 2:
            key = ' '.join(sorted(list(joined)))
            support_x_and_y = frequent_ingredients_2[key][1]
            key = ' '.join(sorted(list(itemset)))
            support_x = frequent_ingredients_1[key][1]
        else:
            return None
    except KeyError:
        return 0

    return (support_x_and_y / support_x)


# find the association rules, each rule is a tuple that contains a set, an ingredient and a confidence
C = 0.05 ### the confidence threshold
association_rules = []
confidences = {}
print("started mining association rules!")
print("going over association rules that are 3->1")
for frequent_itemset in frequent_ingredients_4.values():
    for ingredient in frequent_itemset[0]:
        conf = confidence(frequent_itemset[0].difference({ingredient}), ingredient)
        if conf > C:
            association_rules.append((frequent_itemset[0].difference({ingredient}), ingredient, frequent_itemset[1], conf, frequent_itemset[2]))
            key = ' '.join(sorted(list(frequent_itemset[0].difference({ingredient})))) + ' ' + ingredient
            confidences[key] = conf
print("going over association rules that are 2->1")
for frequent_itemset in frequent_ingredients_3.values():
    for ingredient in frequent_itemset[0]:
        conf = confidence(frequent_itemset[0].difference({ingredient}), ingredient)
        if conf > C:
            association_rules.append((frequent_itemset[0].difference({ingredient}), ingredient, frequent_itemset[1], conf, frequent_itemset[2]))
            key = ' '.join(sorted(list(frequent_itemset[0].difference({ingredient})))) + ' ' + ingredient
            confidences[key] = conf
print("going over association rules that are 1->1")
for frequent_itemset in frequent_ingredients_2.values():
    for ingredient in frequent_itemset[0]:
        conf = confidence(frequent_itemset[0].difference({ingredient}), ingredient)
        if conf > C:
            association_rules.append((frequent_itemset[0].difference({ingredient}), ingredient, frequent_itemset[1], conf, frequent_itemset[2]))
            key = ' '.join(sorted(list(frequent_itemset[0].difference({ingredient})))) + ' ' + ingredient
            confidences[key] = conf


# the function that calculates the interest of an association rule. Given an
# itemset (X) and an ingredient (Y), the function returns the interest of the
# association rule X->Y
def interest(itemset_A, item):
    key = ' '.join(sorted(list(itemset_A))) + ' ' + item
    return confidences[key] - 3*frequent_ingredients_1[item][1]


# remove the association rules with bad interest,
# the final association rule object is (X, Y, support, confidence, interest)
I = 0
final_association_rules = []
print("getting only the association rules that are interesting!")
for rule in association_rules:
    i = interest(rule[0], rule[1])
    if i > I:
        final_association_rules.append((rule[0], rule[1], rule[2], rule[3], i, rule[4]))

# Save the json that contains the association rules. It is a dictionary that
# has keys that are the ordered ingredients in X, and the value is a list of lists,
# where each inner list has 5 values: Y, the interest, and the name, URL and Image URL
# of the top rated recipe which has the ingredients that are in X and Y.
rule_dictionary = {}
for rule in final_association_rules:
    key = ' '.join(sorted(list(rule[0])))
    rule_dictionary[key] = []
for rule in final_association_rules:
    key = ' '.join(sorted(list(rule[0])))
    rule_dictionary[key].append([rule[1], rule[4], rule[5][0], rule[5][1], rule[5][2]])

# save the final json with the association rulezzzzz!!
with open('C:\\Users\\Daniel\\PycharmProjects\\SpiceItUp\\association_rules.json', 'w') as json_file:
    json.dump(rule_dictionary, json_file)

print("FINISHED EVERYTHING!!!")
