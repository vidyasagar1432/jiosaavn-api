from pydantic import BaseSettings

class Settings(BaseSettings):
    DETA_PROJECT_KEY:str
    DETA_BASE_NAME:str = 'jiosaavn'

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

setting = Settings(_env_file='.env')