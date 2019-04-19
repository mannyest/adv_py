import date_simple as ds

dateobj1 = ds.get_date_object()                      # datetime.date object for today
dateobj2 = ds.get_date_object(date='2018-12-26')     # datetime.date object for Feb 26, 2018

print(dateobj1, type(dateobj1))
print(dateobj2, type(dateobj2))

datestr1 = ds.get_date_string()
datestr2 = ds.get_date_string(date_object=dateobj2)
#datestr3 = ds.get_date_string(date_object='2018-12-26')

print(datestr1, type(datestr1))
print(datestr2, type(datestr2))


# datestr = ds.get_date_string(date_object=dateobj2, format='MM/DD/YYYY')
# print(datestr)
# datestr = ds.get_date_string(date_object=dateobj2, format='DD-Mon-YY')
# print(datestr)

