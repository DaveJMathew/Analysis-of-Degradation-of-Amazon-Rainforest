from asyncio.windows_events import NULL
from calendar import month
from cmath import nan
from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def severity_rating(severity):
    if severity == 'Weak' :
        return 1
    elif severity == 'Moderate':
        return 2
    elif severity == 'Strong':
        return 3
    elif severity == 'Very Strong':
        return 4

""" Function to graph a El Nino/ La Nino Severity 1999-2019 """
def ella_sever(ella_data,fire_x,ag_firespots):
    el_years = []
    el_severity = []
    la_years = []
    la_severity=[]

    i = 0
    for line in ella_data.severity:
        if ella_data.phenomenon[i] == 'El Nino':
            el_years.append(ella_data.startyear[i])
            el_severity.append(severity_rating(ella_data.severity[i]))
            diff = ella_data.endyear[i] - ella_data.startyear[i]
            while(diff>1):
                el_years.append(ella_data.startyear[i] + diff - 1)
                el_severity.append(severity_rating(ella_data.severity[i]))
                diff = diff - 1
        else:
            la_years.append(ella_data.startyear[i])
            la_severity.append(severity_rating(ella_data.severity[i]))
            diff = ella_data.endyear[i] - ella_data.startyear[i]
            while(diff>1):
                la_years.append(ella_data.startyear[i] + diff - 1)
                la_severity.append(severity_rating(ella_data.severity[i]))
                diff = diff - 1
        i = i + 1
    print(el_years)
    print(el_severity)
    print("\n\n\n")
    print(la_years)
    print(la_severity)

    ella_x = []
    year = 1999
    while year < 2020:
        ella_x.append(year)
        year = year + 1
    plt.xticks(ella_x, rotation='vertical')
    ella_y = [1,2,3,4]
    ella_ylabels = ['Weak', 'Moderate', 'Strong', 'Very Strong']
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_yticks(ella_y, ella_ylabels)
    ax.set_xticks(ella_x)
    ax.bar(el_years,el_severity,width=0.5,color='#FFCCCC')
    ax.bar(la_years, la_severity, width =0.5,color='#99DDFF')
    ax.set_xlabel('Year')
    ax.set_ylabel('Severity')
    plt.title('El Nino/ La Nina Severity from 1999-2019')
    ax.legend(['El Nino','La Nina'])
    #ax2 = ax.twinx()
    el_fire =[nan for i in range(21)]
    la_fire=[nan for i in range(21)]
    for i in [0,1,6,8,9,11,12,17,18]:
        el_fire[i] = ag_firespots[i]
    for i in [3,5,7,10,15,16,19]:
        la_fire[i]= ag_firespots[i]
    #ax2.plot(fire_x, ag_firespots,color='#FF5733',linewidth = 6, marker='o', markerfacecolor='white',markersize='8',zorder=-3)
    #ax2.scatter(fire_x,el_fire,color='#99DDFF',s=80,edgecolors='black',zorder=2)
    #ax2.scatter(fire_x,la_fire,color='#FFCCCC',s=80,edgecolors='black',zorder=1)
    #ax2.set_ylabel('Total Number of Occurences')
    #ax2.legend(['Aggregated Number of Occurences of firespots'],loc=9)
    plt.show()
def get_corr(ella_data,fire_data):
    firespot = list(fire_data['firespots'])
    year = list(fire_data['year'])
    fire_x = []
    i_year = 1999
    while i_year < 2020:
        fire_x.append(i_year)
        i_year = i_year + 1
    ag_firespots = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    pos = 0
    for y in fire_x:
        x = 0
        for fire in firespot:
            if year[x] == y:
                ag_firespots[pos] = ag_firespots[pos] + firespot[x]
            x = x+1
        pos = pos+1
    ella_sever(ella_data,fire_x,ag_firespots)
def nfunc(year,month,state,latitude,longitude,firespot,fire_x):
    firespot_avg = sum(firespot)/len(firespot)
    print("avg:",firespot_avg)
    below_lat = []
    above_lat = []
    count = 0
    below_long = []
    above_long=[]
    for fire in firespot:
        if fire <= firespot_avg:
            below_lat.append(latitude[count])
            below_long.append(longitude[count])
        else:
            above_lat.append(latitude[count])
            above_long.append(longitude[count])
        count = count + 1
    below_color = "#f4c430"
    above_color = "#FF5733"
    #plt.title("Location of firespots in the Brazillian States")
    #plt.xlabel("Longitude")
    #plt.ylabel("Latitude")
    plt.scatter(below_long,below_lat,color=below_color)
    plt.scatter(above_long,above_lat,color=above_color)
    #plt.legend(["Recorded firespots below or equal to the average occurences",'Recorded firespots above the average occurences'])
    plt.show()
def heatmap(list_data):
    year = list_data[0]
    month = list_data[1]
    state = list_data[2]
    firespot = list_data[3]
    year_numbers = list_data[4]

    states = [[0 for i in range(9)] for j in range(21)]
    count = 0
    for fire in firespot:
        x = year[count] - 1999
        if state[count] == 'TOCANTINS':
            states[x][0] = states[x][0] + fire
        elif state[count] == 'AMAZONAS':
            states[x][5] = states[x][5] + fire
        elif state[count] == 'MATO GROSSO':
            states[x][4] = states[x][4] + fire
        elif state[count] == 'AMAPA':
            states[x][2] = states[x][2] + fire
        elif state[count] == 'ACRE':
            states[x][8] = states[x][8] + fire
        elif state[count]== 'MARANHAO':
            states[x][7] = states[x][7] + fire
        elif state[count] == 'RONDONIA':
            states[x][3] = states[x][3] + fire
        elif state[count] == 'PARA':
            states[x][6] = states[x][6] + fire
        elif state[count] == 'RORAIMA':
            states[x][1] = states[x][1] + fire
        count = count + 1
    state_names = ['TO', 'RR', 'AP', 'RO', 'MT','AM','PA','MA','AC']
    month_x = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    state_nums = [i for i in range(9)]
    year_nums = [i for i in range(21)]
    import seaborn as sns
    plt.figure(figsize=(10,10))
    heat_map = sns.heatmap(states, linewidth = 1)
    sns.color_palette("coolwarm", as_cmap=True)
    plt.title( "HeatMap of firespots over states per year" )
    plt.xlabel("States")
    plt.ylabel("Year")
    plt.xticks(state_nums,state_names)
    plt.yticks(year_nums,year_numbers,rotation = "horizontal")
    plt.show()
def fire(fire_data):
    year = list(fire_data['year'])
    month = list(fire_data['month'])
    state = list(fire_data['state'])
    uniq_state = list(set(state))
    latitude = list(fire_data['latitude'])
    longitude = list(fire_data['longitude'])
    firespot = list(fire_data['firespots'])
    fire_x = []
    i_year = 1999
    while i_year < 2020:
        fire_x.append(i_year)
        i_year = i_year + 1
    nfunc(year,month,state,latitude,longitude,firespot,fire_x)
    list_data = [year,month,state,firespot,fire_x]
    heatmap(list_data)
    """
    fire_total = [0 for i in range(21)]
    fire_num = [0 for i in range(21)]

    count = 0
    for fire in firespot:
        year_no = year[count] - 1999
        fire_total[year_no] = fire_total[year_no] + fire
        fire_num[year_no] = fire_num[year_no] + 1
        count = count + 1
    fire_avg = [fire_total[i]/fire_num[i] for i in range(21)]
    plt.title('Number of firespots per year')
    plt.xlabel('Year')
    plt.ylabel('Occurences of firespots')
    plt.xticks(fire_x)
    #plt.plot(fire_x,fire_avg,color='#FF5733')
    plt.plot(fire_x,fire_num,color = '#FF7F7F')
    #plt.plot(fire_x,fire_total,color='#B22222')
    #plt.legend(['Total Occurences of Firespots','Average Occurences of Firespots'])
    print(fire_avg)
    plt.show()
    """
    
    states = [i for i in range(9)]
    count = 0
    for fire in firespot:
        if state[count] == 'TOCANTINS':
            states[0] = states[0] + fire
        elif state[count] == 'AMAZONAS':
            states[5] = states[5] + fire
        elif state[count] == 'MATO GROSSO':
            states[4] = states[4] + fire
        elif state[count] == 'AMAPA':
            states[2] = states[2] + fire
        elif state[count] == 'ACRE':
            states[8] = states[8] + fire
        elif state[count]== 'MARANHAO':
            states[7] = states[7] + fire
        elif state[count] == 'RONDONIA':
            states[3] = states[3] + fire
        elif state[count] == 'PARA':
            states[6] = states[6] + fire
        elif state[count] == 'RORAIMA':
            states[1] = states[1] + fire
        count = count + 1
    state_names = ['TO', 'RR', 'AP', 'RO', 'MT','AM','PA','MA','AC']
    plt.bar(state_names,states,width=0.5,color='#FF5733')
    fire_y = [0,200000,400000,600000,800000,1000000]
    fire_yl = [0, '200k','400k','600k','800k','1M']
    plt.yticks(fire_y,fire_yl)
    plt.xlabel('States')
    plt.ylabel('Firespot Occurences')
    plt.title('Total Firespot Occurences for each state')
    plt.show()
    
    """
    months = [0 for i in range (12)]
    count = 0
    for i in firespot:
        value = month[count] - 1
        months[value] = months[value] + i
        count = count + 1
    maxis = [i for i in range(12)]
    month_x = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    plt.xticks(maxis,month_x)
    plt.xlabel('Months')
    plt.ylabel('Firespot Occurences')
    plt.title('Total Firespot Occurences for each month')
    plt.bar(maxis,months,width=0.5,color='#FF5733')
    plt.show()
    """
    # plt.xticks(fire_x)
    # plt.scatter(year,firespot)
    # plt.xlabel('Year')
    # plt.ylabel('Number of Occurences')
    # plt.title('Occurences of firespots over 1999 - 2019 [ All Brazillian States]')
    # plt.legend(['Number of Occurences of firespots'])
    # plt.show()
    """
    ag_firespots = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    ll = []
    # Iterate over a sequence of numbers from 0 to 4
    for i in range(9):
    # In each iteration, add an empty list to the main list
        ll.append(ag_firespots)
    pos = 0
    for y in fire_x:
        x = 0
        for fire in firespot:
            if year[x] == y:
                ag_firespots[pos] = ag_firespots[pos] + firespot[x]
                if state[x] == 'TOCANTINS':
                    ll[0][pos] = ll[0][pos] + firespot[x]
                elif state[x] == 'AMAZONAS':
                    ll[1][pos] = ll[1][pos] + firespot[x]
                elif state[x] == 'MATO GROSSO':
                    ll[2][pos] = ll[2][pos] + firespot[x]
                elif state[x] == 'AMAPA':
                    ll[3][pos] = ll[3][pos] + firespot[x]
                elif state[x] == 'ACRE':
                    ll[4][pos] = ll[4][pos] + firespot[x]
                elif state[x] == 'MARANHAO':
                    ll[5][pos] = ll[5][pos] + firespot[x]
                elif state[x] == 'RONDONIA':
                    ll[6][pos] = ll[6][pos] + firespot[x]
                elif state[x] == 'PARA':
                    ll[7][pos] = ll[7][pos] + firespot[x]
                elif state[x] == 'RORAIMA':
                    ll[8][pos] = ll[8][pos] + firespot[x]
            x = x + 1
        pos = pos + 1
    threed_state = []
    for state_name in uniq_state:
        if state_name == 'TOCANTINS':
            threed_state.append(1)
        elif state_name == 'AMAZONAS':
            threed_state.append(2)
        elif state_name == 'MATO GROSSO':
            threed_state.append(3)
        elif state_name == 'AMAPA':
            threed_state.append(4)
        elif state_name == 'ACRE':
            threed_state.append(5)
        elif state_name == 'MARANHAO':
            threed_state.append(6)
        elif state_name == 'RONDONIA':
            threed_state.append(7)
        elif state_name == 'PARA':
            threed_state.append(8)
        elif state_name == 'RORAIMA':
            threed_state.append(9)
    threed_state = threed_state * 21
    threed_year = fire_x * 9
    print(len(threed_state), len(threed_year))
    year_state_agg =  [item for sublist in ll for item in sublist]
    fig = plt.figure(figsize=(10,10))

    ax = fig.add_subplot(111, projection='3d')
    dx= [3 for i in range(len(threed_year))]
    dy = [1+i for i in range(len(threed_state))]
    dz = [3 for i in range(len(year_state_agg))]
    ax.bar3d(threed_year,threed_state,year_state_agg,dx,dy,dz,color='#FF5733')
    ax.set_xticks(fire_x,rotation = 'vertical')
    fire_y = [1,2,3,4,5,6,7,8,9]
    fire_ylabels = ['TO', 'RR', 'AM', 'RO', 'MT','AZ','PA','MA','AC']
    plt.yticks(fire_y, fire_ylabels)

    ax.set_xlabel("Year")

    ax.set_ylabel("State")

    ax.set_zlabel("Aggregate Occurences of firespots")
    ax.set_title("Aggregate Occurences of firespots per state per year")

    plt.show()
    """
    """
    plt.xticks(fire_x)
    plt.plot(fire_x, ag_firespots,color='#FF5733',linewidth = 6)
    plt.xlabel('Year')
    plt.ylabel('Total Number of Occurences')
    plt.title('Aggregated Occurences of firespots over 1999 - 2019 [ All Brazillian States]')
    plt.legend(['Aggregated Number of Occurences of firespots'])
    plt.show() """
fire_data = pd.read_csv("amazon fires.csv")
area_data = pd.read_csv("area.csv")
ella_data = pd.read_csv("el nino la nina.csv")

ella_data.columns = ella_data.columns.str.replace(' ', '')
fire_data.columns = fire_data.columns.str.replace(' ', '')
area_data.columns = area_data.columns.str.replace(' ', '')
"""
df = pd.DataFrame(fire_data, columns=['firespots'])

plt.scatter(fire_data['longitude'], fire_data['latitude'] )
plt.show()
import seaborn as sns
plt.style.use("seaborn")
plt.figure(figsize=(10,10))
heat_map = sns.heatmap(df, linewidth = 1 , annot = True)
plt.title( "HeatMap using Seaborn Method" )
plt.show() """
#ella_sever(ella_data)
#fire(fire_data)
get_corr(ella_data,fire_data)

