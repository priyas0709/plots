import matplotlib.pyplot as plt
import pandas as pd

class AdverseVisualizer:
    @staticmethod
    def adverse_event_and_gender(adverseData: pd.DataFrame):
        """ Create plots """
        plt.bar(adverseData['CI_Gender'], adverseData['RA_Report #'], color='skyblue')

        plt.xlabel('Gender')
        plt.ylabel('Report #')
        plt.title('Bar Graph Example')
        plt.show()
