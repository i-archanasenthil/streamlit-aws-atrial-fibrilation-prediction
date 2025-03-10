**Scenario:** Developing an application to predict the risk of atrial fibrillation (AF) in individuals.

## Functional Requirements:

**Data:**

Previous historical data is needed to help train a deep learning neural network model using pytorch or tensor flow to predict the likelihood of a person to experience Atrial Fibrilation 

A data from the SSC society has been generated with baseline ECG reading and medication history from January 2010 to January 2023 to help train the risk prediction model. The following details are captured in the database:
  - Patient ID
  - Gender
  - Age
  - Disease History
  - ECG readings 
  - medication history

Link to the metadata: https://github.com/i-archanasenthil/streamlit-aws-atrial-fibrilation-prediction/blob/main/data_dictionary.csv
    
**Applications/ Software:**

Google Colab **Jupter Notebook** with python **version Python 3.11.11** to facilitate building a deep learning model.

**Amazon Web Services** user credentials with **EC2 instance** with enough compute power to run the deep learning model by atleast 1000 users at the same time and generate graphs and dashboards for the **web application** through Streamlit.

**s3 storage bucket** to help store the results of the data entered for the patient and also to utilize the graphs, dashboards for our analysis.


