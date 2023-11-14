print("height")
height = float(input())
print("weight")
weight = int(input())

BMI= weight / (height**2)
print(f"{BMI:.2f}")# (:.2f)  ondalık basağını iki basamak yapabilir.  

if BMI < 18.5 :
    print(f"Your BMI is {BMI}, you are underweight.")
elif BMI >= 18.5 and BMI<=24.9 :
    print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI >= 25 and BMI<=29.9 :
    print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI >= 30 and BMI<=34.9 :
    print(f"Your BMI is {BMI}, you are obese.")    
else :
    print(f"Your BMI is {BMI}, you are clinically obese.")