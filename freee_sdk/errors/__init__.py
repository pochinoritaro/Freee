class FreeeClientError(Exception):
    def __init__(self, error):
        self.error = error


class UnAuthorizedError(FreeeClientError):
    """ログインをしてください。"""
    def __str__(self):
        return f"{self.arg}"


class ForbiddenError(FreeeClientError):
    """アクセス権限がありません。"""
    def __str__(self):
        return f"{self.arg}"


class AccessDeniedError(FreeeClientError):
    """アクセスする権限がありません。"""
    def __str__(self):
        return f"{self.arg}"


class NotFoundError(FreeeClientError):
    """存在しないか既に削除されたレコードです。"""    
    def __str__(self):
        return f"{self.arg}"


class InternalServerError(FreeeClientError):
    """エラーが発生しました。再思考しても解消しない場合は、サポートセンターまでご連絡ください。"""
    def __str__(self):
        return f"{self.arg}"
