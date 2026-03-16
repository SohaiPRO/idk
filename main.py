
1 of 3
# A simple script for a future Engineer to factor quadratic equations: ax^2 + bx + c import math 
print("--- Sohaib's Engineering Math Tool ---") 
# We input the coefficients
a = float(input("Enter a: ")) 
b = float(input("Enter b: ")) 
c = float(input("Enter c: ")) 
# Calculate the discriminant (Delta) 
# Formula: Δ = b² - 4ac 
delta = b**2 - 4*a*c 
if delta < 0:
  print("No real factors. The roots are complex!") 
elif delta == 0:
  x = -b / (2*a) 
  print(f"Perfect Square! Factor: (x - {x})^2") 
else: x1 = (-b + math.sqrt(delta)) / (2*a)
  x2 = (-b - math.sqrt(delta)) / (2*a)
print(f"The factors are: (x - {x1})(x - {x2})") 
