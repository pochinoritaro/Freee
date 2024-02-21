from configparser import ConfigParser
from human_resource import HumanResourse

config = ConfigParser()
config.read("./doc/.ini")

hr = HumanResourse(
    client_id=config["freee"]["CLIENT_ID"],
    client_secret=config["freee"]["CLIENT_SECRET"],
    redirect_uri=config["freee"]["REDIRECT_URI"]
    )

hr.access_token = config["freee"]["ACCESS_TOKEN"]
me = hr.get_users_me()
print(me)