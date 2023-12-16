from numpy import double
import tldextract
from collections import Counter
import math
from tld import get_tld

def get_feature_rich_row(domain):
    features = {}

    # Split the domain into subdomains and TLD (Top-Level Domain)
    ext = tldextract.extract(domain)
    
    # Full domain
    #features['full_domain'] = domain
    
    # Top-Level Domain
    features['tld'] = ext.suffix if ext.suffix else 'not_present'    

    features['has_tld'] = 1 if ext.suffix else 0
    
    # Domain and Subdomain lengths
    features['full_domain_length'] = len(domain)
    features['domain_length'] = len(ext.domain)
    
    # Check if the domain has a subdomain
    features['has_subdomain'] = 1 if ext.subdomain else 0

    features['subdomain_length'] = len(ext.subdomain)

    #Calculating the number of subdomains
    features['subdomains_count'] = count_number_of_subdomains(ext)
    
    #Calculating the average length of subdomains
    features['avg_subdomain_length'] = calculate_average_subdomain_length(ext)
    
    #Calculating the entropy of the domain name
    features['entropy_of_domain'] = calculate_entropy(domain)
    
    #Caluclating the average entropy of subdomains
    features['avg_entropy_of_subdomains'] = calculate_average_entropy_of_subdomains(ext)
    
    #Calculating the ratio of alphanumeric characters in the domain name
    features['alphanumeric_ratio'] = calculate_alphanumeric_ratio(domain)
    
    #calculating the ratio of numeric characters in the domain name
    features['numeric_ratio'] = calculate_numeric_ratio(domain)
    
    #Calculating the ratio of special characters in the domain name
    features['special_char_ratio'] = calculate_special_char_ratio(domain)

    features['underscore_ratio'] = domain.count('_') / len(domain)

    number_of_digits = count_digits(domain)

    features['contains_digit']  = 1 if number_of_digits > 0 else 0

    length = double(len(ext.domain) +len(ext.subdomain))
    
    features['digit_ratio'] = number_of_digits / length if length > 0 else 0.0

    features['hyphen_ratio'] = (count_hyphens(domain)) / length if length > 0 else 0.0

    features['underscore_ratio'] = (count_underscore(domain))/ length if length > 0 else 0.0

    features['vowel_ratio'] =  (count_vowels(domain))/ length if length > 0 else 0.0

    features['repeated_chars_ratio'] = calculate_repeated_chars_ratio(ext.domain)

    return features

dataset = []

def calculate_entropy(domain):
    # Count the frequency of each character in the domain
    freq = Counter(domain)
    
    # Calculate the probability of each character
    domain_length = double(len(domain))
    probabilities = [float(freq[char]) / domain_length for char in set(domain)]
    
    # Calculate the entropy using the Shannon entropy formula
    entropy = -sum(p * math.log2(p) for p in probabilities)
    
    return entropy

def calculate_average_entropy_of_subdomains(ext):

    if ext.subdomain == '':
        return 0.0
    # Split the domain into subdomains using the dot separator
    subdomains = ext.subdomain.split('.')
    
    # Calculate the entropy of each subdomain
    subdomain_entropies = [calculate_entropy(sub) for sub in subdomains]
    
    # Calculate the average entropy of subdomains
    avg_entropy = sum(subdomain_entropies)/double(len(subdomain_entropies))
    
    return avg_entropy

def calculate_alphanumeric_ratio(domain):
    # Count the number of alphanumeric characters (lowercase alphabetic or numeric)
    alphanumeric_count = sum(1 for char in domain if char.isalnum() and char.islower())
    
    # Count the total number of characters in the domain
    total_characters = double(len(domain))

    alphanumeric_ratio = alphanumeric_count / total_characters
    
    return alphanumeric_ratio

def count_number_of_subdomains(ext):
    if ext.subdomain == '':
        return 0.0

    subdomains = ext.subdomain.split('.')

    return len(subdomains)


def calculate_average_subdomain_length(ext):
    if ext.subdomain == '':
        return 0.0
    # Split the domain into subdomains using the dot separator
    subdomains = ext.subdomain.split('.')

    subdomains_to_consider = subdomains

    # Calculate the length of each subdomain
    subdomain_lengths = [len(sub) for sub in subdomains_to_consider]

    avg_subdomain_length = sum(subdomain_lengths)/double(len(subdomain_lengths))

    return avg_subdomain_length

def calculate_numeric_ratio(domain):
    # Calculate the number of numeric characters in the domain
    numeric_count = double(sum(1 for char in domain if char.isdigit()))
    
    # Calculate the total length of the domain
    total_length = double(len(domain))
    
    if(total_length == 0):
        return 0.0
    
    numeric_ratio = numeric_count / total_length
    
    return numeric_ratio

def calculate_special_char_ratio(domain):
    # Count the number of special characters in the domain excluding '.'
    special_char_count = sum(1 for char in domain if not (char.isalnum() or char == '.'))

    # Calculate the total length of the domain excluding '.'
    total_length_excluding_dot = double(len([char for char in domain if char != '.']))

    # Calculate the special character ratio
    if total_length_excluding_dot > 0:
        special_char_ratio = double(special_char_count)/double(total_length_excluding_dot)
    else:
        special_char_ratio = 0.0  # Set ratio to 0 if the domain has no characters excluding '.'

    return special_char_ratio

def count_digits(domain):
    # Initialize a counter for digits
    digit_count = 0

    # Iterate through each character in the domain name
    for char in domain:
        if char.isdigit():  # Check if the character is a digit
            digit_count += 1  # Increment the counter for each digit found

    return digit_count

def count_hyphens(domain):
    hyphen_count = 0

    for char in domain:
        if char == '-':  
            hyphen_count += 1  

    return hyphen_count

def count_vowels(domain):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    domain_lower = domain.lower()
    vowel_count = sum(1 for char in domain_lower if char in vowels)
    return vowel_count

def calculate_repeated_chars_ratio(subdomain):
    subdomain_lower = subdomain.lower()
    total_chars = len(subdomain_lower)
    unique_chars = len(set(subdomain_lower))
    repeated_chars = total_chars - unique_chars
    repeated_chars_ratio = double(repeated_chars)/total_chars if total_chars > 0 else 0.0

    return repeated_chars_ratio

def calculate_consecutive_digits_ratio(domain):
    # Extract the domain part without the valid public suffix (TLD)
    ext = tldextract.extract(domain)
    domain_without_tld = ext.domain

    # Convert the domain name to lowercase for consistency
    domain_lower = domain_without_tld.lower()

    # Initialize variables for counting consecutive digits and total characters
    consecutive_digits_count = 0
    total_chars = len(domain_lower)

    # Iterate through the domain characters to count consecutive digits
    i = 0
    while i < total_chars - 1:
        if domain_lower[i].isdigit() and domain_lower[i + 1].isdigit():
            consecutive_digits_count += 1
            # Skip to the next non-digit character
            while i < total_chars - 1 and domain_lower[i].isdigit():
                i += 1
        else:
            i += 1
    print(consecutive_digits_count)
    # Calculate the ratio of consecutive digits
    consecutive_digits_ratio = consecutive_digits_count / total_chars if total_chars > 0 else 0

    return consecutive_digits_ratio

def count_underscore(domain):
    underscore_count = 0

    for char in domain:
        if char == '_':  
            underscore_count += 1  

    return underscore_count