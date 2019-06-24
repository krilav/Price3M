
a = '550 310 v'
search_test = '550 310 сер'
search_test_1 = search_test.split()

tru_or_not_tru = []

for search in search_test_1:

    tru_or_not_tru.append(search in a)

if tru_or_not_tru:
    print('оно')
else:
    print('не оно')
