To install symphony-client on your machine please make sure you have connectivity to your Symphony's northbound IP 
and run the following:

sudo URL=https://<symphony-northbound> bash -c "$(curl -k -sSL https://<symphony-northbound>/install-client.sh)"

In order to start using it, in your python code make sure you set 

PYTHONPATH=/opt/symphony-client

Now, you can easily:

import symphony_client
