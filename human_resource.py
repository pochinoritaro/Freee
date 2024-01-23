from freee_sdk import BaseClient
from freee_sdk.utils import _remove_none_values

class HumanResourse(BaseClient):
    API_URL = "/hr/api/v1/"

    def update_employee_work_record(
        self,
        clock_in_at: str=None,
        clock_out_at: str=None,
        day_pattern: str=None,
        early_leaving_mins: int=None,
        is_absence: bool=None,
        lateness_mins: int=None,
        normal_work_clock_in_at: str=None,
        normal_work_clock_out_at: str=None,
        normal_work_mins: int=None,
        note: str=None,
        paid_holiday: bool=None,
        half_paid_holiday_mins: int=None,
        hourly_paid_holiday_mins: int=None,
        special_holiday: bool=None,
        special_holiday_setting_id: int=None,
        half_special_holiday_mins: int=None,
        hourly_special_holiday_mins: int=None,
        use_attendance_deduction: bool=None,
        use_default_work_pattern: bool=None,
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
        endpoint_url = f"./employees/{employee_id}/work_records/{date}"
        return self.api_call(method="PUT", endpoint_url=endpoint_url)

    def get_users_me(self):
        endpoint_url = f"./users/me"
        return self.api_call(method="GET", endpoint_url=endpoint_url)

    def create_employee(
        self,
        employee_num: str=None,
        working_hours_system_nqme: str=None,
        company_reference_date_rule_name: str=None,
        pay_calc_type: str=None,
        pay_amount: int=None,
        gender: str=None,
        married: bool=False,
        no_payroll_caluclation: bool=False,
        *,
        company_id: int,
        first_name: str,
        last_name: str,
        first_name_kana: str,
        last_name_kana: str,
        birth_date: str,
        entry_date: str=None
        ):
        employee_dict = dict(
            num=employee_num,
            working_hours_system_nqme=working_hours_system_nqme,
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
            no_payroll_caluclation=no_payroll_caluclation
        )
        request_body = dict(
            company_id=company_id,
            employee=_remove_none_values(employee_dict))
        endpoint_url = f"./employees"
        print(request_body)
        return self.api_call(method="POST", endpoint_url=endpoint_url, body=request_body)

def get_approval_flow_route(
	self, 
	*, 
	id: int|None=None, 
	company_id: int|None=None
	):
	endpoint_url = f"./approval_flow_routes/{id}"
	query = dict(
		id=id,
		company_id=company_id,
	
	)
	return self.api_call(method="", endpoint_url=endpoint_url, query=query)


def get_approval_flow_routes(
	self, 
	included_user_id: int|None=None, 
	usage: str|None=None, 
	*, 
	company_id: int|None=None
	):
	endpoint_url = f"./approval_flow_routes"
	query = dict(
		company_id=company_id,
		included_user_id=included_user_id,
		usage=usage,
	
	)
	return self.api_call(method="", endpoint_url=endpoint_url, query=query)


def get_approval_requests_monthly_attendance(
	self, 
	*, 
	company_id: int|None=None, 
	id: int|None=None
	):
	endpoint_url = f"./approval_requests/monthly_attendances/{id}"
	query = dict(
		company_id=company_id,
		id=id,
	
	)
	return self.api_call(method="", endpoint_url=endpoint_url, query=query)


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
	offset: int|None=None, 
	*, 
	company_id: int|None=None
	):
	endpoint_url = f"./approval_requests/monthly_attendances"
	query = dict(
		company_id=company_id,
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
		offset=offset,
	
	)
	return self.api_call(method="", endpoint_url=endpoint_url, query=query)


def get_approval_requests_overtime_work(
	self, 
	*, 
	company_id: int|None=None, 
	id: int|None=None
	):
	endpoint_url = f"./approval_requests/overtime_works/{id}"
	query = dict(
		company_id=company_id,
		id=id,
	
	)
	return self.api_call(method="", endpoint_url=endpoint_url, query=query)


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
	offset: int|None=None, 
	*, 
	company_id: int|None=None
	):
	endpoint_url = f"./approval_requests/overtime_works"
	query = dict(
		company_id=company_id,
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
		offset=offset,
	
	)
	return self.api_call(method="", endpoint_url=endpoint_url, query=query)


def get_approval_requests_paid_holiday(
	self, 
	*, 
	company_id: int|None=None, 
	id: int|None=None
	):
	endpoint_url = f"./approval_requests/paid_holidays/{id}"
	query = dict(
		company_id=company_id,
		id=id,
	
	)
	return self.api_call(method="", endpoint_url=endpoint_url, query=query)


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
	offset: int|None=None, 
	*, 
	company_id: int|None=None
	):
	endpoint_url = f"./approval_requests/paid_holidays"
	query = dict(
		company_id=company_id,
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
		offset=offset,
	
	)
	return self.api_call(method="", endpoint_url=endpoint_url, query=query)


def get_approval_requests_special_holiday(
	self, 
	*, 
	company_id: int|None=None, 
	id: int|None=None
	):
	endpoint_url = f"./approval_requests/special_holidays/{id}"
	query = dict(
		company_id=company_id,
		id=id,
	
	)
	return self.api_call(method="", endpoint_url=endpoint_url, query=query)


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
	offset: int|None=None, 
	*, 
	company_id: int|None=None
	):
	endpoint_url = f"./approval_requests/special_holidays"
	query = dict(
		company_id=company_id,
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
		offset=offset,
	
	)
	return self.api_call(method="", endpoint_url=endpoint_url, query=query)


def get_approval_requests_work_time(
	self, 
	*, 
	company_id: int|None=None, 
	id: int|None=None
	):
	endpoint_url = f"./approval_requests/work_times/{id}"
	query = dict(
		company_id=company_id,
		id=id,
	
	)
	return self.api_call(method="", endpoint_url=endpoint_url, query=query)


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
	offset: int|None=None, 
	*, 
	company_id: int|None=None
	):
	endpoint_url = f"./approval_requests/work_times"
	query = dict(
		company_id=company_id,
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
		offset=offset,
	
	)
	return self.api_call(method="", endpoint_url=endpoint_url, query=query)


def get_bonuses_employee_payroll_statement(
	self, 
	*, 
	company_id: int|None=None, 
	year: int|None=None, 
	month: int|None=None, 
	employee_id: int|None=None
	):
	endpoint_url = f"./bonuses/employee_payroll_statements/{employee_id}"
	query = dict(
		company_id=company_id,
		year=year,
		month=month,
		employee_id=employee_id,
	
	)
	return self.api_call(method="", endpoint_url=endpoint_url, query=query)


def get_bonuses_employee_payroll_statements(
	self, 
	limit: int|None=None, 
	offset: int|None=None, 
	*, 
	company_id: int|None=None, 
	year: int|None=None, 
	month: int|None=None
	):
	endpoint_url = f"./bonuses/employee_payroll_statements"
	query = dict(
		company_id=company_id,
		year=year,
		month=month,
		limit=limit,
		offset=offset,
	
	)
	return self.api_call(method="", endpoint_url=endpoint_url, query=query)


def get_company_employees(
	self, 
	limit: int|None=None, 
	offset: int|None=None, 
	with_no_payroll_calculation: bool|None=None, 
	*, 
	company_id: int|None=None
	):
	endpoint_url = f"./companies/{company_id}/employees"
	query = dict(
		limit=limit,
		offset=offset,
		company_id=company_id,
		with_no_payroll_calculation=with_no_payroll_calculation,
	
	)
	return self.api_call(method="", endpoint_url=endpoint_url, query=query)


def get_employee(
	self, 
	*, 
	company_id: int|None=None, 
	year: int|None=None, 
	month: int|None=None, 
	id: int|None=None
	):
	endpoint_url = f"./employees/{id}"
	query = dict(
		company_id=company_id,
		year=year,
		month=month,
		id=id,
	
	)
	return self.api_call(method="", endpoint_url=endpoint_url, query=query)


def get_employees(
	self, 
	limit: int|None=None, 
	offset: int|None=None, 
	with_no_payroll_calculation: bool|None=None, 
	*, 
	company_id: int|None=None, 
	year: int|None=None, 
	month: int|None=None
	):
	endpoint_url = f"./employees"
	query = dict(
		company_id=company_id,
		year=year,
		month=month,
		limit=limit,
		offset=offset,
		with_no_payroll_calculation=with_no_payroll_calculation,
	
	)
	return self.api_call(method="", endpoint_url=endpoint_url, query=query)


def get_employees_special_holidays(
	self, 
	date: str|None=None, 
	start_date: str|None=None, 
	end_date: str|None=None, 
	*, 
	company_id: int|None=None, 
	employee_id: int|None=None
	):
	endpoint_url = f"./employees/{employee_id}/special_holidays"
	query = dict(
		company_id=company_id,
		employee_id=employee_id,
		date=date,
		start_date=start_date,
		end_date=end_date,
	
	)
	return self.api_call(method="", endpoint_url=endpoint_url, query=query)


def get_employee_bank_account_rule(
	self, 
	*, 
	company_id: int|None=None, 
	year: int|None=None, 
	month: int|None=None, 
	employee_id: int|None=None
	):
	endpoint_url = f"./employees/{employee_id}/bank_account_rule"
	query = dict(
		company_id=company_id,
		year=year,
		month=month,
		employee_id=employee_id,
	
	)
	return self.api_call(method="", endpoint_url=endpoint_url, query=query)


def get_employee_basic_pay_rule(
	self, 
	*, 
	company_id: int|None=None, 
	year: int|None=None, 
	month: int|None=None, 
	employee_id: int|None=None
	):
	endpoint_url = f"./employees/{employee_id}/basic_pay_rule"
	query = dict(
		company_id=company_id,
		year=year,
		month=month,
		employee_id=employee_id,
	
	)
	return self.api_call(method="", endpoint_url=endpoint_url, query=query)


def get_employee_dependent_rules(
	self, 
	*, 
	company_id: int|None=None, 
	year: int|None=None, 
	month: int|None=None, 
	employee_id: int|None=None
	):
	endpoint_url = f"./employees/{employee_id}/dependent_rules"
	query = dict(
		company_id=company_id,
		year=year,
		month=month,
		employee_id=employee_id,
	
	)
	return self.api_call(method="", endpoint_url=endpoint_url, query=query)


def get_employee_group_memberships(
	self, 
	with_no_payroll_calculation: bool|None=None, 
	employee_ids: str|None=None, 
	limit: int|None=None, 
	offset: int|None=None, 
	*, 
	company_id: int|None=None, 
	base_date: str|None=None
	):
	endpoint_url = f"./employee_group_memberships"
	query = dict(
		company_id=company_id,
		base_date=base_date,
		with_no_payroll_calculation=with_no_payroll_calculation,
		employee_ids=employee_ids,
		limit=limit,
		offset=offset,
	
	)
	return self.api_call(method="", endpoint_url=endpoint_url, query=query)


def get_employee_health_insurance_rule(
	self, 
	*, 
	company_id: int|None=None, 
	year: int|None=None, 
	month: int|None=None, 
	employee_id: int|None=None
	):
	endpoint_url = f"./employees/{employee_id}/health_insurance_rule"
	query = dict(
		company_id=company_id,
		year=year,
		month=month,
		employee_id=employee_id,
	
	)
	return self.api_call(method="", endpoint_url=endpoint_url, query=query)


def get_employee_profile_custom_fields_rule(
	self, 
	*, 
	company_id: int|None=None, 
	year: int|None=None, 
	month: int|None=None, 
	employee_id: int|None=None
	):
	endpoint_url = f"./employees/{employee_id}/profile_custom_fields"
	query = dict(
		company_id=company_id,
		year=year,
		month=month,
		employee_id=employee_id,
	
	)
	return self.api_call(method="", endpoint_url=endpoint_url, query=query)


def get_employee_profile_rule(
	self, 
	*, 
	company_id: int|None=None, 
	year: int|None=None, 
	month: int|None=None, 
	employee_id: int|None=None
	):
	endpoint_url = f"./employees/{employee_id}/profile_rule"
	query = dict(
		company_id=company_id,
		year=year,
		month=month,
		employee_id=employee_id,
	
	)
	return self.api_call(method="", endpoint_url=endpoint_url, query=query)


def get_employee_time_clock(
	self, 
	*, 
	company_id: int|None=None, 
	employee_id: int|None=None, 
	id: int|None=None
	):
	endpoint_url = f"./employees/{employee_id}/time_clocks/{id}"
	query = dict(
		company_id=company_id,
		employee_id=employee_id,
		id=id,
	
	)
	return self.api_call(method="", endpoint_url=endpoint_url, query=query)


def get_employee_time_clocks(
	self, 
	from_date: str|None=None, 
	to_date: str|None=None, 
	limit: int|None=None, 
	offset: int|None=None, 
	*, 
	company_id: int|None=None, 
	employee_id: int|None=None
	):
	endpoint_url = f"./employees/{employee_id}/time_clocks"
	query = dict(
		company_id=company_id,
		from_date=from_date,
		to_date=to_date,
		limit=limit,
		offset=offset,
		employee_id=employee_id,
	
	)
	return self.api_call(method="", endpoint_url=endpoint_url, query=query)


def get_employee_time_clocks_available_types(
	self, 
	date: str|None=None, 
	*, 
	company_id: int|None=None, 
	employee_id: int|None=None
	):
	endpoint_url = f"./employees/{employee_id}/time_clocks/available_types"
	query = dict(
		company_id=company_id,
		date=date,
		employee_id=employee_id,
	
	)
	return self.api_call(method="", endpoint_url=endpoint_url, query=query)


def get_employee_welfare_pension_insurance_rule(
	self, 
	*, 
	company_id: int|None=None, 
	year: int|None=None, 
	month: int|None=None, 
	employee_id: int|None=None
	):
	endpoint_url = f"./employees/{employee_id}/welfare_pension_insurance_rule"
	query = dict(
		company_id=company_id,
		year=year,
		month=month,
		employee_id=employee_id,
	
	)
	return self.api_call(method="", endpoint_url=endpoint_url, query=query)


def get_employee_work_record(
	self, 
	*, 
	company_id: int|None=None, 
	employee_id: int|None=None, 
	date: str|None=None
	):
	endpoint_url = f"./employees/{employee_id}/work_records/{date}"
	query = dict(
		company_id=company_id,
		employee_id=employee_id,
		date=date,
	
	)
	return self.api_call(method="", endpoint_url=endpoint_url, query=query)


def get_employee_work_record_summary(
	self, 
	work_records: bool|None=None, 
	*, 
	company_id: int|None=None, 
	employee_id: int|None=None, 
	year: int|None=None, 
	month: int|None=None
	):
	endpoint_url = f"./employees/{employee_id}/work_record_summaries/{year}/{month}"
	query = dict(
		company_id=company_id,
		work_records=work_records,
		employee_id=employee_id,
		year=year,
		month=month,
	
	)
	return self.api_call(method="", endpoint_url=endpoint_url, query=query)


def get_groups(
	self, 
	*, 
	company_id: int|None=None
	):
	endpoint_url = f"./groups"
	query = dict(
		company_id=company_id,
	
	)
	return self.api_call(method="", endpoint_url=endpoint_url, query=query)


def get_positions(
	self, 
	*, 
	company_id: int|None=None
	):
	endpoint_url = f"./positions"
	query = dict(
		company_id=company_id,
	
	)
	return self.api_call(method="", endpoint_url=endpoint_url, query=query)


def get_salaries_employee_payroll_statement(
	self, 
	*, 
	company_id: int|None=None, 
	year: int|None=None, 
	month: int|None=None, 
	employee_id: int|None=None
	):
	endpoint_url = f"./salaries/employee_payroll_statements/{employee_id}"
	query = dict(
		company_id=company_id,
		year=year,
		month=month,
		employee_id=employee_id,
	
	)
	return self.api_call(method="", endpoint_url=endpoint_url, query=query)


def get_salaries_employee_payroll_statements(
	self, 
	limit: int|None=None, 
	offset: int|None=None, 
	*, 
	company_id: int|None=None, 
	year: int|None=None, 
	month: int|None=None
	):
	endpoint_url = f"./salaries/employee_payroll_statements"
	query = dict(
		company_id=company_id,
		year=year,
		month=month,
		limit=limit,
		offset=offset,
	
	)
	return self.api_call(method="", endpoint_url=endpoint_url, query=query)


def get_users_me(self):
	endpoint_url = f"./users/me"
	return self.api_call(method="", endpoint_url=endpoint_url)


def get_yearend_adjustment_employee(
	self, 
	*, 
	company_id: int|None=None, 
	year: int|None=None, 
	employee_id: int|None=None
	):
	endpoint_url = f"./yearend_adjustments/{year}/employees/{employee_id}"
	query = dict(
		company_id=company_id,
		year=year,
		employee_id=employee_id,
	
	)
	return self.api_call(method="", endpoint_url=endpoint_url, query=query)


def get_yearend_adjustment_employees(
	self, 
	limit: int|None=None, 
	offset: int|None=None, 
	*, 
	company_id: int|None=None, 
	year: int|None=None
	):
	endpoint_url = f"./yearend_adjustments/{year}/employees"
	query = dict(
		company_id=company_id,
		year=year,
		limit=limit,
		offset=offset,
	
	)
	return self.api_call(method="", endpoint_url=endpoint_url, query=query)




if __name__ == "__main__":
    CLIENT_ID = "2612398b54dd2a73d45b51c2fdf3b12360fcbb40d346d2f0bb04c34e7bb383ef"
    CLIENT_SECRET = "f2b4272865b6fa0685f8ed0331bc9d2bd7e06a4c85eeb8a4d685bc4ab8bbd07b"
    REDIRECT_URI = "urn:ietf:wg:oauth:2.0:oob"
    
    human_resourse = HumanResourse(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI
    )
    me = human_resourse.get_users_me()
    company_id = me["companies"][0]["id"]

    add_emploee = human_resourse.create_employee(
        company_id=company_id,
        first_name="山田",
        last_name="太郎",
        first_name_kana="ヤマダ",
        last_name_kana="タロウ",
        birth_date="1997-06-21",
        entry_date="2024-01-28"
    )
    print(add_emploee)

