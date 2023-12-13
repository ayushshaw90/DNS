import dns.resolver
import whois
from ipwhois import IPWhois
from openpyxl import Workbook
import requests
import pprint
import json

def perform_dns_query(domain):
    results = {}
    record_types = ['A', 'AAAA', 'MX', 'NS', 'SOA', 'CNAME', 'TXT', 'SRV', 'PTR']

    for record_type in record_types:
        try:
            result = dns.resolver.resolve(domain, record_type)
            results[record_type] = [str(r) for r in result]
        except dns.resolver.NXDOMAIN:
            results[record_type] = None
        except dns.resolver.NoAnswer:
            results[record_type] = None
        except dns.resolver.Timeout:
            results[record_type] = None
        except Exception as e:
            results[record_type] = None
    # print(f"results = {results}")
    return results

def get_country_code(ip):
    try:
        response = requests.get('https://api.cleantalk.org/',params={"method_name": 'ip_info', 'ip':ip})
        if response.ststus_code == 200:
            result_dict = response.json()
            return result_dict['country_code']
        else:
            return ''
    except requests.RequestException as e:
        print(f"Error making API request: {e}")
        return ''

def get_whois_info(domain):
    try:
        whois_result = whois.whois(domain)
        return whois_result
    except whois.parser.PywhoisError:
        return None

# def get_ip_geolocation(ip):
#     try:
#         ipwhois_result = IPWhois(ip).lookup_rdap()
#         return ipwhois_result
#     except Exception:
#         return None

# def write_results_to_excel(domain, results, whois_info, output_file):
#     wb = Workbook()
#     ws = wb.active

#     headers = [
#         "DNS Record Type",
#         "IP Associated",
#         "Country Code (IP)",
#         "Country Code (Registration)",
#         "Registered Organization",
#         "Number of Subdomains",
#         "Top-Level Domain",
#         "Average Response Length",
#     ]

#     ws.append(headers)

#     for record_type, result in results.items():
#         ip = result[0] if result else ""
#         country_code_ip = get_ip_geolocation(ip)["asn_country_code"] if ip else ""
#         country_code_registration = whois_info.get("registrar", "").split()[-1]
#         org = whois_info.get("org", "")
#         num_subdomains = len(result) if result else 0
#         tld = domain.split('.')[-1]
#         avg_response_length = sum(len(r) for r in result) / len(result) if result else 0

#         result_row = [
#             record_type,
#             ip,
#             country_code_ip,
#             country_code_registration,
#             org,
#             num_subdomains,
#             tld,
#             avg_response_length,
#         ]

#         ws.append(result_row)

#     wb.save(output_file)
#     print(f"Results saved to {output_file}")
    
def getwhoisdata(ip_address):
    try:
        res = IPWhois(ip_address).lookup_rdap()
        country_code = res['asn_country_code']
        asn_date = res['asn_date']
        asn = res['asn']
        reg_timestamp = res['network']['events'][0]['timestamp']
        last_updated_timestamp = res['network']['events'][1]['timestamp']
        return {
            'ip_address': ip_address,
            'country_code': country_code,
            'asn_date': asn_date,
            'reg_timestamp': reg_timestamp,
            'last_updated': last_updated_timestamp
        }
    except Exception as e:
        print(e)
        return None
def process_dns_results(dns_result):
    ips = dns_result['A']
    print("done till [2]")
    if ips!=None:
        try:
            response_got = [getwhoisdata(ip) for ip in ips]
            dns_result['A'] = response_got
        except Exception as e:
            print(f"Error : A record")
    ips2 = dns_result['AAAA']
    print("done till [3]")
    if ips2!=None:
        try:
            response_got = [getwhoisdata(ip) for ip in ips2]
            dns_result['AAAA'] = response_got
        except Exception as e:
            print(f"Error : AAAA record")
    
    print("done till [4]")
    return dns_result

def append_dicts_to_json(file_path, dictionaries):
    try:
        with open(file_path, 'w') as json_file:
            # for domain in dictionaries:
            #     json.dump(domain, json_file, indent=4)
            #     json_file.write('\n')
            json.dump({'response': dictionaries}, json_file, indent=4)
    except Exception as e:
        print(f"Error: {e}")

def fun2(domain_names):
    res = []
    for domain in domain_names:
        dns_results = perform_dns_query(domain)
        dns_results = process_dns_results(dns_results)
        dns_results['domain_name']=domain
        res.append(dns_results)
    return res

def main():
    file_path = 'result.json'
    input_file = 'sample_domains.txt'
    try:
        domain_list = []
        with open(input_file, 'r') as file:
            for line2 in file:
                line = line2[:-1]
                # print(f"Line is {line}")
                # dns_results = perform_dns_query(line)
                # dns_results = process_dns_results(dns_results)
                # dns_results['domain_name']=line
                # print("done till [5]")
                # print(dns_results)
                domain_list.append(line)
                # append_dicts_to_json(file_path, line)
                # print("done till [6]")
        print("done till [7]")
        results = fun2(domain_list)
        print("done till [8]")
        append_dicts_to_json('result.json',results)
        print("done till [9]")
        
    except Exception as e:
        print(f"Error: {e}")
    
    
    # domain = input("Enter the domain name: ")

    # dns_results = perform_dns_query(domain)
    # print("Done till [1]")
    # # print(dns_results)
    # dns_results = process_dns_results(dns_results)
    # dns_results['domain_name']=domain
    # print(dns_results)
    
    # if not any(dns_results.values()):
    #     print("No DNS records found for the domain.")
    #     return

    # whois_info = get_whois_info(domain)
    # if not whois_info:
    #     print("Unable to retrieve WHOIS information.")
    #     return

    # output_file = f"{domain}_dns_analysis.xlsx"
    # write_results_to_excel(domain, dns_results, whois_info, output_file)

if __name__ == "__main__":
    main()
