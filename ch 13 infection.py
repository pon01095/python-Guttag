# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 14:11:57 2021

@author: LeeHoonGi
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 10:34:39 2021

@author: LeeHoonGi
"""
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

def simulation(fixed, variable):
    infected = [fixed['initial_infections']]
    new_infections = [fixed['initial_infections']]
    total_infections = fixed['initial_infections']
    
    for t in range(fixed['duration']):
        cur_infections = infected[-1]
        # remove people who are no longer contagious
        if len(new_infections) > fixed['days_spreading']:
            cur_infections -= new_infections[-fixed['days_spreading']-1]
        # if social distancing, change number of datily contacts
        if t >= variable['red_start'] and t < variable['red_end']:
            daily_contacts = variable['red_daily_contacts']
        else:
            daily_contacts = fixed['init_contacts']
        
        # compute number of new cases
        total_contacts = cur_infections * daily_contacts
        susceptible = fixed['pop'] - total_infections
        risky_contacts = total_contacts * (susceptible/fixed['pop'])
        newly_inifected = round(risky_contacts * fixed['contagiousness'])
        
        #update variables
        new_infections.append(newly_inifected)
        total_infections += newly_inifected
        infected.append(cur_infections + newly_inifected)
    return infected, total_infections
        
def plot_infections(infections, total_infections, fixed):
    infection_plot = plt.plot(infections, 'r', label = 'Infected')[0]
    plt.xticks(fontsize = 'large')
    plt.yticks(fontsize = 'large')
    plt.xlabel('Day Since First Infection',fontsize = 'xx-large')
    plt.ylabel('Number of Currently Infected', fontsize = 'xx-large')
    plt.title(('Number of Infections Assuming No Vaccine\n' + 
                f'Pop = {fixed["pop"]:,}'+ 
                f'Contacts/Days = {fixed["init_contacts"]}' + 
                f'Infectivity = {(100*fixed["contagiousness"]):.1f}%' +
                f'Days Contagious = {fixed["days_spreading"]}'), fontsize = 'xx-large')
    plt.legend(fontsize = 'xx-large')
    txt_box = plt.text(plt.xlim()[1]/2, plt.ylim()[1]/1.25, f'Total Infections = {total_infections:,.0f}',
                       fontdict = {'size' : 'xx-large', 'weight' : 'bold', 'color' : 'red'})
    return infection_plot, txt_box

fixed = {'pop' : 5000000, 
         'duration': 500,
         'initial_infections' : 4,
         'init_contacts' : 50,
         'contagiousness' : 0.005,
         'days_spreading' : 10} 
variable = {'red_daily_contacts' : fixed['init_contacts'],
            'red_start' : 20,
            'red_end' : 200} 

infections, total_infections = simulation(fixed, variable)
fig = plt.figure(figsize=(12, 8.5))
infections_ax = plt.axes([0.12, 0.2, 0.8, 0.65])
# infection_plot, txt_box = plot_infections(infections, total_infections, fixed) 
contacts_ax = plt.axes([0.25, 0.09, 0.65, 0.03])
start_ax = plt.axes([0.25, 0.06, 0.65, 0.03])
end_ax = plt.axes([0.25, 0.03, 0.65, 0.03])

contacts_slider = Slider(contacts_ax, # axes object containing the slider
 'reduced\ncontacts/day', # name of slider
 0, # minimal value of the parameter
 50, # maximal value of the parameter
 25) # initial value of the parameter)
contacts_slider.label.set_fontsize(12)
start_day_slider = Slider(start_ax, 'start reduction', 1, 30, 25)
start_day_slider.label.set_fontsize(12)
end_day_slider = Slider(end_ax, 'end reduction', 30, 400, 300)
end_day_slider.label.set_fontsize(12)

def update(fixed, infection_plot, txt_box, contacts_slider, start_day_slider, end_day_slider):
    variable = {'red_daily_contacts' : contacts_slider.value,
                'red_start': start_day_slider.value,
                'red_end' : end_day_slider.val}
    I, total_infections = simulation(fixed, variable)
    infection_plot.set_ydata(I)
    txt_box.set_text(f'Total Infections = {total_infections:,0f}')

slider_update = lambda _: update(fixed, infection_plot, txt_box, contacts_slider, start_day_slider, end_day_slider)
contacts_slider.on_changed(slider_update)
start_day_slider.on_changed(slider_update)
end_day_slider.on_changed(slider_update)
infections, total_infections = simulation(fixed, variable)
plt.axes(infections_ax)
infection_plot, txt_box = plot_infections(infections,  total_infections, fixed)
