import pandas as pd
from anonymizedf.anonymizedf import anonymize
import re
from switch import Switch


class Anonymized:
    def __init__(self,file_loc) -> None:
        self.df = pd.read_csv(file_loc)
        self.an = anonymize(df=self.df)

    def fake_dfs(self,col_name,col_type):
        # fake_df = pd.DataFrame()    
        if col_type == "id":
            fake_df = (
            self.an
            # .fake_names("Customer Name", chaining=True)
            .fake_ids("Customer ID", chaining=True)
            .fake_whole_numbers("Loyalty Reward Points", chaining=True)
            .fake_categories(col_name, chaining=True)
            .fake_dates("Date", chaining=True)
            .fake_decimal_numbers("Fraction", chaining=True)
            .show_data_frame()
            )
            fake_df.to_csv("fake_customers2.csv", index=False)
              
    def col_type(self):  
        col = self.df.columns
        for c in col:
            type_col = self.df[c].dtypes
            data_value = self.df[c].iloc[0]
            if type_col == 'object':
                if 'name' in c.lower():
                    pass                       
                if 'id' in c.lower():
                    self.fake_dfs(c,col_type="id")
    
                match = re.search(r'\d{1,4}[.,/,-]\d{1,4}[.,/,-]\d{1,4}',data_value)
                if match:
                    return c
                else:
                    print("obj")
            if type_col == "int64":
                return c
            if type_col == "float64":
                return c



if __name__ =="__main__":

        # Import the data
        anon = Anonymized(file_loc="https://query.data.world/s/shcktxndtu3ojonm46tb5udlz7sp3e")
        anon.col_type()
    
        # anon.col_anon("one")
        # df = pd.read_csv("https://query.data.world/s/shcktxndtu3ojonm46tb5udlz7sp3e")
        # df = pd.read_csv("fake_customers.csv")
        # anon.col_anon("Customer Name",76.5)


        # Prepare the data to be anonymized
        # an = anonymize(df)

        # Select what data you want to anonymize and your preferred style

        # Example 1 - just updates df
        # an.fake_names("Customer Name")
        # an.fake_ids("Customer ID")
        # an.fake_whole_numbers("Loyalty Reward Points")
        # an.fake_categories("Segment")
        # an.fake_dates("Date")
        # an.fake_decimal_numbers("Fraction")

        # Example 2 - method chaining
        # fake_df = (
        # an
        # # .fake_names("Customer Name", chaining=True)
        # .fake_ids("Customer ID", chaining=True)
        # .fake_whole_numbers("Loyalty Reward Points", chaining=True)
        # .fake_categories("Segment", chaining=True)
        # .fake_dates("Date", chaining=True)
        # .fake_decimal_numbers("Fraction", chaining=True)
        # .show_data_frame()
        # )
        # fake_df.to_csv("fake_customers4.csv", index=False)