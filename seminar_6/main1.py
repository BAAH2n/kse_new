import geometry
import convertor
import taxes
import math
import random
from datetime import datetime
print ("Задача 1: ", geometry.rectangle_area(4, 6))
print ("Задача 2: ", convertor.uah_to_usd(1000, 39.5), convertor.usd_to_uah(1000, 39.5))
print ("Задача 3: ", taxes.calculate_income_tax(taxes.calculate_vat(15000)))
print ("Задача 4: ", math.sqrt(121))
res1 = random.randint(1,6)
res2 = random.randint(1,6)
print (f"Задача 5: перший кидок: {res1}, другий кидок: {res2}, середнє: {(res1+res2)/2} ") 
birth = input ("Введіть дату народження (у форматі рррр-мм-дд): ")
input = datetime.strptime(birth, "%Y-%m-%d")
print ("Задача 6: ", datetime.now()-input)