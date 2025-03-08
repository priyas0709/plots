import pandas as pd

class LoanRepository:
    def __init__(self):
        self.loanData = None

    def get_loan_data(self) -> pd.DataFrame:
        """Fetch data"""
        if self.loanData is None:
            self.loanData = pd.read_csv("Loan_Defaul.csv")
        return self.loanData
