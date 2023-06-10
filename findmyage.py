import datetime

ma = datetime.datetime(2013, 2, 17)

print(ma)

y = datetime.datetime.now()

print(y)

ageresult =  y - ma
ageresult2 = ageresult.days / 365
print("Bouya age >", ageresult2)