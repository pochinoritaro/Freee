from enum import Enum

#人事労務APIの列挙型
class WorkRecords:
    """勤怠の操作
    """
    class DayPttern(Enum):
        """勤務パターン
        Args:
            normal_day (str): 所定労働日
            prescribed_holiday (str): 所定休日
            legal_holiday (str): 法定休日
        """
        normal_day = "normal_day"
        prescribed_holiday = "normal_day"
        legal_holiday = "normal_day"

#会計APIの列挙型



