#Set Methods in python:

# Declaration of 3 sets

Days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
workingDays = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}
Dates = {21, 22, 17}

# Printing elements in set days

print('Days:', Days)
print('Working Days:', workingDays)
print("Dates:", Dates)

# Adding element in  set

Days.add("Sunday")
print("Days:", Days)

# Removing the specified element from set

Days.discard("Wednesday")
print("Days:", Days)

# Union of set working days and dates

print("union of set working days and dates", workingDays.union(Dates))

# Intersection of set days and working days

print("intersection of set working days and days", workingDays.intersection(Dates))

# Checking set days and dates are disjoint or not

print("Is set days and dates are disjoint:", Days.isdisjoint(Dates))

# Difference between days and working days

print("difference between days and working days:", Days.difference(workingDays))
