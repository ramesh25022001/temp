# # (c) @AbirHasan2005

import os


class Config(object):
	API_ID = int(os.environ.get("API_ID", "0"))
	API_HASH = os.environ.get("API_HASH")
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	BOT_USERNAME = os.environ.get("BOT_USERNAME")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-100"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "1445283714"))
	DATABASE_URL = os.environ.get("DATABASE_URL")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", None)
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	BASE_SITE = os.environ.get("BASE_SITE", "ShortUrllink.in")
	DOMAIN = os.environ.get("DOMAIN", "ShortUrllink.in")
	ABOUT_BOT_TEXT = f"""
This is Permanent Files Store Bot!
Send me any file I will save it in my Database. Also works for channel. Add me to channel as Admin with Edit Permission, I will add Save Uploaded File in Channel & add Sharable Button Link.

š¤ **My Name:** [Files Store Bot](https://t.me/{BOT_USERNAME})

š **Language:** [Python3](https://www.python.org)

š **Library:** [Pyrogram](https://docs.pyrogram.org)

š” **Hosted on:** [Heroku](https://heroku.com)

š§š»āš» **Developer:** @AbirHasan2005

š„ **Support Group:** [Linux Repositories](https://t.me/DevsZone)

š¢ **Updates Channel:** [Discovery Projects](https://t.me/Discovery_Updates)
"""
	ABOUT_DEV_TEXT = f"""
**š This Bot Was Devloped By** : @A2z_tech"""
	HOME_TEXT = """
Hello [{}](tg://user?id={})ā\n\nāļø This Is A Unlimited Telegram Could Storage Bot For shorturllink.in. Send Me Any File And Select Method Wait Few Seconds Bot Will Be Upload To Our Server And Genarate shorturllink.in Link For Files. ā”\n\nCurrently Supported Format :\n\nā“ File š\nā“ Video š„\nā“ Photo š¼ļø\nā“ Audio šļø\n\nMore Format Soon ā”\n\nNote : š¬š¢šØ ššš” ššš¦š¢ šØš£šš¢šš š°šš ššššš¦ š„"""
	SHORTENER_API_MESSAGE = """To add or update your Shortner Website API, `/apikey api`
            
Ex: `/apikey 6LZq851sXofffPHugiKQq`

Current Website: {base_site}

Current Shortener API: `{shortener_api}`"""

