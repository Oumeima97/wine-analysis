from process import connect_database, create_table, readCSV, insert_in_table
from sql_queries import create_ratings, create_regions, create_tasters, create_wineries, create_wines, ratings_table_insert, regions_table_insert, tasters_table_insert, wineries_table_insert, wines_table_insert

#Connect to database
cur, conn = connect_database('database.env')

#Create tables
create_table(cur, conn, create_ratings)
create_table(cur, conn, create_regions)
create_table(cur, conn, create_tasters)
create_table(cur, conn, create_wineries)
create_table(cur, conn, create_wines)

#Get list of all the cleaned data rows to insert && Insert data to respective tables
ratings_list = readCSV('ratings.csv')
insert_in_table(cur, ratings_list, ratings_table_insert)

regions_list = readCSV('regions.csv')
insert_in_table(cur, regions_list, regions_table_insert)

tasters_list = readCSV('tasters.csv')
insert_in_table(cur, tasters_list, tasters_table_insert)

wineries_list = readCSV('wineries.csv')
insert_in_table(cur, wineries_list, wineries_table_insert)

wines_list = readCSV('wines.csv')
insert_in_table(cur, wines_list, wines_table_insert)