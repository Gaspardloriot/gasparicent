import pandas as pd
from choices import employee
import constants as const


transac_df = pd.read_excel(const.transactions_file_path)
employees_df = pd.read_excel(const.transactions_file_path, sheet_name="Employee Data")
emp_id = input("Please input your employee ID\n")
level = employees_df["Job Title"][employees_df[const.emp_id] == int(emp_id)].values[0]
if level == const.rep:
    employee.employee_choices_main(emp_id)


possible_emps = [1111111, 2222222]
