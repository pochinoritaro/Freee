from Freee.freee_sdk.oauth import OAuth

def get_session(client_id: str, client_secret: str, redirect_uri:str):
  pass

def get_token(code: str, session: str):
  token = oauth2_session.generate_access_token(
    oauth_session=session["session"],
    authorize_code=code
  )

def get_auth_url(client_id: str, client_secret: str, redirect_uri:str):
  oauth2_session = OAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri
  )
  session = oauth2_session.generate_auth_token_url()

  web_open(session["authorization_url"], new=0, autoraise=True)

  code = input('認可コードを入力: ')

  token = oauth2_session.generate_access_token(
    oauth_session=session["session"],
    authorize_code=code
  )
  print(token)
  return token
