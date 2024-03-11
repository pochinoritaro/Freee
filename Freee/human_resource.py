from Freee.freee_sdk import BaseClient
from Freee.freee_sdk.freee_response import FreeeResponse
from Freee.freee_sdk.utils import _remove_none_values

class HumanResourse(BaseClient):
    """人事労務API
    
    メソッドについての詳細は以下を参照してください。
    https://developer.freee.co.jp/reference/hr/reference#/
    """
    API_URL = "/hr/api/v1/"


    def get_users_me(self) -> FreeeResponse:
        """ログインユーザーの取得

        Returns:
            FreeeResponse: このリクエストの認可セッションにおけるログインユーザーの情報を返します。
        
        Example:
            {
                "id": 0,
                "companies": [
                    {
                        "id": 0,
                        "name": "string",
                        "role": "company_admin",
                        "external_cid": "string",
                        "employee_id": 0,
                        "display_name": "string"
                    }
                ]
            }
        """
        endpoint_url = f"./users/me"
        return self.api_call(method="GET", endpoint_url=endpoint_url)


    def get_approval_flow_route(
        self,
        *,
        id: int|None=None
        ) -> FreeeResponse:
        """指定した事業所の申請経路を取得する。

        Args:
            id (int | None, optional): 申請経路ID

        Returns:
            FreeeResponse: 指定した事業所の申請経路を返します。
        
        Example:
            {
                "approval_flow_route": {
                    "id": 1,
                    "name": "申請経路",
                    "description": "申請経路の説明",
                    "user_id": 1,
                    "definition_system": true,
                    "first_step_id": 1,
                    "usages": [
                        "AttendanceWorkflow"
                    ],
                    "steps": [
                        {
                            "id": 1,
                            "next_step_id": 2,
                            "resource_type": "predefined_user",
                            "user_ids": [
                                3
                            ]
                        }
                    ]
                }
            }
        """
        endpoint_url = f"./approval_flow_routes/{id}"
        return self.api_call(method="GET", endpoint_url=endpoint_url)


#TODO 引数usageの詳細な説明を追記する。
    def get_approval_flow_routes(
        self,
        included_user_id: int|None=None,
        usage: str|None=None
        ) -> FreeeResponse:
        """指定した事業所の申請経路一覧を取得する。

        Args:
            included_user_id (int | None, optional): 経路に含まれるユーザーのユーザーID
            usage (str | None, optional): 申請種別（申請経路を使用できる申請種別を示します。例えば、AttendanceWorkflow の場合は、勤怠申請で使用できる申請経路です。）

        Returns:
            FreeeResponse: 指定した事業所の申請経路を返します。
        
        Example:
            {
                "approval_flow_routes": [
                    {
                        "id": 1,
                        "name": "申請経路",
                        "description": "申請経路の説明",
                        "user_id": 1,
                        "definition_system": true,
                        "first_step_id": 1,
                        "usages": [
                            "AttendanceWorkflow"
                        ]
                    }
                ]
            }
        """
        endpoint_url = f"./approval_flow_routes"
        query = dict(
            included_user_id=included_user_id,
            usage=usage
        )
        return self.api_call(method="GET", endpoint_url=endpoint_url, query=query)


    def get_approval_requests_monthly_attendance(
        self,
        *,
        id: int|None=None
        ) -> FreeeResponse:
        """指定した事業所の月次勤怠締め申請情報を取得します。

        Args:
            id (int | None, optional): 月次勤怠締め申請ID

        Returns:
            FreeeResponse: 指定した事業所の月次勤怠締め申請情報を返します。
        
        Example:
            {
                "monthly_attendance": {
                    "id": 1,
                    "company_id": 1,
                    "application_number": 1,
                    "applicant_id": 1,
                    "approver_ids": [
                        1
                    ],
                    "target_date": "2022-02-01",
                    "issue_date": "string",
                    "status": "in_progress",
                    "passed_auto_check": true,
                    "approval_flow_route_id": 1,
                    "approval_flow_route_name": "申請経路",
                    "approval_flow_logs": [
                        {
                            "user_id": 1,
                            "action": "approve",
                            "update_at": "2022-06-08T09:46:46.000+09:00"
                        }
                    ],
                    "current_step_id": 1,
                    "current_round": 1
                }
            }
        """
        endpoint_url = f"./approval_requests/monthly_attendances/{id}"
        return self.api_call(method="GET", endpoint_url=endpoint_url)


    def get_approval_requests_monthly_attendances(
        self,
        status: str|None=None,
        application_number: int|None=None,
        start_issue_date: str|None=None,
        end_issue_date: str|None=None,
        approver_id: int|None=None,
        applicant_id: int|None=None,
        start_target_date: str|None=None,
        end_target_date: str|None=None,
        passed_auto_check: bool|None=None,
        limit: int|None=50,
        offset: int|None=0
        ) -> FreeeResponse:
        """指定した事業所の指定日付時点における月次勤怠締め申請情報をリストで返します。

        Args:
            status (str | None, optional): 申請ステータス
                exapmle:
                    draft - 下書き\n
                    in_progress - 申請中\n
                    approved - 承認済\n
                    feedback - 差戻し\n
            application_number (int | None, optional): 申請No
            start_issue_date (str | None, optional): 申請開始日
            end_issue_date (str | None, optional): 申請終了日
            approver_id (int | None, optional): 現在承認ステップの承認者のユーザーID
                warning:
                    approver_idに値を指定する場合、指定なしの申請経路を利用した申請は返却されません
            applicant_id (int | None, optional): 申請者のユーザーID
            start_target_date (str | None, optional): 対象開始日
            end_target_date (str | None, optional): 対象終了日
            passed_auto_check (bool | None, optional): 自動チェック結果
                noticve:
                    trueを指定した場合、自動チェック結果がtrueの申請のみ返却します。\n
                    falseを指定した場合、自動チェック結果がfalseの申請のみ返却します。\n
                    キーごと指定しない場合、すべての申請を返却します。\n
            limit (int | None, optional): 取得レコードの件数(デフォルト: 50, 最小: 1, 最大: 100)
            offset (int | None, optional): 取得レコードのオフセット (デフォルト: 0)

        Returns:
            FreeeResponse: 指定した事業所の指定日付時点における月次勤怠締め申請情報をリストで返します。
        
        Example:
            {
                "monthly_attendances": [
                    {
                        "id": 1,
                        "company_id": 1,
                        "application_number": 1,
                        "applicant_id": 1,
                        "approver_ids": [
                            1
                        ],
                        "target_date": "2022-02-01",
                        "issue_date": "string",
                        "status": "in_progress",
                        "passed_auto_check": true
                    }
                ],
                "total_count": 1
            }
        """
        endpoint_url = f"./approval_requests/monthly_attendances"
        query = dict(
            status=status,
            application_number=application_number,
            start_issue_date=start_issue_date,
            end_issue_date=end_issue_date,
            approver_id=approver_id,
            applicant_id=applicant_id,
            start_target_date=start_target_date,
            end_target_date=end_target_date,
            passed_auto_check=passed_auto_check,
            limit=limit,
            offset=offset
        )
        return self.api_call(method="GET", endpoint_url=endpoint_url, query=query)


    def get_approval_requests_overtime_work(
        self,
        *,
        id: int|None=None
        ) -> FreeeResponse:
        """指定した事業所の残業申請情報を取得します。

        Args:
            id (int | None, optional): 残業申請ID. Defaults to None.

        Returns:
            FreeeResponse: 指定した事業所の残業申請情報を返します。
        
        Example:
            {
                "overtime_work": {
                    "id": 1,
                    "company_id": 1,
                    "application_number": 1,
                    "applicant_id": 1,
                    "approver_ids": [
                        1
                    ],
                    "target_date": "string",
                    "start_at": "12:00",
                    "end_at": "23:59",
                    "issue_date": "string",
                    "comment": "申請理由",
                    "status": "in_progress",
                    "revoke_status": "revoking",
                    "passed_auto_check": true,
                    "approval_flow_route_id": 1,
                    "approval_flow_route_name": "申請経路",
                    "approval_flow_logs": [
                        {
                            "user_id": 1,
                            "action": "approve",
                            "update_at": "2022-06-08T09:46:46.000+09:00"
                        }
                    ],
                    "current_step_id": 1,
                    "current_round": 1
                }
            }
        """
        endpoint_url = f"./approval_requests/overtime_works/{id}"
        return self.api_call(method="GET", endpoint_url=endpoint_url)


    def get_approval_requests_overtime_works(
        self,
        status: str|None=None,
        application_number: int|None=None,
        start_issue_date: str|None=None,
        end_issue_date: str|None=None,
        approver_id: int|None=None,
        applicant_id: int|None=None,
        start_target_date: str|None=None,
        end_target_date: str|None=None,
        passed_auto_check: bool|None=None,
        limit: int|None=50,
        offset: int|None=0
        ) -> FreeeResponse:
        """指定した事業所の指定日付時点における残業申請情報をリストで返します。

        Args:
            status (str | None, optional): 申請ステータス
                exapmle:
                    draft - 下書き\n
                    in_progress - 申請中\n
                    approved - 承認済\n
                    feedback - 差戻し\n
            application_number (int | None, optional): 申請No
            start_issue_date (str | None, optional): 申請開始日
            end_issue_date (str | None, optional): 申請終了日
            approver_id (int | None, optional): 現在承認ステップの承認者のユーザーID
                warning:
                    approver_idに値を指定する場合、指定なしの申請経路を利用した申請は返却されません
            applicant_id (int | None, optional): 申請者のユーザーID
            start_target_date (str | None, optional): 対象開始日
            end_target_date (str | None, optional): 対象終了日
            passed_auto_check (bool | None, optional): 自動チェック結果
                noticve:
                    trueを指定した場合、自動チェック結果がtrueの申請のみ返却します。\n
                    falseを指定した場合、自動チェック結果がfalseの申請のみ返却します。\n
                    キーごと指定しない場合、すべての申請を返却します。\n
            limit (int | None, optional): 取得レコードの件数(デフォルト: 50, 最小: 1, 最大: 100)
            offset (int | None, optional): 取得レコードのオフセット (デフォルト: 0)

        Returns:
            FreeeResponse: 指定した事業所の指定日付時点における残業申請情報をリストで返します。
        
        Example:
            {
                "overtime_works": [
                    {
                        "id": 1,
                        "company_id": 1,
                        "application_number": 1,
                        "applicant_id": 1,
                        "approver_ids": [
                            1
                        ],
                        "target_date": "string",
                        "start_at": "12:00",
                        "end_at": "23:59",
                        "issue_date": "string",
                        "comment": "申請理由",
                        "status": "in_progress",
                        "revoke_status": "revoking",
                        "passed_auto_check": true
                    }
                ],
                "total_count": 1
            }
        """
        endpoint_url = f"./approval_requests/overtime_works"
        query = dict(
            status=status,
            application_number=application_number,
            start_issue_date=start_issue_date,
            end_issue_date=end_issue_date,
            approver_id=approver_id,
            applicant_id=applicant_id,
            start_target_date=start_target_date,
            end_target_date=end_target_date,
            passed_auto_check=passed_auto_check,
            limit=limit,
            offset=offset
        )
        return self.api_call(method="GET", endpoint_url=endpoint_url, query=query)


    def get_approval_requests_paid_holiday(
        self,
        *,
        id: int|None=None
        ) -> FreeeResponse:
        """指定した事業所の有給申請情報を取得します。

        Args:
            id (int | None, optional): 有給申請ID. Defaults to None.

        Returns:
            FreeeResponse: 指定した事業所の有給申請情報を返します。
        
        Example:
            {
                "paid_holiday": {
                    "id": 1,
                    "company_id": 1,
                    "application_number": 1,
                    "applicant_id": 1,
                    "approver_ids": [
                        1
                    ],
                    "target_date": "string",
                    "holiday_type": "half",
                    "start_at": "12:00",
                    "end_at": "23:59",
                    "issue_date": "string",
                    "comment": "申請理由",
                    "status": "in_progress",
                    "revoke_status": "revoking",
                    "passed_auto_check": true,
                    "approval_flow_route_id": 1,
                    "approval_flow_route_name": "申請経路",
                    "approval_flow_logs": [
                        {
                            "user_id": 1,
                            "action": "approve",
                            "update_at": "2022-06-08T09:46:46.000+09:00"
                        }
                    ],
                    "current_step_id": 1,
                    "current_round": 1
                }
            }
        """
        endpoint_url = f"./approval_requests/paid_holidays/{id}"
        return self.api_call(method="GET", endpoint_url=endpoint_url)


    def get_approval_requests_paid_holidays(
        self,
        status: str|None=None,
        application_number: int|None=None,
        start_issue_date: str|None=None,
        end_issue_date: str|None=None,
        approver_id: int|None=None,
        applicant_id: int|None=None,
        start_target_date: str|None=None,
        end_target_date: str|None=None,
        passed_auto_check: bool|None=None,
        limit: int|None=50,
        offset: int|None=0
        ) -> FreeeResponse:
        """指定した事業所の指定日付時点における有給申請情報をリストで返します。

        Args:
            status (str | None, optional): 申請ステータス
                exapmle:
                    draft - 下書き\n
                    in_progress - 申請中\n
                    approved - 承認済\n
                    feedback - 差戻し\n
            application_number (int | None, optional): 申請No
            start_issue_date (str | None, optional): 申請開始日
            end_issue_date (str | None, optional): 申請終了日
            approver_id (int | None, optional): 現在承認ステップの承認者のユーザーID
                warning:
                    approver_idに値を指定する場合、指定なしの申請経路を利用した申請は返却されません
            applicant_id (int | None, optional): 申請者のユーザーID
            start_target_date (str | None, optional): 対象開始日
            end_target_date (str | None, optional): 対象終了日
            passed_auto_check (bool | None, optional): 自動チェック結果
                noticve:
                    trueを指定した場合、自動チェック結果がtrueの申請のみ返却します。\n
                    falseを指定した場合、自動チェック結果がfalseの申請のみ返却します。\n
                    キーごと指定しない場合、すべての申請を返却します。\n
            limit (int | None, optional): 取得レコードの件数(デフォルト: 50, 最小: 1, 最大: 100)
            offset (int | None, optional): 取得レコードのオフセット (デフォルト: 0)

        Returns:
            FreeeResponse: 指定した事業所の指定日付時点における有給申請情報をリストで返します。
        
        Example:
            {
                "paid_holidays": [
                    {
                        "id": 1,
                        "company_id": 1,
                        "application_number": 1,
                        "applicant_id": 1,
                        "approver_ids": [
                            1
                        ],
                        "target_date": "string",
                        "holiday_type": "half",
                        "start_at": "12:00",
                        "end_at": "23:59",
                        "issue_date": "string",
                        "comment": "申請理由",
                        "status": "in_progress",
                        "revoke_status": "revoking",
                        "passed_auto_check": true
                    }
                ],
                "total_count": 1
            }
        """
        endpoint_url = f"./approval_requests/paid_holidays"
        query = dict(
            status=status,
            application_number=application_number,
            start_issue_date=start_issue_date,
            end_issue_date=end_issue_date,
            approver_id=approver_id,
            applicant_id=applicant_id,
            start_target_date=start_target_date,
            end_target_date=end_target_date,
            passed_auto_check=passed_auto_check,
            limit=limit,
            offset=offset
        )
        return self.api_call(method="GET", endpoint_url=endpoint_url, query=query)


    def get_approval_requests_special_holiday(
        self,
        *,
        id: int|None=None
        ) -> FreeeResponse:
        """指定した事業所の特別休暇申請情報を取得します。

        Args:
            id (int | None, optional): 特別休暇申請ID. Defaults to None.

        Returns:
            FreeeResponse: 指定した事業所の特別休暇申請情報を返します。
        
        Example:
            {
                "special_holiday": {
                    "id": 1,
                    "company_id": 1,
                    "application_number": 1,
                    "applicant_id": 1,
                    "approver_ids": [
                        1
                    ],
                    "target_date": "string",
                    "special_holiday_setting_id": 1,
                    "special_holiday_name": "特別休暇名称",
                    "holiday_type": "half",
                    "start_at": "12:00",
                    "end_at": "23:59",
                    "issue_date": "string",
                    "comment": "申請理由",
                    "status": "in_progress",
                    "revoke_status": null,
                    "passed_auto_check": true,
                    "approval_flow_route_id": 1,
                    "approval_flow_route_name": "申請経路",
                    "approval_flow_logs": [
                        {
                            "user_id": 1,
                            "action": "approve",
                            "update_at": "2022-06-08T09:46:46.000+09:00"
                        }
                    ],
                    "current_step_id": 1,
                    "current_round": 1
                }
            }
        """
        endpoint_url = f"./approval_requests/special_holidays/{id}"
        return self.api_call(method="GET", endpoint_url=endpoint_url)


    def get_approval_requests_special_holidays(
        self,
        status: str|None=None,
        application_number: int|None=None,
        start_issue_date: str|None=None,
        end_issue_date: str|None=None,
        approver_id: int|None=None,
        applicant_id: int|None=None,
        start_target_date: str|None=None,
        end_target_date: str|None=None,
        passed_auto_check: bool|None=None,
        limit: int|None=50,
        offset: int|None=0
        ) -> FreeeResponse:
        """指定した事業所の指定日付時点における特別休暇申請情報をリストで返します。

        Args:
            status (str | None, optional): 申請ステータス
                exapmle:
                    draft - 下書き\n
                    in_progress - 申請中\n
                    approved - 承認済\n
                    feedback - 差戻し\n
            application_number (int | None, optional): 申請No
            start_issue_date (str | None, optional): 申請開始日
            end_issue_date (str | None, optional): 申請終了日
            approver_id (int | None, optional): 現在承認ステップの承認者のユーザーID
                warning:
                    approver_idに値を指定する場合、指定なしの申請経路を利用した申請は返却されません
            applicant_id (int | None, optional): 申請者のユーザーID
            start_target_date (str | None, optional): 対象開始日
            end_target_date (str | None, optional): 対象終了日
            passed_auto_check (bool | None, optional): 自動チェック結果
                noticve:
                    trueを指定した場合、自動チェック結果がtrueの申請のみ返却します。\n
                    falseを指定した場合、自動チェック結果がfalseの申請のみ返却します。\n
                    キーごと指定しない場合、すべての申請を返却します。\n
            limit (int | None, optional): 取得レコードの件数(デフォルト: 50, 最小: 1, 最大: 100)
            offset (int | None, optional): 取得レコードのオフセット (デフォルト: 0)

        Returns:
            FreeeResponse: 指定した事業所の指定日付時点における特別休暇申請情報をリストで返します。
        
        Example:
            {
                "special_holidays": [
                    {
                        "id": 1,
                        "company_id": 1,
                        "application_number": 1,
                        "applicant_id": 1,
                        "approver_ids": [
                            1
                        ],
                        "target_date": "string",
                        "special_holiday_setting_id": 1,
                        "special_holiday_name": "特別休暇名称",
                        "holiday_type": "half",
                        "start_at": "12:00",
                        "end_at": "23:59",
                        "issue_date": "string",
                        "comment": "申請理由",
                        "status": "in_progress",
                        "revoke_status": null,
                        "passed_auto_check": true
                    }
                ],
                "total_count": 1
            }
        """
        endpoint_url = f"./approval_requests/special_holidays"
        query = dict(
            status=status,
            application_number=application_number,
            start_issue_date=start_issue_date,
            end_issue_date=end_issue_date,
            approver_id=approver_id,
            applicant_id=applicant_id,
            start_target_date=start_target_date,
            end_target_date=end_target_date,
            passed_auto_check=passed_auto_check,
            limit=limit,
            offset=offset
        )
        return self.api_call(method="GET", endpoint_url=endpoint_url, query=query)


    def get_approval_requests_work_time(
        self,
        *,
        id: int|None=None
        ) -> FreeeResponse:
        """指定した事業所の勤務時間修正申請情報を取得します。

        Args:
            id (int | None, optional): 勤務時間修正申請ID. Defaults to None.

        Returns:
            FreeeResponse: 指定した事業所の勤務時間修正申請情報を返します。
        
        Example:
            {
                "work_time": {
                    "id": 1,
                    "company_id": 1,
                    "application_number": 1,
                    "applicant_id": 1,
                    "approver_ids": [
                        1
                    ],
                    "target_date": "string",
                    "clear_work_time": false,
                    "clock_in_at": "12:00",
                    "clock_out_at": "23:59",
                    "lateness_mins": 0,
                    "early_leaving_mins": 0,
                    "break_records": [
                        {
                            "clock_in_at": "12:00",
                            "clock_out_at": "23:59"
                        }
                    ],
                    "issue_date": "string",
                    "comment": "申請理由",
                    "status": "in_progress",
                    "passed_auto_check": true,
                    "approval_flow_route_id": 1,
                    "approval_flow_route_name": "申請経路",
                    "approval_flow_logs": [
                        {
                            "user_id": 1,
                            "action": "approve",
                            "update_at": "2022-06-08T09:46:46.000+09:00"
                        }
                    ],
                    "current_step_id": 1,
                    "current_round": 1
                }
            }
        """
        endpoint_url = f"./approval_requests/work_times/{id}"
        return self.api_call(method="GET", endpoint_url=endpoint_url)


    def get_approval_requests_work_times(
        self,
        status: str|None=None,
        application_number: int|None=None,
        start_issue_date: str|None=None,
        end_issue_date: str|None=None,
        approver_id: int|None=None,
        applicant_id: int|None=None,
        start_target_date: str|None=None,
        end_target_date: str|None=None,
        passed_auto_check: bool|None=None,
        limit: int|None=50,
        offset: int|None=0
        ) -> FreeeResponse:
        """指定した事業所の指定日付時点における勤務時間修正申請情報をリストで返します。

        Args:
            status (str | None, optional): 申請ステータス
                exapmle:
                    draft - 下書き\n
                    in_progress - 申請中\n
                    approved - 承認済\n
                    feedback - 差戻し\n
            application_number (int | None, optional): 申請No
            start_issue_date (str | None, optional): 申請開始日
            end_issue_date (str | None, optional): 申請終了日
            approver_id (int | None, optional): 現在承認ステップの承認者のユーザーID
                warning:
                    approver_idに値を指定する場合、指定なしの申請経路を利用した申請は返却されません
            applicant_id (int | None, optional): 申請者のユーザーID
            start_target_date (str | None, optional): 対象開始日
            end_target_date (str | None, optional): 対象終了日
            passed_auto_check (bool | None, optional): 自動チェック結果
                noticve:
                    trueを指定した場合、自動チェック結果がtrueの申請のみ返却します。\n
                    falseを指定した場合、自動チェック結果がfalseの申請のみ返却します。\n
                    キーごと指定しない場合、すべての申請を返却します。\n
            limit (int | None, optional): 取得レコードの件数(デフォルト: 50, 最小: 1, 最大: 100)
            offset (int | None, optional): 取得レコードのオフセット (デフォルト: 0)

        Returns:
            FreeeResponse: 指定した事業所の指定日付時点における勤務時間修正申請情報をリストで返します。
        
        Example:
            {
                "work_times": [
                    {
                        "id": 1,
                        "company_id": 1,
                        "application_number": 1,
                        "applicant_id": 1,
                        "approver_ids": [
                            1
                        ],
                        "target_date": "string",
                        "clear_work_time": true,
                        "clock_in_at": "12:00",
                        "clock_out_at": "23:59",
                        "lateness_mins": 0,
                        "early_leaving_mins": 0,
                        "break_records": [
                            {
                            "clock_in_at": "12:00",
                            "clock_out_at": "23:59"
                            }
                        ],
                        "issue_date": "string",
                        "comment": "申請理由",
                        "status": "in_progress",
                        "passed_auto_check": true
                    }
                ],
                "total_count": 1
            }
        """
        endpoint_url = f"./approval_requests/work_times"
        query = dict(
            status=status,
            application_number=application_number,
            start_issue_date=start_issue_date,
            end_issue_date=end_issue_date,
            approver_id=approver_id,
            applicant_id=applicant_id,
            start_target_date=start_target_date,
            end_target_date=end_target_date,
            passed_auto_check=passed_auto_check,
            limit=limit,
            offset=offset
        )
        return self.api_call(method="GET", endpoint_url=endpoint_url, query=query)


    def get_bonuses_employee_payroll_statement(
        self,
        *,
        year: int|None=None,
        month: int|None=None,
        employee_id: int|None=None
        ) -> FreeeResponse:
        """指定した従業員ID、年月の賞与明細を返します。

        指定した年月に支払いのある賞与明細が返されます。

        Args:
            year (int | None, optional): 従業員情報を取得したい年. Defaults to None.
            month (int | None, optional): 従業員情報を取得したい月. Defaults to None.
            employee_id (int | None, optional): 従業員ID. Defaults to None.

        Returns:
            FreeeResponse: 指定した従業員ID、年月の賞与明細を返します。
        
        Example:
            {
                "employee_payroll_statement": {
                    "id": 0,
                    "company_id": 0,
                    "employee_id": 0,
                    "employee_name": "string",
                    "employee_display_name": "string",
                    "employee_num": "string",
                    "closing_date": "string",
                    "pay_date": "string",
                    "fixed": true,
                    "calc_status": "string",
                    "calculated_at": "2024-03-11T03:19:30.369Z",
                    "bonus_amount": "string",
                    "total_allowance_amount": "string",
                    "total_deduction_amount": "string",
                    "net_payment_amount": "string",
                    "gross_payment_amount": "string",
                    "total_taxable_payment_amount": "string",
                    "allowances": [
                        {
                            "name": "string",
                            "amount": "string"
                        }
                    ],
                    "deductions": [
                        {
                            "name": "string",
                            "amount": "string"
                        }
                    ],
                    "remark": "string"
                }
            }
        """
        endpoint_url = f"./bonuses/employee_payroll_statements/{employee_id}"
        query = dict(
            year=year,
            month=month
        )
        return self.api_call(method="GET", endpoint_url=endpoint_url, query=query)


    def get_bonuses_employee_payroll_statements(
        self,
        limit: int|None=50,
        offset: int|None=0,
        *,
        year: int|None=None,
        month: int|None=None
        ) -> FreeeResponse:
        """指定した事業所に所属する従業員の賞与明細をリストで返します。

        指定した年月に支払いのある賞与明細が返されます。

        Args:
            limit (int | None, optional): 取得レコードの件数(デフォルト: 50, 最小: 1, 最大: 100). Defaults to None.
            offset (int | None, optional): 取得レコードのオフセット (デフォルト: 0). Defaults to None.
            year (int | None, optional): 従業員情報を取得したい年. Defaults to None.
            month (int | None, optional): 従業員情報を取得したい月. Defaults to None.

        Returns:
            FreeeResponse: 指定した事業所に所属する従業員の賞与明細をリストで返します。
        
        Example:
            {
                "employee_payroll_statements": [
                    {
                        "id": 0,
                        "company_id": 0,
                        "employee_id": 0,
                        "employee_name": "string",
                        "employee_display_name": "string",
                        "employee_num": "string",
                        "closing_date": "string",
                        "pay_date": "string",
                        "fixed": true,
                        "calc_status": "string",
                        "calculated_at": "2024-03-11T03:20:56.319Z",
                        "bonus_amount": "string",
                        "total_allowance_amount": "string",
                        "total_deduction_amount": "string",
                        "net_payment_amount": "string",
                        "gross_payment_amount": "string",
                        "total_taxable_payment_amount": "string",
                        "allowances": [
                            {
                            "name": "string",
                            "amount": "string"
                            }
                        ],
                        "deductions": [
                            {
                            "name": "string",
                            "amount": "string"
                            }
                        ],
                        "remark": "string"
                        }
                    ],
                "total_count": 0
            }
        """
        endpoint_url = f"./bonuses/employee_payroll_statements"
        query = dict(
            year=year,
            month=month,
            limit=limit,
            offset=offset
        )
        return self.api_call(method="GET", endpoint_url=endpoint_url, query=query)


    def get_company_employees(
        self,
        limit: int=50, 
        offset: int=0, 
        with_no_payroll_calculation: bool|None=False
        ) -> FreeeResponse:
        """指定した事業所に所属する従業員をリストで返します。

        Args:
            limit (int, optional): 取得レコードの件数 (デフォルト: 50, 最小: 1, 最大: 100)
            offset (int, optional): 取得レコードのオフセット (デフォルト: 0)
            with_no_payroll_calculation (bool | None, optional): trueを指定すると給与計算対象外の従業員情報をレスポンスに含めます。

        Returns:
            FreeeResponse: 指定した事業所に所属する従業員をリストで返します。
        
        Example:
            [
                {
                    "id": 0,
                    "num": "string",
                    "display_name": "string",
                    "entry_date": "string",
                    "retire_date": "string",
                    "user_id": 0,
                    "email": "string",
                    "payroll_calculation": true,
                    "closing_day": 31,
                    "pay_day": 15,
                    "month_of_pay_day": "next_month"
                }
            ]
        """
        endpoint_url = f"./companies/{self.company_id}/employees"
        query = dict(
            limit=limit,
            offset=offset,
            with_no_payroll_calculation=with_no_payroll_calculation,
        )
        return self.api_call(method="GET", endpoint_url=endpoint_url, query=query)


    def get_employee(
        self,
        *,
        year: int|None=None,
        month: int|None=None,
        id: int|None=None
        ) -> FreeeResponse:
        """指定したIDの従業員を返します。

        Args:
            year (int | None, optional): 従業員情報を取得したい年. Defaults to None.
            month (int | None, optional): 従業員情報を取得したい月. Defaults to None.
                notice:
                    締日支払日設定が翌月払いの従業員情報の場合は、 指定したmonth + 1の値が検索結果として返します。
                    翌月払いの従業員の2022/01の従業員情報を取得する場合は、year=2021,month=12を指定してください。
            id (int | None, optional): 従業員ID. Defaults to None.

        Returns:
            FreeeResponse: 指定したIDの従業員を返します。
        
        Example:
            {
                "employee": {
                    "id": 0,
                    "company_id": 0,
                    "num": "string",
                    "display_name": "string",
                    "base_pension_num": "string",
                    "employment_insurance_reference_number": "string",
                    "birth_date": "string",
                    "entry_date": "string",
                    "retire_date": "string",
                    "user_id": 0,
                    "profile_rule": {
                        "id": 0,
                        "company_id": 0,
                        "employee_id": 0,
                        "last_name": "string",
                        "first_name": "string",
                        "last_name_kana": "string",
                        "first_name_kana": "string",
                        "zipcode1": "000",
                        "zipcode2": "0000",
                        "prefecture_code": 4,
                        "address": "string",
                        "address_kana": "string",
                        "phone1": "000",
                        "phone2": "0000",
                        "phone3": "0000",
                        "residential_zipcode1": "000",
                        "residential_zipcode2": "0000",
                        "residential_prefecture_code": 4,
                        "residential_address": "string",
                        "residential_address_kana": "string",
                        "employment_type": "string",
                        "title": "string",
                        "gender": "male",
                        "married": true,
                        "is_working_student": true,
                        "widow_type": "string",
                        "disability_type": "string",
                        "email": "test@example.com",
                        "householder_name": "山田 吾郎",
                        "householder": "father"
                    },
                    "health_insurance_rule": {
                        "id": 0,
                        "company_id": 0,
                        "employee_id": 0,
                        "entried": true,
                        "health_insurance_salary_calc_type": "manual",
                        "health_insurance_bonus_calc_type": "manual",
                        "manual_health_insurance_amount_of_employee_salary": 8888,
                        "manual_health_insurance_amount_of_employee_bonus": 7777,
                        "manual_health_insurance_amount_of_company_salary": 6666.0001,
                        "manual_health_insurance_amount_of_company_bonus": 5555.0001,
                        "care_insurance_salary_calc_type": "manual",
                        "care_insurance_bonus_calc_type": "manual",
                        "manual_care_insurance_amount_of_employee_salary": 4444,
                        "manual_care_insurance_amount_of_employee_bonus": 3333,
                        "manual_care_insurance_amount_of_company_salary": 2222.0001,
                        "manual_care_insurance_amount_of_company_bonus": 1111.0001,
                        "reference_num": "string",
                        "standard_monthly_remuneration": 0
                    },
                    "welfare_pension_insurance_rule": {
                        "id": 0,
                        "child_allowance_contribution_bonus_calc_type": "manual",
                        "child_allowance_contribution_salary_calc_type": "manual",
                        "company_id": 0,
                        "employee_id": 0,
                        "entried": true,
                        "manual_child_allowance_contribution_amount_bonus": 111.0001,
                        "manual_child_allowance_contribution_amount_salary": 222.0001,
                        "manual_welfare_pension_insurance_amount_of_company_bonus": 333.0001,
                        "manual_welfare_pension_insurance_amount_of_company_salary": 444.0001,
                        "manual_welfare_pension_insurance_amount_of_employee_bonus": 555,
                        "manual_welfare_pension_insurance_amount_of_employee_salary": 666,
                        "reference_num": "string",
                        "standard_monthly_remuneration": 0,
                        "welfare_pension_insurance_bonus_calc_type": "manual",
                        "welfare_pension_insurance_salary_calc_type": "manual"
                    },
                    "dependent_rules": [
                        {
                            "id": 0,
                            "company_id": 0,
                            "employee_id": 0,
                            "last_name": "string",
                            "first_name": "string",
                            "last_name_kana": "string",
                            "first_name_kana": "string",
                            "gender": "unselected",
                            "relationship": "string",
                            "birth_date": "string",
                            "residence_type": "string",
                            "zipcode1": "string",
                            "zipcode2": "string",
                            "prefecture_code": 4,
                            "address": "string",
                            "address_kana": "string",
                            "base_pension_num": "string",
                            "income": 0,
                            "annual_revenue": 0,
                            "disability_type": "string",
                            "occupation": "string",
                            "annual_remittance_amount": 0,
                            "employment_insurance_receive_status": "unselected",
                            "employment_insurance_receives_from": "string",
                            "phone_type": "unselected",
                            "phone1": "000",
                            "phone2": "0000",
                            "phone3": "0000",
                            "social_insurance_and_tax_dependent": "string",
                            "social_insurance_dependent_acquisition_date": "string",
                            "social_insurance_dependent_acquisition_reason": "",
                            "social_insurance_other_dependent_acquisition_reason": "string",
                            "social_insurance_dependent_disqualification_date": "string",
                            "social_insurance_dependent_disqualification_reason": "",
                            "social_insurance_other_dependent_disqualification_reason": "string",
                            "tax_dependent_acquisition_date": "string",
                            "tax_dependent_acquisition_reason": "",
                            "tax_other_dependent_acquisition_reason": "string",
                            "tax_dependent_disqualification_date": "string",
                            "tax_dependent_disqualification_reason": "",
                            "tax_other_dependent_disqualification_reason": "string",
                            "non_resident_dependents_reason": "none"
                        }
                    ],
                    "bank_account_rule": {
                        "id": 0,
                        "company_id": 0,
                        "employee_id": 0,
                        "bank_name": "string",
                        "bank_name_kana": "string",
                        "bank_code": "string",
                        "branch_name": "string",
                        "branch_name_kana": "string",
                        "branch_code": "string",
                        "account_number": "string",
                        "account_name": "string",
                        "account_type": "string"
                    },
                    "basic_pay_rule": {
                        "id": 0,
                        "company_id": 0,
                        "employee_id": 0,
                        "pay_calc_type": "monthly",
                        "pay_amount": 0
                    },
                    "payroll_calculation": true,
                    "company_reference_date_rule_name": "当月締め翌月払い"
                }
            }
        """
        endpoint_url = f"./employees/{id}"
        query = dict(
            year=year,
            month=month
        )
        return self.api_call(method="GET", endpoint_url=endpoint_url, query=query)


    def get_employees(
        self,
        limit: int=50, 
        offset: int=0, 
        with_no_payroll_calculation: bool|None=False,
        *,
        year: int|None=None,
        month: int|None=None
        ) -> FreeeResponse:
        """指定した対象年月に事業所に所属する従業員をリストで返します。

        Args:
            limit (int, optional): 取得レコードの件数 (デフォルト: 50, 最小: 1, 最大: 100)
            offset (int, optional): 取得レコードのオフセット (デフォルト: 0)
            with_no_payroll_calculation (bool | None, optional): trueを指定すると給与計算対象外の従業員情報をレスポンスに含めます。. Defaults to None.
            year (int | None, optional): 従業員情報を取得したい年. Defaults to None.
            month (int | None, optional): 従業員情報を取得したい月. Defaults to None.
                notice:
                    締日支払日設定が翌月払いの従業員情報の場合は、 指定したmonth + 1の値が検索結果として返します。
                    翌月払いの従業員の2022/01の従業員情報を取得する場合は、year=2021,month=12を指定してください。

        Returns:
            FreeeResponse: 指定した対象年月に事業所に所属する従業員をリストで返します。
        
        Example:
            {
                "employees": [
                    {
                        "id": 0,
                        "company_id": 0,
                        "num": "string",
                        "display_name": "string",
                        "base_pension_num": "string",
                        "employment_insurance_reference_number": "string",
                        "birth_date": "string",
                        "entry_date": "string",
                        "retire_date": "string",
                        "user_id": 0,
                        "profile_rule": {
                            "id": 0,
                            "company_id": 0,
                            "employee_id": 0,
                            "last_name": "string",
                            "first_name": "string",
                            "last_name_kana": "string",
                            "first_name_kana": "string",
                            "zipcode1": "000",
                            "zipcode2": "0000",
                            "prefecture_code": 4,
                            "address": "string",
                            "address_kana": "string",
                            "phone1": "000",
                            "phone2": "0000",
                            "phone3": "0000",
                            "residential_zipcode1": "000",
                            "residential_zipcode2": "0000",
                            "residential_prefecture_code": 4,
                            "residential_address": "string",
                            "residential_address_kana": "string",
                            "employment_type": "string",
                            "title": "string",
                            "gender": "male",
                            "married": true,
                            "is_working_student": true,
                            "widow_type": "string",
                            "disability_type": "string",
                            "email": "test@example.com",
                            "householder_name": "山田 吾郎",
                            "householder": "father"
                        },
                        "health_insurance_rule": {
                            "id": 0,
                            "company_id": 0,
                            "employee_id": 0,
                            "entried": true,
                            "health_insurance_salary_calc_type": "manual",
                            "health_insurance_bonus_calc_type": "manual",
                            "manual_health_insurance_amount_of_employee_salary": 8888,
                            "manual_health_insurance_amount_of_employee_bonus": 7777,
                            "manual_health_insurance_amount_of_company_salary": 6666.0001,
                            "manual_health_insurance_amount_of_company_bonus": 5555.0001,
                            "care_insurance_salary_calc_type": "manual",
                            "care_insurance_bonus_calc_type": "manual",
                            "manual_care_insurance_amount_of_employee_salary": 4444,
                            "manual_care_insurance_amount_of_employee_bonus": 3333,
                            "manual_care_insurance_amount_of_company_salary": 2222.0001,
                            "manual_care_insurance_amount_of_company_bonus": 1111.0001,
                            "reference_num": "string",
                            "standard_monthly_remuneration": 0
                        },
                        "welfare_pension_insurance_rule": {
                            "id": 0,
                            "child_allowance_contribution_bonus_calc_type": "manual",
                            "child_allowance_contribution_salary_calc_type": "manual",
                            "company_id": 0,
                            "employee_id": 0,
                            "entried": true,
                            "manual_child_allowance_contribution_amount_bonus": 111.0001,
                            "manual_child_allowance_contribution_amount_salary": 222.0001,
                            "manual_welfare_pension_insurance_amount_of_company_bonus": 333.0001,
                            "manual_welfare_pension_insurance_amount_of_company_salary": 444.0001,
                            "manual_welfare_pension_insurance_amount_of_employee_bonus": 555,
                            "manual_welfare_pension_insurance_amount_of_employee_salary": 666,
                            "reference_num": "string",
                            "standard_monthly_remuneration": 0,
                            "welfare_pension_insurance_bonus_calc_type": "manual",
                            "welfare_pension_insurance_salary_calc_type": "manual"
                        },
                    "dependent_rules": [
                        {
                            "id": 0,
                            "company_id": 0,
                            "employee_id": 0,
                            "last_name": "string",
                            "first_name": "string",
                            "last_name_kana": "string",
                            "first_name_kana": "string",
                            "gender": "unselected",
                            "relationship": "string",
                            "birth_date": "string",
                            "residence_type": "string",
                            "zipcode1": "string",
                            "zipcode2": "string",
                            "prefecture_code": 4,
                            "address": "string",
                            "address_kana": "string",
                            "base_pension_num": "string",
                            "income": 0,
                            "annual_revenue": 0,
                            "disability_type": "string",
                            "occupation": "string",
                            "annual_remittance_amount": 0,
                            "employment_insurance_receive_status": "unselected",
                            "employment_insurance_receives_from": "string",
                            "phone_type": "unselected",
                            "phone1": "000",
                            "phone2": "0000",
                            "phone3": "0000",
                            "social_insurance_and_tax_dependent": "string",
                            "social_insurance_dependent_acquisition_date": "string",
                            "social_insurance_dependent_acquisition_reason": "",
                            "social_insurance_other_dependent_acquisition_reason": "string",
                            "social_insurance_dependent_disqualification_date": "string",
                            "social_insurance_dependent_disqualification_reason": "",
                            "social_insurance_other_dependent_disqualification_reason": "string",
                            "tax_dependent_acquisition_date": "string",
                            "tax_dependent_acquisition_reason": "",
                            "tax_other_dependent_acquisition_reason": "string",
                            "tax_dependent_disqualification_date": "string",
                            "tax_dependent_disqualification_reason": "",
                            "tax_other_dependent_disqualification_reason": "string",
                            "non_resident_dependents_reason": "none"
                        }
                    ],
                    "bank_account_rule": {
                        "id": 0,
                        "company_id": 0,
                        "employee_id": 0,
                        "bank_name": "string",
                        "bank_name_kana": "string",
                        "bank_code": "string",
                        "branch_name": "string",
                        "branch_name_kana": "string",
                        "branch_code": "string",
                        "account_number": "string",
                        "account_name": "string",
                        "account_type": "string"
                    },
                    "basic_pay_rule": {
                        "id": 0,
                        "company_id": 0,
                        "employee_id": 0,
                        "pay_calc_type": "monthly",
                        "pay_amount": 0
                    },
                    "payroll_calculation": true,
                    "company_reference_date_rule_name": "当月締め翌月払い"
                    }
                ],
                "total_count": 0
            }
        """
        endpoint_url = f"./employees"
        query = dict(
            year=year,
            month=month,
            limit=limit,
            offset=offset,
            with_no_payroll_calculation=with_no_payroll_calculation
        )
        return self.api_call(method="GET", endpoint_url=endpoint_url, query=query)


    def get_employees_special_holidays(
        self,
        date: str|None=None,
        start_date: str|None=None,
        end_date: str|None=None,
        *,
        employee_id: int|None=None
        ) -> FreeeResponse:
        """指定した従業員に付与された特別休暇情報をリストで返します。

        Args:
            date (str | None, optional): 対象日. Defaults to None.
            start_date (str | None, optional): 対象開始日. Defaults to None.
            end_date (str | None, optional): 対象終了日. Defaults to None.
            employee_id (int | None, optional): 従業員ID. Defaults to None.

        Returns:
            FreeeResponse: 指定した従業員に付与された特別休暇情報をリストで返します。
        
        Example:
            {
                "employee_special_holidays": [
                    {
                        "id": 1,
                        "company_id": 1,
                        "employee_id": 1,
                        "special_holiday_setting_id": 1,
                        "name": "育休",
                        "type_name": "育児休業日",
                        "paid_type": "paid",
                        "attendance_rate_calc_type": "in_workdays",
                        "usage_day": "half",
                        "valid_date_from": "string",
                        "valid_date_to": "string",
                        "days": 2,
                        "used": 0.5,
                        "num_days_and_hours_used": {
                            "days": 0.5,
                            "hours": 0
                        },
                        "left": 1.5,
                        "num_days_and_hours_left": {
                            "days": 1.5,
                            "hours": 0
                        }
                    }
                ]
            }
        """
        endpoint_url = f"./employees/{employee_id}/special_holidays"
        query = dict(
            date=date,
            start_date=start_date,
            end_date=end_date
        )
        return self.api_call(method="GET", endpoint_url=endpoint_url, query=query)


    def get_employee_bank_account_rule(
        self,
        *,
        year: int|None=None,
        month: int|None=None,
        employee_id: int|None=None
        ) -> FreeeResponse:
        """指定した従業員・日付の銀行口座情報を返します。

        Args:
            year (int | None, optional): 従業員情報を取得したい年. Defaults to None.
            month (int | None, optional): 従業員情報を取得したい月. Defaults to None.
                notice:
                    締日支払日設定が翌月払いの従業員情報の場合は、 指定したmonth + 1の値が検索結果として返します。
                    翌月払いの従業員の2022/01の従業員情報を取得する場合は、year=2021,month=12を指定してください。
            employee_id (int | None, optional): 従業員ID. Defaults to None.

        Returns:
            FreeeResponse: 指定した従業員・日付の銀行口座情報を返します。
        
        Example:
            {
                "employee_bank_account_rule": {
                    "id": 0,
                    "company_id": 0,
                    "employee_id": 0,
                    "bank_name": "string",
                    "bank_name_kana": "string",
                    "bank_code": "string",
                    "branch_name": "string",
                    "branch_name_kana": "string",
                    "branch_code": "string",
                    "account_number": "string",
                    "account_name": "string",
                    "account_type": "string"
                }
            }
        """
        endpoint_url = f"./employees/{employee_id}/bank_account_rule"
        query = dict(
            year=year,
            month=month
        )
        return self.api_call(method="GET", endpoint_url=endpoint_url, query=query)


    def get_employee_basic_pay_rule(
        self,
        *,
        year: int|None=None,
        month: int|None=None,
        employee_id: int|None=None
        ) -> FreeeResponse:
        """指定した従業員・日付の基本給情報を返します。

        Args:
            year (int | None, optional): 従業員情報を取得したい年. Defaults to None.
            month (int | None, optional): 従業員情報を取得したい月. Defaults to None.
                notice:
                    締日支払日設定が翌月払いの従業員情報の場合は、 指定したmonth + 1の値が検索結果として返します。
                    翌月払いの従業員の2022/01の従業員情報を取得する場合は、year=2021,month=12を指定してください。
            employee_id (int | None, optional): 従業員ID. Defaults to None.

        Returns:
            FreeeResponse: 指定した従業員・日付の基本給情報を返します。
        
        Example:
            {
                "employee_basic_pay_rule": {
                    "id": 0,
                    "company_id": 0,
                    "employee_id": 0,
                    "pay_calc_type": "monthly",
                    "pay_amount": 0
                }
            }
        """
        endpoint_url = f"./employees/{employee_id}/basic_pay_rule"
        query = dict(
            year=year,
            month=month
        )
        return self.api_call(method="GET", endpoint_url=endpoint_url, query=query)


    def get_employee_dependent_rules(
        self,
        *,
        year: int|None=None,
        month: int|None=None,
        employee_id: int|None=None
        ) -> FreeeResponse:
        """指定した従業員・日付の家族情報を返します。

        Args:
            year (int | None, optional): 従業員情報を取得したい年. Defaults to None.
            month (int | None, optional): 従業員情報を取得したい月. Defaults to None.
                notice:
                    締日支払日設定が翌月払いの従業員情報の場合は、 指定したmonth + 1の値が検索結果として返します。
                    翌月払いの従業員の2022/01の従業員情報を取得する場合は、year=2021,month=12を指定してください。
            employee_id (int | None, optional): 従業員ID. Defaults to None.

        Returns:
            FreeeResponse: 指定した従業員・日付の家族情報を返します。
        
        Example:
            {
                "employee_dependent_rules": [
                    {
                        "id": 0,
                        "company_id": 0,
                        "employee_id": 0,
                        "last_name": "string",
                        "first_name": "string",
                        "last_name_kana": "string",
                        "first_name_kana": "string",
                        "gender": "unselected",
                        "relationship": "string",
                        "birth_date": "string",
                        "residence_type": "string",
                        "zipcode1": "string",
                        "zipcode2": "string",
                        "prefecture_code": 4,
                        "address": "string",
                        "address_kana": "string",
                        "base_pension_num": "string",
                        "income": 0,
                        "annual_revenue": 0,
                        "disability_type": "string",
                        "occupation": "string",
                        "annual_remittance_amount": 0,
                        "employment_insurance_receive_status": "unselected",
                        "employment_insurance_receives_from": "string",
                        "phone_type": "unselected",
                        "phone1": "000",
                        "phone2": "0000",
                        "phone3": "0000",
                        "social_insurance_and_tax_dependent": "string",
                        "social_insurance_dependent_acquisition_date": "string",
                        "social_insurance_dependent_acquisition_reason": "",
                        "social_insurance_other_dependent_acquisition_reason": "string",
                        "social_insurance_dependent_disqualification_date": "string",
                        "social_insurance_dependent_disqualification_reason": "",
                        "social_insurance_other_dependent_disqualification_reason": "string",
                        "tax_dependent_acquisition_date": "string",
                        "tax_dependent_acquisition_reason": "",
                        "tax_other_dependent_acquisition_reason": "string",
                        "tax_dependent_disqualification_date": "string",
                        "tax_dependent_disqualification_reason": "",
                        "tax_other_dependent_disqualification_reason": "string",
                        "non_resident_dependents_reason": "none"
                    }
                ]
            }
        """
        endpoint_url = f"./employees/{employee_id}/dependent_rules"
        query = dict(
            year=year,
            month=month
        )
        return self.api_call(method="GET", endpoint_url=endpoint_url, query=query)


    def get_employee_group_memberships(
        self,
        with_no_payroll_calculation: bool|None=False,
        employee_ids: str|None=None,
        limit: int|None=50,
        offset: int|None=0,
        *,
        base_date: str|None=None
        ) -> FreeeResponse:
        """指定した事業所の指定日付時点における所属情報をリストで返します。

        Args:
            with_no_payroll_calculation (bool | None, optional): trueを指定すると給与計算対象外の従業員情報をレスポンスに含めます。. Defaults to None.
            employee_ids (str | None, optional): 取得対象とする従業員IDを指定することができます。指定しない場合は全従業員が対象となります。(例:1,2,3,4,5). Defaults to None.
            limit (int | None, optional): 取得レコードの件数 (デフォルト: 50, 最小: 1, 最大: 100). Defaults to None.
            offset (int | None, optional): 取得レコードのオフセット (デフォルト: 0). Defaults to None.
            base_date (str | None, optional): 指定日。指定日付時点における所属情報をリストで返します。(YYYY-MM-DD). Defaults to None.

        Returns:
            FreeeResponse: 指定した事業所の指定日付時点における所属情報をリストで返します。
        
        Example:
            {
                "employee_group_memberships": [
                    {
                        "id": 1,
                        "num": "A-001",
                        "display_name": "山田 太郎",
                        "entry_date": "2021-04-01",
                        "retire_date": "2022-03-31",
                        "user_id": 1,
                        "login_email": "example@example.com",
                        "birth_date": "2000-01-01",
                        "gender": "male",
                        "payroll_calculation": true,
                        "group_memberships": [
                            {
                            "start_date": "2000-01-01",
                            "end_date": "2020-01-01",
                            "group_id": 10,
                            "group_code": "group2",
                            "group_name": "営業部",
                            "level": 2,
                            "position_id": 1,
                            "position_code": "position1",
                            "position_name": "部長",
                            "parent_group_id": 1,
                            "parent_group_code": "group1",
                            "parent_group_name": "営業統括"
                            }
                        ]
                    }
                ],
                "total_count": 1
            }
        """
        endpoint_url = f"./employee_group_memberships"
        query = dict(
            base_date=base_date,
            with_no_payroll_calculation=with_no_payroll_calculation,
            employee_ids=employee_ids,
            limit=limit,
            offset=offset
        )
        return self.api_call(method="GET", endpoint_url=endpoint_url, query=query)


    def get_employee_health_insurance_rule(
        self,
        *,
        year: int|None=None,
        month: int|None=None,
        employee_id: int|None=None
        ) -> FreeeResponse:
        """指定した従業員・日付の健康保険情報を返します。

        Args:
            year (int | None, optional): 従業員情報を取得したい年. Defaults to None.
            month (int | None, optional): 従業員情報を取得したい月. Defaults to None.
                notice:
                    締日支払日設定が翌月払いの従業員情報の場合は、 指定したmonth + 1の値が検索結果として返します。
                    翌月払いの従業員の2022/01の従業員情報を取得する場合は、year=2021,month=12を指定してください。
            employee_id (int | None, optional): 従業員ID. Defaults to None.

        Returns:
            FreeeResponse: 指定した従業員・日付の健康保険情報を返します。
        
        Example:
            {
                "employee_health_insurance_rule": {
                    "id": 0,
                    "company_id": 0,
                    "employee_id": 0,
                    "entried": true,
                    "health_insurance_salary_calc_type": "manual",
                    "health_insurance_bonus_calc_type": "manual",
                    "manual_health_insurance_amount_of_employee_salary": 8888,
                    "manual_health_insurance_amount_of_employee_bonus": 7777,
                    "manual_health_insurance_amount_of_company_salary": 6666.0001,
                    "manual_health_insurance_amount_of_company_bonus": 5555.0001,
                    "care_insurance_salary_calc_type": "manual",
                    "care_insurance_bonus_calc_type": "manual",
                    "manual_care_insurance_amount_of_employee_salary": 4444,
                    "manual_care_insurance_amount_of_employee_bonus": 3333,
                    "manual_care_insurance_amount_of_company_salary": 2222.0001,
                    "manual_care_insurance_amount_of_company_bonus": 1111.0001,
                    "reference_num": "string",
                    "standard_monthly_remuneration": 0
                }
            }
        """
        endpoint_url = f"./employees/{employee_id}/health_insurance_rule"
        query = dict(
            year=year,
            month=month
        )
        return self.api_call(method="GET", endpoint_url=endpoint_url, query=query)


    def get_employee_profile_custom_fields_rule(
        self,
        *,
        year: int|None=None,
        month: int|None=None,
        employee_id: int|None=None
        ) -> FreeeResponse:
        """指定した従業員・日付のカスタム項目情報を返します。

        Args:
            year (int | None, optional): 従業員情報を取得したい年. Defaults to None.
            month (int | None, optional): 従業員情報を取得したい月. Defaults to None.
                notice:
                    締日支払日設定が翌月払いの従業員情報の場合は、 指定したmonth + 1の値が検索結果として返します。
                    翌月払いの従業員の2022/01の従業員情報を取得する場合は、year=2021,month=12を指定してください。
            employee_id (int | None, optional): 従業員ID. Defaults to None.

        Returns:
            FreeeResponse: 指定した従業員・日付のカスタム項目情報を返します。
        
        Example:
            {
                "profile_custom_field_groups": [
                    {
                        "id": 1,
                        "name": "資格取得結果",
                        "profile_custom_field_rules": [
                            {
                                "id": 1,
                                "field_type": "file",
                                "name": "証明書ファイル",
                                "value": "null",
                                "file_name": "証明書ファイル.jpeg"
                            }
                        ]
                    }
                ]
            }
        """
        endpoint_url = f"./employees/{employee_id}/profile_custom_fields"
        query = dict(
            year=year,
            month=month,
            employee_id=employee_id
        )
        return self.api_call(method="GET", endpoint_url=endpoint_url, query=query)


    def get_employee_profile_rule(
        self,
        *,
        year: int|None=None,
        month: int|None=None,
        employee_id: int|None=None
        ) -> FreeeResponse:
        """指定した従業員・日付の姓名などの情報を返します。

        Args:
            year (int | None, optional): 従業員情報を取得したい年. Defaults to None.
            month (int | None, optional): 従業員情報を取得したい月. Defaults to None.
                notice:
                    締日支払日設定が翌月払いの従業員情報の場合は、 指定したmonth + 1の値が検索結果として返します。
                    翌月払いの従業員の2022/01の従業員情報を取得する場合は、year=2021,month=12を指定してください。
            employee_id (int | None, optional): 従業員ID. Defaults to None.

        Returns:
            FreeeResponse: 指定した従業員・日付の姓名などの情報を返します。
        
        Example:
            {
                "employee_profile_rule": {
                    "id": 0,
                    "company_id": 0,
                    "employee_id": 0,
                    "last_name": "string",
                    "first_name": "string",
                    "last_name_kana": "string",
                    "first_name_kana": "string",
                    "zipcode1": "000",
                    "zipcode2": "0000",
                    "prefecture_code": 4,
                    "address": "string",
                    "address_kana": "string",
                    "phone1": "000",
                    "phone2": "0000",
                    "phone3": "0000",
                    "residential_zipcode1": "000",
                    "residential_zipcode2": "0000",
                    "residential_prefecture_code": 4,
                    "residential_address": "string",
                    "residential_address_kana": "string",
                    "employment_type": "string",
                    "title": "string",
                    "gender": "male",
                    "married": true,
                    "is_working_student": true,
                    "widow_type": "string",
                    "disability_type": "string",
                    "email": "test@example.com",
                    "householder_name": "山田 吾郎",
                    "householder": "father"
                }
            }
        """
        endpoint_url = f"./employees/{employee_id}/profile_rule"
        query = dict(
            year=year,
            month=month
        )
        return self.api_call(method="GET", endpoint_url=endpoint_url, query=query)


    def get_employee_time_clock(
        self,
        *,
        employee_id: int|None=None,
        id: int|None=None
        ) -> FreeeResponse:
        """指定した従業員・指定した打刻の詳細情報を返します。

        Args:
            employee_id (int | None, optional): 従業員ID. Defaults to None.
            id (int | None, optional): 打刻ID. Defaults to None.

        Returns:
            FreeeResponse: 指定した従業員・指定した打刻の詳細情報を返します。
        
        Example:
            {
                "employee_time_clock": {
                    "id": 0,
                    "date": "string",
                    "type": "clock_in",
                    "datetime": "2024-03-11T02:59:43.723Z",
                    "original_datetime": "2024-03-11T02:59:43.723Z",
                    "note": "string"
                }
            }
        """
        endpoint_url = f"./employees/{employee_id}/time_clocks/{id}"
        return self.api_call(method="GET", endpoint_url=endpoint_url)


    def get_employee_time_clocks(
        self,
        from_date: str|None=None,
        to_date: str|None=None,
        limit: int|None=50,
        offset: int|None=0,
        *,
        employee_id: int|None=None
        ) -> FreeeResponse:
        """指定した従業員・期間の打刻情報を返します。

        Args:
            from_date (str | None, optional): 取得する打刻期間の開始日(YYYY-MM-DD)(デフォルト: 当月の打刻開始日). Defaults to None.
            to_date (str | None, optional): 取得する打刻期間の終了日(YYYY-MM-DD)(デフォルト: 当日). Defaults to None.
            limit (int | None, optional): 取得レコードの件数 (デフォルト: 50, 最小: 1, 最大: 100). Defaults to None.
            offset (int | None, optional): 取得レコードのオフセット (デフォルト: 0). Defaults to None.
            employee_id (int | None, optional): 従業員ID. Defaults to None.

        Returns:
            FreeeResponse: 指定した従業員・期間の打刻情報を返します。
        
        Example:
            [
                {
                    "id": 0,
                    "date": "string",
                    "type": "clock_in",
                    "datetime": "2024-03-11T03:00:51.597Z",
                    "original_datetime": "2024-03-11T03:00:51.597Z",
                    "note": "string"
                }
            ]
        """
        endpoint_url = f"./employees/{employee_id}/time_clocks"
        query = dict(
            from_date=from_date,
            to_date=to_date,
            limit=limit,
            offset=offset
        )
        return self.api_call(method="GET", endpoint_url=endpoint_url, query=query)


    def get_employee_time_clocks_available_types(
        self,
        date: str|None=None,
        *,
        employee_id: int|None=None
        ) -> FreeeResponse:
        """指定した従業員・日付の打刻可能種別と打刻基準日を返します。

        例: すでに出勤した状態だと、休憩開始、退勤が配列で返ります。

        Args:
            date (str | None, optional): 従業員情報を取得したい年月日(YYYY-MM-DD)(例:2018-08-01)(デフォルト：当日). Defaults to None.
            employee_id (int | None, optional): 従業員ID. Defaults to None.

        Returns:
            FreeeResponse: 指定した従業員・日付の打刻可能種別と打刻基準日を返します。
        
        Example:
            {
                "available_types": [
                    "clock_in"
                ],
                "base_date": "2018-07-31"
            }
        """
        endpoint_url = f"./employees/{employee_id}/time_clocks/available_types"
        query = dict(
            date=date
        )
        return self.api_call(method="GET", endpoint_url=endpoint_url, query=query)


    def get_employee_welfare_pension_insurance_rule(
        self,
        *,
        year: int|None=None,
        month: int|None=None,
        employee_id: int|None=None
        ) -> FreeeResponse:
        """指定した従業員・日付の厚生年金保険情報を返します。

        Args:
            year (int | None, optional): 従業員情報を取得したい年. Defaults to None.
            month (int | None, optional): 従業員情報を取得したい月. Defaults to None.
                notice:
                    締日支払日設定が翌月払いの従業員情報の場合は、 指定したmonth + 1の値が検索結果として返します。
                    翌月払いの従業員の2022/01の従業員情報を取得する場合は、year=2021,month=12を指定してください。
            employee_id (int | None, optional): 従業員ID. Defaults to None.

        Returns:
            FreeeResponse: 指定した従業員・日付の厚生年金保険情報を返します。
        
        Example:
            {
                "employee_welfare_pension_insurance_rule": {
                    "id": 0,
                    "child_allowance_contribution_bonus_calc_type": "manual",
                    "child_allowance_contribution_salary_calc_type": "manual",
                    "company_id": 0,
                    "employee_id": 0,
                    "entried": true,
                    "manual_child_allowance_contribution_amount_bonus": 111.0001,
                    "manual_child_allowance_contribution_amount_salary": 222.0001,
                    "manual_welfare_pension_insurance_amount_of_company_bonus": 333.0001,
                    "manual_welfare_pension_insurance_amount_of_company_salary": 444.0001,
                    "manual_welfare_pension_insurance_amount_of_employee_bonus": 555,
                    "manual_welfare_pension_insurance_amount_of_employee_salary": 666,
                    "reference_num": "string",
                    "standard_monthly_remuneration": 0,
                    "welfare_pension_insurance_bonus_calc_type": "manual",
                    "welfare_pension_insurance_salary_calc_type": "manual"
                }
            }
        """
        endpoint_url = f"./employees/{employee_id}/welfare_pension_insurance_rule"
        query = dict(
            year=year,
            month=month
        )
        return self.api_call(method="GET", endpoint_url=endpoint_url, query=query)


    def get_employee_work_record(
        self,
        *,
        employee_id: int|None=None,
        date: str|None=None
        ) -> FreeeResponse:
        """指定した従業員・日付の勤怠情報を返します。

        Args:
            employee_id (int | None, optional): 従業員ID. Defaults to None.
            date (str | None, optional): 従業員情報を取得したい年月日(YYYY-MM-DD). Defaults to None.

        Returns:
            FreeeResponse: 指定した従業員・日付の勤怠情報を返します。
        
        Example:
            {
                "break_records": [
                    {
                    "clock_in_at": "2024-03-11T03:08:12.200Z",
                    "clock_out_at": "2024-03-11T03:08:12.200Z"
                    }
                ],
                "clock_in_at": "2024-03-11T03:08:12.200Z",
                "clock_out_at": "2024-03-11T03:08:12.200Z",
                "date": "2024-03-11T03:08:12.200Z",
                "day_pattern": "normal_day",
                "schedule_pattern": "",
                "early_leaving_mins": 0,
                "half_paid_holiday_mins": 0,
                "half_special_holiday_mins": 0,
                "hourly_paid_holiday_mins": 0,
                "hourly_special_holiday_mins": 0,
                "is_absence": false,
                "is_editable": true,
                "lateness_mins": 0,
                "normal_work_clock_in_at": "2024-03-11T03:08:12.200Z",
                "normal_work_clock_out_at": "2024-03-11T03:08:12.200Z",
                "normal_work_mins": 0,
                "note": "string",
                "paid_holiday": 0,
                "special_holiday": 0,
                "special_holiday_setting_id": 0,
                "use_attendance_deduction": true,
                "use_default_work_pattern": true,
                "use_half_compensatory_holiday": false,
                "total_overtime_work_mins": 0,
                "total_holiday_work_mins": 0,
                "total_latenight_work_mins": 0,
                "not_auto_calc_work_time": false,
                "total_excess_statutory_work_mins": 0,
                "total_latenight_excess_statutory_work_mins": 0,
                "total_overtime_except_normal_work_mins": 0,
                "total_latenight_overtime_except_normal_work_min": 0
            }
        """
        endpoint_url = f"./employees/{employee_id}/work_records/{date}"
        return self.api_call(method="GET", endpoint_url=endpoint_url)


    def get_employee_work_record_summary(
        self,
        work_records: bool|None=None,
        *,
        employee_id: int|None=None,
        year: int|None=None,
        month: int|None=None
        ) -> FreeeResponse:
        """指定した従業員、月の勤怠情報のサマリを返します。

        Args:
            work_records (bool | None, optional): サマリ情報に日次の勤怠情報を含める. Defaults to None.
            employee_id (int | None, optional): 従業員ID. Defaults to None.
            year (int | None, optional): 従業員情報を取得したい年. Defaults to None.
            month (int | None, optional): 従業員情報を取得したい月. Defaults to None.

        Returns:
            FreeeResponse: 指定した従業員、月の勤怠情報のサマリを返します。
        
        Example:
            {
                "year": 0,
                "month": 0,
                "start_date": "string",
                "end_date": "string",
                "work_days": 0,
                "total_work_mins": 0,
                "total_normal_work_mins": 0,
                "total_excess_statutory_work_mins": 0,
                "total_overtime_except_normal_work_mins": 0,
                "total_overtime_within_normal_work_mins": 0,
                "total_holiday_work_mins": 0,
                "total_latenight_work_mins": 0,
                "num_absences": 0,
                "num_paid_holidays": 0,
                "num_paid_holidays_and_hours": {
                    "days": 0,
                    "hours": 0
                },
                "num_paid_holidays_left": 0,
                "num_paid_holidays_and_hours_left": {
                    "days": 0,
                    "hours": 0
                },
                "num_substitute_holidays_used": 0,
                "num_compensatory_holidays_used": 0,
                "num_special_holidays_used": 0,
                "num_special_holidays_and_hours_used": {
                    "days": 0,
                    "hours": 0
                },
                "total_lateness_and_early_leaving_mins": 0,
                "multi_hourly_wages": [
                    {
                    "name": "string",
                    "total_normal_time_mins": 0
                    }
                ],
                "work_records": [
                    {
                        "break_records": [
                            {
                            "clock_in_at": "2024-03-11T03:09:02.078Z",
                            "clock_out_at": "2024-03-11T03:09:02.078Z"
                            }
                        ],
                        "clock_in_at": "2024-03-11T03:09:02.078Z",
                        "clock_out_at": "2024-03-11T03:09:02.078Z",
                        "date": "2024-03-11T03:09:02.078Z",
                        "day_pattern": "normal_day",
                        "schedule_pattern": "",
                        "early_leaving_mins": 0,
                        "half_paid_holiday_mins": 0,
                        "half_special_holiday_mins": 0,
                        "hourly_paid_holiday_mins": 0,
                        "hourly_special_holiday_mins": 0,
                        "is_absence": false,
                        "is_editable": true,
                        "lateness_mins": 0,
                        "normal_work_clock_in_at": "2024-03-11T03:09:02.078Z",
                        "normal_work_clock_out_at": "2024-03-11T03:09:02.078Z",
                        "normal_work_mins": 0,
                        "note": "string",
                        "paid_holiday": 0,
                        "special_holiday": 0,
                        "special_holiday_setting_id": 0,
                        "use_attendance_deduction": true,
                        "use_default_work_pattern": true,
                        "use_half_compensatory_holiday": false,
                        "total_overtime_work_mins": 0,
                        "total_holiday_work_mins": 0,
                        "total_latenight_work_mins": 0,
                        "not_auto_calc_work_time": false,
                        "total_excess_statutory_work_mins": 0,
                        "total_latenight_excess_statutory_work_mins": 0,
                        "total_overtime_except_normal_work_mins": 0,
                        "total_latenight_overtime_except_normal_work_min": 0
                    }
                ],
                "total_shortage_work_mins": 0,
                "total_deemed_paid_excess_statutory_work_mins": 0,
                "total_deemed_paid_overtime_except_normal_work_mins": 0
            }
        """
        endpoint_url = f"./employees/{employee_id}/work_record_summaries/{year}/{month}"
        query = dict(
            work_records=work_records,
        )
        return self.api_call(method="GET", endpoint_url=endpoint_url, query=query)


    def get_groups(self) -> FreeeResponse:
        """指定した事業所の指定日付時点における部門情報をリストで返します。
        
        部門APIの使い方については、[部門APIを利用した組織図の取得について](https://developer.freee.co.jp/tips/groups-api-hierarchy) をご参照ください。

        Returns:
            FreeeResponse: 指定した事業所の指定日付時点における部門情報をリストで返します。
        
        Example:
            {
                "groups": [
                    {
                        "id": 3,
                        "code": "group2",
                        "name": "営業部門",
                        "level": 2,
                        "parent_group_id": 2,
                        "parent_group_code": "group1",
                        "parent_group_name": "営業統括"
                    }
                ],
                "total_count": 1
            }
        """
        endpoint_url = f"./groups"
        return self.api_call(method="GET", endpoint_url=endpoint_url)


    def get_positions(self) -> FreeeResponse:
        """指定した事業所の指定日付時点における役職情報をリストで返します。

        Returns:
            FreeeResponse: 指定した事業所の指定日付時点における役職情報をリストで返します。
        
        Example:
            {
                "positions": [
                    {
                        "id": 1,
                        "code": "position1",
                        "name": "部長"
                    }
                ],
                "total_count": 1
            }
        """
        endpoint_url = f"./positions"
        return self.api_call(method="GET", endpoint_url=endpoint_url)


    def get_salaries_employee_payroll_statement(
        self,
        *,
        year: int|None=None,
        month: int|None=None,
        employee_id: int|None=None
        ) -> FreeeResponse:
        """指定した従業員ID、年月の給与明細を返します。

        指定した年月に支払いのある給与明細が返されます。

        Args:
            year (int | None, optional): 従業員情報を取得したい年. Defaults to None.
            month (int | None, optional): 従業員情報を取得したい月. Defaults to None.
            employee_id (int | None, optional): 従業員ID. Defaults to None.

        Returns:
            FreeeResponse: 指定した従業員ID、年月の給与明細を返します。
        
        Example:
            {
                "employee_payroll_statement": {
                    "id": 0,
                    "company_id": 0,
                    "employee_id": 0,
                    "employee_name": "string",
                    "employee_display_name": "string",
                    "employee_num": "string",
                    "pay_date": "string",
                    "start_date": "string",
                    "closing_date": "string",
                    "variable_pay_start_date": "string",
                    "variable_pay_closing_date": "string",
                    "fixed": true,
                    "calc_status": "string",
                    "calculated_at": "2024-03-11T03:13:45.296Z",
                    "pay_calc_type": "monthly",
                    "board_member_remuneration_amount": "string",
                    "basic_pay_amount": "string",
                    "work_days": "string",
                    "normal_work_time": "string",
                    "normal_work_days": "string",
                    "work_mins_by_paid_holiday": "string",
                    "num_paid_holidays": "string",
                    "is_board_member": true,
                    "total_attendance_deduction_amount": "string",
                    "total_allowance_amount": "string",
                    "total_deduction_amount": "string",
                    "net_payment_amount": "string",
                    "gross_payment_amount": "string",
                    "total_worked_days_count": "string",
                    "total_taxable_payment_amount": "string",
                    "total_expense_amount": "string",
                    "total_transfer_amount": "string",
                    "total_annual_payment_amount": "string",
                    "payments": [
                        {
                            "name": "string",
                            "amount": "string"
                        }
                    ],
                    "deductions": [
                        {
                            "name": "string",
                            "amount": "string"
                        }
                    ],
                    "attendances": [
                        {
                            "name": "string",
                            "time": "string",
                            "amount": "string"
                        }
                    ],
                    "overtime_pays": [
                        {
                            "name": "時間外労働",
                            "time": "60.0",
                            "amount": "1000.0",
                            "code": "12345abcde"
                        }
                    ],
                    "remark": "string"
                }
            }
        """
        endpoint_url = f"./salaries/employee_payroll_statements/{employee_id}"
        query = dict(
            year=year,
            month=month
        )
        return self.api_call(method="GET", endpoint_url=endpoint_url, query=query)


    def get_salaries_employee_payroll_statements(
        self,
        limit: int|None=50,
        offset: int|None=0,
        *,
        year: int|None=None,
        month: int|None=None
        ) -> FreeeResponse:
        """指定した事業所に所属する従業員の給与明細をリストで返します。

        指定した年月に支払いのある給与明細が返されます。

        Args:
            limit (int | None, optional): 取得レコードの件数 (デフォルト: 50, 最小: 1, 最大: 100). Defaults to None.
            offset (int | None, optional): 取得レコードのオフセット (デフォルト: 0). Defaults to None.
            year (int | None, optional): 従業員情報を取得したい年. Defaults to None.
            month (int | None, optional): 従業員情報を取得したい月. Defaults to None.

        Returns:
            FreeeResponse: 指定した事業所に所属する従業員の給与明細をリストで返します。
        
        Example:
            {
                "employee_payroll_statements": [
                    {
                        "id": 0,
                        "company_id": 0,
                        "employee_id": 0,
                        "employee_name": "string",
                        "employee_display_name": "string",
                        "employee_num": "string",
                        "pay_date": "string",
                        "start_date": "string",
                        "closing_date": "string",
                        "variable_pay_start_date": "string",
                        "variable_pay_closing_date": "string",
                        "fixed": true,
                        "calc_status": "string",
                        "calculated_at": "2024-03-11T03:15:50.062Z",
                        "pay_calc_type": "monthly",
                        "board_member_remuneration_amount": "string",
                        "basic_pay_amount": "string",
                        "work_days": "string",
                        "normal_work_time": "string",
                        "normal_work_days": "string",
                        "work_mins_by_paid_holiday": "string",
                        "num_paid_holidays": "string",
                        "is_board_member": true,
                        "total_attendance_deduction_amount": "string",
                        "total_allowance_amount": "string",
                        "total_deduction_amount": "string",
                        "net_payment_amount": "string",
                        "gross_payment_amount": "string",
                        "total_worked_days_count": "string",
                        "total_taxable_payment_amount": "string",
                        "total_expense_amount": "string",
                        "total_transfer_amount": "string",
                        "total_annual_payment_amount": "string",
                        "payments": [
                            {
                            "name": "string",
                            "amount": "string"
                            }
                        ],
                        "deductions": [
                            {
                            "name": "string",
                            "amount": "string"
                            }
                        ],
                        "attendances": [
                            {
                            "name": "string",
                            "time": "string",
                            "amount": "string"
                            }
                        ],
                        "overtime_pays": [
                            {
                            "name": "時間外労働",
                            "time": "60.0",
                            "amount": "1000.0",
                            "code": "12345abcde"
                            }
                        ],
                        "remark": "string"
                        }
                    ],
                    "total_count": 1
                }
        """
        endpoint_url = f"./salaries/employee_payroll_statements"
        query = dict(
            year=year,
            month=month,
            limit=limit,
            offset=offset
        )
        return self.api_call(method="GET", endpoint_url=endpoint_url, query=query)


    def get_yearend_adjustment_employee(
        self,
        *,
        year: int|None=None,
        employee_id: int|None=None
        ) -> FreeeResponse:
        """指定した年、従業員IDの年末調整の詳細内容を返します。
        年末調整対象外の従業員は、本人情報、給与・賞与、前職情報のみが取得できます。

        Args:
            year (int | None, optional): 年末調整を取得したい年. Defaults to None.
            employee_id (int | None, optional): 従業員ID

        Returns:
            FreeeResponse: 指定した年、従業員IDの年末調整の詳細内容を返します。
        
        Example:
            {
                "employee": {
                    "employee_id": 0,
                    "num": "A-001",
                    "last_name": "山田",
                    "first_name": "太郎",
                    "last_name_kana": "ヤマダ",
                    "first_name_kana": "タロウ",
                    "birth_date": "string",
                    "entry_date": "string",
                    "retire_date": "string",
                    "employment_type": "string",
                    "title": "string",
                    "zipcode1": "141",
                    "zipcode2": "0031",
                    "prefecture_code": 12,
                    "address": "品川区大崎1-2-2",
                    "address_kana": "シナガワクオオサキ1-2-2",
                    "payer_type": "kou",
                    "widow_type": "na",
                    "disability_type": "na",
                    "married": true,
                    "is_working_student": true,
                    "is_foreigner": true,
                    "other_company_revenue": 1000000,
                    "all_other_income": 1000000,
                    "householder": "myself",
                    "householder_name": "山田 太郎",
                    "is_calc_income_tax": true
                },
                "dependents": [
                    {
                        "id": 1,
                        "last_name": "山田",
                        "first_name": "花子",
                        "last_name_kana": "ヤマダ",
                        "first_name_kana": "ハナコ",
                        "relationship": "spouse",
                        "birth_date": "1999-01-01",
                        "social_insurance_and_tax_dependent": "social_insurance_and_tax",
                        "income": 0,
                        "employment_revenue": 0,
                        "all_other_income": 0,
                        "disability_type": "na",
                        "residence_type": "live_in",
                        "zipcode1": "141",
                        "zipcode2": "0031",
                        "prefecture_code": 12,
                        "address": "品川区大崎1-2-2",
                        "address_kana": "シナガワクオオサキ1-2-2",
                        "annual_remittance_amount": 0,
                        "non_resident_dependents_reason": "none",
                        "is_resident_tax_only_deduction": true,
                        "retirement_income": 0
                    }
                ],
                "insurances": [
                    {
                        "id": 0,
                        "type": "life_care_pension_insurance",
                        "category": "life",
                        "new_or_old": "new",
                        "company_name": "freee生命保険株式会社",
                        "kind_of_purpose": "利差配当付終身",
                        "period": "終身",
                        "policyholder_last_name": "契約",
                        "policyholder_first_name": "太郎",
                        "recipient_last_name": "受取",
                        "recipient_first_name": "太郎",
                        "recipient_relationship": "child",
                        "payment_start_date": "2000-04-01",
                        "amount": 1000000
                    }
                ],
                "housing_loan_deduction": 500000,
                "housing_loans": [
                    {
                        "id": 1,
                        "residence_start_date": "2022-03-31",
                        "remaining_balance_at_yearend": 5000000,
                        "category": "general",
                        "specific_case_type": "not_qualified"
                    }
                ],
                "payroll_and_bonus": {
                    "fixed_payroll": 10000000,
                    "fixed_payroll_deduction": 1000000,
                    "fixed_payroll_income_tax": 1000000,
                    "fixed_bonus": 10000000,
                    "fixed_bonus_deduction": 1000000,
                    "fixed_bonus_income_tax": 1000000,
                    "unentered_payroll_amount": 500000,
                    "unentered_payroll_deduction_amount": 500000,
                    "unentered_payroll_income_tax_amount": 500000,
                    "unentered_bonus_amount": 500000,
                    "unentered_bonus_deduction_amount": 500000,
                    "unentered_bonus_income_tax_amount": 500000
                },
                "previous_job": {
                    "income": 5000000,
                    "deduction": 1200000,
                    "withholding_tax_amount": 100000,
                    "company_name": "株式会社 前職",
                    "company_address": "品川区大崎1-2-2",
                    "retire_date": "2022-03-31"
                }
            }
        """
        endpoint_url = f"./yearend_adjustments/{year}/employees/{employee_id}"
        query = dict(
            year=year
        )
        return self.api_call(method="GET", endpoint_url=endpoint_url, query=query)


    # POSTメソッド
    def create_employee(
        self,
        employee_num: str|None=None,
        working_hours_system_name: str|None=None,
        company_reference_date_rule_name: str|None=None,
        gender: str|None=None,
        married: bool|None=None,
        no_payroll_calculation: bool|None=None,
        *,
        first_name: str,
        last_name: str,
        first_name_kana: str,
        last_name_kana: str,
        pay_amount: int,
        birth_date: str,
        entry_date: str|None=None,
        pay_calc_type: str="monthly"
        ) -> FreeeResponse:
        """従業員を新規作成します。

        Args:
            first_name (str) -> FreeeResponse: _description_
            last_name (str) -> FreeeResponse: _description_
            first_name_kana (str) -> FreeeResponse: _description_
            last_name_kana (str) -> FreeeResponse: _description_
            pay_amount (int) -> FreeeResponse: _description_
            birth_date (str) -> FreeeResponse: _description_
            employee_num (str | None, optional) -> FreeeResponse: 従業員番号 Defaults to None.
            working_hours_system_name (str | None, optional) -> FreeeResponse: 勤務・賃金設定名 で設定した名称を指定してください。Defaults to None.
            company_reference_date_rule_name (str | None, optional) -> FreeeResponse: 締め日支払い日グループ名 で設定した締め日支払い日を指定してください。\n
            - 未指定の際は、最初に登録したデータが利用されます。
            - 入力パラメータのno_payroll_calculationがtrueの場合に指定するとエラーになります。 Defaults to None.
            gender (str | None, optional) -> FreeeResponse: _description_
            married (bool | None, optional) -> FreeeResponse: _description_
            no_payroll_calculation (bool | None, optional) -> FreeeResponse: _description_
            entry_date (str | None, optional) -> FreeeResponse: _description_
            pay_calc_type (str, optional) -> FreeeResponse: _description_. Defaults to "monthly".

        """
        employee_dict = dict(
            num=employee_num,
            working_hours_system_nqme=working_hours_system_name,
            company_reference_date_rule_name=company_reference_date_rule_name,
            first_name=first_name,
            last_name=last_name,
            first_name_kana=first_name_kana,
            last_name_kana=last_name_kana,
            birth_date=birth_date,
            entry_date=entry_date,
            pay_calc_type=pay_calc_type,
            pay_amount=pay_amount,
            gender=gender,
            married=married,
            no_payroll_calculation=no_payroll_calculation
        )

        request_body = dict(employee=_remove_none_values(employee_dict))
        endpoint_url = f"./employees"
        return self.api_call(method="POST", endpoint_url=endpoint_url, body=request_body)

    def create_employee_time_clock(
        self,
        base_date: str|None=None,
        datetime: str|None=None,
        *,
        employee_id: int,
        type: str
        ) -> FreeeResponse:
        endpoint_url = f"./employees/{employee_id}/time_clocks"
        
        body = dict(
            type=type,
            base_date=base_date,
            datetime=datetime
            )
        return self.api_call(method="POST", endpoint_url=endpoint_url, body=body)


    def create_group(
        self,
        code: str|None=None,
        parent_group_id: int|None=None,
        *,
        name: str
        ) -> FreeeResponse:
        endpoint_url = f"./groups"
        group = dict(
            code=code,
            name=name,
            parent_group_id=parent_group_id
            )
        body = dict(
            group=group
            )
        return self.api_call(method="POST", endpoint_url=endpoint_url, body=body)


    def create_position(
        self,
        code: str|None=None,
        *,
        name: str
        ) -> FreeeResponse:
        endpoint_url = f"./positions"
        position = dict(
        code=code,
            name=name
            )
        body = dict(
            position=position
            )
        return self.api_call(method="POST", endpoint_url=endpoint_url, body=body)


    def create_approval_requests_monthly_attendance(
        self,
        approver_id: int|None=None,
        *,
        target_year: int,
        target_month: int,
        approval_flow_route_id: int
        ) -> FreeeResponse:
        endpoint_url = f"./approval_requests/monthly_attendances"
        
        body = dict(
            target_year=target_year,
            target_month=target_month,
            approval_flow_route_id=approval_flow_route_id,
            approver_id=approver_id
            )
        return self.api_call(method="POST", endpoint_url=endpoint_url, body=body)


    def action_approval_requests_monthly_attendance(
        self,
        next_approver_id: int|None=None,
        *,
        id: int,
        approval_action: str,
        target_round: int,
        target_step_id: int
        ) -> FreeeResponse:
        endpoint_url = f"./approval_requests/monthly_attendances/{id}/actions"
        
        body = dict(
            approval_action=approval_action,
            target_round=target_round,
            target_step_id=target_step_id,
            next_approver_id=next_approver_id
            )
        return self.api_call(method="POST", endpoint_url=endpoint_url, body=body)


    def create_approval_requests_work_time(
        self,
        clear_work_time: bool|None=None,
        clock_in_at: str|None=None,
        clock_out_at: str|None=None,
        lateness_mins: int|None=None,
        early_leaving_mins: int|None=None,
        comment: str|None=None,
        approver_id: int|None=None,
        *,
        target_date: str,
        approval_flow_route_id: int
        ) -> FreeeResponse:
        endpoint_url = f"./approval_requests/work_times"
        break_records = dict(
            clock_in_at=clock_in_at,
            clock_out_at=clock_out_at
            )
        body = dict(
            target_date=target_date,
            clear_work_time=clear_work_time,
            lateness_mins=lateness_mins,
            early_leaving_mins=early_leaving_mins,
            break_records=_remove_none_values(break_records),
            comment=comment,
            approval_flow_route_id=approval_flow_route_id,
            approver_id=approver_id
            )
        return self.api_call(method="POST", endpoint_url=endpoint_url, body=body)


    def action_approval_requests_work_time(
        self,
        next_approver_id: int|None=None,
        *,
        id: int,
        approval_action: str,
        target_round: int,
        target_step_id: int
        ) -> FreeeResponse:
        endpoint_url = f"./approval_requests/work_times/{id}/actions"
        
        body = dict(
            approval_action=approval_action,
            target_round=target_round,
            target_step_id=target_step_id,
            next_approver_id=next_approver_id
            )
        return self.api_call(method="POST", endpoint_url=endpoint_url, body=body)


    def create_approval_requests_paid_holiday(
        self,
        start_at: str|None=None,
        end_at: str|None=None,
        comment: str|None=None,
        approver_id: int|None=None,
        *,
        target_date: str,
        holiday_type: str,
        approval_flow_route_id: int
        ) -> FreeeResponse:
        endpoint_url = f"./approval_requests/paid_holidays"
        
        body = dict(
            target_date=target_date,
            holiday_type=holiday_type,
            start_at=start_at,
            end_at=end_at,
            comment=comment,
            approval_flow_route_id=approval_flow_route_id,
            approver_id=approver_id
            )
        return self.api_call(method="POST", endpoint_url=endpoint_url, body=body)


    def action_approval_requests_paid_holiday(
        self,
        next_approver_id: int|None=None,
        *,
        id: int,
        approval_action: str,
        target_round: int,
        target_step_id: int
        ) -> FreeeResponse:
        endpoint_url = f"./approval_requests/paid_holidays/{id}/actions"
        
        body = dict(
            approval_action=approval_action,
            target_round=target_round,
            target_step_id=target_step_id,
            next_approver_id=next_approver_id
            )
        return self.api_call(method="POST", endpoint_url=endpoint_url, body=body)


    def create_approval_requests_special_holiday(
        self,
        start_at: str|None=None,
        end_at: str|None=None,
        comment: str|None=None,
        approver_id: int|None=None,
        *,
        target_date: str,
        special_holiday_setting_id: int,
        holiday_type: str,
        approval_flow_route_id: int
        ) -> FreeeResponse:
        endpoint_url = f"./approval_requests/special_holidays"
        
        body = dict(
            target_date=target_date,
            special_holiday_setting_id=special_holiday_setting_id,
            holiday_type=holiday_type,
            start_at=start_at,
            end_at=end_at,
            comment=comment,
            approval_flow_route_id=approval_flow_route_id,
            approver_id=approver_id
            )
        return self.api_call(method="POST", endpoint_url=endpoint_url, body=body)


    def action_approval_requests_special_holiday(
        self,
        next_approver_id: int|None=None,
        *,
        id: int,
        approval_action: str,
        target_round: int,
        target_step_id: int
        ) -> FreeeResponse:
        endpoint_url = f"./approval_requests/special_holidays/{id}/actions"
        
        body = dict(
            approval_action=approval_action,
            target_round=target_round,
            target_step_id=target_step_id,
            next_approver_id=next_approver_id
            )
        return self.api_call(method="POST", endpoint_url=endpoint_url, body=body)


    def create_approval_requests_overtime_work(
        self,
        comment: str|None=None,
        approver_id: int|None=None,
        *,
        target_date: str,
        start_at: str,
        end_at: str,
        approval_flow_route_id: int
        ) -> FreeeResponse:
        endpoint_url = f"./approval_requests/overtime_works"
        
        body = dict(
            target_date=target_date,
            start_at=start_at,
            end_at=end_at,
            comment=comment,
            approval_flow_route_id=approval_flow_route_id,
            approver_id=approver_id
            )
        return self.api_call(method="POST", endpoint_url=endpoint_url, body=body)


    def action_approval_requests_overtime_work(
        self,
        next_approver_id: int|None=None,
        *,
        id: int,
        approval_action: str,
        target_round: int,
        target_step_id: int
        ) -> FreeeResponse:
        endpoint_url = f"./approval_requests/overtime_works/{id}/actions"
        
        body = dict(
            approval_action=approval_action,
            target_round=target_round,
            target_step_id=target_step_id,
            next_approver_id=next_approver_id
            )
        return self.api_call(method="POST", endpoint_url=endpoint_url, body=body)


    def post_yearend_adjustment_insurances(
        self,
        company_name: str|None=None,
        kind_of_purpose: str|None=None,
        period: str|None=None,
        policyholder_last_name: str|None=None,
        policyholder_first_name: str|None=None,
        recipient_last_name: str|None=None,
        recipient_first_name: str|None=None,
        recipient_relationship: str|None=None,
        payment_start_date: str|None=None,
        *,
        year: int,
        employee_id: int,
        type: str,
        category: str,
        new_or_old: str,
        amount: int
        ) -> FreeeResponse:
        endpoint_url = f"./yearend_adjustments/{year}/insurances/{employee_id}"
        insurance = dict(
            type=type,
            category=category,
            new_or_old=new_or_old,
            company_name=company_name,
            kind_of_purpose=kind_of_purpose,
            period=period,
            policyholder_last_name=policyholder_last_name,
            policyholder_first_name=policyholder_first_name,
            recipient_last_name=recipient_last_name,
            recipient_first_name=recipient_first_name,
            recipient_relationship=recipient_relationship,
            payment_start_date=payment_start_date,
            amount=amount
            )
        body = dict(
            insurance=insurance
            )
        return self.api_call(method="POST", endpoint_url=endpoint_url, body=body)


    def post_yearend_adjustment_housing_loan(
        self,
        *,
        year: int,
        employee_id: int,
        residence_start_date: str,
        remaining_balance_at_yearend: int,
        category: str,
        specific_case_type: str
        ) -> FreeeResponse:
        endpoint_url = f"./yearend_adjustments/{year}/housing_loans/{employee_id}"
        housing_loan = dict(
            residence_start_date=residence_start_date,
            remaining_balance_at_yearend=remaining_balance_at_yearend,
            category=category,
            specific_case_type=specific_case_type
            )
        body = dict(
            housing_loan=housing_loan
            )
        return self.api_call(method="POST", endpoint_url=endpoint_url, body=body)


    def get_yearend_adjustment_employees(
        self,
        limit: int|None=50,
        offset: int|None=0,
        *,
        year: int|None=None
        ) -> FreeeResponse:
        endpoint_url = f"./yearend_adjustments/{year}/employees"
        query = dict(
            year=year,
            limit=limit,
            offset=offset
        )
        return self.api_call(method="GET", endpoint_url=endpoint_url, query=query)


    # PUTメソッド
    def update_employee(
        self,
        year: int|None=None,
        month: int|None=None,
        num: str|None=None,
        display_name: str|None=None,
        base_pension_num: str|None=None,
        employment_insurance_reference_number: str|None=None,
        retire_date: str|None=None,
        company_reference_date_rule_name: str|None=None,
        *,
        id: int,
        birth_date: str,
        entry_date: str
        ) -> FreeeResponse:
        endpoint_url = f"/api/v1/employees/{id}"
        employee = dict(
            num=num,
            display_name=display_name,
            base_pension_num=base_pension_num,
            employment_insurance_reference_number=employment_insurance_reference_number,
            birth_date=birth_date,
            entry_date=entry_date,
            retire_date=retire_date,
            company_reference_date_rule_name=company_reference_date_rule_name
            )
        body = dict(
            year=year,
            month=month,
            employee=employee
            )
        return self.api_call(method="PUT", endpoint_url=endpoint_url, body=body)


    def update_employee_profile_rule(
        self,
        zipcode1: str|None=None,
        zipcode2: str|None=None,
        prefecture_code: int|None=None,
        address: str|None=None,
        address_kana: str|None=None,
        phone1: str|None=None,
        phone2: str|None=None,
        phone3: str|None=None,
        residential_zipcode1: str|None=None,
        residential_zipcode2: str|None=None,
        residential_prefecture_code: int|None=None,
        residential_address: str|None=None,
        residential_address_kana: str|None=None,
        employment_type: str|None=None,
        title: str|None=None,
        gender: str|None=None,
        married: bool|None=None,
        is_working_student: bool|None=None,
        widow_type: str|None=None,
        disability_type: str|None=None,
        email: str|None=None,
        householder_name: str|None=None,
        householder: str|None=None,
        *,
        employee_id: int,
        year: int,
        month: int,
        last_name: str,
        first_name: str,
        last_name_kana: str,
        first_name_kana: str
        ) -> FreeeResponse:
        endpoint_url = f"/api/v1/employees/{employee_id}/profile_rule"
        employee_profile_rule = dict(
            last_name=last_name,
            first_name=first_name,
            last_name_kana=last_name_kana,
            first_name_kana=first_name_kana,
            zipcode1=zipcode1,
            zipcode2=zipcode2,
            prefecture_code=prefecture_code,
            address=address,
            address_kana=address_kana,
            phone1=phone1,
            phone2=phone2,
            phone3=phone3,
            residential_zipcode1=residential_zipcode1,
            residential_zipcode2=residential_zipcode2,
            residential_prefecture_code=residential_prefecture_code,
            residential_address=residential_address,
            residential_address_kana=residential_address_kana,
            employment_type=employment_type,
            title=title,
            gender=gender,
            married=married,
            is_working_student=is_working_student,
            widow_type=widow_type,
            disability_type=disability_type,
            email=email,
            householder_name=householder_name,
            householder=householder
            )
        body = dict(
            year=year,
            month=month,
            employee_profile_rule=employee_profile_rule
            )
        return self.api_call(method="PUT", endpoint_url=endpoint_url, body=body)


    def update_employee_health_insurance_rule(
        self,
        entried: bool|None=None,
        health_insurance_salary_calc_type: str|None=None,
        health_insurance_bonus_calc_type: str|None=None,
        manual_health_insurance_amount_of_employee_salary: int|None=None,
        manual_health_insurance_amount_of_employee_bonus: int|None=None,
        manual_health_insurance_amount_of_company_salary: int|None=None,
        manual_health_insurance_amount_of_company_bonus: int|None=None,
        care_insurance_salary_calc_type: str|None=None,
        care_insurance_bonus_calc_type: str|None=None,
        manual_care_insurance_amount_of_employee_salary: int|None=None,
        manual_care_insurance_amount_of_employee_bonus: int|None=None,
        manual_care_insurance_amount_of_company_salary: int|None=None,
        manual_care_insurance_amount_of_company_bonus: int|None=None,
        reference_num: str|None=None,
        *,
        employee_id: int,
        year: int,
        month: int,
        standard_monthly_remuneration: int
        ) -> FreeeResponse:
        endpoint_url = f"/api/v1/employees/{employee_id}/health_insurance_rule"
        employee_health_insurance_rule = dict(
            entried=entried,
            health_insurance_salary_calc_type=health_insurance_salary_calc_type,
            health_insurance_bonus_calc_type=health_insurance_bonus_calc_type,
            manual_health_insurance_amount_of_employee_salary=manual_health_insurance_amount_of_employee_salary,
            manual_health_insurance_amount_of_employee_bonus=manual_health_insurance_amount_of_employee_bonus,
            manual_health_insurance_amount_of_company_salary=manual_health_insurance_amount_of_company_salary,
            manual_health_insurance_amount_of_company_bonus=manual_health_insurance_amount_of_company_bonus,
            care_insurance_salary_calc_type=care_insurance_salary_calc_type,
            care_insurance_bonus_calc_type=care_insurance_bonus_calc_type,
            manual_care_insurance_amount_of_employee_salary=manual_care_insurance_amount_of_employee_salary,
            manual_care_insurance_amount_of_employee_bonus=manual_care_insurance_amount_of_employee_bonus,
            manual_care_insurance_amount_of_company_salary=manual_care_insurance_amount_of_company_salary,
            manual_care_insurance_amount_of_company_bonus=manual_care_insurance_amount_of_company_bonus,
            reference_num=reference_num,
            standard_monthly_remuneration=standard_monthly_remuneration
            )
        body = dict(
            year=year,
            month=month,
            employee_health_insurance_rule=employee_health_insurance_rule
            )
        return self.api_call(method="PUT", endpoint_url=endpoint_url, body=body)


    def update_employee_welfare_pension_insurance_rule(
        self,
        entried: bool|None=None,
        welfare_pension_insurance_salary_calc_type: str|None=None,
        welfare_pension_insurance_bonus_calc_type: str|None=None,
        manual_welfare_pension_insurance_amount_of_employee_salary: int|None=None,
        manual_welfare_pension_insurance_amount_of_employee_bonus: int|None=None,
        manual_welfare_pension_insurance_amount_of_company_salary: int|None=None,
        manual_welfare_pension_insurance_amount_of_company_bonus: int|None=None,
        child_allowance_contribution_salary_calc_type: str|None=None,
        child_allowance_contribution_bonus_calc_type: str|None=None,
        manual_child_allowance_contribution_amount_salary: int|None=None,
        manual_child_allowance_contribution_amount_bonus: int|None=None,
        reference_num: str|None=None,
        *,
        employee_id: int,
        year: int,
        month: int,
        standard_monthly_remuneration: int
        ) -> FreeeResponse:
        endpoint_url = f"/api/v1/employees/{employee_id}/welfare_pension_insurance_rule"
        employee_welfare_pension_insurance_rule = dict(
            entried=entried,
            welfare_pension_insurance_salary_calc_type=welfare_pension_insurance_salary_calc_type,
            welfare_pension_insurance_bonus_calc_type=welfare_pension_insurance_bonus_calc_type,
            manual_welfare_pension_insurance_amount_of_employee_salary=manual_welfare_pension_insurance_amount_of_employee_salary,
            manual_welfare_pension_insurance_amount_of_employee_bonus=manual_welfare_pension_insurance_amount_of_employee_bonus,
            manual_welfare_pension_insurance_amount_of_company_salary=manual_welfare_pension_insurance_amount_of_company_salary,
            manual_welfare_pension_insurance_amount_of_company_bonus=manual_welfare_pension_insurance_amount_of_company_bonus,
            child_allowance_contribution_salary_calc_type=child_allowance_contribution_salary_calc_type,
            child_allowance_contribution_bonus_calc_type=child_allowance_contribution_bonus_calc_type,
            manual_child_allowance_contribution_amount_salary=manual_child_allowance_contribution_amount_salary,
            manual_child_allowance_contribution_amount_bonus=manual_child_allowance_contribution_amount_bonus,
            reference_num=reference_num,
            standard_monthly_remuneration=standard_monthly_remuneration
            )
        body = dict(
            year=year,
            month=month,
            employee_welfare_pension_insurance_rule=employee_welfare_pension_insurance_rule
            )
        return self.api_call(method="PUT", endpoint_url=endpoint_url, body=body)


    def bulk_update_employee_dependent_rules(
        self,
        *,
        employee_id: int,
        year: int,
        month: int,
        employee_dependent_rules: None
        ) -> FreeeResponse:
        endpoint_url = f"/api/v1/employees/{employee_id}/dependent_rules/bulk_update"
        
        body = dict(
            year=year,
            month=month,
            employee_dependent_rules=employee_dependent_rules
            )
        return self.api_call(method="PUT", endpoint_url=endpoint_url, body=body)


    def update_employee_bank_account_rule(
        self,
        bank_name: str|None=None,
        bank_name_kana: str|None=None,
        bank_code: str|None=None,
        branch_name: str|None=None,
        branch_name_kana: str|None=None,
        branch_code: str|None=None,
        account_number: str|None=None,
        account_name: str|None=None,
        account_type: str|None=None,
        *,
        employee_id: int,
        year: int,
        month: int
        ) -> FreeeResponse:
        endpoint_url = f"/api/v1/employees/{employee_id}/bank_account_rule"
        employee_bank_account_rule = dict(
            bank_name=bank_name,
            bank_name_kana=bank_name_kana,
            bank_code=bank_code,
            branch_name=branch_name,
            branch_name_kana=branch_name_kana,
            branch_code=branch_code,
            account_number=account_number,
            account_name=account_name,
            account_type=account_type
            )
        body = dict(
            year=year,
            month=month,
            employee_bank_account_rule=employee_bank_account_rule
            )
        return self.api_call(method="PUT", endpoint_url=endpoint_url, body=body)


    def update_employee_basic_pay_rule(
        self,
        *,
        employee_id: int,
        year: int,
        month: int,
        pay_calc_type: str,
        pay_amount: int
        ) -> FreeeResponse:
        endpoint_url = f"/api/v1/employees/{employee_id}/basic_pay_rule"
        employee_basic_pay_rule = dict(
            pay_calc_type=pay_calc_type,
            pay_amount=pay_amount
            )
        body = dict(
            year=year,
            month=month,
            employee_basic_pay_rule=employee_basic_pay_rule
            )
        return self.api_call(method="PUT", endpoint_url=endpoint_url, body=body)


    def update_employee_work_record(
        self,
        break_clock_in_at: str|None=None,
        break_clock_out_at: str|None=None,
        work_clock_in_at: str|None=None,
        work_clock_out_at: str|None=None,
        day_pattern: str|None=None,
        early_leaving_mins: int|None=None,
        is_absence: bool|None=None,
        lateness_mins: int|None=None,
        normal_work_clock_in_at: str|None=None,
        normal_work_clock_out_at: str|None=None,
        normal_work_mins: int|None=None,
        note: str|None=None,
        paid_holiday: bool|None=None,
        half_paid_holiday_mins: int|None=None,
        hourly_paid_holiday_mins: int|None=None,
        special_holiday: bool|None=None,
        special_holiday_setting_id: int|None=None,
        half_special_holiday_mins: int|None=None,
        hourly_special_holiday_mins: int|None=None,
        use_attendance_deduction: bool|None=None,
        use_default_work_pattern: bool|None=None,
        *,
        employee_id: int,
        date: int
        ) -> FreeeResponse:
        """
        勤怠の更新\n
        Args:
            employee_id (int) -> FreeeResponse: 従業員ID
            
            date (int) -> FreeeResponse: 更新対象年月日(YYYY-MM-DD)
            
            clock_in_at (str, optional) -> FreeeResponse: 開始時刻
            
            clock_out_at (str, optional) -> FreeeResponse: 終了時刻
            
            day_pattern (WorkRecords.DayPttern, optional) -> FreeeResponse: 勤務パターン
                prescribed_holiday、legal_holidayを指定すると、以下のパラメータについて、指定した値が反映されず無視されます。
                    - early_leaving_mins
                    - lateness_mins
                    - paid_holiday
            
            early_leaving_mins (int, optional) -> FreeeResponse: 早退分の時間(分単位)
            
            is_absence (bool, optional) -> FreeeResponse: 欠勤かどうか
                trueを指定すると、以下のパラーメータについて、指定した値が反映されず無視されます。
                    - break_records
                    - clock_in_at
                    - clock_out_at
                    - clock_in_at
                    - clock_out_at
                    - early_leaving_mins
                    - lateness_mins
                    - normal_work_clock_in_at
                    - normal_work_clock_out_at
                    - normal_work_mins
                    - normal_work_mins_by_paid_holiday
                    - paid_holiday
            
            lateness_mins (int, optional) -> FreeeResponse: 遅刻分の時間
            
            normal_work_clock_in_at (str, optional) -> FreeeResponse: 所定労働開始時刻
                指定しない場合はデフォルト設定が使用されます。(デフォルト設定は従業員に設定した勤務賃金設定の出退勤時刻と労働時間の設定を参照して値が決まります。)
            
            normal_work_clock_out_at (str, optional) -> FreeeResponse: 所定労働終了時刻
                指定しない場合はデフォルト設定が使用されます。(デフォルト設定は従業員に設定した勤務賃金設定の出退勤時刻と労働時間の設定を参照して値が決まります。)
            
            normal_work_mins (int, optional) -> FreeeResponse: 所定労働時間
                指定しない場合はデフォルト設定が使用されます。(デフォルト設定は従業員に設定した勤務賃金設定の出退勤時刻と労働時間の設定を参照して値が決まります。)
            
            note (str, optional) -> FreeeResponse: 勤怠メモ
            
            paid_holiday (bool, optional) -> FreeeResponse: この日の有休取得日数。1日単位で指定します。
            
            half_paid_holiday_mins (int, optional) -> FreeeResponse: 有給休暇の半休を利用した時間(分単位)
            
            hourly_paid_holiday_mins (int, optional) -> FreeeResponse: 有給休暇の時間休を利用した時間(分単位)
            
            special_holiday (bool, optional) -> FreeeResponse: この日の特別休暇取得日数。1日単位で指定します。
            
            special_holiday_setting_id (int, optional) -> FreeeResponse: 特別休暇設定ID
            
            half_special_holiday_mins (int, optional) -> FreeeResponse: 特別休暇の半休を利用した時間(分単位)
            
            hourly_special_holiday_mins (int, optional) -> FreeeResponse: 特別休暇の時間休を利用した時間(分単位)
            
            use_attendance_deduction (bool, optional) -> FreeeResponse: 欠勤・遅刻・早退を控除対象時間に算入するかどうか
            
            use_default_work_pattern (bool, optional) -> FreeeResponse: デフォルトの勤務設定を使うかどうか
                trueを指定した場合、以下のパラメータについて、指定した値に関係なく、従業員に設定した勤務賃金設定の休日の設定を参照して値が決まります
                    - day_pattern
                
                trueを指定した場合、以下のパラメータについて、指定した値に関係なく、従業員に設定した勤務賃金設定の出退勤時刻と労働時間の設定を参照して値が決まります。
                    - normal_work_clock_in_at
                    - normal_work_clock_out_at
                    - normal_work_mins
        """
        #TODO JSON作成を見直す
        break_records = dict(
            clock_in_at=break_clock_in_at,
            clock_out_at=break_clock_out_at
        )
        body = dict(
            break_records=list(),
            clock_in_at=work_clock_in_at,
            clock_out_at=work_clock_out_at,
            day_pattern=day_pattern,
            early_leaving_mins=early_leaving_mins,
            is_absence=is_absence,
            lateness_mins=lateness_mins,
            normal_work_clock_in_at=normal_work_clock_in_at,
            normal_work_clock_out_at=normal_work_clock_out_at,
            normal_work_mins=normal_work_mins,
            note=note,
            paid_holiday=paid_holiday,
            half_paid_holiday_mins=half_paid_holiday_mins,
            hourly_paid_holiday_mins=hourly_paid_holiday_mins,
            special_holiday=special_holiday,
            special_holiday_setting_id=special_holiday_setting_id,
            half_special_holiday_mins=half_special_holiday_mins,
            hourly_special_holiday_mins=hourly_special_holiday_mins,
            use_attendance_deduction=use_attendance_deduction,
            use_default_work_pattern=use_default_work_pattern
        )
        body["break_records"].append(break_records) if break_clock_in_at and break_clock_out_at is not None else None
        endpoint_url = f"./employees/{employee_id}/work_records/{date}"
        return self.api_call(method="PUT", endpoint_url=endpoint_url, body=body)


    def update_employee_work_record_summary(
        self,
        work_days: int|None=None,
        work_days_on_weekdays: int|None=None,
        work_days_on_prescribed_holidays: int|None=None,
        work_days_on_legal_holidays: int|None=None,
        total_work_mins: int|None=None,
        total_normal_work_mins: int|None=None,
        total_excess_statutory_work_mins: int|None=None,
        total_holiday_work_mins: int|None=None,
        total_latenight_work_mins: int|None=None,
        total_actual_excess_statutory_work_mins: int|None=None,
        total_overtime_work_mins: int|None=None,
        num_absences: int|None=None,
        num_absences_for_deduction: int|None=None,
        total_lateness_mins: int|None=None,
        total_lateness_mins_for_deduction: int|None=None,
        total_early_leaving_mins: int|None=None,
        total_early_leaving_mins_for_deduction: int|None=None,
        num_paid_holidays: int|None=None,
        total_shortage_work_mins: int|None=None,
        total_deemed_paid_excess_statutory_work_mins: int|None=None,
        total_deemed_paid_overtime_except_normal_work_mins: int|None=None,
        *,
        employee_id: int,
        year: int,
        month: int
        ) -> FreeeResponse:
        endpoint_url = f"/api/v1/employees/{employee_id}/work_record_summaries/{year}/{month}"
        
        body = dict(
            work_days=work_days,
            work_days_on_weekdays=work_days_on_weekdays,
            work_days_on_prescribed_holidays=work_days_on_prescribed_holidays,
            work_days_on_legal_holidays=work_days_on_legal_holidays,
            total_work_mins=total_work_mins,
            total_normal_work_mins=total_normal_work_mins,
            total_excess_statutory_work_mins=total_excess_statutory_work_mins,
            total_holiday_work_mins=total_holiday_work_mins,
            total_latenight_work_mins=total_latenight_work_mins,
            total_actual_excess_statutory_work_mins=total_actual_excess_statutory_work_mins,
            total_overtime_work_mins=total_overtime_work_mins,
            num_absences=num_absences,
            num_absences_for_deduction=num_absences_for_deduction,
            total_lateness_mins=total_lateness_mins,
            total_lateness_mins_for_deduction=total_lateness_mins_for_deduction,
            total_early_leaving_mins=total_early_leaving_mins,
            total_early_leaving_mins_for_deduction=total_early_leaving_mins_for_deduction,
            num_paid_holidays=num_paid_holidays,
            total_shortage_work_mins=total_shortage_work_mins,
            total_deemed_paid_excess_statutory_work_mins=total_deemed_paid_excess_statutory_work_mins,
            total_deemed_paid_overtime_except_normal_work_mins=total_deemed_paid_overtime_except_normal_work_mins
            )
        return self.api_call(method="PUT", endpoint_url=endpoint_url, body=body)


    def update_group(
        self,
        code: str|None=None,
        *,
        id: int,
        name: str
        ) -> FreeeResponse:
        endpoint_url = f"/api/v1/groups/{id}"
        group = dict(
        code=code,
            name=name
            )
        body = dict(
            group=group
            )
        return self.api_call(method="PUT", endpoint_url=endpoint_url, body=body)


    def update_position(
        self,
        code: str|None=None,
        *,
        id: int,
        name: str
        ) -> FreeeResponse:
        endpoint_url = f"/api/v1/positions/{id}"
        position = dict(
        code=code,
            name=name
            )
        body = dict(
            position=position
            )
        return self.api_call(method="PUT", endpoint_url=endpoint_url, body=body)


    def update_approval_requests_monthly_attendance(
        self,
        approver_id: int|None=None,
        *,
        id: int,
        approval_flow_route_id: int
        ) -> FreeeResponse:
        endpoint_url = f"/api/v1/approval_requests/monthly_attendances/{id}"
        
        body = dict(
            approval_flow_route_id=approval_flow_route_id,
            approver_id=approver_id
            )
        return self.api_call(method="PUT", endpoint_url=endpoint_url, body=body)


    def update_approval_requests_work_time(
        self,
        clear_work_time: bool|None=None,
        clock_in_at: str|None=None,
        clock_out_at: str|None=None,
        lateness_mins: int|None=None,
        early_leaving_mins: int|None=None,
        comment: str|None=None,
        approver_id: int|None=None,
        *,
        id: int,
        target_date: str,
        approval_flow_route_id: int
        ) -> FreeeResponse:
        endpoint_url = f"/api/v1/approval_requests/work_times/{id}"
        break_records = dict(
            clock_in_at=clock_in_at,
            clock_out_at=clock_out_at
        )
        body = dict(
            target_date=target_date,
            clear_work_time=clear_work_time,
            clock_in_at=clock_in_at,
            clock_out_at=clock_out_at,
            lateness_mins=lateness_mins,
            early_leaving_mins=early_leaving_mins,
            break_records=break_records,
            comment=comment,
            approval_flow_route_id=approval_flow_route_id,
            approver_id=approver_id
            )
        return self.api_call(method="PUT", endpoint_url=endpoint_url, body=body)


    def update_approval_requests_paid_holiday(
        self,
        start_at: str|None=None,
        end_at: str|None=None,
        comment: str|None=None,
        approver_id: int|None=None,
        *,
        id: int,
        target_date: str,
        holiday_type: str,
        approval_flow_route_id: int
        ) -> FreeeResponse:
        endpoint_url = f"/api/v1/approval_requests/paid_holidays/{id}"
        
        body = dict(
            target_date=target_date,
            holiday_type=holiday_type,
            start_at=start_at,
            end_at=end_at,
            comment=comment,
            approval_flow_route_id=approval_flow_route_id,
            approver_id=approver_id
            )
        return self.api_call(method="PUT", endpoint_url=endpoint_url, body=body)


    def update_approval_requests_special_holiday(
        self,
        start_at: str|None=None,
        end_at: str|None=None,
        comment: str|None=None,
        approver_id: int|None=None,
        *,
        id: int,
        target_date: str,
        special_holiday_setting_id: int,
        holiday_type: str,
        approval_flow_route_id: int
        ) -> FreeeResponse:
        endpoint_url = f"/api/v1/approval_requests/special_holidays/{id}"
        
        body = dict(
            target_date=target_date,
            special_holiday_setting_id=special_holiday_setting_id,
            holiday_type=holiday_type,
            start_at=start_at,
            end_at=end_at,
            comment=comment,
            approval_flow_route_id=approval_flow_route_id,
            approver_id=approver_id
            )
        return self.api_call(method="PUT", endpoint_url=endpoint_url, body=body)


    def update_approval_requests_overtime_work(
        self,
        comment: str|None=None,
        approver_id: int|None=None,
        *,
        id: int,
        target_date: str,
        start_at: str,
        end_at: str,
        approval_flow_route_id: int
        ) -> FreeeResponse:
        endpoint_url = f"/api/v1/approval_requests/overtime_works/{id}"
        
        body = dict(
            target_date=target_date,
            start_at=start_at,
            end_at=end_at,
            comment=comment,
            approval_flow_route_id=approval_flow_route_id,
            approver_id=approver_id
            )
        return self.api_call(method="PUT", endpoint_url=endpoint_url, body=body)


    def put_yearend_adjustment_employee(
        self,
        address_kana: str|None=None,
        payer_type: str|None=None,
        widow_type: str|None=None,
        disability_type: str|None=None,
        married: bool|None=None,
        is_working_student: bool|None=None,
        is_foreigner: bool|None=None,
        other_company_revenue: int|None=None,
        all_other_income: int|None=None,
        householder: str|None=None,
        householder_name: str|None=None,
        *,
        year: int,
        employee_id: int,
        last_name: str,
        first_name: str,
        last_name_kana: str,
        first_name_kana: str,
        zipcode1: str,
        zipcode2: str,
        prefecture_code: int,
        address: str
        ) -> FreeeResponse:
        endpoint_url = f"/api/v1/yearend_adjustments/{year}/employees/{employee_id}"
        employee = dict(
            last_name=last_name,
            first_name=first_name,
            last_name_kana=last_name_kana,
            first_name_kana=first_name_kana,
            zipcode1=zipcode1,
            zipcode2=zipcode2,
            prefecture_code=prefecture_code,
            address=address,
            address_kana=address_kana,
            payer_type=payer_type,
            widow_type=widow_type,
            disability_type=disability_type,
            married=married,
            is_working_student=is_working_student,
            is_foreigner=is_foreigner,
            other_company_revenue=other_company_revenue,
            all_other_income=all_other_income,
            householder=householder,
            householder_name=householder_name
            )
        body = dict(
            employee=employee
            )
        return self.api_call(method="PUT", endpoint_url=endpoint_url, body=body)


    def put_yearend_adjustment_payroll_and_bonus(
        self,
        unentered_payroll_amount: int|None=None,
        unentered_payroll_deduction_amount: int|None=None,
        unentered_payroll_income_tax_amount: int|None=None,
        unentered_bonus_amount: int|None=None,
        unentered_bonus_deduction_amount: int|None=None,
        unentered_bonus_income_tax_amount: int|None=None,
        *,
        year: int,
        employee_id: int
        ) -> FreeeResponse:
        endpoint_url = f"/api/v1/yearend_adjustments/{year}/payroll_and_bonus/{employee_id}"
        payroll_and_bonus = dict(
            unentered_payroll_amount=unentered_payroll_amount,
            unentered_payroll_deduction_amount=unentered_payroll_deduction_amount,
            unentered_payroll_income_tax_amount=unentered_payroll_income_tax_amount,
            unentered_bonus_amount=unentered_bonus_amount,
            unentered_bonus_deduction_amount=unentered_bonus_deduction_amount,
            unentered_bonus_income_tax_amount=unentered_bonus_income_tax_amount
            )
        body = dict(
            payroll_and_bonus=payroll_and_bonus
            )
        return self.api_call(method="PUT", endpoint_url=endpoint_url, body=body)


    def put_yearend_adjustment_dependents(
        self,
        *,
        year: int,
        employee_id: int,
        dependents: None
        ) -> FreeeResponse:
        endpoint_url = f"/api/v1/yearend_adjustments/{year}/dependents/{employee_id}"
        
        body = dict(
            dependents=dependents
            )
        return self.api_call(method="PUT", endpoint_url=endpoint_url, body=body)


    def put_yearend_adjustment_previous_job(
        self,
        *,
        year: int,
        employee_id: int,
        income: int,
        deduction: int,
        withholding_tax_amount: int,
        company_name: str,
        company_address: str,
        retire_date: str
        ) -> FreeeResponse:
        endpoint_url = f"/api/v1/yearend_adjustments/{year}/previous_jobs/{employee_id}"
        previous_job = dict(
            income=income,
            deduction=deduction,
            withholding_tax_amount=withholding_tax_amount,
            company_name=company_name,
            company_address=company_address,
            retire_date=retire_date
            )
        body = dict(
            previous_job=previous_job
            )
        return self.api_call(method="PUT", endpoint_url=endpoint_url, body=body)


    def put_yearend_adjustment_insurances(
        self,
        company_name: str|None=None,
        kind_of_purpose: str|None=None,
        period: str|None=None,
        policyholder_last_name: str|None=None,
        policyholder_first_name: str|None=None,
        recipient_last_name: str|None=None,
        recipient_first_name: str|None=None,
        recipient_relationship: str|None=None,
        payment_start_date: str|None=None,
        *,
        year: int,
        employee_id: int,
        id: int,
        type: str,
        category: str,
        new_or_old: str,
        amount: int
        ) -> FreeeResponse:
        endpoint_url = f"/api/v1/yearend_adjustments/{year}/insurances/{employee_id}/{id}"
        insurance = dict(
            type=type,
            category=category,
            new_or_old=new_or_old,
            company_name=company_name,
            kind_of_purpose=kind_of_purpose,
            period=period,
            policyholder_last_name=policyholder_last_name,
            policyholder_first_name=policyholder_first_name,
            recipient_last_name=recipient_last_name,
            recipient_first_name=recipient_first_name,
            recipient_relationship=recipient_relationship,
            payment_start_date=payment_start_date,
            amount=amount
            )
        body = dict(
            insurance=insurance
            )
        return self.api_call(method="PUT", endpoint_url=endpoint_url, body=body)


    def put_yearend_adjustment_housing_loan_deduction(
        self,
        *,
        year: int,
        employee_id: int,
        housing_loan_deduction: int
        ) -> FreeeResponse:
        endpoint_url = f"/api/v1/yearend_adjustments/{year}/housing_loan_deductions/{employee_id}"
        
        body = dict(
            housing_loan_deduction=housing_loan_deduction
            )
        return self.api_call(method="PUT", endpoint_url=endpoint_url, body=body)


    def put_yearend_adjustment_housing_loan(
        self,
        *,
        year: int,
        employee_id: int,
        id: int,
        residence_start_date: str,
        remaining_balance_at_yearend: int,
        category: str,
        specific_case_type: str
        ) -> FreeeResponse:
        endpoint_url = f"/api/v1/yearend_adjustments/{year}/housing_loans/{employee_id}/{id}"
        housing_loan = dict(
            residence_start_date=residence_start_date,
            remaining_balance_at_yearend=remaining_balance_at_yearend,
            category=category,
            specific_case_type=specific_case_type
            )
        body = dict(
            housing_loan=housing_loan
            )
        return self.api_call(method="PUT", endpoint_url=endpoint_url, body=body)


    # DELETEメソッド
    def destroy_employee(
        self,
        *,
        id: int
        ) -> FreeeResponse:
        endpoint_url = f"./employees/{id}"
        
        return self.api_call(method="DELETE", endpoint_url=endpoint_url)


    def destroy_employee_work_record(
        self,
        *,
        employee_id: int,
        date: str
        ) -> FreeeResponse:
        endpoint_url = f"./employees/{employee_id}/work_records/{date}"
        
        return self.api_call(method="DELETE", endpoint_url=endpoint_url)


    def destroy_group(
        self,
        *,
        id: int
        ) -> FreeeResponse:
        endpoint_url = f"./groups/{id}"
        
        return self.api_call(method="DELETE", endpoint_url=endpoint_url)


    def destroy_position(
        self,
        *,
        id: int
        ) -> FreeeResponse:
        endpoint_url = f"./positions/{id}"
        
        return self.api_call(method="DELETE", endpoint_url=endpoint_url)


    def destroy_approval_requests_monthly_attendance(
        self,
        *,
        id: int
        ) -> FreeeResponse:
        endpoint_url = f"./approval_requests/monthly_attendances/{id}"
        
        return self.api_call(method="DELETE", endpoint_url=endpoint_url)


    def destroy_approval_requests_work_time(
        self,
        *,
        id: int
        ) -> FreeeResponse:
        endpoint_url = f"./approval_requests/work_times/{id}"
        
        return self.api_call(method="DELETE", endpoint_url=endpoint_url)


    def destroy_approval_requests_paid_holiday(
        self,
        *,
        id: int
        ) -> FreeeResponse:
        endpoint_url = f"./approval_requests/paid_holidays/{id}"
        
        return self.api_call(method="DELETE", endpoint_url=endpoint_url)


    def destroy_approval_requests_special_holiday(
        self,
        *,
        id: int
        ) -> FreeeResponse:
        endpoint_url = f"./approval_requests/special_holidays/{id}"
        
        return self.api_call(method="DELETE", endpoint_url=endpoint_url)


    def destroy_approval_requests_overtime_work(
        self,
        *,
        id: int
        ) -> FreeeResponse:
        endpoint_url = f"./approval_requests/overtime_works/{id}"
        
        return self.api_call(method="DELETE", endpoint_url=endpoint_url)


    def destroy_yearend_adjustment_previous_job(
        self,
        *,
        year: int,
        employee_id: int
        ) -> FreeeResponse:
        endpoint_url = f"./yearend_adjustments/{year}/previous_jobs/{employee_id}"
        
        return self.api_call(method="DELETE", endpoint_url=endpoint_url)


    def destroy_yearend_adjustment_insurances(
        self,
        *,
        year: int,
        employee_id: int,
        id: int
        ) -> FreeeResponse:
        endpoint_url = f"./yearend_adjustments/{year}/insurances/{employee_id}/{id}"
        
        return self.api_call(method="DELETE", endpoint_url=endpoint_url)


    def destroy_yearend_adjustment_housing_loan(
        self,
        *,
        year: int,
        employee_id: int,
        id: int
        ) -> FreeeResponse:
        endpoint_url = f"./yearend_adjustments/{year}/housing_loans/{employee_id}/{id}"
        
        return self.api_call(method="DELETE", endpoint_url=endpoint_url)


if __name__ == "__main__":
    pass
