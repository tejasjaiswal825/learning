from datetime import datetime

employee_data = [
    {'id': 101,'name': 'Vishal Kashikar','gender': 'Male','dob': '08-07-2000','state': 'Maharashtra',},
    {'id': 102,'name': 'Shubham Chamote','gender': 'Male','dob': '12-18-1998','state': 'Delhi',},
    {'id': 103,'name': 'Ankita Belekar','gender': 'Female','dob': '11-25-1992','state': 'Uttar Pradesh',},
    {'id': 104,'name': 'Nikhil Latkar','gender': 'Male','dob': '10-13-1999','state': 'Gujarat',},
    {'id': 105,'name': 'Abhit Mishra','gender': 'Male','dob': '09-12-1999','state': 'Telangana',},
    {'id': 106,'name': 'Shiv Likhare','gender': 'Male','dob': '01-15-2003','state': 'Haryana',},
    {'id': 107,'name': 'Harsh Nikam','gender': 'Male','dob': '02-01-2002','state': 'Punjab',},
    {'id': 108,'name': 'Jatin Raut','gender': 'Male','dob': '10-24-2001','state': 'Rajasthan',},
    {'id': 109,'name': 'Aparna Bhajbhuje','gender': 'Female','dob': '10-14-1998','state': 'Madhya Pradesh',},
    {'id': 110,'name': 'Rahul Selokar','gender': 'Male','dob': '01-17-2001','state': 'Odisha',},
    {'id': 111,'name': 'Priti Sharnagat','gender': 'Female','dob': '04-10-1999','state': 'Bihar',},
    {'id': 112,'name': 'Monali Gawande','gender': 'Female','dob': '09-02-1998','state': 'Karnataka',},
    {'id': 113,'name': 'Shubham Dubey','gender': 'Male','dob': '05-30-1997','state': 'West Bengal',},
    {'id': 114,'name': 'Tejas Jaiswal','gender': 'Male','dob': '09-25-1998','state': 'Assam',},
    {'id': 115,'name': 'Milind Raut','gender': 'Male','dob': '12-01-1996','state': 'Tamil Nadu',},
    {'id': 116,'name': 'Rakesh Bhowate','gender': 'Male','dob': '09-15-1998','state': 'Andhra Pradesh',},
    {'id': 117,'name': 'Bhagyashree Raut','gender': 'Female','dob': '10-02-2002','state': 'Uttarakhand',},
    {'id': 118,'name': 'Shruti Punekar','gender': 'Female','dob': '07-02-2003','state': 'Kerala',},
    {'id': 119,'name': 'Saurabh Thosar','gender': 'Male','dob': '01-01-2000','state': 'Jharkhand',},
    {'id': 120,'name': 'Yashshree Kawale','gender': 'Female','dob': '07-19-1995','state': 'Chhattisgarh',},
    {'id': 121,'name': 'Pravina Dighore','gender': 'Female','dob': '11-22-2000','state': 'Goa',},
    {'id': 122,'name': 'Harish Patel','gender': 'Male','dob': '07-24-1988','state': 'Himachal Pradesh',},
    {'id': 123,'name': 'Mohan Verma','gender': 'Male','dob': '01-31-1995','state': 'Manipur',},
    {'id': 124,'name': 'Naina Kapoor','gender': 'Female','dob': '06-18-1986','state': 'Meghalaya',},
    {'id': 125,'name': 'Prateek Sharma','gender': 'Male','dob': '02-03-1989','state': 'Mizoram',},
    {'id': 126,'name': 'Ritu Deshmukh','gender': 'Female','dob': '08-16-1981','state': 'Nagaland',},
    {'id': 127,'name': 'Amit Roy','gender': 'Male','dob': '04-07-1993','state': 'Sikkim',},
    {'id': 128,'name': 'Neeta Sharma','gender': 'Female','dob': '10-20-1984','state': 'Tripura',},
    {'id': 129,'name': 'Vishal Kapoor','gender': 'Male','dob': '05-13-1990','state': 'Uttar Pradesh',},
    {'id': 130,'name': 'Pooja Singh','gender': 'Female', 'dob': '02-05-1987','state': 'West Bengal',},
]

def month_from_dob(dob):
    dob_date = datetime.strptime(dob, "%m-%d-%Y")
    current_date = datetime.now()
    
    if current_date.month > dob_date.month or (current_date.month == dob_date.month and current_date.day >= dob_date.day):
        year_of_birth = current_date.year
    else:
        year_of_birth = current_date.year - 1
    
    dob_date = dob_date.replace(year=year_of_birth)
    
    month_name = dob_date.strftime("%B")
    day_name = dob_date.strftime("%A")
    day_number = dob_date.strftime("%d")
    
    return month_name, day_name, day_number

def name_from_month(month, employee_data):
    matching_names = [employee['name'] for employee in employee_data if month_from_dob(employee['dob'])[0] == month]
    return matching_names

input_value = input("Enter either an employee name or a month name: ")

if input_value in [employee['name'] for employee in employee_data]:
    for employee in employee_data:
        if employee['name'] == input_value:
            month, day, date = month_from_dob(employee['dob'])
            print(f"{input_value}'s birthday is on {day}, {date} {month}.")
else:
    matching_names = name_from_month(input_value.capitalize(), employee_data)
    if matching_names:
        print(f"The employees born in {input_value.capitalize()} have birthdays on:") 
        for employee in employee_data:
            if employee['name'] in matching_names:
                month, day, date = month_from_dob(employee['dob'])
                print(f"{employee['name']}: {day}, {date} {month}")
    else:
        print(f"Please enter a valid input. {input_value.capitalize()}.")
