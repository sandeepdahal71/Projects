import argparse, sqlite3, time, random
from datetime import datetime
DB='sensor.db'
def init(c): c.execute('CREATE TABLE IF NOT EXISTS readings(ts TEXT PRIMARY KEY,temp_c REAL,humidity REAL)')
def read_sensor(sim=False):
 if sim:return round(random.uniform(20,30),2),round(random.uniform(35,70),2)
 import Adafruit_DHT; h,t=Adafruit_DHT.read_retry(Adafruit_DHT.DHT22,4); return round(t,2),round(h,2)
def main():
 p=argparse.ArgumentParser();p.add_argument('--simulate',action='store_true');p.add_argument('--interval',type=int,default=5);p.add_argument('--temp-alert',type=float,default=32);a=p.parse_args()
 c=sqlite3.connect(DB);init(c)
 try:
  while True:
   t,h=read_sensor(a.simulate);ts=datetime.now().isoformat(timespec='seconds');c.execute('INSERT OR REPLACE INTO readings VALUES(?,?,?)',(ts,t,h));c.commit();print(ts,t,h,'ALERT' if t>=a.temp_alert else '');time.sleep(a.interval)
 except KeyboardInterrupt: pass
if __name__=='__main__':main()
