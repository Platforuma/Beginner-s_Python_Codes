'''
Write a Python program to convert month name to a number of days. 
Expected Output:
List of months: January, February, March, April, May, June, July, August
, September, October, November, December                                
Input the name of Month: February                                       
No. of days: 28/29 days 
'''

month = input('Enter a month: ')

print('----Using multiple if statemetns----')

if month=='January' or month=='january':
    print('No of Days: 31 Days')

elif month=='February' or month=='february':
    print('No of Days: 28/29 Days')

elif month=='March' or month=='march':
    print('No of Days: 31 Days')

elif month=='April' or month=='april':
    print('No of Days: 30 Days')

elif month=='May' or month=='may':
    print('No of Days: 31 Days')

elif month=='June' or month=='june':
    print('No of Days: 30 Days')

elif month=='July' or month=='july':
    print('No of Days: 31 Days')

elif month=='August' or month=='august':
    print('No of Days: 31 Days')

elif month=='September' or month=='september':
    print('No of Days: 30 Days')

elif month=='October' or month=='october':
    print('No of Days: 31 Days')

elif month=='November' or month=='november':
    print('No of Days: 30 Days')

elif month=='December' or month=='december':
    print('No of Days: 31 Days')

else:
    print('Enter the month from "January, February, March, April, May, June, July, August, September, October, November, December"')

print(' ' )

#using Dictionary
print('----Using Dictionary----')
month_day = {'January' : '31 Days', 'january' : '31 Days',
             'February' : '28/29 Days', 'february' : '28/29 Days',
             'March' : '31 Days', 'march' : '31 Days',
             'April' : '30 Days', 'april' : '30 Days',
             'May' : '31 Days', 'may' : '31 Days',
             'June' : '30 Days', 'june' : '30 Days',
             'July' : '31 Days', 'july' : '31 Days',
             'August' : '31 Days', 'august' : '31 Days',
             'September' : '30 Days', 'september' : '30 Days',
             'October' : '31 Days', 'october' : '31 Days',
             'November' : '30 Days', 'november' : '30 Days',
             'December' : '31 Days', 'december' : '31 Days'}

if month in month_day.keys():
    print('No. of days: ', month_day[month])
else:
    print('Enter the month from "January, February, March, April, May, June, July, August, September, October, November, December"')
