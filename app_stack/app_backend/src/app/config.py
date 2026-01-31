from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # No defaults here = They MUST be provided by the environment
    DB_HOST: str
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_PORT: int

    # This tells Pydantic where to look if they aren't already in the OS environment
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()