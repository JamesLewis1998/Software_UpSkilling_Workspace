# ========== Sets ==========

print( "Sets")

## ======= Sets Summary =========
# - Another python data structure 
# - Look like tuples but are not immutable so you can change them 
# - Also kind of look like dictionaries but don't have keys 

names ={"roger","syd"}
# Sets are not ordered 
# For example: 
set1 = {"roger","sid"}
set2 = {"roger"}

intersection = set1 & set2
print(intersection)
# Shows the two values common between the two hence the term intersection

# Also can show union with two sets
mod_union = set1 | set2
print(mod_union)
# this unites the two sets - ie combines them into one 

# Finding the difference between two sets
mod_diff = set1 - set2
print(mod_diff)
# returns {'sid'}

## ======= Superset and Subset =========
# Superset meaning if all the info in one set is contained in another set, the other set is a superset of the first set
mod_superset_true = set1 > set2 # ie does set1 have everything from set2
print(mod_superset_true)        # ie set2 is a subset of set1 and set2 is a superset of set1

## ======= Final Notes about Sets =========
# Can also get a list from the items in a set by passing the set to the list constructor
print(list(set1))
# then can check items contained in the set with the in operator

# Another useful bit of info - a set cannot have two of the same item
set3 = {"roger","sid","roger"}
print(set3) # will only show {'roger', 'sid'} because a set cannot have two of the same item