# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 14:45:48 2021

@author: LeeHoonGi
"""

import matplotlib.pyplot as plt
plt.plot([1,2,3,4], [1,7,3,5]) #draw on current figure

plt.figure(1) #create figure 1
plt.plot([1,2,3,4], [1,2,3,4]) #draw on figure 1
plt.figure(2) #create figure 2
plt.plot([1,4,2,3], [5,6,7,8]) #draw on figure 2
plt.savefig('Figure-Addie') #save figure 2
plt.figure(1) #go back to working on figure1
plt.plot([5,6,10,3]) #draw again on figure 1
plt.savefig('Figure-Jane') #save figure 1

# principal = 10000
# interest_rate = 0.05
# years = 20
# values = []

# for i in range(years + 1):
#     values.append(principal)
#     principal += principal * interest_rate

# plt.plot(values)    
# # plt.plot(values, 'ko')
# plt.title('5% Growth, Compounded Annually')
# plt.xlabel('Years of Compounding')
# plt.ylabel('Value of Principal ($)')

# plt.plot(values, '-k', linewidth = 30)
# plt.title('5% Growth, Compounded Annually', fontsize = 'xx-large')
# plt.xlabel('Years of Compounding', fontsize = 'x-small')
# plt.ylabel('Value of Principal ($)')


# plt.rcParams['lines.linewidth'] = 6