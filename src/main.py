import pandas as pd
from utils.data_processing import extract_domain_features

def main():
    # Load original dataset
    df = pd.read_csv(r'data/input_data/only_non_malicious.txt')
    
    #dropping all the duplicate domains
    df = df.drop_duplicates(subset=['DomainName'])
    # Extract features
    df_new = df.head(10)
    df_new['DomainFeatures'] = df_new['DomainName'].apply(extract_domain_features)
    df_new.head()

    # Save the new dataset
  #  original_dataset.to_csv('data/output/new_dataset.csv', index=False)

if __name__ == "__main__":
    main()
