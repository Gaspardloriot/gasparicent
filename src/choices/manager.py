import pandas as pd
import constants as const
import numpy as np
from calculations import monthly, quarterly, spiff, payslip
import enquiries


transac_df = pd.read_excel(const.transactions_file_path)


def get_my_team(emp_id, employees_df):
    my_team = list(
        employees_df[const.emp_id][employees_df[const.manager_col] == int(emp_id)]
    )

    return my_team


def get_team_performance(my_team):
    final_df_rows = []
    for rep in my_team:
        emp_payslip = payslip.get_payslip(rep, transac_df)
        row = list(emp_payslip.loc[["total"]].values)[0]
        row = np.insert(row, 0, rep, axis=0)
        final_df_rows.append(row)
    final_df = pd.DataFrame(final_df_rows, columns=const.team_performance_columns)

    return final_df


def get_bonus(quarter_sales):
    bonus = 0
    rate = 0
    sales_to_target = quarter_sales / const.regional_quarterly
    if sales_to_target >= 0.5:
        bonus = const.OTE * 0.5
        rate = 0.5
    if sales_to_target >= 0.75:
        bonus = const.OTE * 0.75
        rate = 0.75
    if sales_to_target >= 1:
        bonus = const.OTE * 1
        rate = 1

    return [bonus, sales_to_target, rate]


def manager_choices_main(emp_id, employees_df):

    chosen_option = enquiries.choose(
        "What do you wish to access? ", const.manager_choices
    )
    my_team = get_my_team(emp_id, employees_df)
    # Get sales of team for recorded period
    if chosen_option == const.manager_choices[0]:
        team_sales = transac_df[(transac_df[const.emp_id].isin(my_team))]
        team_sales.to_excel(
            f"../output_files/emp_{emp_id}_team_sales.xlsx", index=False
        )
        print(
            "Your team sales data has been printed into the team_sales file in the output_folder"
        )
    # Get salary breakdown for team
    if chosen_option == const.manager_choices[1]:
        sales_performance_df = get_team_performance(my_team)
        print(sales_performance_df)
        print("\n\n\n\n")
        sales_performance_df.to_excel(
            f"../output_files/emp_{emp_id}_team_salaries.xlsx", index=False
        )
        print(
            "Your team salary data has been printed into the team_salaries file in the output_folder"
        )
    # Get quarterly bonus info
    if chosen_option == const.manager_choices[2]:
        available_quarters = quarterly.get_available_quarters(transac_df)
        chosen_quarter = enquiries.choose("Select a quarter", available_quarters)
        months_to_get_sales = quarterly.get_available_months_in_chosen_quarter(
            chosen_quarter, transac_df
        )
        team_quarter_sales = []
        for rep in my_team:
            rep_quarter_sales = []
            for month in months_to_get_sales:
                rep_monthly_sales = monthly.get_monthly_sales(rep, month, transac_df)
                rep_quarter_sales.append(rep_monthly_sales)
            rep_total_sales = sum(rep_quarter_sales)
            team_quarter_sales.append(rep_total_sales)
        team_quarter_total = sum(team_quarter_sales)
        bonus_info = get_bonus(team_quarter_total)
        result = {
            "team_sales": team_quarter_total,
            "completed_objective": bonus_info[1],
            "bonus_rate": bonus_info[2],
            "bonus": bonus_info[0],
        }
        result_df = pd.DataFrame([result], columns=result.keys())

        print(result_df)
    # Get info of manager's team
    if chosen_option == const.manager_choices[3]:
        my_team_info = employees_df[employees_df[const.manager_col] == int(emp_id)]
        print(my_team_info)
    # Get info of manager
    if chosen_option == const.manager_choices[4]:
        my_info = employees_df[employees_df[const.emp_id] == int(emp_id)]
        print(my_info)
