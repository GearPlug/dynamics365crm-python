from client import Client
import pprint

"""
MAIN INSTANCE (petition)
"""
tenant_id = ""
client_id = ""
client_secret = ""
dynamics_resource = ""
CRM_resource = ""
refresh_token = ""
token = ""
petition = Client(client_id=client_id, client_secret=client_secret, token=token)

"""
API ENDPOINTS EXAMPLES
"contacts", "accounts", "opportunities", "leads", "campaigns", "EntityDefinitions(LogicalName='contact')/Attributes"
"""

"""
REFRESH TOKEN
to refresh the token you have to send the client_id, the client_secret, the refresh_token, the redirect_uri, and the resource
Example:
    refresh = petition.refresh_token(refresh_token, redirect_uri, resource)
    pprint.pprint(refresh)
"""

"""
GET DATA METHOD
for get data just have to indicate the endpoint and the other filter options if you want
Example: 
    get_data = petition.get_data('contacts')
    pprint.pprint(get_data)
"""

"""
CREATE DATA METHOD
to create data you have to specify the endpoint where you will create data and send the data in **kwarg
Example: 
    data = {"firstname": "TEST", "lastname": "ITS A TEST", "middlename": "TESTING", "emailaddress1": "check@test.com"}
    create_data = petition.create_data('contacts', **data)
    pprint.pprint(create_data)
"""

"""
UPDATE DATA METHOD
to update data you have to specify the endpoint where you will update data, also you have to specify the id of the thing to update and send te update data in **kwargs
Example:
    data = {"firstname": "TESTCHANGE", "lastname": "UPDATE THE TEST", "middlename": "UPDATE TESTING", "emailaddress1": "upcheck@test.com"}
    update_data = petition.update_data(type='contacts', id='ID', **data)
    pprint.pprint(update_data)
"""

"""
DELETE DATA METHOD
is simple, just send the endpoint where you'll delete data and the id of the data to delete
Example:
    delete_data = petition.delete_data(type='contacts', id='ID')
    pprint.pprint(delete_data)
"""
