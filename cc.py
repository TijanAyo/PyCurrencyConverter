'''
Currency Converter using Python
Author: Tijani Ayomide
Reference: Ayushi Rawat
Check out her blog to find out more: https://ayushirawat.com/currency-converter-using-python
Forex-Python Docs: https://forex-python.readthedocs.io/en/latest/usage.html#currency-rates
'''

import time, math
from datetime import datetime
from tqdm import tqdm
from forex_python.converter import CurrencyCodes, CurrencyRates
from forex_python.bitcoin import BtcConverter

c = CurrencyCodes()
cr = CurrencyRates()

print('CurrencyC0nverter in Terminal :) ')
time.sleep(1)
print('Choose: \n 1.) Compare Rates \n 2.) Check Rate \n 3.) To quit program')
choose = int(input(': '))

while True:
    if choose == 3:
        print('Come again :@')
        break
    elif choose == 1:
        print('To compare rates you must use the currency symbols e.g United State dollar as USD or Indian Ruppes as INR')
        time.sleep(1)
        compare_1 = str(input('Your currency : ')).upper()
        compare_2 = str(input('Compared with: ')).upper()
        
        # Getting the currency symbol 
        cur_name = c.get_currency_name(compare_2)
        
        cur_symbol_1 = c.get_symbol(compare_1)
        cur_symbol_2 = c.get_symbol(compare_2)
        
        time.sleep(1)
        print('You want to compare ' + cur_symbol_1 + ' against  ' + cur_symbol_2)
        rate= cr.get_rate(compare_1, compare_2)

        # Addig the cool loading screen before ouput
        mylist = range(9)
        for i in tqdm(mylist):
            time.sleep(1)
        
        print('The conversion rate of ' + compare_1 + ' TO ' + compare_2 + ' is : ')
        print(rate) # The output
        print('To the nearest integer ' + str('1 ') + compare_1 + ' goes for ' + str(round(rate)) + cur_name)
        break
    elif choose == 2:
        print('Please enter a currency: ')
        currency = str(input('Your currency : ')).upper()
        
        rate = cr.get_rates(currency)
        cur_symbol = c.get_symbol(currency)
        
        print('The current rate of ' + cur_symbol + ' is ' + str(rate))
        break
    else:
        print('Invalid Syntax')
        break
    
    