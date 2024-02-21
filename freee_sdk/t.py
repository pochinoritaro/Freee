from Freee.freee_sdk.oauth import OAuth

def get_session(client_id: str, client_secret: str, redirect_uri:str):
    session = OAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri
    )
    return session

def get_auth_url(session: OAuth):
    return session.generate_auth_token_url()

def get_token(session: OAuth, auth_code: str):
    return session.generate_access_token(
        oauth_session=
    )