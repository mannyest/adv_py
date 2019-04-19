import pandas as pd

def by_pandas():

    file_buys = pd.read_csv('ad_buys.csv')
    file_comp = pd.read_csv('ad_companies.csv')

    query_buys = file_buys.groupby('buyer_id').sum()
    query_comps = file_comp.groupby('company_id').sum()

    merged = pd.merge(query_comps, query_buys, left_index = True, right_index = True)
    output = merged[['company_name', 'volume']]
    return(output)

print(by_pandas())

# def by_pandas():
# def by_pandas():

#     file_buys = pd.read_csv('ad_buys.csv')
#     file_comp = pd.read_csv('ad_companies.csv')

#     print(file_buys)
#     print(file_comp)

#     query_buys = file_buys.groupby('buyer_id').sum()
#     print(query_buys)

#     agg_file = pd.merge(file_comp, file_buys, how = 'inner', left_on = 'company_id', right_on = 'buyer_id')
#     print(agg_file)


# print(by_pandas())
