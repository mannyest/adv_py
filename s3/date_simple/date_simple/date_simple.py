import datetime as dt

def get_date_object(date = None):
    if date:
        return dt.datetime.strptime(date, '%Y-%m-%d').date()
    else:
        return dt.datetime.today().date()



def get_date_string(date_object = None):
    today = dt.datetime.today().date()
    if date_object == None:
        return today.strftime('%Y-%m-%d')
    else:
        return date_object.strftime('%Y-%m-%d')


# def get_date_string(date_object = None):
#
#     if date_object:
#         return date_object.strftime('%Y-%m-%d')
#     else:
#         today = dt.datetime.today()
#         return today.strftime('%Y-%m-%d')


# def get_date_string(date_object = None, format = '%Y-%m-%d'):
#
#     if date_object:
#
#         strdt = f.strftime('%Y-%m-%d')
#         return strdt
#     else:
#         today = dt.datetime.today()
#         return today.strftime('%Y-%m-%d')