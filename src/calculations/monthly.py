import pandas as pd
import constants as const


def monthly_compensation(emp_id, month, transac_df):
    # monthly_salary=transac_df[const.sales][(transac_df[const.date].dt.month == 4) & (transac_df[const.emp_id].isin(possible_emps))].sum()
    monthly_sales = get_monthly_sales(emp_id, month, transac_df)
    rate = get_monthly_rate(monthly_sales)
    monthly_salary = round(monthly_sales * rate, 1)
    monthly_results = {"sales": monthly_sales, "rate": rate, "salary": monthly_salary}

    return monthly_results


def get_monthly_sales(emp_id, month, transac_df):
    monthly_sales = transac_df[const.sales][
        (transac_df[const.date].dt.month == month)
        & (transac_df[const.emp_id] == int(emp_id))
    ].sum()

    return monthly_sales


def get_available_months(transac_df):
    available_months_names = []
    available_months_nums = list(transac_df[const.date].dt.month.unique())
    available_months_nums = [x for x in available_months_nums if str(x) != "nan"]
    for num in available_months_nums:
        name = const.get_date_info(int(num), "num")["name"]
        available_months_names.append(name)

    return available_months_names


def get_monthly_rate(monthly_sales):
    monthly_rate = 0
    if monthly_sales >= 200:
        monthly_rate = 0.035
    if monthly_sales >= 300:
        monthly_rate = 0.05
    if monthly_sales >= 400:
        monthly_rate = 0.07
    if monthly_sales >= 550:
        monthly_rate = 0.1

    return monthly_rate
