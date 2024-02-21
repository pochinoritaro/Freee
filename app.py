import requests
from json import dumps

access_token = "b612894d73c542a31c53e85bd08ec19c5430f5dbcb988fc3c5858d99322793ae"
header = {
		"accept": "application/json",
		"Content-Type": "application/json",
		"Authorization": f"Bearer {access_token}",
		"FREEE-VERSION": "2022-02-01"
		}

company_id = 11130099
employee_id = 2363402


url = f"https://api.freee.co.jp/hr/api/v1/employees/{employee_id}/work_record_summaries/2024/1"
params = dumps({'company_id': 11130099, 'work_records': True}, ensure_ascii=False)


res = requests.request(method="GET", url=url, headers=header, json=params)
print(res.url)
print(res.json())