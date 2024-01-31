from bs4 import BeautifulSoup 
import requests
import pandas as pd    
import sqlite3
from datetime import datetime

url = 'https://web.archive.org/web/20230908091635 /https://en.wikipedia.org/wiki/List_of_largest_banks' 
db_name = "Banks.db"
table_attribs = ["Name", "MC_USD_Billion", "MC_GBP_Billion", "MC_EUR_Billion", "MC_INR_Billion"]
table_name = 'Largest_banks'
csv_path = '/home/jordans/Extract_transform_load/etl4/Largest_banks_data.csv'
count = 0 

def extract(url):
    html_page = requests.get(url).text
    data = BeautifulSoup(html_page, 'html.parser')
    heading = data.find('span', text='By market capitalization')
    table = heading.find_next('table')
    
    if table:
        rows = table.find_all('tr')
        extracted_data = []
        
        for row in rows:
            data = []
            cells = row.find_all(['th', 'td'])

            for cell in cells:
                data.append(cell.text.strip())
            print(data)
            extracted_data.append(data)

        table_headers = extracted_data[0]
        final_data = []

        for data_row in extracted_data[1:]:
            if len(data_row) == len(table_headers):
                final_data.append(data_row)

        df = pd.DataFrame(final_data, columns=table_headers)
       
        return df
    else:
        return None
    
    
target_file = "Largest_banks_data.csv"
log_file = "code_log.txt"
    
  
        
def transform(df):
    
    df['Market cap(US$ billion)'] = df['Market cap(US$ billion)'].astype('float')*0.10
    df['MC_EUR_Billion']=df['Market cap(US$ billion)']*0.93
    df["MC_GBP_Billion"]=df['Market cap(US$ billion)'] * 0.8
    df["MC_INR_Billion"]=df['Market cap(US$ billion)'] * 82.95
    return df       
    
if __name__ == "__main__": 
    df1 = extract(url)
    # print(df1)
    df2 = transform(df1)
    print(df2)
    #
    print (csv_path)  
    
   
   
    def load_to_data(df2, csv_path):
        df2.to_csv(csv_path)  
   
    load_to_data(df2, csv_path) 
    
    import sqlalchemy


    def load_to_db(df2, table_name, connection_string):
        
        #create an engine to connect the database 
         engine = sqlalchemy.create_engine(connection_string)
         df2.to_sql(table_name, conn=engine, if_exists='replace', index=False)
        
        
    # load_to_db(df2, 'Banks.db', 'Largest_banks')  
    
    
    
    def run_query(query_statement, sql_connection):
        print(query_statement)
        query_output = pd.read_sql(query_statement, sql_connection)
        print(query_output)

    
    def log_progress(message): 
        timestamp_format = '%Y-%h-%d-%H:%M:%S' 
        now = datetime.now()
        timestamp = now.strftime(timestamp_format) 
        with open(code_log.txt,"a") as f: 
            f.write(timestamp + ':' + message + '\n')
            
            
    log_progress("extraction")
    df = extract(url)

    
    











   
# def transform(df):
  
#     df = pd.DataFrame({'MC_USD_Billion': [0.8, 0.93, 82.95]})
#     # df_merged = pd.merge(df, exchange_rates, on="Currency")
#     df["MC_GBP_Billion"] = df["MC_USD_Billion"] * 0.8
#     df["MC_EUR_Billion"] = df["MC_USD_Billion"] * 0.93
#     df["MC_INR_Billion"] = df["MC_USD_Billion"] * 82.95
#     # df_transformed = df_merged[["Name", "MC_USD_Billion", "MC_GBP_Billion", "MC_EUR_Billion", "MC_INR_Billion"]]
#     # df_transformed = df_transformed.round(2)
#     # return df_transformed

# # df_transformed = transform(df)
# print(df)
