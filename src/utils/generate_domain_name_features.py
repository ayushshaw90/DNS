import tldextract
from collections import Counter
import math


def extract_domain_name_features(domain):
    features = {}

    # Split the domain into subdomains and TLD (Top-Level Domain)
    ext = tldextract.extract(domain)
    
    # Full domain
    features['full_domain'] = domain
    
    # Top-Level Domain
    features['tld'] = ext.suffix if ext.suffix else None
    
    # Domain and Subdomain lengths
    features['full_domain_length'] = len(domain)
    features['domain_length'] = len(ext.domain)
    
    # Check if the domain has a subdomain
    features['has_subdomain'] = 1 if ext.subdomain else 0

    features['subdomain_length'] = len(ext.subdomain)

    #Calculating the number of subdomains
    features['subdomains_count'] = count_number_of_subdomains(domain)
    
    #Calculating the average length of subdomains
    features['avg_subdomain_length'] = calculate_average_subdomain_length(domain)
    
    #Calculating the entropy of the domain name
    features['entropy_of_domain'] = calculate_entropy(domain)
    
    #Caluclating the average entropy of subdomains
    features['avg_entropy_of_subdomains'] = calculate_average_entropy_of_subdomains(domain)
    
    #Calculating the ratio of alphanumeric characters in the domain name
    features['alphanumeric_ratio'] = calculate_alphanumeric_ratio(domain)
    
    #calculating the ratio of numeric characters in the domain name
    features['numeric_ratio'] = calculate_numeric_ratio(domain)
    
    #Calculating the ratio of special characters in the domain name
    features['special_char_ratio'] = calculate_special_char_ratio(domain)
    
    return features

################################################################################################

def calculate_entropy(domain):
    # Count the frequency of each character in the domain
    freq = Counter(domain)
    
    # Calculate the probability of each character
    domain_length = len(domain)
    probabilities = [float(freq[char]) / domain_length for char in set(domain)]
    
    # Calculate the entropy using the Shannon entropy formula
    entropy = -sum(p * math.log2(p) for p in probabilities)
    
    return entropy

def calculate_average_entropy_of_subdomains(domain):
    # Split the domain into subdomains using the dot separator
    subdomains = domain.split('.')
    
    if(len(subdomains) == 2):
        return 0
    
    # Calculate the entropy of each subdomain
    subdomain_entropies = [calculate_entropy(sub) for sub in subdomains]
    
    # Calculate the average entropy of subdomains
    avg_entropy = sum(subdomain_entropies)/len(subdomain_entropies)
    
    return avg_entropy

def calculate_alphanumeric_ratio(domain):
    # Count the number of alphanumeric characters (lowercase alphabetic or numeric)
    alphanumeric_count = sum(1 for char in domain if char.isalnum() and char.islower())
    
    # Count the total number of characters in the domain
    total_characters = len(domain)

    alphanumeric_ratio = alphanumeric_count / total_characters
    
    return alphanumeric_ratio

def count_number_of_subdomains(domain):
    # Split the domain into subdomains using the dot separator
    subdomains = domain.split('.')
    
    if(len(subdomains) <= 2):
        return 0
    else:
        return len(subdomains) -2

def calculate_average_subdomain_length(domain):
    # Split the domain into subdomains using the dot separator
    subdomains = domain.split('.')
    
    if(len(subdomains) <= 2):
        return 0

    # Exclude TLD and second-level domain (last two segments)
    subdomains_to_consider = subdomains[:-2] 

    # Calculate the length of each subdomain
    subdomain_lengths = [len(sub) for sub in subdomains_to_consider]

    avg_subdomain_length = sum(subdomain_lengths)/len(subdomain_lengths)

    return avg_subdomain_length

def calculate_numeric_ratio(domain):
    # Calculate the number of numeric characters in the domain
    numeric_count = sum(1 for char in domain if char.isdigit())
    
    # Calculate the total length of the domain
    total_length = len(domain)
    
    if(total_length == 0):
        return 0
    
    numeric_ratio = numeric_count / total_length
    
    return numeric_ratio

def calculate_special_char_ratio(domain):
    # Count the number of special characters in the domain excluding '.'
    special_char_count = sum(1 for char in domain if not (char.isalnum() or char == '.'))

    # Calculate the total length of the domain excluding '.'
    total_length_excluding_dot = len([char for char in domain if char != '.'])

    # Calculate the special character ratio
    if total_length_excluding_dot > 0:
        special_char_ratio = special_char_count / total_length_excluding_dot
    else:
        special_char_ratio = 0.0  # Set ratio to 0 if the domain has no characters excluding '.'

    return special_char_ratio
