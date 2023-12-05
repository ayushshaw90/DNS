'''This code creates a DNS server which gets the DNS packets. On receiving a packet, it decodes the packet and looks for question fields. If any question field matches the list of blocked domains, it creates a custom response which sends an "A record pointing to trap IP address". If no entry in question field matches the blocked domains, it sends the DNS request to google's DNS server and returns it's response to the original sender.
'''

import socket
import threading
import dns
from dns import message, rdata, query

blacklisted_domains = {
    'mail.google.com',
    'facebook.com',
    'hotmail.com',
    'www.google.com'
}

trap_ip_address = '127.0.0.1'

def decode_dns_packet(packet):
    # This function decodes the DNS packet from bitwise format, checks if it contains any blocked domain names as question.

    dns_message = message.from_wire(packet)
    # print(dns_message)
    for qn in dns_message.question:
        # used for debugging 
        # ----------
        # print(qn)
        # print(qn.name.to_text())
        # print(type(qn.name.to_text()))
        # print(qn.name.to_text()[:-1])
        # ----------
        if qn.name.to_text()[:-1] in blacklisted_domains:
            print(f"Found the blacklisted domain {qn.name.to_text()[:-1]}")
            return True, qn.name.to_text()
    return False, ""


def dns_proxy():
    # Set the DNS server's address
    dns_server = ('8.8.8.8', 53)

    # Create a UDP socket to listen for DNS requests
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as proxy_socket:
        # Bind the socket to a specific address and port
        proxy_socket.bind(('127.0.0.1', 53))
        print("DNS proxy is running on 127.0.0.1:53")

        while True:
            # Receive data and address from the client
            data, client_address = proxy_socket.recvfrom(1024)
            # print(data.decode('utf-8'))
            should_it_be_blacklisted, question_name = decode_dns_packet(data)
            dns_message = message.from_wire(data)
            if should_it_be_blacklisted:
                # Create custom packet
                response = message.make_response(dns_message)
                # Create an A record with the specified IP address
                a_record = dns.rrset.from_text(question_name, 300, dns.rdataclass.IN, dns.rdatatype.A, trap_ip_address)
                # Add the A record to the answer section of the response
                response.answer.append(a_record)
                # send response to trap IP address
                proxy_socket.sendto(response.to_wire(), client_address)
            else:
            # Forward the DNS request to the DNS server
                with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as dns_socket:
                    dns_socket.sendto(data, dns_server)
                    # Receive the response from the DNS server
                    response, _ = dns_socket.recvfrom(1024)

                # Send the DNS response back to the client
                proxy_socket.sendto(response, client_address)

def main():
    # Start the DNS proxy in a separate thread
    proxy_thread = threading.Thread(target=dns_proxy)
    proxy_thread.start()

    try:
        # Keep the main thread running
        proxy_thread.join()
    except KeyboardInterrupt:
        print("DNS proxy stopped.")

if __name__ == "__main__":
    main()
