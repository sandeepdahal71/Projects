import os
from flask import Flask, request, jsonify
import mysql.connector
app=Flask(__name__)
def db(): return mysql.connector.connect(host=os.getenv('DB_HOST','localhost'),user=os.getenv('DB_USER','root'),password=os.getenv('DB_PASSWORD',''),database=os.getenv('DB_NAME','organic_market'))
@app.get('/api/items')
def items():
 c=db(); cur=c.cursor(dictionary=True); cur.execute('SELECT item_id,name,price,stock_qty FROM item ORDER BY name'); rows=cur.fetchall(); c.close(); return jsonify(rows)
@app.post('/api/items')
def add_item():
 d=request.get_json(force=True); required={'name','price','stock_qty','vendor_id'}
 if not required<=d.keys(): return {'error':'missing fields'},400
 c=db(); cur=c.cursor(); cur.execute('INSERT INTO item(name,price,stock_qty,vendor_id) VALUES(%s,%s,%s,%s)',(d['name'],d['price'],d['stock_qty'],d['vendor_id'])); c.commit(); i=cur.lastrowid;c.close();return {'item_id':i},201
@app.patch('/api/items/<int:i>/stock')
def stock(i):
 q=request.get_json(force=True).get('stock_qty');
 if q is None or int(q)<0:return {'error':'invalid stock'},400
 c=db();cur=c.cursor();cur.execute('UPDATE item SET stock_qty=%s WHERE item_id=%s',(q,i));c.commit();c.close();return {'updated':True}
if __name__=='__main__':app.run(debug=True)
