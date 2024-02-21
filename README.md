# Freee
FreeeのAPIをPythonから扱えるようにするライブラリ
<br>Vertion: Python 3.12.1

外部ライブラリ
| ライブラリ名       | バージョン | 依存先            | ライセンス | 
| ------------------ | ---------- | ----------------- | ---------- | 
| requests-oauthlib  | 1.3.1      | None              | ISC        | 
| oauthlib           | 3.2.2      | requests-oauthlib | BSD        | 
| requests           | 2.31.0     | requests-oauthlib | Apache 2.0 | 
| certifi            | 2023.11.17 | requests          | MPL-2.0    | 
| charset-normalizer | 3.3.2      | requests          | MIT        | 
| idna               | 3.6        | requests          | None       | 
| urllib3            | 2.1.0      | requests          | None       | 


## 人事労務(HumanResource)
[人事労務リファレンス](https://developer.freee.co.jp/reference/hr/reference)
<br>本ライブラリで提供されている各種メソッドについては上記リファレンスを参照してください。
'''from human_resource import HumanResourse

config = ConfigParser()
config.read("./doc/.ini")

hr = HumanResourse(
    client_id=config["freee"]["CLIENT_ID"],
    client_secret=config["freee"]["CLIENT_SECRET"],
    redirect_uri=config["freee"]["REDIRECT_URI"]
    )

hr.access_token = config["freee"]["ACCESS_TOKEN"]
me = hr.get_users_me()
print(me)'''