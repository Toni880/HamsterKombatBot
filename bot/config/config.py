from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

    API_ID: int = 10655360
    API_HASH: str = "32aa547bd6cc2e9f61063cd31e0bc0a5"

    ACTION: int = 0 # Added this as default, to show options

    MIN_AVAILABLE_ENERGY: int = 100
    SLEEP_BY_MIN_ENERGY: list[int] = [1800, 2400]

    ADD_TAPS_ON_TURBO: int = 2500

    AUTO_UPGRADE: bool = True
    MAX_LEVEL: int = 20

    BALANCE_TO_SAVE: int = 1000000
    UPGRADES_COUNT: int = 10

    APPLY_DAILY_ENERGY: bool = True
    APPLY_DAILY_TURBO: bool = True

    RANDOM_TAPS_COUNT: list[int] = [10, 50]
    SLEEP_BETWEEN_TAP: list[int] = [10, 25]

    USE_RANDOM_USERAGENT: bool = False

    USE_PROXY_FROM_FILE: bool = False


settings = Settings()
