
#BMI weight guide
#  BMI = weight (kg) / height² (m²)

## under weight = less than 18.6

# normal range = 18.6 and 24.9
## overweight = greater than 24.9
#
#  input height in cm
# input weight in kg


while True:
   try: 
     height = float(input("Enter your height in cm: "))
     weight = float(input("Enter your weight in kg: "))
    
   
     bmi = weight/( ( height/100 )**2)
     break                                         # is used to exit the loop when we successfully get valid input and calculate the BMI.

   except ValueError:
       print("Please number only valid")


if bmi < 18.6:
    print(f"You are underweight. BMI: {bmi:.2f}")
elif bmi >= 18.6 and bmi < 24.9:
    print(f"You are normal. BMI: {bmi:.2f}")
else:
    print(f"You are overweight. BMI: {bmi:.2f}")
