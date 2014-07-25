import csv
import sqlite3


with open('../raw_data/presidents-death-dates.csv', 'rb') as fin:
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin)  # comma is default delimiter
    to_db = [(i['death_order'],
              i['birth_order'],
              i['name'],
              i['death_date'],
              i['president_order'],
              i['death_cause'],
              i['age'],
              i['death_place'],
              i['burial_date'],
              i['burial_place']) for i in dr]

drop_query = "DROP TABLE IF EXISTS death;"
create_query = "CREATE TABLE death (death_order, \
                                    birth_order, \
                                    name, \
                                    death_date, \
                                    president_order, \
                                    death_cause, \
                                    age, \
                                    death_place, \
                                    burial_date, \
                                    burial_place);"

con = sqlite3.connect("./presidents.db")
cur = con.cursor()
cur.execute(drop_query)
cur.execute(create_query)

insert_query = "INSERT INTO death (death_order, \
                                   birth_order, \
                                   name, \
                                   death_date, \
                                   president_order, \
                                   death_cause, \
                                   age, \
                                   death_place, \
                                   burial_date, \
                                   burial_place) \
                                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"
cur.executemany(insert_query, to_db)
con.commit()
