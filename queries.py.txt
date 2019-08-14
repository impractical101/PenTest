from __future__ import print_function
import sys
import dns.resolver

def help_text():
        print("\nUsage:\npython dns_queries.py domain\n")
        sys.exit()

def extract_dns_records(domain):
    for qtype in 'A', 'AAAA', 'MX', 'NS', 'TXT', 'SOA':
        answer = dns.resolver.query(domain,qtype, raise_on_no_answer=False)
        if answer.rrset is not None:
            print(answer.rrset)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        help_text()
    domain = sys.argv[1]
    extract_dns_records(domain)
    
