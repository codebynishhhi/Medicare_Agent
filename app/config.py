from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """ 
    Central configuration for the entire application. 
    Every module imports setting from here instead of reading environment variable directly
    """

    groq_api_key : str
    model_name : str = "llama-3.3-70b-versatile"
    temperature : float = 0
    data_path : str = "data/patient_data.csv"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

@lru_cache
def get_settings() -> Settings:
    """
    Creates the Settings object only once.

    Think of this as a singleton configuration object.
    """

    return Settings()
settings = get_settings()