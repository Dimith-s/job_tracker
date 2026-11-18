from pydantic_settings import BaseSettings,SettingsConfigDict
from sqlalchemy import URL


class settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env')

    app_name : str = 'Job Tracker1'

    #database details

    POSTGRES_USER: str
    POSTGRES_PASSWORD:str
    POSTGRES_DB: str
    POSTGRES_HOST: str = 'localhost'
    POSTGRES_PORT: int

    @property
    def database_url(self):
        database_url = URL.create(
            drivername = 'postgresql+asyncpg',
            username = self.POSTGRES_USER,
            password = self.POSTGRES_PASSWORD,
            host = self.POSTGRES_HOST,
            port = self.POSTGRES_PORT,
            database = self.POSTGRES_DB

        )
        return database_url
    

    # read and check all settings

setting = settings()

print("Settings fields:", settings.model_fields.keys())
print("Settings object:", setting)