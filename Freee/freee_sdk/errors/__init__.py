class FreeeClientError(Exception):
    def __init__(self, error: str=""):
        self.error = error

    def __str__(self):
        return f"{self.error}"


class BadRequestError(FreeeClientError):
    """リクエストパラメータが不正"""


class UnAuthorizedError(FreeeClientError):
    """アクセストークンが無効"""


class AccessDeniedError(FreeeClientError):
    """アクセストークンが無効"""


class ForbiddenError(FreeeClientError):
    """アクセス権限がない"""


class NotFoundError(FreeeClientError):
    """リソースが存在しない"""


class TooManyRequestsError(FreeeClientError):
    """リクエスト回数制限を超えた"""


class InternalServerError(FreeeClientError):
    """システム内で予期しないエラーが発生"""
