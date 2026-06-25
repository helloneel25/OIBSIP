# Python programm for the BMI calculator 

'''BODY MASS INDEX (BMI) = RATIO OF WEIGHT IN KGS TO THE SQUARE OF HEIGHT IN METERS

                           BMI = weight(in kgs)/height square(in meters)
                           units = kg per meter square (kg/m.sq)

BMI < 18.5 ---> Under Weight
18.5 <= BMI <= 24.9  ---> Healthy Weight / Normal weight
25 <= BMI <= 29.9 ---> Over Weight
BMI >= 30 ---> obese'''


def details():                                  
    name = input("Please enter your name: ")     # take the inputs from the user

    while True:
        try:
            weight = float(input("Enter your weight in kilograms: "))       # input validation for the weight
            if weight <= 0:
                print("Weight must be greater than 0.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    while True:
        try:
            height = float(input("Enter your height in feet: "))            # input validation for the height
            if height <= 0:
                print("Height must be greater than 0.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    height = round(height * 0.3048, 2)

    return name, weight, height


def show(name,Weight,H):                                                    # display the inputs 
    print(f"{name} your weight is {Weight} kg")
    print(f"{name} your height in meters {H} mts")

def BMI_cal(name,Weight,H):                                                 #calculating the  BMI
    BMI = Weight/(H**2) 
    BMI = round(BMI,2)

    if(BMI<18.5):
        print(f"hello {name} is your BMI value is {BMI} kg/m.sq")
        print("Category: Underweight")
        print("Suggestion: Eat a balanced, nutritious diet and consult a healthcare professional if needed.")

    elif(18.5 <= BMI <= 24.9):
        print(f"hello {name} is your BMI value is {BMI} kg/m.sq")
        print("Category: Healthy weight")
        print("Suggestion: Great job! Continue maintaining a balanced diet and regular physical activity.")  

    elif(25 <= BMI <= 29.9):
        print(f"hello {name} is your BMI value is {BMI} kg/m.sq")
        print("Category: Overweight")
        print("Suggestion: Focus on a balanced diet, regular exercise, and healthy daily habits")

    elif(BMI >= 30):
        print(f"hello {name} is your BMI value is {BMI} kg/m.sq")
        print("Category: Obese")
        print("Suggestion: Adopt sustainable lifestyle changes to improve overall health.")


# Main 

print("Welcome to the BMI Calculator! Please enter your weight (kg) and height (m) to calculate your Body Mass Index.")
name,Weight,H =details()
show(name,Weight,H)
BMI_cal(name,Weight,H)















