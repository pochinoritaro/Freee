"""
    OAuth2認証を提供するクラス
    class:
        OAuth
        - methods:
            get_auth_url(staticmethod): 認証URLを生成。
            get_access_token(staticmethod): アクセストークンを取得。
            access_token_refresh(staticmethod): トークンのリフレッシュ
"""
from datetime import datetime, timedelta
from urllib.parse import urljoin
from requests import post
from requests_oauthlib import OAuth2Session
from Freee.freee_sdk.errors import UnAuthorizedError, InternalServerError


class OAuth:
    """OAuth2認証クラス
    
    Description:
        各種IDを使いOAuth認証からアクセストークンの生成、トークンのリフレッシュを行う。
    
    Attributes:
        AUTH_CODE_URL (str): 認証を行うURLのベース。
        ACCESS_TOKEN_URL (str): トークン発行を行うURLのベース。
    """
    __AUTH_URL_BASE = "https://accounts.secure.freee.co.jp/"
    __AUTH_TOKEN = "/public_api/authorize"
    __ACCESS_TOKEN = "/public_api/token"
    AUTH_CODE_URL = urljoin(__AUTH_URL_BASE, __AUTH_TOKEN)
    ACCESS_TOKEN_URL = urljoin(__AUTH_URL_BASE, __ACCESS_TOKEN)


    def __init__(
        self,
        client_id: str=None,
        client_secret: str=None,
        redirect_uri: str=None
        ) -> None:
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri


    def get_auth_url(self) -> str|None:
        #TODO エラーハンドリングを実装(2024/02/08)
        """認可コードの取得
        
        APIの認可用URLを取得します。

        Args:
            client_id (str): アプリケーションのクライアントID。
            redirect_uri (str): アプリケーションのリダイレクトURI。

        Returns:
            str|None: 認可用URLを返却する。
        """
        oauth_session = OAuth2Session(
            client_id=self.client_id,
            redirect_uri=self.redirect_uri
        )
        authorization_url, _ = oauth_session.authorization_url(OAuth.AUTH_CODE_URL)
        return authorization_url


    def get_access_token(
        self,
        *,
        state: str
        ) -> dict|None:
        #TODO エラーハンドリングを実装(2024/02/08)
        """アクセストークンの取得
        
        APIのアクセストークンを取得します。

        Args:
            client_id (str): アプリケーションのクライアントID。
            client_secret (str): アプリケーションのクライアントシークレットID。
            redirect_uri (str): アプリケーションのリダイレクトURI。
            state (str): 認可後に返却される一意のcode。

        Returns:
            dict|None: アクセストークン、リフレッシュトークンなどを含む辞書を返却。
        """
        header = {
            "grant_type": "authorization_code",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "code": state,
            "redirect_uri": self.redirect_uri
            }
        token_response = post(OAuth.ACCESS_TOKEN_URL, data=header)
        match token_response.status_code:
            case 200:
                return token_response.json()
            
            case 401:
                raise UnAuthorizedError

            case _:
                print(f"function: get_access_token\nstatus: {token_response.status_code}")
                raise InternalServerError


    def access_token_refresh(
        self,
        *,
        refresh_token: str
        ) -> dict|None:
        #TODO エラーハンドリングを実装(2024/02/08)
        """アクセストークンのリフレッシュ
        
        リフレッシュトークンを使用し、アクセストークンをリフレッシュします。

        Args:
            client_id (str): アプリケーションのクライアントID。
            client_secret (str): アプリケーションのクライアントシークレットID。
            refresh_token (str): アプリケーションのリフレッシュトークン。

        Returns:
            dict|None: アクセストークン、リフレッシュトークンなどを含む辞書を返却。
        """
        header = {
            "grant_type": "refresh_token",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "refresh_token": refresh_token
            }
        token_response = post(OAuth.ACCESS_TOKEN_URL, data=header)
        return token_response

    def access_token_is_valid(self, token_create_at: int) -> bool:
        token_spend_by_generated = datetime.now()-datetime.fromtimestamp(token_create_at)
        #TODO アクセストークン発行から6時間以上経過しているが、リフレッシュトークンが有効期限内だった場合の処理は?2024/02/08
        if abs(token_spend_by_generated) <= timedelta(hours=6):
            return True
        else:
            return False
            
    def refresh__token_is_valid(self, token_create_at: int) -> bool:
        token_spend_by_generated = datetime.now()-datetime.fromtimestamp(token_create_at)
        #TODO アクセストークン発行から6時間以上経過しているが、リフレッシュトークンが有効期限内だった場合の処理は?2024/02/08
        if abs(token_spend_by_generated) <= timedelta(days=90):
            return True
        else:
            return False
