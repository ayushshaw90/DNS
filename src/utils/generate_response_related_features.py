import pandas as pd
import numpy as np

def extract_features_from_response(df):
     features = {}
      
     features['ipv4_address'] = df['A__ip_address'].iloc[0]

     features['A_response_country_code'] = df['A__country_code'].iloc[0] if df['A__country_code'].notna().any() else None

     features['has_AAAA_response'] = 1 if df['AAAA__ip_address'].notna().any() else 0

     features['ipv6_address'] = df['AAAA__ip_address'].iloc[0] if df['AAAA__ip_address'].notna().any() else None

     features['AAAA_response_country_code'] = df['AAAA__country_code'].iloc[0] if df['AAAA__country_code'].notna().any() else None

     features['has_TXT_response'] = 1 if df['TXT__001'].notna().any() else 0

     features['has_MX_response'] = 1 if df['MX__001'].notna().any() else 0

     features['has_NS_response'] = 1 if df['NS__001'].notna().any() else 0

     features['number_of_TXT_responses'] = count_number_of_TXT_responses(df)

     features['number_of_MX_responses'] = count_number_of_MX_responses(df)

     features['number_of_NS_responses'] = count_number_of_NS_responses(df)

     features['NS__001'] = df['NS__001'].iloc[0] if df['NS__001'].notna().any() else None

     features['NS__002'] = df['NS__002'].iloc[0] if df['NS__002'].notna().any() else None

     features['NS__003'] = df['NS__003'].iloc[0] if df['NS__003'].notna().any() else None
     
     features['NS__004'] = df['NS__004'].iloc[0] if df['NS__004'].notna().any() else None
     
     features['NS__005'] = df['NS__005'].iloc[0] if df['NS__005'].notna().any() else None
     
     features['NS__006'] = df['NS__006'].iloc[0] if df['NS__006'].notna().any() else None
     
     features['NS__007'] = df['NS__007'].iloc[0] if df['NS__007'].notna().any() else None
     
     features['NS__008'] = df['NS__008'].iloc[0] if df['NS__008'].notna().any() else None
    
     return features

def count_number_of_TXT_responses(df):
    txt_columns = [col for col in df.columns if col.startswith('TXT')]
    count_non_null_values = 0
    for col in txt_columns:
        count_non_null_values += df[col].count()

    return count_non_null_values

def count_number_of_MX_responses(df):
    mx_columns = [col for col in df.columns if col.startswith('MX')]
    count_non_null_values = 0
    for col in mx_columns:
        count_non_null_values += df[col].count()

    return count_non_null_values

def count_number_of_NS_responses(df):
    ns_columns = [col for col in df.columns if col.startswith('NS')]
    count_non_null_values = 0
    for col in ns_columns:
        count_non_null_values += df[col].count()

    return count_non_null_values

