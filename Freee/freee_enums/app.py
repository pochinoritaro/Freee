from configparser import ConfigParser
from datetime import datetime
from Freee.human_resource import HumanResourse

config = ConfigParser()
config.read("./doc/.ini")

hr = HumanResourse(
    client_id=config["freee"]["CLIENT_ID"],
    client_secret=config["freee"]["CLIENT_SECRET"],
    redirect_uri=config["freee"]["REDIRECT_URI"]
    )

hr.access_token = config["freee"]["ACCESS_TOKEN"]
hr.company_id = hr.get_users_me()["companies"][0]["id"]

def paid_holiday(employee_id, date: datetime):
    today = datetime.today()
    work_record = hr.get_employee_work_record_summary(
        employee_id=employee_id,
        year=today.year,
        month=today.month
        )
    print(work_record)

if __name__ == "__main__":
    pass