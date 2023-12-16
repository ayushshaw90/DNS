import json
import pandas as pd

#this method converts the json dataset to csv
def json_to_csv_converter_dataset():
    json_file_path_top_domains= r'data/dnsdata_top_domains.json'
    json_file_path_malicious_domains = r'data/malicious_domain_response.json'

    with open(json_file_path_top_domains) as file:
        json_response_normal = json.load(file)

    convert_json_response_to_csv(json_response_normal,False)

    with open(json_file_path_malicious_domains) as file:
        json_response_malicious = json.load(file)

    convert_json_response_to_csv(json_response_malicious,True)


#helper method to convert json dataset to csv
def convert_json_response_to_csv(json_response,isMalicious):
  # json_response = json.loads(json_response_string)
   data = []
   for record in json_response['response']:
    print(type(record)) 
    row = {
        'A': None,
        'AAAA': None,
        'A__ip_address': record.get('A')[0]['ip_address'] if record.get('A') and record.get('A')[0] else None,
        'A__country_code': record.get('A')[0]['country_code'] if record.get('A') and record.get('A')[0] else None,
        'A__asn_date': record.get('A')[0]['asn_date'] if record.get('A') and record.get('A')[0] else None,
        'A__reg_timestamp': record.get('A')[0]['reg_timestamp'] if record.get('A') and record.get('A')[0] else None,
        'A__last_updated': record.get('A')[0]['last_updated'] if record.get('A') and record.get('A')[0] else None,
        'AAAA__ip_address': record.get('AAAA')[0]['ip_address'] if record.get('AAAA') and record.get('AAAA')[0] else None,
        'AAAA__country_code': record.get('AAAA')[0]['country_code'] if record.get('AAAA') and record.get('AAAA')[0] else None,
        'AAAA__asn_date': record.get('AAAA')[0]['asn_date'] if record.get('AAAA') and record.get('AAAA')[0] else None,
        'AAAA__reg_timestamp': record.get('AAAA')[0]['reg_timestamp'] if record.get('AAAA') and record.get('AAAA')[0] else None,
        'AAAA__last_updated': record.get('AAAA')[0]['last_updated'] if record.get('AAAA') and record.get('AAAA')[0] else None,
        'MX': None,
        'NS': None,
        'SOA': None,
        'MX__001': record.get('MX')[0] if record.get('MX') and len(record.get('MX')) > 0 else None,
        'MX__002': record.get('MX')[1] if record.get('MX') and len(record.get('MX')) > 1 else None,
        'MX__003': record.get('MX')[2] if record.get('MX') and len(record.get('MX')) > 2 else None,
        'MX__004': record.get('MX')[3] if record.get('MX') and len(record.get('MX')) > 3 else None,
        'MX__005': record.get('MX')[4] if record.get('MX') and len(record.get('MX')) > 4 else None,
        'MX__006': record.get('MX')[5] if record.get('MX') and len(record.get('MX')) > 5 else None,
        'MX__007': record.get('MX')[6] if record.get('MX') and len(record.get('MX')) > 6 else None,
        'MX__008': record.get('MX')[7] if record.get('MX') and len(record.get('MX')) > 7 else None,
        # Add more columns for MX__002, MX__003, and so on as needed
        'NS__001': record.get('NS')[0] if record.get('NS') and len(record.get('NS')) > 0 else None,
        'NS__002': record.get('NS')[1] if record.get('NS') and len(record.get('NS')) > 1 else None,
        'NS__003': record.get('NS')[2] if record.get('NS') and len(record.get('NS')) > 2 else None,
        'NS__004': record.get('NS')[3] if record.get('NS') and len(record.get('NS')) > 3 else None,
        'NS__005': record.get('NS')[4] if record.get('NS') and len(record.get('NS')) > 4 else None,
        'NS__006': record.get('NS')[5] if record.get('NS') and len(record.get('NS')) > 5 else None,
        'NS__007': record.get('NS')[6] if record.get('NS') and len(record.get('NS')) > 6 else None,
        'NS__008': record.get('NS')[7] if record.get('NS') and len(record.get('NS')) > 7 else None,
        'NS__009': record.get('NS')[8] if record.get('NS') and len(record.get('NS')) > 8 else None,
        'NS__010': record.get('NS')[9] if record.get('NS') and len(record.get('NS')) > 9 else None,
        'NS__011': record.get('NS')[10] if record.get('NS') and len(record.get('NS')) > 10 else None,
        'NS__012': record.get('NS')[11] if record.get('NS') and len(record.get('NS')) > 11 else None,
        'NS__013': record.get('NS')[12] if record.get('NS') and len(record.get('NS')) > 12 else None,
        'NS__014': record.get('NS')[13] if record.get('NS') and len(record.get('NS')) > 13 else None,
        'NS__015': record.get('NS')[14] if record.get('NS') and len(record.get('NS')) > 14 else None,
        # Add more columns for NS__002, NS__003, and so on as needed
        'SOA__-': record.get('SOA')[0] if record.get('SOA') else None,
        'CNAME': None,
        'TXT' : None,
        'TXT__001': record.get('TXT')[0] if record.get('TXT') and len(record.get('TXT')) > 0 else None,
        'TXT__002': record.get('TXT')[1] if record.get('TXT') and len(record.get('TXT')) > 1 else None,
        'TXT__003': record.get('TXT')[2] if record.get('TXT') and len(record.get('TXT')) > 2 else None,
        'TXT__004': record.get('TXT')[3] if record.get('TXT') and len(record.get('TXT')) > 3 else None,
        'TXT__005': record.get('TXT')[4] if record.get('TXT') and len(record.get('TXT')) > 4 else None,
        'TXT__006': record.get('TXT')[5] if record.get('TXT') and len(record.get('TXT')) > 5 else None,
        'TXT__007': record.get('TXT')[6] if record.get('TXT') and len(record.get('TXT')) > 6 else None,
        'TXT__008': record.get('TXT')[7] if record.get('TXT') and len(record.get('TXT')) > 7 else None,
        'TXT__009': record.get('TXT')[8] if record.get('TXT') and len(record.get('TXT')) > 8 else None,
        'TXT__010': record.get('TXT')[9] if record.get('TXT') and len(record.get('TXT')) > 9 else None,
        'TXT__011': record.get('TXT')[10] if record.get('TXT') and len(record.get('TXT')) > 10 else None,
        'TXT__012': record.get('TXT')[11] if record.get('TXT') and len(record.get('TXT')) > 11 else None,
        'TXT__013': record.get('TXT')[12] if record.get('TXT') and len(record.get('TXT')) > 12 else None,
        'TXT__014': record.get('TXT')[13] if record.get('TXT') and len(record.get('TXT')) > 13 else None,
        'TXT__015': record.get('TXT')[14] if record.get('TXT') and len(record.get('TXT')) > 14 else None,
        'TXT__016': record.get('TXT')[15] if record.get('TXT') and len(record.get('TXT')) > 15 else None,
        'TXT__017': record.get('TXT')[16] if record.get('TXT') and len(record.get('TXT')) > 16 else None,
        'TXT__018': record.get('TXT')[17] if record.get('TXT') and len(record.get('TXT')) > 17 else None,
        'TXT__019': record.get('TXT')[18] if record.get('TXT') and len(record.get('TXT')) > 18 else None,
        'TXT__020': record.get('TXT')[19] if record.get('TXT') and len(record.get('TXT')) > 19 else None,
        'TXT__021': record.get('TXT')[20] if record.get('TXT') and len(record.get('TXT')) > 20 else None,
        # Add more columns for TXT__002, TXT__003, and so on as needed
        'SRV': None,
        'PTR': None,
        'domain_name': record.get('domain_name')
    }
    data.append(row)

    df = pd.DataFrame(data)
    if(isMalicious):
        print('writing to csv for malicious domains')
        df.to_csv(r'data/malicious_domain_response.csv', index=False)
    else:
        print('writing to csv for normal domains')
        df.to_csv(r'data/dnsdata_top_domains.csv', index=False)
    





    