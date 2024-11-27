import sqlite3
from db import queries

db= sqlite3.connect('db/store.sqlite3')
cursor = db.cursor()

async def sql_create():
    if db:
        print('База данных подключена')
    cursor.execute(queries.CREATE_TABLE_TABLE)
    cursor.execute(queries.CREATE_TABLE_TABLE_DETAIL)

async def sql_create_store(name_product, product_id, size, price, photo):
    cursor.execute(queries.INSERT_STORE,(
        name_product, product_id, size, price, photo
    ))
    db.commit()

async def sql_create_store_detail(info_product, product_id, category):
    cursor.execute(queries.INSERT_STORE,(
        info_product, product_id, category
    ))
    db.commit()



