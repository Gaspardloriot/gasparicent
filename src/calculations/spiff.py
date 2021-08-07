import constants as const


def get_spiff(emp_id, transac_df):
    sales = transac_df[const.qty][
        (transac_df[const.product].isin(const.spiff_products))
        & (transac_df[const.emp_id] == int(emp_id))
    ].sum()

    total_spiff = const.pay_per_item * sales
    spiff_results = {"quantity": sales, "payout": total_spiff}

    return spiff_results
