from fastapi import APIRouter, UploadFile, File
import pandas as pd
from deps import schemas 
from deps.analysis import *
import math
import pandas as pd
import os
import datetime
from sklearn import preprocessing


router = APIRouter()

@router.get('/')
def index():
    return {'data': 'This API is for Analyzing data'}

@router.post('/getRFM', response_model=schemas.RFMresponse)
def getRFM(file: UploadFile = File(...)):
    file_name, file_extension = os.path.splitext(file.filename)
    if file_extension == ".xlsx":
        cs_df = pd.read_excel(file.file._file)

        #drop not used columns
        remove_columns(cs_df)

        #convert the data type of InvoiceDate column from str to datetime
        cs_df['InvoiceDate']= pd.to_datetime(cs_df['InvoiceDate'])

        #create a new pandas dataframe called customer_history_df
        #calculate the recency and add its column to the customer_history_df
        refrence_date = cs_df.InvoiceDate.max() + datetime.timedelta(days = 1)
        #print('Reference Date:', refrence_date)
        cs_df['days_since_last_purchase'] = (refrence_date - cs_df.InvoiceDate).astype('timedelta64[D]')
        customer_history_df =  cs_df[['CustomerID', 'days_since_last_purchase']].groupby("CustomerID").min().reset_index()
        customer_history_df.rename(columns={'days_since_last_purchase':'recency'}, inplace=True)
        customer_history_df.describe().transpose()

        #calculate the frequency and add its column to the customer_history_df
        customer_freq = (cs_df[['CustomerID', 'InvoiceNo']].groupby(["CustomerID", 'InvoiceNo']).count().reset_index()).\
        groupby(["CustomerID"]).count().reset_index()
        customer_freq.rename(columns={'InvoiceNo':'frequency'},inplace=True)
        customer_history_df = customer_history_df.merge(customer_freq)

        #calculate the monetary and add its column(amount) to the customer_history_df
        customer_monetary_val = cs_df[['CustomerID', 'amount']].groupby("CustomerID").sum().reset_index()
        customer_history_df = customer_history_df.merge(customer_monetary_val)

        #drop all 0s rows
        customer_history_df = customer_history_df[customer_history_df['amount'] != 0]

        #One of the requirements for proper functioning of the algorithm is the mean centering of the variable values. 
        # Mean centering of a variable value means that we will replace the actual value of the variable with a standardized value, 
        # so that the variable has a mean of 0 and variance of 1.
        customer_history_df['recency_log'] = customer_history_df['recency'].apply(math.log)
        customer_history_df['frequency_log'] = customer_history_df['frequency'].apply(math.log)
        customer_history_df['amount_log'] = customer_history_df['amount'].apply(math.log)
        feature_vector = ['amount_log', 'recency_log','frequency_log']
        X_subset = customer_history_df[feature_vector] #.as_matrix()
        scaler = preprocessing.StandardScaler().fit(X_subset)
        X_scaled = scaler.transform(X_subset)
        
        #k-means algorithm
        model = k_mean(X_scaled)
      
        
        return {
        'recency_log': customer_history_df['recency_log'].tolist(),
        'frequency_log': customer_history_df['frequency_log'].tolist(),
        'amount_log': customer_history_df['amount_log'].tolist(),
        'lables': model.labels_.tolist()
        }

    return {"data": 'you have to upload xlxs files only'}