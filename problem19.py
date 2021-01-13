# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

def get_days():
   week_days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
   week_days_num = [i for i in range(1, 8)]

   months = [i for i in range(1, 13)]
   month_30_days = [4, 6, 9, 11]
   month_31_days = [1, 3, 5, 7, 8, 10, 12]
   month_28_days = [2]

   
   cur_day = 1 # 1 Jan 1900 was Monday
   sundays = 0
   
   for year in range(1900, 2001):
      for month in range(1, 13):
         if month in month_30_days:
            days = 30
         elif month in month_31_days:
            days = 31
         elif month in month_28_days:
            if year % 4 == 0 and not year == 1900:
               days = 29
            else:
               days = 28

         for day in range(1, days + 1):
            today = week_days[cur_day]
            
            if today == "Sun" and day == 1 and year != 1900:
               sundays += 1
               print("Year: ", year, "Month: ", month, "Day: ", day, today)

            cur_day += 1
            cur_day = cur_day % 7

   print(sundays)


if __name__ == "__main__":
   get_days()
   