from datetime import date

#Constants to be used in target list
MONTH_INDEX = 0
DATE_INDEX = 1
YEAR_INDEX = 2

#returns the weekday of a specific date
def searchWeekday(date):
    return date.isoweekday()

#Get the day to search from the user
userInput = input("Please enter the date in \"Month, Date, Year\" format\n")


target = userInput.split(", ")

#Numerical value of named months and weekdays
months = {

    "January" : 1,
    "February" : 2,
    "March" : 3,
    "April" : 4,
    "May" : 5,
    "June" : 6,
    "July" : 7,
    "August" : 8,
    "September" : 9,
    "October" : 10,
    "November" : 11,
    "December" : 12   

}
days = {

    1 : "Monday",
    2 : "Tuesday",
    3 : "Wednesday",
    4 : "Thursday",
    5 : "Friday",
    6 : "Saturday",
    7 : "Sunday"

}
targetMonthNumerical = months[target[MONTH_INDEX]]

#The date of which the weekday is to be returned
searchingDay = date(int(target[YEAR_INDEX]), targetMonthNumerical, int(target[DATE_INDEX]))

print(days[searchWeekday(searchingDay)])