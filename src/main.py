import pandas as pd
from utils.generate_domain_name_features import extract_domain_features

def main():  
    
    # Load original dataset
    df_normal = pd.read_csv(r'data/dnsdata_top_domains.csv')
    df_malicious = pd.read_csv(r'data/malicious_domain_response.csv')
    
    df_normal['label'] = 0
    df_malicious['label'] = 1 
    
    # Concatenate the dataframes
    df = pd.concat([df_normal, df_malicious])

    # Shuffle the rows
    df = df.sample(frac=1).reset_index(drop=True)
    df.drop('CNAME__-',axis=1,inplace=True)
    
    df = df.drop_duplicates(subset=['domain_name'])
    
    df = df.drop(['A', 'AAAA', 'MX', 'NS', 'SOA', 'CNAME', 'TXT', 'SRV', 'PTR'], axis=1)
    
    ###### Generating features by analysing the domain name ######
    
    dict = {}
    dict = extract_domain_features('xxxxxxxxxxxxxxxxxxxxx.xmail.google.com')
    #print(df.head(1))
    print(dict)
    
    # Save the new dataset
    # original_dataset.to_csv('data/output/new_dataset.csv', index=False)

if __name__ == "__main__":
    main()
