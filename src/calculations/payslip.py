import pandas as pd
import constants as const
from calculations import quarterly, monthly, spiff
import numpy as np


def get_payslip(emp_id, transac_df):
    all_quarters_results = []
    available_quarters = quarterly.get_available_quarters(transac_df)
    for quarter in available_quarters:
        quarter_monthlies = get_quarter_monthlies_total(quarter, emp_id, transac_df)
        quarter_warranties = quarterly.get_quart_warranties(
            emp_id, quarter, transac_df
        )["salary"]
        quarter_result = {
            "quarter": quarter,
            "monthlies": quarter_monthlies,
            "warranties": quarter_warranties,
            "total": quarter_monthlies + quarter_warranties,
        }
        all_quarters_results.append(quarter_result)
        total_spiff = spiff.get_spiff(emp_id, transac_df)
    payslip = setup_payslip_df(all_quarters_results, total_spiff["payout"])

    return payslip


def get_quarter_monthlies_total(quarter, emp_id, transac_df):
    quarterly_monthlies = []
    months_in_quarter = quarterly.get_available_months_in_chosen_quarter(
        quarter, transac_df
    )
    for month in months_in_quarter:
        monthly_salary = monthly.monthly_compensation(emp_id, month, transac_df)[
            "salary"
        ]
        quarterly_monthlies.append(monthly_salary)
    total = sum(quarterly_monthlies)

    return total


def setup_payslip_df(all_quarters_results, total_spiff):
    final_df = pd.DataFrame([], columns=const.payslip_df_quarters)
    for i in range(len(all_quarters_results)):
        column_to_update = all_quarters_results[i]["quarter"] - 1
        active_df = pd.DataFrame(
            np.array(
                [
                    all_quarters_results[i]["monthlies"],
                    all_quarters_results[i]["warranties"],
                    all_quarters_results[i]["total"],
                ]
            ),
            columns=[const.payslip_df_quarters[column_to_update]],
        )
        final_df[const.payslip_df_quarters[column_to_update]] = active_df
    final_df.rename(index={0: "monthlies"}, inplace=True)
    final_df.rename(index={1: "warranties"}, inplace=True)
    final_df.rename(index={2: "total"}, inplace=True)
    final_df["spiff"] = np.nan
    final_df["spiff"]["total"] = total_spiff
    final_df["Year"] = final_df[list(final_df.columns)].sum(axis=1)
    const.clearConsole()

    return final_df
