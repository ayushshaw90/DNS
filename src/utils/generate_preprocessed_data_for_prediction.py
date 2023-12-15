import pandas as pd
from datetime import datetime
from sklearn.preprocessing import StandardScaler
import category_encoders as ce
from sklearn.preprocessing import train_test_split

def preprocess_data_of_dataset():
     df = pd.read_csv(r'data/generated_dataset_from_dns_response.csv')
     
     #1. Drop unnecessary columns
     df = drop_unnecessary_columns(df)

     #2. handling date columns
     df = handling_date_columns(df)
     
     #3. drop date columns
     df = drop_unnecessary_date_columns(df)

     #4. handling missing values
     df = handling_missing_values(df)

     #5. perform binary encoding
     df = perform_label_encoding(df)

     #6. split data into train and test
     X_train, X_test, y_train, y_test = split_data_into_train_and_test(df)

     #7. perform standardization to scale the data
     # Now, apply the standardization
     X_train, X_test, scaler = perform_standardization(X_train, X_test)

     return X_train, X_test, y_train, y_test, scaler

def drop_unnecessary_columns(df):
     columns_to_be_dropped = [col for col in df.columns if col.startswith('NS')]
     columns_to_be_dropped.append('full_domain')
     #columns_to_be_dropped.append('tld')
     columns_to_be_dropped.append('ipv4_address')
     columns_to_be_dropped.append('ipv6_address')
     df = df.drop(columns_to_be_dropped, axis=1)
     return df

def drop_unnecessary_date_columns(df):
     columns_to_be_dropped = ['creation_date','last_updated_date','expiration_date']
     columns_to_be_dropped.append('domain_expired')

     df = df.drop(columns_to_be_dropped, axis=1)
     return df

def handling_date_columns(df):
     current_date = datetime.now()

     # Convert 'creation_date' and 'expiration_date' columns to datetime
     df['creation_date'] = pd.to_datetime(df['creation_date'])
#df['last_updated_date'] = pd.to_datetime(df['last_updated_date'])
     df['expiration_date'] = pd.to_datetime(df['expiration_date'])

     df['days_since_creation'] = (current_date - df['creation_date']).dt.days
     #df['days_since_last_updated'] = (current_date - df['last_updated_date']).dt.days

     # Calculate days left to expire and mark expired domains
     df['days_left_to_expire'] = (df['expiration_date'] - current_date).dt.days
     df.loc[df['days_left_to_expire'] < 0, 'days_left_to_expire'] = 0

     # Mark the expired domains (if expiration_date < current_date)
     df['domain_expired'] = df['expiration_date'] < current_date

     return df

def handling_missing_values(df):
     df['A_response_country_code'] = df['A_response_country_code'].fillna('XX')
     df['AAAA_response_country_code'] = df['AAAA_response_country_code'].fillna('XX')
     df['days_since_creation'] = df['days_since_creation'].fillna(-1)
     df['days_left_to_expire'] = df['days_left_to_expire'].fillna(-1)
     df['organization_name'] = df['organization_name'].fillna('NAA')
     df['has_organization_name'] = df['has_organization_name'].fillna(-1)

def perform_label_encoding(df):
     encoder = ce.BinaryEncoder(cols=['tld','A_response_country_code','AAAA_response_country_code','organization_name'])
     df = encoder.fit_transform(df)
     df = df.drop(['tld','A_response_country_code','AAAA_response_country_code','organization_name'], axis=1)
     return df

def perform_standardization(X_train, X_test):
    scaler = StandardScaler().fit(X_train)
    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)
    return X_train, X_test, scaler

def split_data_into_train_and_test(df):
     X = df.drop('label',axis=1)
     y = df['label']

     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

     return X_train, X_test, y_train, y_test

