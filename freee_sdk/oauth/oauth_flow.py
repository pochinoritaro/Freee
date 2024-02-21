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
from os import getenv
from urllib.parse import urljoin
from requests import post
from requests_oauthlib import OAuth2Session


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


    @staticmethod
    def get_auth_url(*, client_id: str, redirect_uri: str) -> str|None:
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
            client_id=client_id,
            redirect_uri=redirect_uri
        )
        authorization_url, _ = oauth_session.authorization_url(OAuth.AUTH_CODE_URL)
        return authorization_url


    @staticmethod
    def get_access_token(
        *,
        client_id: str,
        client_secret: str,
        redirect_uri: str,
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
            "client_id": client_id,
            "client_secret": client_secret,
            "code": state,
            "redirect_uri": redirect_uri
            }
        token_response = post(OAuth.ACCESS_TOKEN_URL, data=header)
        return token_response


    @staticmethod
    def access_token_refresh(
        *,
        client_id: str,
        client_secret: str,
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
            "client_id": client_id,
            "client_secret": client_secret,
            "refresh_token": refresh_token
            }
        token_response = post(OAuth.ACCESS_TOKEN_URL, data=header)
        return token_response

    @staticmethod
    def access_token_is_valid(token_create_at: int) -> bool:
        token_spend_by_generated = datetime.now()-datetime.fromtimestamp(token_create_at)
        #TODO アクセストークン発行から6時間以上経過しているが、リフレッシュトークンが有効期限内だった場合の処理は?2024/02/08
        if abs(token_spend_by_generated) <= timedelta(hours=6):
            return True
        else:
            return False
            
    @staticmethod
    def refresh__token_is_valid(token_create_at: int) -> bool:
        token_spend_by_generated = datetime.now()-datetime.fromtimestamp(token_create_at)
        #TODO アクセストークン発行から6時間以上経過しているが、リフレッシュトークンが有効期限内だった場合の処理は?2024/02/08
        if abs(token_spend_by_generated) <= timedelta(days=90):
            return True
        else:
            return False


if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv("./docs/.env")
    
    auth_url = OAuth.get_auth_url(client_id=getenv("CLIENT_ID"), redirect_uri=getenv("REDIRECT_URI"))
    print(auth_url)
