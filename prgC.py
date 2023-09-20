month= input("enter the month:")
if month in('December','January','February'):
 season = 'winter'
elif month in ('March','April','May'):
 season = 'spring'
elif month in ('June','July','August'):
 season = 'summer'
else:
 season = 'autumn'
print("Season is",season)
