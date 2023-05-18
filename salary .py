# month=int(input("Enter number of days: "))
# holidays=int(input("Enter number of holidays: "))
# working_days=int(month-holidays)
# print(working_days)
# salary_per_day=int(input("Enter the daily salary: "))
# monthly_salary=int(31*salary_per_day)
# print(monthly_salary)
# late_entry=int(input("Enter the no of let days: "))
# total_salary=monthly_salary

# late_counter=0
# for i in range (late_entry):
#     late_counter+=1
#     if late_counter==3:
#         total_salary-=salary_per_day
#         late_counter=0
# print(total_salary)
# Early_Going=int(input("Enter the no of early: "))
# output=0
# for j in range(Early_Going):
#     output+=1
#     if output==4:
#         total_salary-=salary_per_day
#         output=0
# print("tolal salary",total_salary)

month = int(input("enter the working day: "))
holiday = int(input("enter the holiday: "))
workaing_day = int(month-holiday)
print(workaing_day)
salary_par_day = int(input("enter salary par day: "))
monthly_salary = int(30*salary_par_day)
print(monthly_salary)

late_entry = int(input("enter the late entry: "))
total_salary = monthly_salary

late_countr = 0
for i in range(late_entry):
    late_countr+=1
    if late_countr==3:
        total_salary-=salary_par_day
        late_countr = 0
print(total_salary)

early_going = int(input("enter the early going day: "))
total_salary = monthly_salary

early_counter = 0
for j in range(early_going):
    early_going+=1
    if early_going==4:
        total_salary-=salary_par_day
        early_counter = 0
print(total_salary)
