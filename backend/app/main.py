from fastapi import FastAPI
from app.core.config import setting


app = FastAPI(title=setting.app_name)

@app.get('/')
async def home():
    return {'message': 'welcome to job tracker api'}
@app.get('/health')
async def health():
    return {'status':'ok'}