import pandas as pd
import enquiries
import time
import sys
import constants as const
from choices import employee, manager


def end_of_step():
    next_step = enquiries.choose(
        "\n\n  Do you want to know anything else ? ", ["Yes", "No"]
    )
    if next_step == "Yes":
        const.clearConsole()
        run_choices()
    if next_step == "No":
        const.clearConsole()


def greet_user(name):
    const.clearConsole()
    print(f"\n  Welcome back {name}")
    time.sleep(3)
    const.clearConsole()


def run_choices():
    if level == const.rep:
        employee.employee_choices_main(emp_id, employees_df)
    if level == const.manager:
        manager.manager_choices_main(emp_id, employees_df)
    end_of_step()


transac_df = pd.read_excel(const.transactions_file_path)
employees_df = pd.read_excel(const.transactions_file_path, sheet_name="Employee Data")
emp_id = input("Please input your employee ID\n")
try:
    level = employees_df[const.job][employees_df[const.emp_id] == int(emp_id)].values[0]
except:
    print("user not found")
    sys.exit()

emp_name = employees_df[const.first_name][
    employees_df[const.emp_id] == int(emp_id)
].values[0]
greet_user(emp_name)
run_choices()
