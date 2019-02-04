year = 2015
if (year % 4) == 0:
 if (year % 100) == 0:
   if (year % 400) == 0:
     print("{0} is a LEAP year".format(year))
   else:
     print("{0} is not a LEAP year".format(year))
 else:
   print("{0} is a LEAP year".format(year))
else:
  print("{0} is not a LEAP year".format(year))
