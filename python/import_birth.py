import csv
import sqlite3


with open('../raw_data/presidents-birth-dates.csv', 'rb') as fin:
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin)  # comma is default delimiter
    to_db = [(i['birth_order'],
              i['name'],
              i['birth_date'],
              i['sign'],
              i['birth_name'],
              i['president_order'],
              i['birth_place'],
              i['birth_state'],
              i['age_president']) for i in dr]

drop_query = "DROP TABLE IF EXISTS birth;"
create_query = "CREATE TABLE birth (birth_order, \
                                    name, \
                                    birth_date, \
                                    sign, \
                                    birth_name, \
                                    presidential_order, \
                                    birth_place, \
                                    birth_state, \
                                    age_president);"

con = sqlite3.connect("./presidents.db")
cur = con.cursor()
cur.execute(drop_query)
cur.execute(create_query)

insert_query = "INSERT INTO birth (birth_order, \
                            name, \
                            birth_date, \
                            sign, \
                            birth_name, \
                            presidential_order, \
                            birth_place, \
                            birth_state, \
                            age_president) \
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);"
cur.executemany(insert_query, to_db)
con.commit()
