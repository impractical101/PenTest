import argparse
from netaddr import IPAddress, IPNetwork, IPSet, IPRange

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--range', nargs=1)
    parser.add_argument('--exclude', nargs='*')
    args = parser.parse_args()
    return args.range, args.exclude

def list_scan(range, exclude):
    for ip in range:
        if ip in exclude:
            range.remove(ip)
    return range

if __name__ == '__main__':
    r,e = parse_arguments()
    range = IPSet(r)
    exclude = IPSet(e)
    print(range)
    print(exclude)
    final_list = list_scan(range, exclude)
    for ip in final_list:
        print(ip)