create_ratings = ("""CREATE TABLE IF NOT EXISTS ratings \
(id SERIAL PRIMARY KEY, \
rating_id varchar, description varchar, \
rating varchar, wine_id varchar, taster_id varchar);
""")

create_regions = ("""CREATE TABLE IF NOT EXISTS regions \
(id SERIAL PRIMARY KEY, \
region_id varchar, province varchar, \
region_1 varchar, region_2 varchar);
""")

create_tasters = ("""CREATE TABLE IF NOT EXISTS tasters \
(id SERIAL PRIMARY KEY, \
taster_id varchar, taster_name varchar, \
taster_twitter_handle varchar);
""")

create_wineries = ("""CREATE TABLE IF NOT EXISTS wineries \
(id SERIAL PRIMARY KEY, \
winery_id varchar, winery varchar, \
country varchar);
""")

create_wines = ("""CREATE TABLE IF NOT EXISTS wines \
(id SERIAL PRIMARY KEY, \
wine_id varchar, designation varchar, \
title varchar, price varchar, \
winery_id varchar, region_id varchar);
""")

ratings_table_insert = ("""INSERT INTO ratings (id, rating_id, description, rating, wine_id, taster_id) \
VALUES (%s, %s, %s, %s, %s, %s)
""")

regions_table_insert = ("""INSERT INTO regions (id, region_id, province, region_1, region_2) \
VALUES (%s, %s, %s, %s, %s)
""")

tasters_table_insert = ("""INSERT INTO tasters (id, taster_id, taster_name, taster_twitter_handle) \
VALUES (%s, %s, %s, %s)
""")

wineries_table_insert = ("""INSERT INTO wineries (id, winery_id, winery, country) \
VALUES (%s, %s, %s, %s)
""")

wines_table_insert = ("""INSERT INTO wines (id, wine_id, title, designation, price, winery_id, region_id) \
VALUES (%s, %s, %s, %s, %s, %s, %s)
""")

#################

select_user = ("""SELECT id FROM users \
WHERE name = %s \
;""")

select_outlet = ("""SELECT id FROM outlet \
WHERE id_outlet = %s \
;""")

reviews_table_insert = ("""INSERT INTO reviews (user_id, outlet_id, review, rate, source) \
VALUES (%s, %s, %s, %s, %s);
""")

menu_table_insert = ("""INSERT INTO menu (brand, price, volume, name, source) \
VALUES (%s, %s, %s, %s, %s)
""")
