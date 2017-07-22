import sys
import argparse
import requests
sys.path.append('/opt/symphony-client')

import symphony_client 



def get_args():
    parser = argparse.ArgumentParser(description='***Stratoscale*** domain Usage Tool')
    parser.add_argument('--cluster_ip', required=True, help='Cluster IP. e.g. 10.20.30.45')
    parser.add_argument('--domain', required=True, help='Domain used to retrieve date')
    parser.add_argument('--username', required=True, help='User name used to retrieve date')
    parser.add_argument('--password', required=True, help='Password used to retrieve date')
    parser.add_argument('--project', default="default", help='Password used to retrieve date')
    return parser.parse_args()

if __name__ == "__main__":
    my_args = get_args()
    my_session = requests.Session()
    my_session.verify = False
    client = symphony_client.Client(url='https://%s' % my_args.cluster_ip, session=my_session)
    client.login(domain=my_args.domain, username=my_args.username, password=my_args.password, project=my_args.project)
    print "Hello this is first node's access ip - %s" % client.nodes.list()[0].access_ip
