class FreeeClientError(Exception):
    def __init__(self, error):
        self.error = error

    def __str__(self):
        return f"{self.error}"

class UnAuthorizedError(FreeeClientError):
    """リクエストパラメータが不正"""


class AccessDeniedError(FreeeClientError):
    """アクセストークンが無効"""


class ForbiddenError(FreeeClientError):
    """アクセス権限がない"""


class NotFoundError(FreeeClientError):
    """リソースが存在しない"""


class InternalServerError(FreeeClientError):
    """システム内で予期しないエラーが発生"""
