from dataclasses import dataclass
from environs import Env


@dataclass
class TgBOT:
    token: str


@dataclass
class Config:
    tg_bot: TgBOT


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(tg_bot=TgBOT(token=env('BOT_TOKEN')))
