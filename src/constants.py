import os


# Date logic
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

# Transaction data
transactions_file_path = "../source_files/comp_scenario.xlsx"
# column_names
date = "Date of Sale"
emp_id = "EmployeeID"
sales = "Total Sale"
warranty = "Warranty? (Y/N)"
qty = "Qty"
product = "Product"


# Warranty rates
warranty_rate = 0.5

# spiff products
spiff_products = ["USO Pen", "USO Pencil"]
pay_per_item = 2


# Employee data
#    Employee levels
rep = "Sales Associate"
manager = "Regional Sales Manager"
#    Employee choices
emp_choices = [
    "My sales",
    "Monthly Compensation",
    "Quarterly Warranties",
    "Total Spiff",
    "Total Compensation (Payslip)",
    "My Info",
]

payslip_df_quarters = ["Q1", "Q2", "Q3", "Q4"]


def get_date_info(month, type="name"):
    if type == "name":
        month_num = months.index(month) + 1
        quarter = int(month_num / 3) if month_num % 3 == 0 else int(month_num / 3) + 1
        date_info = {"quarter": quarter, "name": month, "number": month_num}
    if type == "num":
        quarter = int(month / 3) if month % 3 == 0 else int(month / 3) + 1
        month_name = months[month - 1]
        date_info = {"quarter": quarter, "name": month_name, "number": month}

    return date_info


def clearConsole():
    command = "clear"
    if os.name in ("nt", "dos"):  # If Machine is running on Windows, use cls
        command = "cls"
    os.system(command)


clearConsole()
