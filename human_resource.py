from freee_sdk import BaseClient
from freee_sdk.utils import _remove_none_values

class HumanResourse(BaseClient):
    API_URL = "/hr/api/v1/"

    def update_employee_work_record(
        self,
        clock_in_at: str|None=None,
        clock_out_at: str|None=None,
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
        ):
        """
        勤怠の更新\n
        Args:
            employee_id (int): 従業員ID
            
            date (int): 更新対象年月日(YYYY-MM-DD)
            
            clock_in_at (str, optional): 開始時刻. Defaults to None.
            
            clock_out_at (str, optional): 終了時刻. Defaults to None.
            
            day_pattern (WorkRecords.DayPttern, optional): 勤務パターン. Defaults to None.
                prescribed_holiday、legal_holidayを指定すると、以下のパラメータについて、指定した値が反映されず無視されます。
                    - early_leaving_mins
                    - lateness_mins
                    - paid_holiday
            
            early_leaving_mins (int, optional): 早退分の時間(分単位). Defaults to None.
            
            is_absence (bool, optional): 欠勤かどうか. Defaults to None.
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
            
            lateness_mins (int, optional): 遅刻分の時間. Defaults to None.
            
            normal_work_clock_in_at (str, optional): 所定労働開始時刻. Defaults to None.
                指定しない場合はデフォルト設定が使用されます。(デフォルト設定は従業員に設定した勤務賃金設定の出退勤時刻と労働時間の設定を参照して値が決まります。)
            
            normal_work_clock_out_at (str, optional): 所定労働終了時刻. Defaults to None.
                指定しない場合はデフォルト設定が使用されます。(デフォルト設定は従業員に設定した勤務賃金設定の出退勤時刻と労働時間の設定を参照して値が決まります。)
            
            normal_work_mins (int, optional): 所定労働時間. Defaults to None.
                指定しない場合はデフォルト設定が使用されます。(デフォルト設定は従業員に設定した勤務賃金設定の出退勤時刻と労働時間の設定を参照して値が決まります。)
            
            note (str, optional): 勤怠メモ. Defaults to None.
            
            paid_holiday (bool, optional): この日の有休取得日数。1日単位で指定します。. Defaults to None.
            
            half_paid_holiday_mins (int, optional): 有給休暇の半休を利用した時間(分単位). Defaults to None.
            
            hourly_paid_holiday_mins (int, optional): 有給休暇の時間休を利用した時間(分単位). Defaults to None.
            
            special_holiday (bool, optional): この日の特別休暇取得日数。1日単位で指定します。. Defaults to None.
            
            special_holiday_setting_id (int, optional): 特別休暇設定ID. Defaults to None.
            
            half_special_holiday_mins (int, optional): 特別休暇の半休を利用した時間(分単位). Defaults to None.
            
            hourly_special_holiday_mins (int, optional): 特別休暇の時間休を利用した時間(分単位). Defaults to None.
            
            use_attendance_deduction (bool, optional): 欠勤・遅刻・早退を控除対象時間に算入するかどうか. Defaults to None.
            
            use_default_work_pattern (bool, optional): デフォルトの勤務設定を使うかどうか. Defaults to None.
                trueを指定した場合、以下のパラメータについて、指定した値に関係なく、従業員に設定した勤務賃金設定の休日の設定を参照して値が決まります
                    - day_pattern
                
                trueを指定した場合、以下のパラメータについて、指定した値に関係なく、従業員に設定した勤務賃金設定の出退勤時刻と労働時間の設定を参照して値が決まります。
                    - normal_work_clock_in_at
                    - normal_work_clock_out_at
                    - normal_work_mins
        """
        #TODO JSON作成を見直す
        break_records = dict(
            clock_in_at=clock_in_at,
            clock_out_at=clock_out_at
            )
        body = dict(
            break_records=break_records,
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
        print(body)
        endpoint_url = f"./employees/{employee_id}/work_records/{date}"
        return self.api_call(method="PUT", endpoint_url=endpoint_url, body=body)


    def get_users_me(self):
        endpoint_url = f"./users/me"
        return self.api_call(method="GET", endpoint_url=endpoint_url)


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
        ):
        """従業員を新規作成します。

        Args:
            first_name (str): _description_
            last_name (str): _description_
            first_name_kana (str): _description_
            last_name_kana (str): _description_
            pay_amount (int): _description_
            birth_date (str): _description_
            employee_num (str | None, optional): 従業員番号 Defaults to None.
            working_hours_system_name (str | None, optional): 勤務・賃金設定名 で設定した名称を指定してください。Defaults to None.
            company_reference_date_rule_name (str | None, optional): 締め日支払い日グループ名 で設定した締め日支払い日を指定してください。\n
            - 未指定の際は、最初に登録したデータが利用されます。
            - 入力パラメータのno_payroll_calculationがtrueの場合に指定するとエラーになります。 Defaults to None.
            gender (str | None, optional): _description_. Defaults to None.
            married (bool | None, optional): _description_. Defaults to None.
            no_payroll_calculation (bool | None, optional): _description_. Defaults to None.
            entry_date (str | None, optional): _description_. Defaults to None.
            pay_calc_type (str, optional): _description_. Defaults to "monthly".

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


    def get_approval_flow_route(
        self,
        *,
        id: int|None=None
        ):
        endpoint_url = f"./approval_flow_routes/{id}"
        return self.api_call(method="GET", endpoint_url=endpoint_url)

#TODO ここまで実装済(2024/02/22)
    def get_approval_flow_routes(
        self,
        included_user_id: int|None=None,
        usage: str|None=None
        ):
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
        ):
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
        limit: int|None=None,
        offset: int|None=None
        ):
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
        ):
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
        limit: int|None=None,
        offset: int|None=None
        ):
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
        ):
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
        limit: int|None=None,
        offset: int|None=None
        ):
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
        ):
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
        limit: int|None=None,
        offset: int|None=None
        ):
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
        ):
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
        limit: int|None=None,
        offset: int|None=None
        ):
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
        ):
        endpoint_url = f"./bonuses/employee_payroll_statements/{employee_id}"
        query = dict(
            year=year,
            month=month
        )
        return self.api_call(method="GET", endpoint_url=endpoint_url, query=query)


    def get_bonuses_employee_payroll_statements(
        self,
        limit: int|None=None,
        offset: int|None=None,
        *,
        year: int|None=None,
        month: int|None=None
        ):
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
        with_no_payroll_calculation: bool|None=None,
        #TODO *,
        #TODO company_id: int|None=None
        ):
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
        ):
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
        with_no_payroll_calculation: bool|None=None,
        *,
        year: int|None=None,
        month: int|None=None
        ):
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
        ):
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
        ):
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
        ):
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
        ):
        endpoint_url = f"./employees/{employee_id}/dependent_rules"
        query = dict(
            year=year,
            month=month
        )
        return self.api_call(method="GET", endpoint_url=endpoint_url, query=query)


    def get_employee_group_memberships(
        self,
        with_no_payroll_calculation: bool|None=None,
        employee_ids: str|None=None,
        limit: int|None=None,
        offset: int|None=None,
        *,
        base_date: str|None=None
        ):
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
        ):
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
        ):
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
        ):
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
        ):
        endpoint_url = f"./employees/{employee_id}/time_clocks/{id}"
        return self.api_call(method="GET", endpoint_url=endpoint_url)


    def get_employee_time_clocks(
        self,
        from_date: str|None=None,
        to_date: str|None=None,
        limit: int|None=None,
        offset: int|None=None,
        *,
        employee_id: int|None=None
        ):
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
        ):
        endpoint_url = f"./employees/{employee_id}/time_clocks/available_types"
        query = dict(
            company_id=company_id,
            date=date
        )
        return self.api_call(method="GET", endpoint_url=endpoint_url, query=query)


    def get_employee_welfare_pension_insurance_rule(
        self,
        *,
        year: int|None=None,
        month: int|None=None,
        employee_id: int|None=None
        ):
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
        ):
        endpoint_url = f"./employees/{employee_id}/work_records/{date}"
        return self.api_call(method="GET", endpoint_url=endpoint_url)


    def get_employee_work_record_summary(
        self,
        work_records: bool|None=None,
        *,
        employee_id: int|None=None,
        year: int|None=None,
        month: int|None=None
        ):
        endpoint_url = f"./employees/{employee_id}/work_record_summaries/{year}/{month}"
        query = dict(
            work_records=work_records,
        )
        return self.api_call(method="GET", endpoint_url=endpoint_url, query=query)


    def get_groups(self):
        endpoint_url = f"./groups"
        return self.api_call(method="GET", endpoint_url=endpoint_url)


    def get_positions(self):
        endpoint_url = f"./positions"
        return self.api_call(method="GET", endpoint_url=endpoint_url)


    def get_salaries_employee_payroll_statement(
        self,
        *,
        year: int|None=None,
        month: int|None=None,
        employee_id: int|None=None
        ):
        endpoint_url = f"./salaries/employee_payroll_statements/{employee_id}"
        query = dict(
            year=year,
            month=month
        )
        return self.api_call(method="GET", endpoint_url=endpoint_url, query=query)


    def get_salaries_employee_payroll_statements(
        self,
        limit: int|None=None,
        offset: int|None=None,
        *,
        year: int|None=None,
        month: int|None=None
        ):
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
        ):
        endpoint_url = f"./yearend_adjustments/{year}/employees/{employee_id}"
        query = dict(
            year=year
        )
        return self.api_call(method="GET", endpoint_url=endpoint_url, query=query)


    # POSTメソッド
    def create_employee(
        self,
        num: str|None=None,
        working_hours_system_name: str|None=None,
        company_reference_date_rule_name: str|None=None,
        pay_calc_type: str|None=None,
        pay_amount: int|None=None,
        gender: str|None=None,
        married: bool|None=None,
        no_payroll_calculation: bool|None=None,
        *,
        last_name: str,
        first_name: str,
        last_name_kana: str,
        first_name_kana: str,
        birth_date: str,
        entry_date: str
        ):
        endpoint_url = f"./employees"
        employee = dict(
        num=num,
        working_hours_system_name=working_hours_system_name,
        company_reference_date_rule_name=company_reference_date_rule_name,
        last_name=last_name,
        first_name=first_name,
        last_name_kana=last_name_kana,
        first_name_kana=first_name_kana,
        birth_date=birth_date,
        entry_date=entry_date,
        pay_calc_type=pay_calc_type,
        pay_amount=pay_amount,
        gender=gender,
        married=married,
        no_payroll_calculation=no_payroll_calculation
        )
        body = dict(
            employee=employee
            )
        return self.api_call(method="POST", endpoint_url=endpoint_url, body=body)


    def create_employee_time_clock(
        self,
        base_date: str|None=None,
        datetime: str|None=None,
        *,
        employee_id: int,
        type: str
        ):
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
        ):
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
        ):
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
        ):
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
        ):
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
        ):
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
        ):
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
        ):
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
        ):
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
        ):
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
        ):
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
        ):
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
        ):
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
        ):
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
        ):
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
        limit: int|None=None,
        offset: int|None=None,
        *,
        year: int|None=None
        ):
        endpoint_url = f"./yearend_adjustments/{year}/employees"
        query = dict(
            year=year,
            limit=limit,
            offset=offset
        )
        return self.api_call(method="GET", endpoint_url=endpoint_url, query=query)


if __name__ == "__main__":
    import configparser
    config = configparser.ConfigParser()

    #設定ファイル読み込み
    config.read("./doc/.ini")
    CLIENT_ID = config["freee"]["CLIENT_ID"]
    CLIENT_SECRET = config["freee"]["CLIENT_SECRET"]
    REDIRECT_URI = config["freee"]["REDIRECT_URI"]
    
    human_resourse = HumanResourse(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI
    )
    me = human_resourse.get_users_me()
    
    company_id = me["companies"][0]["id"]
    employees = human_resourse.get_company_employees(
        company_id=company_id
    )

    for employee in employees:
        user_id = employee["id"]
        user_name = employee["display_name"]
    print(f"id: {user_id}\nname: {user_name}")
    work_summary = human_resourse.get_employee_work_record_summary(
        company_id=company_id,
        employee_id=user_id,
        year=2024,
        month=1
    )
    print(work_summary)

    pd = human_resourse.update_employee_work_record(
        paid_holiday=1,
        employee_id=user_id,
        date="2024-01-9"
    )
    print(pd)
    
    """add_emploee = human_resourse.create_employee(
        company_id=company_id,
        first_name="佐藤",
        last_name="太郎",
        first_name_kana="サトウ",
        last_name_kana="タロウ",
        pay_amount=3,
        birth_date="1997-06-21",
        entry_date="2024-01-01"
    )
    print(add_emploee)
    employees = human_resourse.get_company_employees(
        company_id=company_id
    )
    print(employees)"""

