def get_approval_flow_route(
	self, 
	*, 
	id: int|None=None, 
	company_id: int|None=None):
	endpoint_url = "/api/v1/approval_flow_routes/{id}"
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
	company_id: int|None=None):
	endpoint_url = "/api/v1/approval_flow_routes"
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
	id: int|None=None):
	endpoint_url = "/api/v1/approval_requests/monthly_attendances/{id}"
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
	company_id: int|None=None):
	endpoint_url = "/api/v1/approval_requests/monthly_attendances"
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
	id: int|None=None):
	endpoint_url = "/api/v1/approval_requests/overtime_works/{id}"
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
	company_id: int|None=None):
	endpoint_url = "/api/v1/approval_requests/overtime_works"
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
	id: int|None=None):
	endpoint_url = "/api/v1/approval_requests/paid_holidays/{id}"
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
	company_id: int|None=None):
	endpoint_url = "/api/v1/approval_requests/paid_holidays"
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
	id: int|None=None):
	endpoint_url = "/api/v1/approval_requests/special_holidays/{id}"
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
	company_id: int|None=None):
	endpoint_url = "/api/v1/approval_requests/special_holidays"
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
	id: int|None=None):
	endpoint_url = "/api/v1/approval_requests/work_times/{id}"
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
	company_id: int|None=None):
	endpoint_url = "/api/v1/approval_requests/work_times"
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
	employee_id: int|None=None):
	endpoint_url = "/api/v1/bonuses/employee_payroll_statements/{employee_id}"
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
	month: int|None=None):
	endpoint_url = "/api/v1/bonuses/employee_payroll_statements"
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
	company_id: int|None=None):
	endpoint_url = "/api/v1/companies/{company_id}/employees"
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
	id: int|None=None):
	endpoint_url = "/api/v1/employees/{id}"
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
	month: int|None=None):
	endpoint_url = "/api/v1/employees"
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
	employee_id: int|None=None):
	endpoint_url = "/api/v1/employees/{employee_id}/special_holidays"
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
	employee_id: int|None=None):
	endpoint_url = "/api/v1/employees/{employee_id}/bank_account_rule"
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
	employee_id: int|None=None):
	endpoint_url = "/api/v1/employees/{employee_id}/basic_pay_rule"
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
	employee_id: int|None=None):
	endpoint_url = "/api/v1/employees/{employee_id}/dependent_rules"
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
	base_date: str|None=None):
	endpoint_url = "/api/v1/employee_group_memberships"
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
	employee_id: int|None=None):
	endpoint_url = "/api/v1/employees/{employee_id}/health_insurance_rule"
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
	employee_id: int|None=None):
	endpoint_url = "/api/v1/employees/{employee_id}/profile_custom_fields"
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
	employee_id: int|None=None):
	endpoint_url = "/api/v1/employees/{employee_id}/profile_rule"
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
	id: int|None=None):
	endpoint_url = "/api/v1/employees/{employee_id}/time_clocks/{id}"
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
	employee_id: int|None=None):
	endpoint_url = "/api/v1/employees/{employee_id}/time_clocks"
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
	employee_id: int|None=None):
	endpoint_url = "/api/v1/employees/{employee_id}/time_clocks/available_types"
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
	employee_id: int|None=None):
	endpoint_url = "/api/v1/employees/{employee_id}/welfare_pension_insurance_rule"
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
	date: str|None=None):
	endpoint_url = "/api/v1/employees/{employee_id}/work_records/{date}"
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
	month: int|None=None):
	endpoint_url = "/api/v1/employees/{employee_id}/work_record_summaries/{year}/{month}"
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
	company_id: int|None=None):
	endpoint_url = "/api/v1/groups"
	query = dict(
		company_id=company_id,
	
	)
	return self.api_call(method="", endpoint_url=endpoint_url, query=query)


def get_positions(
	self, 
	*, 
	company_id: int|None=None):
	endpoint_url = "/api/v1/positions"
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
	employee_id: int|None=None):
	endpoint_url = "/api/v1/salaries/employee_payroll_statements/{employee_id}"
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
	month: int|None=None):
	endpoint_url = "/api/v1/salaries/employee_payroll_statements"
	query = dict(
		company_id=company_id,
		year=year,
		month=month,
		limit=limit,
		offset=offset,
	
	)
	return self.api_call(method="", endpoint_url=endpoint_url, query=query)


def get_users_me(self):
	endpoint_url = "/api/v1/users/me"
	return self.api_call(method="", endpoint_url=endpoint_url)


def get_yearend_adjustment_employee(
	self, 
	*, 
	company_id: int|None=None, 
	year: int|None=None, 
	employee_id: int|None=None):
	endpoint_url = "/api/v1/yearend_adjustments/{year}/employees/{employee_id}"
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
	year: int|None=None):
	endpoint_url = "/api/v1/yearend_adjustments/{year}/employees"
	query = dict(
		company_id=company_id,
		year=year,
		limit=limit,
		offset=offset,
	
	)
	return self.api_call(method="", endpoint_url=endpoint_url, query=query)


