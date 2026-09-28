#datetimemodule

from datetime import datetime

def get_current_datetime():
    return datetime.now()

def get_current_date():
    return datetime.now().date()

def get_current_time():
    return datetime.now().time()
