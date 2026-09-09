'''
# BMI (Body Mass Index)

# Formula of BMI - (weight)/((height)**2) , weight-kg , height-m
n = int(input("enter no. of records:"))
for i in range(n):
    name = input(f'\nenter your name{i+1}:')
    weight = float(input("enter your weight in kgs:"))
    height = float(input("enter your height in meters:"))
    if weight > 0 and height > 0:
        BMI = (weight)/((height)**2)
        if BMI < 18.5:
            print(f'{name} is in Under Weight and BMI is {BMI:.2f}\n')
        elif 18.5 <= BMI <=24.9:
            print(f'{name} is in Normal Weight and BMI is {BMI:.2f}\n')
        elif 25 <= BMI <=29.9:
            print(f'{name} is in Over Weight and BMI is {BMI:.2f}\n')
        else:
            print(f'{name} is in Obesity and BMI is {BMI:.2f}\n')
    else:
        print("your weight and height should strictly greater than 0\n")

'''
#Repition --> While
#Task --> Store the results of name , weight , height --> BMI into a collection
#Same above task we need to handle the errors(Exception Handling) and also make sure strictly to enter only numeric values

while True:
    
    #in this case we prefer Exception Handling
    try:
        weight = float(input("Enter the weight in kgs:"))
        height = float(input("Enter the height in metres:"))
        if weight > 0 and height > 0:
            # Calculate BMI
            break
        else:
            print("Make sure to enter only +ve values")

    #except ValueError:
         #print("Invalid input! Please enter only numeric values.")
    except Exception as e:
        print(e)
BMI = weight / (height ** 2)
print(BMI)
# BMI Category
if BMI < 18.5:
    category = "Underweight"
elif 18.5 <= BMI <= 24.9:
    category = "Normal weight"
elif 25 <= BMI <= 29.9:
    category = "Overweight"
else:
    category = "Obesity"
    print("Category:", category)     
