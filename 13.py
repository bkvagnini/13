## 13.py
## Brian K. Vagnini
## 11/10/18
## This program finds every occurence of Friday,the 13th,
## in the Month of October

from datetime import date
#import calendar
# lets you have pretty day of week names with calendar.day_name

results = []
#day_to_check = ? what goes here?
#stop_year = input("What's the last year you are looking for?: ")

today = date.today()
year = today.year
month = today.month
day = today.day
day_of_week = today.isoweekday()
# Below doesn't work right just yet
##year = date.year
##month = date.month
##day = date.day
##day_of_week = date.weekday

print (today)
print (year)
print (month)
print (day)
print (day_of_week)

# Below doesn't work right just yet
##for i in range (2018,3000):
##    if datetime.day == "13" and datetime.isoweekday() == "5" and datetime.month == "10":
##        results.append (datetime.year)
##    else:
##        print (str(datetime.year) + " is not the year.")
##        


print("The years where there is a Friday the 13th, ")
print ("in the month of October are as follows: ")

print (results)
