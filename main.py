import os
# only for running the code from command line
from dotenv import load_dotenv
#loaded the enviroment variables
load_dotenv()

from src.extract import extract_transactional_data
from src.transform import identify_and_remove_duplicates
from src.load_to_s3 import load_df_to_s3

# fetch the environment variables from the .env file using the getenv function
aws_access_key=os.getenv("aws_access_key")
aws_secret_access_key=os.getenv("aws_secret_access_key")
aws_s3_bucket="waia-march-bootcamp"

print(aws_access_key)

# extracting the online transaction data from the tables in th database
ot_transformed=extract_transactional_data()
print(ot_transformed.shape)

#remove the duplicates
ot_wout_duplicates=identify_and_remove_duplicates(ot_transformed)

# load the data to s3
key="etl/jz_online_trans_final.csv"
load_df_to_s3(ot_wout_duplicates,key,aws_s3_bucket,aws_access_key,aws_secret_access_key)