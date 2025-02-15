# ETL pipeline

## Introduction
This repository contains code from an ETL pipeline project I did in my bootcamp:

## Data Quality Audit
Before running the ETL pipeline, a [Data Quality Audit](https://github.com/Junyi116/etl-pipeline/blob/main/Data%20Quality%20Audit.ipynb) was performed to ensure the quality and accuracy of the data. This audit included:
- **Data Uniqueness**:  Identified duplicate records.
- **Data Completeness**:  Checked for and addressed any missing values in the data.
- **Data Validity**: Confirmed that data adhered to predefined formats and constraints.
- **Data Consistency**: Ensured consistency in data formats and values across datasets.
- **Data Timeliness**: Verified the data time range and frequency.
- **Data Preparation**: Ensured data quality and consistency before analysis.

## ETL Tasks
- [Extracts transactional data form a local database](https://github.com/Junyi116/etl-pipeline/blob/main/src/extract.py)
- [Identifies and removes duplicates](https://github.com/Junyi116/etl-pipeline/blob/main/src/transform.py)
- [Loads the transformed data to a s3 bucket](https://github.com/Junyi116/etl-pipeline/blob/main/src/transform.py)
- [Inserts the transformed data into the database](https://github.com/Junyi116/etl-pipeline/blob/main/src/data_insert.py)

## Requirements
- The minimum requirement is Python3 
- Import the necessary libraries as [here](https://github.com/Junyi116/etl-pipeline/blob/main/requirements.txt)

## Step by step:
1. Clone the repository, and change the directory to **etl-pipeline**:
   ```
   git clone https://github.com/Junyi116/etl-pipeline.git
   ```
2. Please contact me for a copy of the database if you do not have it, otherwise update the [file path](https://github.com/Junyi116/etl-pipeline/blob/5040b224b2ea434bcd8a655d5d57daf710a777eb/src/extract.py#L6) accordingly. 
3. Create a .env file with connection passwords in your  **etl-pipeline** folder, similar to [this](https://github.com/Junyi116/etl-pipeline/blob/main/.env.copy).
4. To execute the code to extract, transform and load data to s3, run the [`main.py`](https://github.com/Junyi116/etl-pipeline/blob/main/main.py) file:

   Mac users:
   ```
   python3 main.py
   ```

   Window users:
   ```
   python main.py
   ```

## Workflow Overview
Here is a workflow diagram illustrating the steps involved in the ETL process:

### ETL Workflow
![ETL Workflow Diagram](https://github.com/Junyi116/etl-pipeline/blob/main/Workflow/ETL.PNG)

For the analysis process following the ETL, refer to the Customer Segmentation repository.

### Analysis Workflow After ETL in Related Projects
![Analysis Workflow Diagram](https://github.com/Junyi116/etl-pipeline/blob/main/Workflow/Analysis.PNG)

## Related Projects
For the analysis process, you can check out my [Customer Segmentation Project](https://github.com/Junyi116/Customer_Segmentation).