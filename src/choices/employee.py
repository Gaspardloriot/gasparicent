import pandas as pd
import constants as const
from calculations import monthly, quarterly, spiff, payslip
import enquiries


transac_df = pd.read_excel(const.transactions_file_path)


def employee_choices_main(emp_id):

    chosen_option = enquiries.choose("What do you wish to access? ", const.emp_choices)
    # Choice 1: Selecting to see all sales data for recorded period
    if chosen_option == const.emp_choices[0]:
        total_sales = transac_df[transac_df[const.emp_id] == int(emp_id)]
        total_sales.to_excel(
            f"../output_files/emp_{emp_id}total_sales.xlsx", index=False
        )
        print(
            "Your sales data has been printed into the total_sales file in the output_folder"
        )
    # Choice 2: Selecting monthly compensation for a specific month
    if chosen_option == const.emp_choices[1]:
        chosen_month = enquiries.choose(
            "Please select a month", monthly.get_available_months(transac_df)
        )
        chosen_month_number = const.get_date_info(chosen_month)["number"]
        results = monthly.monthly_compensation(emp_id, chosen_month_number, transac_df)
        results_df = pd.DataFrame([results], columns=results.keys())
        print(results_df)
    # Choice 3: Selecting quarterly warranty payout
    if chosen_option == const.emp_choices[2]:
        chosen_quarter = enquiries.choose(
            "Please Select a quarter", quarterly.get_available_quarters(transac_df)
        )
        results = quarterly.get_quart_warranties(emp_id, chosen_quarter, transac_df)
        results_df = pd.DataFrame([results], columns=results.keys())
        print(results_df)
    # Choice 4: Selecting total spiff payout
    if chosen_option == const.emp_choices[3]:
        results = spiff.get_spiff(emp_id, transac_df)
        results_df = pd.DataFrame([results], columns=results.keys())
        print(results_df)
    # Choice 5: Getting total compensation for the year
    if chosen_option == const.emp_choices[4]:
        payslip_df = payslip.get_payslip(emp_id, transac_df)
        payslip_df.to_excel(
            f"../output_files/employee_{emp_id}_payslip.xlsx", index=True
        )
        print(
            "Your payslip has been printed into the total_sales file in the output_folder"
        )
