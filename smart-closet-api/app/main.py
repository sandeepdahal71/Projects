import os, sqlite3, requests
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app=FastAPI(title='Smart Closet API',version='1.0')
DB=os.getenv('DB','closet.db')
def con(): c=sqlite3.connect(DB);c.row_factory=sqlite3.Row;c.execute('CREATE TABLE IF NOT EXISTS preferences(id INTEGER PRIMARY KEY, cold REAL DEFAULT 10, hot REAL DEFAULT 27, city TEXT DEFAULT "Arlington")');c.execute('INSERT OR IGNORE INTO preferences(id) VALUES(1)');c.commit();return c
class Pref(BaseModel): cold:float;hot:float;city:str
@app.get('/preferences')
def prefs(): c=con();r=dict(c.execute('SELECT * FROM preferences WHERE id=1').fetchone());c.close();return r
@app.put('/preferences')
def setprefs(p:Pref): c=con();c.execute('UPDATE preferences SET cold=?,hot=?,city=? WHERE id=1',(p.cold,p.hot,p.city));c.commit();c.close();return p
@app.get('/recommend')
def recommend(temp_c:float):
 p=prefs(); category='cold' if temp_c<p['cold'] else 'hot' if temp_c>p['hot'] else 'mild'; items={'cold':['jacket','sweater','pants'],'mild':['shirt','light layer','jeans'],'hot':['t-shirt','shorts','breathable shoes']}[category];return {'temperature_c':temp_c,'category':category,'recommended':items}
@app.post('/led/{section}')
def led(section:str,color:str='00AAFF'):
 host=os.getenv('WLED_HOST');
 if not host:return {'simulated':True,'section':section,'color':color}
 try:r=requests.post(f'http://{host}/json/state',json={'on':True,'seg':[{'col':[[int(color[i:i+2],16) for i in (0,2,4)]]}]},timeout=2);r.raise_for_status();return {'ok':True}
 except Exception as e:raise HTTPException(502,str(e))
