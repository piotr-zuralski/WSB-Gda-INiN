from datetime import datetime


class Holiday:
    def __init__(self, date, local_name, name):
        self.date = datetime.strptime(date, "%Y-%m-%d")
        self.local_name = local_name
        self.name = name
    
    def __repr__(self):
        return f"{self.local_name} ({self.date.year})"
