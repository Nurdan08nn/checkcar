from fastapi import FastAPI
import uvicorn
from check_app.api.routers import router
from check_app.db.database import init_db
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


check_app = FastAPI()
check_app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(check_app, host='127.0.0.1', port=8000)

