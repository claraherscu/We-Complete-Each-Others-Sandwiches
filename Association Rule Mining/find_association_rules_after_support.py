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


# load the itemsets from the files:
with open('C:\\Users\\Daniel\\PycharmProjects\\SpiceItUp\\itemsets\\itemsets_size_1.pickle', 'rb') as f:
    frequent_ingredients_1 = pickle.load(f)
with open('C:\\Users\\Daniel\\PycharmProjects\\SpiceItUp\\itemsets\\itemsets_size_2.pickle', 'rb') as f:
    frequent_ingredients_2 = pickle.load(f)
with open('C:\\Users\\Daniel\\PycharmProjects\\SpiceItUp\\itemsets\\itemsets_size_3.pickle', 'rb') as f:
    frequent_ingredients_3 = pickle.load(f)
with open('C:\\Users\\Daniel\\PycharmProjects\\SpiceItUp\\itemsets\\itemsets_size_4.pickle', 'rb') as f:
    frequent_ingredients_4 = pickle.load(f)


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
