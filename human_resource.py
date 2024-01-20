from freee_enums import WorkRecords
from freee_sdk import BaseClient

class HumanResourse(BaseClient):
    API_URL = "hr"

    def update_employee_work_record(
        self,
        clock_in_at: str=None,
        clock_out_at: str=None,
        day_pattern: WorkRecords.DayPttern=None,
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
            
            day_pattern (WorkRecords.DayPttern, optional): 勤務パターン. Defaults to None.
                prescribed_holiday、legal_holidayを指定すると、以下のパラメータについて、指定した値が反映されず無視されます。
                    - early_leaving_mins
                    - lateness_mins
                    - paid_holiday
            
            early_leaving_mins (int, optional): 早退分の時間（分単位）. Defaults to None.
            
            is_absence (bool, optional): 欠勤かどうか. Defaults to None.
                trueを指定すると、以下のパラーメータについて、指定した値が反映されず無視されます。
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
                指定しない場合はデフォルト設定が使用されます。（デフォルト設定は従業員に設定した勤務賃金設定の出退勤時刻と労働時間の設定を参照して値が決まります。）
            
            normal_work_clock_out_at (str, optional): 所定労働終了時刻. Defaults to None.
                指定しない場合はデフォルト設定が使用されます。（デフォルト設定は従業員に設定した勤務賃金設定の出退勤時刻と労働時間の設定を参照して値が決まります。）
            
            normal_work_mins (int, optional): 所定労働時間. Defaults to None.
                指定しない場合はデフォルト設定が使用されます。（デフォルト設定は従業員に設定した勤務賃金設定の出退勤時刻と労働時間の設定を参照して値が決まります。）
            
            note (str, optional): 勤怠メモ. Defaults to None.
            
            paid_holiday (bool, optional): この日の有休取得日数。1日単位で指定します。. Defaults to None.
            
            half_paid_holiday_mins (int, optional): 有給休暇の半休を利用した時間（分単位）. Defaults to None.
            
            hourly_paid_holiday_mins (int, optional): 有給休暇の時間休を利用した時間（分単位）. Defaults to None.
            
            special_holiday (bool, optional): この日の特別休暇取得日数。1日単位で指定します。. Defaults to None.
            
            special_holiday_setting_id (int, optional): 特別休暇設定ID. Defaults to None.
            
            half_special_holiday_mins (int, optional): 特別休暇の半休を利用した時間（分単位）. Defaults to None.
            
            hourly_special_holiday_mins (int, optional): 特別休暇の時間休を利用した時間（分単位）. Defaults to None.
            
            use_attendance_deduction (bool, optional): 欠勤・遅刻・早退を控除対象時間に算入するかどうか. Defaults to None.
            
            use_default_work_pattern (bool, optional): デフォルトの勤務設定を使うかどうか. Defaults to None.
                trueを指定した場合、以下のパラメータについて、指定した値に関係なく、従業員に設定した勤務賃金設定の休日の設定を参照して値が決まります
                    - day_pattern
                
                trueを指定した場合、以下のパラメータについて、指定した値に関係なく、従業員に設定した勤務賃金設定の出退勤時刻と労働時間の設定を参照して値が決まります。
                    - normal_work_clock_in_at
                    - normal_work_clock_out_at
                    - normal_work_mins
        """
        endpoint_url = f"/api/v1/employees/{employee_id}/work_records/{date}"
        pass

if __name__ == "__main__":
    human_resourse = HumanResourse()
    print(human_resourse.request_url)