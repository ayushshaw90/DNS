import whois
from datetime import datetime

def get_domain_info(domain_name):
    
    features = {
    "creation_date": None,
    "last_updated_date": None,
    "expiration_date": None,
    "organization_name": None
    #"domain_status": None
    # Add other columns here with default values as needed
}

    try:
        domain_info = whois.whois(domain_name)

        #if domain_info is None:
        
        # Extract creation and last updated dates
        creation_date = domain_info.creation_date
        creation_date = get_latest_date(creation_date)
        features['creation_date'] = creation_date

        last_updated_date = domain_info.updated_date
        if last_updated_date is None:
            features['last_updated_date'] = None
        else:
            last_updated_date = format_date(last_updated_date)
            features['last_updated_date'] = last_updated_date

        expiration_date = domain_info.expiration_date
        expiration_date = get_latest_date(expiration_date)
        features['expiration_date'] = expiration_date

        organization_name = domain_info.get('org', None)
        features['organization_name'] = organization_name

        #domain_status = domain_info.get('status', None)
       # features['domain_status'] = domain_status

       
    except Exception as e:
         print(f"Error: {e}")

    return features
    

def get_latest_date(creation_date):
    if creation_date is None:
        return None

    if isinstance(creation_date, list):
        formatted_dates = [d.strftime("%Y-%m-%d %H:%M:%S") if isinstance(d, datetime) else None for d in creation_date]
        return max(formatted_dates, default=None)
    elif isinstance(creation_date, datetime):
        return creation_date.strftime("%Y-%m-%d %H:%M:%S")
    else:
        return None
    
def format_date(date):
    if isinstance(date, list):
        return [d.strftime("%Y-%m-%d %H:%M:%S") if isinstance(d, datetime) else None for d in date]
    elif isinstance(date, datetime):
        return date.strftime("%Y-%m-%d %H:%M:%S")
    else:
        return None



