# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 18:54:06 2021

@author: LeeHoonGi
"""

# import math
# x = 20
# print(math.log(x, 2))


import calendar as cal
cal_english = cal.TextCalendar()
print(cal_english.formatmonth(1949, 3))

print(cal.LocaleTextCalendar(locale='fr_FR').formatmonth(2049, 3))
print(cal.LocaleTextCalendar(locale='pl_PL').formatmonth(2049, 3))

print(cal.day_name[cal.weekday(2033, 12, 25)])

def find_thanksgiving(year):
    month = cal.monthcalendar(year, 11)
    if month[0][cal.THURSDAY] != 0:
        thanksgiving = month[3][cal.THURSDAY]
    else:
        thanksgiving = month[4][cal.THURSDAY]
    return thanksgiving

print('In 2011', 'U.S. Thanksgiving was on November', find_thanksgiving(2011))

def find_canadian_thanksgiving(year):
    month = cal.monthcalendar(year, 10)
    if month[0][cal.MONDAY] != 0:
        thanksgiving = month[1][cal.MONDAY]
    else:
        thanksgiving = month[2][cal.MONDAY]
    return thanksgiving

def shopping_days(year):
    """year a number >= 1941 
    returns the number of days between U.S.
    Thanksgiving and Christmas in year"""
    tday = find_thanksgiving(year)
    return 55 - tday 

