import pandas as pd
import constants as const


def get_quart_warranties(emp_id, chosen_quarter, transac_df):
    valid_months = get_available_months_in_chosen_quarter(chosen_quarter, transac_df)
    quarterly_warranty_sales = get_quart_warranty_sales(
        emp_id, valid_months, transac_df
    )

    quart_warranty_salary = const.warranty_rate * quarterly_warranty_sales
    warranty_results = {
        "sales": quarterly_warranty_sales,
        "salary": quart_warranty_salary,
    }

    return warranty_results


def get_quart_warranty_sales(emp_id, valid_months, transac_df):
    sales = transac_df[const.sales][
        (transac_df[const.date].dt.month.isin(valid_months))
        & (transac_df[const.emp_id] == int(emp_id))
        & (transac_df[const.warranty] == "Y")
    ].sum()

    return sales


def get_available_months_in_chosen_quarter(chosen_quarter, transac_df):
    available_months_in_chosen_quarter = []
    available_months_nums = get_available_months_nums(transac_df)
    for month in available_months_nums:
        quarter = const.get_date_info(int(month), "num")["quarter"]
        if quarter == chosen_quarter:
            available_months_in_chosen_quarter.append(int(month))

    return available_months_in_chosen_quarter


def get_available_quarters(transac_df):
    available_quarters = []
    available_months_nums = get_available_months_nums(transac_df)
    for month in available_months_nums:
        quarter = const.get_date_info(int(month), "num")["quarter"]
        available_quarters.append(quarter)
    available_quarters = list(set(available_quarters))

    return available_quarters


def get_available_months_nums(transac_df):
    available_months_nums = list(transac_df[const.date].dt.month.unique())
    available_months_nums = [x for x in available_months_nums if str(x) != "nan"]

    return available_months_nums
