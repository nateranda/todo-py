import sqlite3
import os
from datetime import date, timedelta

def parse_command(text, name):
    command = text.split()[0]
    if command == 'create':
        day = text.split()[-1]
        task_name = ' '.join(text.split()[1:-1])
        return create_task(task_name, name, day)
    elif command == 'clear':
        return clear_database(name)

def initialize_database():
    os.system('clear')
    conn = sqlite3.connect('main.db')
    c = conn.cursor()
    return c, conn

def create_table(name):
    c, conn = initialize_database()
    c.execute(f"""CREATE TABLE IF NOT EXISTS {name} (
        name text,
        start_date date,
        do_date date,
        end_date date,
        completed bool
        )""")
    conn.commit()
    conn.close()

def clear_database(name):
    c, conn = initialize_database()
    try:
        c.execute(f"DROP TABLE IF EXISTS {name}")
    except:
        return "there was an arror clearing the database."
    conn.commit()
    conn.close()
    return True

def create_task(task_name, name, day):
    c, conn = initialize_database()
    start_date = date.today()
    do_date = date.today()
    end_date = parse_day(day)
    if end_date == "invalid":
        return "invalid date."
    try:
        c.execute(f"INSERT INTO {name} VALUES ('{task_name}','{start_date}','{do_date}','{end_date}',False)")
    except:
        return "there was an error adding the task to the database."
    conn.commit()
    conn.close()
    return True

def parse_day(day):
    if day == "mon": end_date = 0
    elif day == "tue": end_date = 1
    elif day == "wed": end_date = 2
    elif day == "thu": end_date = 3
    elif day == "fri": end_date = 4
    elif day == "sat": end_date = 5
    elif day == "sun": end_date = 6
    else: return "invalid"
    d = date.today()
    if d.weekday() == end_date:
        return d
    while d.weekday() != end_date:
        d += timedelta(1)
    return d
