import pandas as pd

class AdverseRepository:
    def __init__(self):
        self.adverseData = None

    def get_adverse_data(self) -> pd.DataFrame:
        """Fetch data"""
        if self.adverseData is None:
            self.adverseData = pd.read_csv("data/Adverse_Events.csv")
        return self.adverseData
