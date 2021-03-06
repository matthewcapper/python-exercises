import json
from itertools import product as pro
from itertools import combinations as combo
from itertools import groupby
import functions_exercises
from functions_exercises import is_two
from functions_exercises import is_vowel as vowl
from functions_exercises import handle_commas

# trying out a couple different functions from
# the imported functions_exercises using full import,
# alias, function only

print(functions_exercises.is_consonant('B'))

print(is_two(2))

print(vowl('r'))

# itertools exercises
# combine abc with 123 in pairs

toup1 = ('a', 'b', 'c')
toup2 = ('1', '2', '3')
comb_list = pro(toup1, toup2)
amount = 0
comb_string = ''
for n in comb_list:
    comb_string += str(n)
    amount += 1
print('If we combine {} and {}, we get {} combinations'.format(toup1, toup2, amount))
print('It looks like this: ')
print('{}'.format(comb_string))

# combine abcd in pairs

comb_list2 = list(combo('abcd', 2))
comb_string2 = ''
amount2 = 0
for n in comb_list2:
    comb_string2 += str(n)
    amount2 += 1

print('If we combine a,b,c,d in pairs, we get {} combinations'.format(amount2))
print('It looks like this: ')
print('{}'.format(comb_string2))

# heres a whole bunch of initializations

full_load = json.load(open('profiles.json'))
count_total = 0
count_active = 0
count_inactive = 0
total_bal = 0.0
num_bal = 0.0
bal_list = []
fruit_list = []
unread_list = []
name_list = []
total_unread = 0
# apple_count = 0
# banana_count = 0
# strawberry_count = 0
fruit_dict = {}
bal_dict = {}

# Print full list of files on hand count total number of users:

for dict in full_load:
    for key in dict:
        # this will print out all the records if you want that
        # print('{}: {}'.format(key, dict[key]))
        # if key == 'favoriteFruit':
        #     print('-------------------')
        if key == 'isActive':
            count_total += 1

print('\nHi! Here''s some analysis on this json file!\n')

print('Number of all users: {}'.format(count_total))

# Iterate through data, give list of all active users only

for dict in full_load:
    for key in dict:
        if key == 'isActive':
            if dict[key]:
                count_active += 1
print('Number of active users: {}'.format(count_active))

# count of inactive users

for dict in full_load:
    for key in dict:
        if key == 'isActive':
            if not dict[key]:
                count_inactive += 1
print('Number of inactive users: {}'.format(count_inactive))

# Grand total of balances
# also unread emails from greeting message
# also favorite fruit list builder
# also balance list builder

for dict in full_load:
    for key in dict:
        if key == 'greeting':
            file_unread = ''
            for letter in dict[key]:
                if letter in('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz !.,'):
                    continue
                else:
                    file_unread += letter
            unread_list.append(int((file_unread)))
        if key == 'favoriteFruit':
            fruit_list.append(dict[key])
        if key == 'balance':
            num_bal += 1.0
            total_bal += float(dict[key].replace('$',
                                                 '').replace(',', '').strip())
            bal_list.append(float(dict[key].replace(
                '$', '').replace(',', '').strip()))
        if key == 'name':
            name_list.append(dict[key])

for item in name_list:
    bal_dict[item] = bal_list[name_list.index(item)]

print('Total balances: ${}'.format(total_bal))

average_bal = sum(bal_list) / num_bal
min_balance = min(bal_list)
max_balance = max(bal_list)
print('Average balance: ${0:.6}'.format(average_bal))
for key in bal_dict:
    if bal_dict[key] == max_balance:
        print('The maximum balance holder is {} with a balance of ${}'.format(
            key, bal_dict[key]))
    if bal_dict[key] == min_balance:
        print('The minimum balance holder is {} with a balance of ${}'.format(
            key, bal_dict[key]))

# actual functional way of finding favorite fruits
for key, group in groupby(sorted(fruit_list)):
    fruit_dict[key] = len(list(group))

# dumb forced way if you know all the categories and there arent a lot of them
# for fruit in fruit_list:
#     if fruit == 'apple':
#         apple_count += 1
#     elif fruit == 'strawberry':
#         strawberry_count += 1
#     elif fruit == 'banana':
#         banana_count += 1

# fruit_dict = {'apple': apple_count,
#               'banana': banana_count, 'strawberry': strawberry_count}

for key in fruit_dict:
    if fruit_dict[key] == max(fruit_dict.values()):
        print('The most popular fruit is {} with {} votes'.format(
            key, fruit_dict[key]))
    if fruit_dict[key] == min(fruit_dict.values()):
        print('The least popular fruit is {} with {} votes'.format(
            key, fruit_dict[key]))


unread_total = sum(unread_list)
print('total unread emails: {}'.format(unread_total))
