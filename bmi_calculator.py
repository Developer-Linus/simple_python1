# Function to calculate BMI and return classification
def calculate_bmi(weight, height):
    # BMI formula: BMI = weight(kgs)/(height(m)*height(m))
    bmi = weight/(height**2)
    # Determine weight classification based on BMI value
    if bmi<18.5:
        category = "Underweight"
    elif bmi <25:
        category = "Normal"
    elif bmi >30:
        category = "Overweight"
    else: 
        category = "Obese"
    return bmi, category
# Main program starts here
def main():
    # Get the weight of the user in kilograms
    weight = float(input("Please enter your weight in kilograms: "))
    # Get the height of user in meters
    height = float(input("Please input your height in meters: "))
    # call the function to calculate bmi
    bmi, category = calculate_bmi(weight, height)
    # Output the results to the user
    print(f"\n Your BMI is {bmi:.2f}")
    print(f"Based on your BMI, you are classified as: {category}")
# Call the main function to run the program
if __name__ == "__main__":
        main()