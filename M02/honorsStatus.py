"""
Name of Application:    honorsStatus.py
Author:                 Ryan Alvey
Description:

This application will accept a studen's name and GPA information and return if their status qualifies for 
Dean's list or Honor Roll. 

"""

try:
    # Initiate variable for test condition
    last_name_request = ""

    while last_name_request != "ZZZ":
        # Begin to evaluate for test condition to exit loop
        last_name_request = input("Please enter the student's last name: ")

        # If the user enters 'ZZZ', then the program will stop
        if last_name_request == "ZZZ":
            break

        # If valid input other than 'ZZZ', app begins to evaluate GPA vs Dean's list, Honor Roll, or neither.
        else:
            # Request remaining user input (First name and GPA)
            first_name_request = input("Please enter the student's first name: ")
            gpa_request = float(input("Please enter the student's GPA: "))
            
            # Evaluate GPA vs status (Dean's list, Honor Roll, or neither.)
            if gpa_request >= 3.5:
                print(f"{first_name_request} {last_name_request} has qualified for Dean's List with a GPA of {gpa_request}. \n")
            elif gpa_request >= 3.25:
                print(f"{first_name_request} {last_name_request} has qualified for Honor Roll with a GPA of {gpa_request}. \n")
            else:
                print(f"{first_name_request} {last_name_request} has not qualified for Dean's List or Honor Roll with a GPA of {gpa_request}. \n")

# If a user enters anything other than a number for GPA, this will raise an exception that will end the application.
except ValueError:
    print("Please use a valid number for the student's GPA")
