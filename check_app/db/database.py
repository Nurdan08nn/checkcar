from motor.motor_asyncio import AsyncIOMotorClient
from check_app.config import config
from beanie import init_beanie
from check_app.db.models import PredictionModel

client = (AsyncIOMotorClient(
    config.MONGODB_URL)
)
db = client[config.DB_NAME]


async def init_db():
    await init_beanie(database=db, document_models=[PredictionModel])

try:
    client.server_info()
    print('✅ База данныхка кошулду')
except Exception as e:
        print(f' Ошибка: {e}')
