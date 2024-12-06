import pandas as pd
from datetime import date as d
from datetime import datetime as dt
import sys
from langchain_anthropic import ChatAnthropic
from langchain.document_loaders import DataFrameLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import LLMChain

class Exp_Tracker:
    def __init__(self):
        self.df = pd.read_csv('exp_page.csv')

        self.li_page = ['Show Table','Make an Entry','Sum of Transactions','Ask AI','Exit System']
        self.li_func = ['self.show_table()','self.append_rows()','self.sum_rows()','self.Ask()','sys.exit()']

    def show_table(self):
        print(self.df)
        self.page()

            
    def page(self):
        print('\n')
        for i in range(1,len(self.li_page)+1):
                print(f'{i} - ',self.li_page[i-1])

        try:
            ch = int(input('\nEnter the Choice ->'))
            if 0 < ch <= len(self.li_func):
                return eval(self.li_func[ch - 1])
            else:
                print('Invalid Entry')
               
        except Exception as e:
            print(f'Error - {e}')
            print('Try Again')
        
        self.page()
        
    def append_rows(self):
        x = len(self.df.index)
        dt = d.today()
        tr = input('Enter the Transcation Details ->')
        am = float(input('Enter the  Amount ->'))
        
        self.df.loc[x] = [dt,tr,am]
        try:
            self.df.to_csv('exp_page.csv',index=False)
            print('Entry is made in the File')
          
        except Exception as e:
            print(f'Error - {e}')
            print('Try Again')
        
        self.page()

    def sum_rows(self):
        print('format(yyyy-mm-dd)')

        start_date = input('Enter the Start Date ->')
        end_date = input('Enter the End Date ->')

        try:

            start_date = dt.strptime(start_date, '%Y-%m-%d').date()
            end_date = dt.strptime(end_date, '%Y-%m-%d').date()

            if start_date < end_date:
                print('Start Date should be before End Date')
                return self.sum_rows()

            mask = (self.df['Date'] >= start_date) & (self.df['Date'] <= end_date)
            filtered_data = self.df.loc[mask]
            print(filtered_data['Amount'].sum())

            
        except Exception as e:
            print(f'Error - {e}')
            print('Try Again')

        self.page()
        
    def AI(self):
        model = ChatAnthropic(model="claude-3-5-sonnet-20240620",api_key="")

        loader = DataFrameLoader(self.df)
        documents = loader.load()

        prompt = """ 
        You are given a table of transactions with the following columns: Date, Transaction, and Amount.
        Here are the details of your transactions:
        {data}

        Now, I need to answer this question for user: {question}

        Output: 
        """

        prompt_template = ChatPromptTemplate.from_template(prompt)
        chain = LLMChain(llm=model, prompt=prompt_template)
    
        response = chain.run({"data": documents, "question": self.user_input})
        print(response)
        
        self.page()

    def Ask(self):
        self.user_input = input('Ask a question to AI ->').lower()

        if self.user_input == 'stop':
            sys.exit()

        self.AI()

v = Exp_Tracker()
v.page()
