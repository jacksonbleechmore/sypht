import sys

month_days = {
    1:31,
    2:28,
    3:31,
    4:30,
    5:31,
    6:30,
    7:31,
    8:31,
    9:30,
    10:31,
    11:30,
    12:31
}

def is_leap_year(year):
    return year%4 == 0

def calculate_year_difference(start_date, end_date): 
    return end_date['year'] - start_date['year']

def days_from_date_to_EOY(date):
    days = month_days[date['month']] - date['day']
    for m in range(date['month']+1, 12 + 1):
        days += month_days[m]
        #add additional day in February for a leap year 
        if m == 2 and is_leap_year(date['year']):
            days += 1
    return days

def days_from_EOY_to_date(date):
    days = date['day']
    for m in range(1, date['month']):
        days+= month_days[m]
        #add additional day in February for a leap year 
        if m == 2 and is_leap_year(date['year']):
            days += 1
    return days

def days_for_whole_years(start_date, end_date):
    days = 0
    for y in range(start_date['year']+1,end_date['year']):
        if is_leap_year(y):
            days += 366
        else:
            days += 365
    return days
            
def is_date_valid(date):
    if date['month']==2:
        if is_leap_year(date['year']):
            max_days = month_days[date['month']] + 1
        else:
            max_days = month_days[date['month']]        
    else:
        max_days = month_days[date['month']]
    
    return date['days']<=max_days
    

def extract_date_from_str(date_str):
    day,month,year = date_str.split('/')
    date = {
        'day':int(day),
        'month':int(month),
        'year':int(year)
    }
    return date


def order_dates(date1, date2):
    #check year
    if(date1['year'] != date2['year']):
        if date1['year'] < date2['year']:
            start_date, end_date = date1, date2
        else:
            start_date, end_date = date2, date1       
    elif(date1['month'] != date2['month']):
        if date1['month'] < date2['month']:
            start_date, end_date = date1, date2
        else:
            start_date, end_date = date2, date1 
    else:
        if(date1['day'] < date2['day']):
            start_date, end_date = date1, date2
        else:
            start_date, end_date = date2, date1

    return start_date, end_date       



def days_between_dates(start_date, end_date):
    if calculate_year_difference(start_date, end_date) > 0:
        days = days_from_date_to_EOY(start_date) + days_from_EOY_to_date(end_date)
        days += days_for_whole_years(start_date, end_date)
        days -= 1

    else:
        days = days_from_EOY_to_date(end_date) - days_from_EOY_to_date(start_date) 
        days -= 1 
    
    if days < 0:
        days = 0
    return days

    
def main():
    date1 = extract_date_from_str(sys.argv[1])
    date2 = extract_date_from_str(sys.argv[2])
    
    start_date, end_date = order_dates(date1, date2)
    days = days_between_dates(start_date, end_date)
    
    print(days)

main()