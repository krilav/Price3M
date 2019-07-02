

cost_of_search = []
cost_tmp = 0
cost_tmp_opt = 0
cost_tmp_kopt = 0

ws1 = [i * 2 for i in range(20)]


for row_i in range(10):
    cost_of_search.append('''Прайсов цена - {0} руб. с НДС или {1} EUR Без НДС
    Оптовая цена - {2} руб. с НДС / Крупнооптовая цена {3} руб. с НДС'''
                          .format(str(cost_tmp), ws1[row_i + 2], str(cost_tmp_opt),
                                  str(cost_tmp_kopt)))
print(cost_of_search)
