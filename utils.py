from datetime import datetime, timedelta

class Utils:
    def get_date(self) -> str:
        yesterday = datetime.now() - timedelta(1)
        return yesterday.strftime("%Y-%m-%d")
