import sys
import argparse
import requests
import boto3
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
    # access = client.access.get()
    # secret = client.secret.get()
    access = "fe16c4d196cc4c889ff197294d962d2f"
    secret = "3fcb3cc709ea4d8db1c185e22d5ddf8c"
    botoclient = boto3.Session.client(boto3.session.Session(), service_name="ec2", region_name="symphony",
                                  endpoint_url="https://%s/api/v2/ec2/" % my_args.cluster_ip,
                                  verify=False,
                                  aws_access_key_id=access,
                                  aws_secret_access_key=secret)

    # finding our Centos image, grabbing its image ID
    images = botoclient.describe_images()
    import ipdb; ipdb.set_trace()
