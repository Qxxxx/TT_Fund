import pandas as pd


def pick_fund_by_rank(rank=1500):
    fund = pd.read_csv(
        "/home/q/TT_Fund/fund_earning_list_20211113.csv", dtype={'code': str})
    # print(fund.code[0])

    fund_1m = fund.sort_values(
        "rate_recent_month", ascending=False)[0:rank]

    fund_3m = fund.sort_values(
        "rate_recent_3month", ascending=False)[0:rank]

    fund_6m = fund.sort_values(
        "rate_recent_6month", ascending=False)[0:rank]

    fund_1y = fund.sort_values(
        "rate_recent_year", ascending=False)[0:rank]

    fund_index = fund_1m.index.intersection(fund_3m.index)\
        .intersection(fund_6m.index)\
        .intersection(fund_1y.index)\

    fund_selected = fund.loc[fund_index]
    fund_selected.set_index("code", inplace=True)

    return fund_selected


if __name__ == '__main__':

    print(pick_fund_by_rank(1500).index[0])
    pick_fund_by_rank(1500).to_csv("1500.csv")
