from pydantic.v1.networks import MultiHostDsn
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Annotated, Any, Literal, List, Generator
from pydantic import AnyUrl, BeforeValidator, computed_field, Field, MySQLDsn

def parse_core(v: Any) -> list | str:
    if isinstance(v, str) and v is not v.startswith("["):
        return (i.strip() for i in v.split(','))
    elif isinstance(v, list | str):
        return v
    raise ValueError()

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        env_ignore_empty=True,
    )

    DOMAIN = "localhost"
    ENVIRONMENT = Literal["local", "staging", "production"] = "local"
    JST_TOKEN = str

    @computed_field()
    @property
    def server_host(self) -> str:
        if self.ENVIRONMENT == "local":
            return f"http://{self.DOMAIN}"
        return f"https://{self.DOMAIN}"

    BACKEND_CORS_ORIGINS: Annotated[
        List[AnyUrl] | str, BeforeValidator(parse_core)
    ] = Field(default_factory=list)

    MYSQL_USERNAME = str
    MYSQL_PASSWORD = str
    MYSQL_HOST = str
    MYSQL_PORT = int
    MYSQL_DATABASE = str

    @computed_field()
    @property
    def MYALCHEMY_DATABASE_URL(self) -> MySQLDsn:
        return f"mysql://{self.MYSQL_USERNAME}:{self.MYSQL_PASSWORD}@{self.MYSQL_HOST}:{self.MYSQL_PORT}/{self.MYSQL_DATABASE}"

    # mysql://username:password@host1.example.com:3307/mydatabase

settings = Settings()

