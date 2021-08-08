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
    # Get sales breakdown for team
    if chosen_option == const.manager_choices[1]:
        sales_performance_df = get_team_performance(my_team)
        print(sales_performance_df)
        print("\n\n\n\n\n")
        sales_performance_df.to_excel(
            f"../output_files/emp_{emp_id}_team_salaries.xlsx", index=False
        )
        print(
            "Your team salary data has been printed into the team_salaries file in the output_folder"
        )
