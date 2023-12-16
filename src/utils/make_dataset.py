import pandas as pd
from utils.generate_domain_name_features import extract_domain_name_features
from utils.generate_response_related_features import extract_features_from_response
from utils.generate_whois_features import get_domain_info
from utils.dga_domain_name_preprocessor import get_feature_rich_row

def generate_dataset_from_csv_dns_response():

     # Load original dataset
    df_normal = pd.read_csv(r'data/dnsdata_top_domains.csv')
    df_malicious = pd.read_csv(r'data/malicious_domain_response.csv')
    
    df_normal['label'] = 0
    df_malicious['label'] = 1
    
    # Concatenate the dataframes
    df = pd.concat([df_normal, df_malicious])

    # Shuffle the rows
    df = df.sample(frac=1).reset_index(drop=True)
    
    df = df.drop_duplicates(subset=['domain_name'])

    df = df[df['domain_name'].notna() & (df['domain_name'] != '')]

    df = df[df['A__ip_address'].notna()]
    
    df = df.drop(['A', 'AAAA', 'MX', 'NS', 'SOA', 'CNAME', 'TXT', 'SRV', 'PTR'], axis=1)

    #GENERATE FEATURES FOR DATASET FROM DNS RESPONSE & DOMAIN NAME
    dataset = []
    
    for index, row in df.iterrows():
      #capturing the features for each row
      features_row =  generate_features_for_dataset_from_response(row)
      dataset.append(features_row)
    
    dataset_df = pd.DataFrame(dataset)

    dataset_df.to_csv(r'data/generated_dataset_from_dns_response.csv', index=False)
    #--------the dataset is generated and saved in the data folder----------------------#

#------------------------------------------------------------------------------------#
    
#this method takes one row from the dataframe and generates a row of features for it
def generate_features_for_dataset_from_response(df_series):
   df = df_series.to_frame().transpose()
   print(df)
   merged_dict = {}
   
   dict1 = {}
   dict1 = extract_domain_name_features(df['domain_name'].iloc[0])
   #print('dict1############\n')
   print(dict1)
   
   dict2 = {}  
   dict2 = extract_features_from_response(df)
  # print('dict3############\n')
  # print(dict2)

   dict3 = {}
   dict3 = get_domain_info(df['domain_name'].iloc[0])
   #print('dict3############\n')
   #print(dict3)

   merged_dict = {**dict1, **dict2, **dict3}
  # print(merged_dict)
   return merged_dict