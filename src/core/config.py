from pydantic_settings import BaseSettings, SettingsConfigDict

env_path = ".env"

class DatabaseConfig(BaseSettings):
    
    username: str
    password: str
    host: str
    port: int
    name: str # Database name

    
    model_config = SettingsConfigDict(
        env_file=env_path,
        env_prefix="DB_",
    )
    
    
    @property
    def async_database_url(self) -> str:
        return f"postgresql+asyncpg://{self.username}:{self.password}@{self.host}:{self.port}/{self.name}"
    
    
class Settings(BaseSettings):
    db_config: DatabaseConfig
        

settings = Settings(
    db_config=DatabaseConfig() # type: ignore
)