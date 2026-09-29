from fastapi.testclient import TestClient
from app.main import app
c=TestClient(app)
def test_recommend(): assert c.get('/recommend?temp_c=5').json()['category']=='cold'
