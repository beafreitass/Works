def circle_area(radius):
    pi = 3.14159
    area = pi * radius ** 2
    return area

def calcuate_tax(money, tax_rate):
    total_due = money + (money * tax_rate)
    return total_due

def fahrenheit_to_celcius(fahrenheit):
    celcius = (fahrenheit - 32) * (5 / 9)
    return celcius

#Circle
radius = float(input("Enter the radius of the circle: "))
area = circle_area(radius)
print(f"The area of the circle is: {area:.2f}")

#Taxes
money = float(input("Enter the amount of money: "))
tax_rate = float(input("Enter the tax rate (as a decimal, e.g. 0.06 for 6%): "))
total_due = calcuate_tax(money, tax_rate)
print(f"The total due is: {total_due:.2f}")

#Temperature
fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
celsius =fahrenheit_to_celcius(fahrenheit)
print(f"The temperature in Celsius is: {celsius}")