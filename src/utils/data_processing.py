import tldextract

def extract_domain_features(domain):
    extracted = tldextract.extract(domain)
    return {
        'subdomain': extracted.subdomain,
        'domain': extracted.domain,
        'suffix': extracted.suffix,
        'is_https': int('https' in domain),
        'is_www': int('www' in domain),
        # Add more features as needed based on your analysis
    }
