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
    parser.add_argument('--project', default="default", help='Project to use')
    return parser.parse_args()

if __name__ == "__main__":
    my_args = get_args()
    my_session = requests.Session()
    my_session.verify = False
    client = symphony_client.Client(url='https://%s' % my_args.cluster_ip, session=my_session)
    client.login(domain=my_args.domain, username=my_args.username, password=my_args.password, project=my_args.project)
    for user in client.users.list():
        if user['name'] == my_args.username:
            userID = user['id']
    for project in client.projects.list():
        if project['name'] == my_args.project:
            projectID = project['id']
    ec2_credentials = client.users.create_ec2_credentials(userID, projectID)
    botoclient = boto3.Session.client(boto3.session.Session(), service_name="ec2", region_name="symphony",
                                  endpoint_url="https://%s/api/v2/ec2/" % my_args.cluster_ip,
                                  verify=False,
                                  aws_access_key_id=ec2_credentials['access'],
                                  aws_secret_access_key=ec2_credentials['secret'])

    images = botoclient.describe_images()
    print images
