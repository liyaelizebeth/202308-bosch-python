def day_name(index):
    
    day_names=("Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday")
    return day_names[index]


def week_day_name(dd,mm,yyyy):
    d=week_day_number(dd,mm,yyyy)
    return day_name(d)
    
def week_day_number(dd,mm,yyyy):

    ref_date_value= day_value(1,1,2012)
    date_value = day_value(dd,mm,yyyy)

    diff = date_value - ref_date_value
    return diff%7


def day_value(dd,mm,yyyy):
    '''
    takes date in dd,mm,yyy format
    returns the number of days elapsed since 01/01/0000
    '''

    # step find total days before the start of year yyyy
    y=yyyy-1
    days =   y*365  \
           + y//4   \
           - y//100 \
           + y//400
    
    # to this add days in month till mm-1
    m=1
    while m< mm:
        days+= days_in_month(m,yyyy)
        m+=1

    # add dd to the running total
    return days+dd

def is_leap_year(year):
    return year % (4 if year%100!=0 else 400) ==0


def days_in_month(month, year=2001):
    if month==2:
        return 28 if not is_leap_year(year) else 29
    elif month<8 and month%2==1 or month>=8 and month%2==0:
        return 31
    else:
        return 30
        