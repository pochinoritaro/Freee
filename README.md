# Freee
FreeeのAPIをPythonから扱えるようにするライブラリ
<br>Vertion: Python 3.12.1

<br>外部ライブラリ
| ライブラリ名       | バージョン | 依存先            | ライセンス | 
| ------------------ | ---------- | ----------------- | ---------- | 
| requests-oauthlib  | 1.3.1      |                   | ISC        | 
| oauthlib           | 3.2.2      | requests-oauthlib | BSD        | 
| requests           | 2.31.0     | requests-oauthlib | Apache 2.0 | 
| certifi            | 2023.11.17 | requests          | MPL-2.0    | 
| charset-normalizer | 3.3.2      | requests          | MIT        | 
| idna               | 3.6        | requests          |            | 
| urllib3            | 2.1.0      | requests          |            | 
<br>

## 人事労務(HumanResource)
[人事労務リファレンス](https://developer.freee.co.jp/reference/hr/reference)
<br>本ライブラリで提供されている各種メソッドについては上記リファレンスを参照してください。
<br>(使用例)
```play ground.py
from human_resource import HumanResourse

hr = HumanResourse(
    client_id=クライアントID,
    client_secret=シークレットID,
    redirect_uri=リダイレクト先
    )

# アクセストークンを登録
hr.access_token = アクセストークン

# ログイン中のユーザが所属している事業所情報を取得
me = hr.get_users_me()
print(me)
```