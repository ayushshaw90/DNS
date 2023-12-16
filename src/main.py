import pandas as pd
import numpy as np
from utils.data_preprocessor import preprocess_data_of_dataset
from utils.json_to_csv_converter import json_to_csv_converter_dataset
from utils.make_dataset import generate_dataset_from_csv_dns_response
from utils.split_dataset_into_train_and_test import train_and_test_data_splitter
from sklearn.preprocessing import StandardScaler


def main():  
    
    #CONVERT JSON RESPONSE TO CSV DATASET.
    json_to_csv_converter_dataset()# converts the json datasets to csv datasets

    #GENERATE FEATURE RICH DATASET FROM CSV DNS DATASETS.
    generate_dataset_from_csv_dns_response() # generates the feature rich dataset from the csv datasets

    #LOAD THE FEATURE RICH DATASET
    df = pd.read_csv(r'data/generated_dataset_from_dns_response.csv')

    #PREPROCESS THE DATASET
    df = preprocess_data_of_dataset(df)

    #SPLIT THE DATASET INTO TRAIN AND TEST
    X_train, X_test, y_train, y_test = train_and_test_data_splitter(df) 

    #perform standardization to scale the data
    X_train, X_test, scaler = perform_standardization(X_train, X_test)

    #-----------------------------------#


    # # Preprocess incoming data (using the preprocessor object or pipeline created during training)
    # preprocessed_input_data = preprocessor.transform(input_data)  # Adjust based on your preprocessor object or pipeline

    # # Load the trained model
    # loaded_model = load_model('path/to/saved_model.pkl')  # Replace 'load_model' with your specific model loading function

    # # Make predictions
    # predictions = loaded_model.predict(preprocessed_input_data)
    # # You might have probabilities, classes, or continuous values depending on the model used





     
def perform_standardization(X_train, X_test):
    scaler = StandardScaler().fit(X_train)
    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)
    return X_train, X_test, scaler
    
if __name__ == "__main__":
    main()
