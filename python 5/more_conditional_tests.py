#writing more conditional tests
#1.
#equality and inequality with strings
#(1)
pen_company = 'pentonic'
print(pen_company == 'pentonic')#equality
print(pen_company != 'pentonic')#inequality
#(2)
my_mobile_company ='realme'
print(my_mobile_company == 'realme')
print(my_mobile_company !='realme')
#2.tests using lower() method
name='Rama Deepika'
print(name.lower() == 'rama deepika')
print(name.lower() == 'Rama Deepika')
#3.Numerical tests
#(1)equality&inequality
my_cgpa = 9.07
print(my_cgpa == 9.07)
print(my_cgpa != 9.07)
#(2)greaterthan&lessthan
my_weight = 42
print(my_weight > 40)
print(my_weight < 39)
#(3)greater than or equal to, and less than or equal to
my_height = 5.2
print(my_height >= 5.2)
print(my_height <= 4.8)
#(4)Tests using the and keyword and the or keyword
charge = 99
print(charge > 90 and charge < 100)
print(charge > 98 or charge < 90)
#(4)Test whether an item is in a list
brands_of_pens=['pentonic','reynolds','elkos','bitco']
print('pentonic'in brands_of_pens)
print('gausier'in brands_of_pens)
#(5)Test whether an item is not in a list
print('bitco' not in brands_of_pens)
print('ball_pen' not in brands_of_pens)