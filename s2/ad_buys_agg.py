## NYU - Adv Python - Blaikie - Homework Session 2 2018.06.19

#built-in python solution

def by_builtin():

    file_buys = open('ad_buys.csv')
    next(file_buys)
    buys_dict = {}

    for line in file_buys:
        line = line.rstrip()
        line = line.split(',')
        if line[1] in buys_dict:
            buys_dict[line[1]] += int(line[3])
        else:
            buys_dict[line[1]] = int(line[3])

    file_comp = open('ad_companies.csv')
    next(file_comp)
    comps_dict = {}

    for row in file_comp:
        row = row.rstrip()
        row = row.split(',')
        comps_dict[row[0]] = row[1]

    output = []

    for key in buys_dict:
        if key in comps_dict:
            output.append((int(key), comps_dict[key], buys_dict[key]))

    return(output)

#SQL solution

import sqlite3

def by_sql():

    conn = sqlite3.connect('session_2.db')
    cursor = conn.cursor()

    query = cursor.execute(
                            ''' SELECT ad_companies.company_id, ad_companies.company_name, sum(ad_buys.volume)
                                FROM ad_companies
                                JOIN ad_buys ON ad_buys.buyer_id = ad_companies.company_id
                                GROUP BY 1
                            ''')
    output = []
    for line in query:
        output.append(line)

    return(output)

#pandas solution

import pandas as pd

def by_pandas():

    file_buys = pd.read_csv('ad_buys.csv')
    file_comp = pd.read_csv('ad_companies.csv')

    agg_buys = file_buys.groupby('buyer_id').sum()

    merged = pd.merge(file_comp, agg_buys, left_on = 'company_id', right_on = 'buyer_id')

    output = merged[['company_id', 'company_name', 'volume']]

    return(output)

