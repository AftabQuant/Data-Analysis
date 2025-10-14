import datetime as dt
x = dt.datetime.now()
print(x)

y = dt.datetime.date(x)
print(y)

# Print Day
print(x.strftime("%A"))

# Print Month
print(x.strftime("%B"))

# Print Year
print(x.strftime("%Y"))