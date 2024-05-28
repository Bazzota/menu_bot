from environs import Env
from dataclasses import dataclass


@dataclass
class TgBot:
    token: str


@dataclass
class Config:
    tg_bot: TgBot


env = Env()
env.read_env()

main_config = Config(tg_bot=TgBot(token=env('token')))