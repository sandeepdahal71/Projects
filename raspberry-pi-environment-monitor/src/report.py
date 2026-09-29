import sqlite3
c=sqlite3.connect('sensor.db');
for r in c.execute("SELECT date(ts),ROUND(MIN(temp_c),1),ROUND(MAX(temp_c),1),ROUND(AVG(temp_c),1),ROUND(AVG(humidity),1) FROM readings GROUP BY date(ts) ORDER BY date(ts) DESC"):print(r)
