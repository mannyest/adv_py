#!/usr/bin/env python

## NYU - Adv Python - Blaikie - Homework Session 1 2018.06.10

def m_builtin():
    ## 'built-in python' method

    file = open('weather_newyork.csv')
    weather_data = file.readlines()
    temps = []
    count = 0

    for line in weather_data[1:]:
        line = line.split(',')
        temps.append(int(line[1]))
        count += 1

    t_max = max(temps)
    t_min = min(temps)
    t_mean = sum(temps) / count
    mean_dif = [(t - t_mean) ** 2 for t in temps]
    variance = sum(mean_dif) / count
    std_dev = variance ** 0.5

    print('Count: {}\nMax: {}\nMin: {}\nMean: {}\nStddev: {}'.format(count, t_max, t_min, t_mean, std_dev))


import csv

def m_csv():
    ## 'csv' method

    file = open('weather_newyork.csv')
    weather_data = csv.reader(file)
    next(weather_data)

    temps = []
    count = 0

    for line in weather_data:
        temps.append(int(line[1]))
        count += 1

    t_max = max(temps)
    t_min = min(temps)
    t_mean = sum(temps) / count
    mean_dif = [(t - t_mean) ** 2 for t in temps]
    variance = sum(mean_dif) / count
    std_dev = variance ** 0.5

    print('Count: {}\nMax: {}\nMin: {}\nMean: {}\nStddev: {}'.format(count, t_max, t_min, t_mean, std_dev))

m_csv()

import sqlite3

def m_sql():
    ## 'SQL' method

    conn = sqlite3.connect('session_1.db')
    c = conn.cursor()
    temps = []
    count = 0

    t_mean = c.execute('SELECT * FROM weather_newyork')

    for line in t_mean:
        temp = line[1]
        temps.append(temp)
        count += 1

    t_max = max(temps)
    t_min = min(temps)
    t_mean = sum(temps) / count
    mean_dif = [(t - t_mean) ** 2 for t in temps]
    variance = sum(mean_dif) / count
    std_dev = variance ** 0.5

    print('Count: {}\nMax: {}\nMin: {}\nMean: {}\nStddev: {}'.format(count, t_max, t_min, t_mean, std_dev))

m_sql()


import pandas

def m_panda():
    ## pandas method

    weather_file = pandas.read_csv('weather_newyork.csv')
    temps = weather_file['mean_temp']

    count = len(temps)
    t_max = max(temps)
    t_min = min(temps)
    t_mean = sum(temps) / count
    mean_dif = [(t - t_mean) ** 2 for t in temps]
    variance = sum(mean_dif) / count
    std_dev = variance ** 0.5

    print('Count: {}\nMax: {}\nMin: {}\nMean: {}\nStddev: {}'.format(count, t_max, t_min, t_mean, std_dev))

m_panda()

##manny.est
