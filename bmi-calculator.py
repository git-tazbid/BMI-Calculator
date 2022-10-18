# BMI Calculator
import math
weight=float(input("Please enter your weight in KG: "))
height=float(input("Please enter your height in meter: "))
bmi=weight/math.pow(height,2)
if bmi<18.5:
  print("Your BMI :", bmi)
  print("Your body type: Under Weight")
elif bmi>=18.5 and bmi<24.9:
  print("Your BMI :", bmi)
  print("Your body type: Normal")
elif bmi>=25 and bmi<29.9:
  print("Your BMI :", bmi)
  print("Your body type: Over weight")
elif bmi>=30 and bmi<34.9:
  print("Your BMI :", bmi)
  print("Your body type: Obese")
else:
  print("Your BMI :", bmi)
  print("Your body type: Extremely obese")
