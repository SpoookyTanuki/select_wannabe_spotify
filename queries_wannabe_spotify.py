import sqlalchemy

engine = sqlalchemy.create_engine('postgresql://spookytanuki:admin@localhost:5432/wannabe_spotify')
connection = engine.connect()
# print(engine.table_names())

check = connection.execute("""SELECT DISTINCT * FROM genre;
""").fetchall()
# print(check)

last_albums = connection.execute("""SELECT name, year FROM album
WHERE year BETWEEN '20180101' AND '20190101';
""").fetchall()
# print(last_albums)

longest_track = connection.execute("""SELECT name FROM track
ORDER BY duration DESC;
""").fetchone()
# print(longest_track)

long_tracks = connection.execute("""SELECT name FROM track
WHERE duration > '033000';
""").fetchall()
# print(long_tracks)

last_collections = connection.execute("""SELECT name FROM collection
WHERE year BETWEEN '20180101' AND '20210101';
""").fetchall()
# print(last_collections)

one_word_artist = connection.execute("""SELECT name FROM artist
WHERE name NOT LIKE '%% %%';
""").fetchall()
# print(one_word_artist)

my_track = connection.execute("""SELECT name FROM track
WHERE name  LIKE '%%my%%';
""").fetchall()
print(my_track)