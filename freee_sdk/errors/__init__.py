class FreeeClientError(Exception):
	"""freeeのエラーベース"""


class UnAuthorizedError(FreeeClientError):
	"""ログインをしてください。"""


class ForbiddenError(FreeeClientError):
	"""アクセス権限がありません。"""


class AccessDeniedError(FreeeClientError):
	"""アクセスする権限がありません。"""


class NotFoundError(FreeeClientError):
	"""存在しないか既に削除されたレコードです。"""	


class InternalServerError(FreeeClientError):
	"""エラーが発生しました。再思考しても解消しない場合は、サポートセンターまでご連絡ください。"""

