from os import environ as env

from dotenv import load_dotenv

load_dotenv("config.env")

"""
READ EVERYTHING CAREFULLY!!!
"""


DEPLOYING_ON_HEROKU = (
    True  # Make this False if you're not deploying On heroku/Docker
)


if not DEPLOYING_ON_HEROKU:
    BOT_TOKEN = "8167388254:AAE5Fbts2L8erz7Sa_t4pqFqziQi9g06DXc"
    SUDOERS = [7775259302]
    NSFW_LOG_CHANNEL = -1002272021040
    SPAM_LOG_CHANNEL = -1002272021040
    ARQ_API_KEY = "XPCGWV-LKIIJY-HHGYWE-OUHQKU-ARQ"  # Get it from @ARQRobot
else:
    BOT_TOKEN = env.get("BOT_TOKEN")
    SUDOERS = [int(x) for x in env.get("SUDO_USERS_ID", "7775259302").split()]
    NSFW_LOG_CHANNEL = int(env.get("NSFW_LOG_CHANNEL"))
    SPAM_LOG_CHANNEL = int(env.get("SPAM_LOG_CHANNEL"))
    ARQ_API_KEY = env.get("ARQ_API_KEY")
