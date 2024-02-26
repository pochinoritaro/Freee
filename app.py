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
hr.company_id = hr.get_users_me()["companies"][0]["id"]
print(hr.get_groups())
print(hr.get_employee_work_record_summary(employee_id=2363402, year=2024, month=1, work_records=True))