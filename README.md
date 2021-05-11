# dynamics365crm-python
Dynamics365CRM API wrapper for Dynamics 365 written in Python.
This library works for API version: v9.0

## Installing
```
pip install dynamics365crm-python
```

## Usage (Method I)
If you will not use the oauth authentication and you already have an access token, call the library like this:
- resource = the url of the CRM, example: https://example.crm2.dynamics.com/
```
from dynamics365crm.client import Client
client = Client('RESOURCE', 'ACCESS_TOKEN')
```

If you will use the oauth authentication call the library like this:
```
from dynamics365crm.client import Client
client = Client('RESOURCE', 'CLIENT_ID', 'CLIENT_SECRET')
```

#### Get authorization url
```
url = client.url_petition("REDIRECT_URL")
```

#### Exchange the code for an access token
```
token = client.exchange_code('REDIRECT_URL', 'CODE')
```

#### Refresh token
```
token = client.refresh_token('REFRESH TOKEN', 'REDIRECT_URL')
```

#### Set token
```
token = client.set_token('TOKEN')
```

# Usage (Method II):
If we're planning to use the `tenant_id` and `scope` with currently present `client_id` and `client_secret`, we can get the authentication token via the following steps:

```py
# Pre-Step:
# Setting environment variables
# export CLIENT_ID="YOUR_CLIENT_ID_HERE"
# export CLIENT_SECRET="YOUR_CLIENT_ID_HERE"
# export TENANT_ID="YOUR_TENANT_ID_HERE"
# export SCOPE="https://graph.microsoft.com/.default"

# Step 1:
# Initialize the client

# Imports
import os
from dynamics365crm.client import Client

# Data Initializations
resource = os.getenv("RESOURCE")
client_id = os.getenv("CLIENT_ID"),
client_secret = os.getenv("CLIENT_SECRET")
tenant_id = os.getenv("TENANT_ID")
scope = os.getenv("SCOPE")

client = Client(resource, client_id, client_secret)

# Step 2:
# Call the API to set the token as client.token

client.set_auth_token_via_tenant(tenant_id, scope)

# Step 3:
# Verify by printing client.token
print(f"client token obtained: {client.token}")
```

### Contacts Section
- see the documentation https://docs.microsoft.com/es-es/dynamics365/customer-engagement/web-api/contact?view=dynamics-ce-odata-9

#### Get Contacts
can receive orderby, filter, select, top, expand
```
list_contacts = client.get_contacts()
```

#### Create Contact
```
create_contact = client.create_contact(firstname="FIRSTNAME", lastname="LASTNAME", middlename="MIDDLENAME", emailaddress1="EMAILADDRESS")
```

#### Delete Contact
```
delete_contact = client.delete_contact('ID')
```

#### Update Contact
```
update_contact = client.update_contact('ID', firstname="FIRSTNAME", lastname="LASTNAME", middlename="MIDDLENAME", emailaddress1="EMAILADDRESS")
```

### Accounts Section
- see the documentation https://docs.microsoft.com/es-es/dynamics365/customer-engagement/web-api/account?view=dynamics-ce-odata-9

#### Get Accounts
can receive orderby, filter, select, top, expand
```
get_accounts = client.get_accounts()
```

#### Create Account
```
create_account = client.create_account(name="NAME", websiteurl="WWW.WEBSITE.COM")
```

#### Delete Account
```
create_account = client.delete_account('ID')
```

#### Update Account
```
update_account = client.update_account(id="ID", name="NAME")
```

### Opportunities Section
- see the documentation https://docs.microsoft.com/es-es/dynamics365/customer-engagement/web-api/opportunity?view=dynamics-ce-odata-9

#### Get Opportunities
can receive orderby, filter, select, top, expand
```
list_opportunities = client.get_opportunities()
```

#### Create Opportunities
```
create_opportunities = client.create_opportunity(name="OPPORTUNITY NAME")
```

#### Delete Opportunities
```
delete_opportunities = client.delete_opportunity(id="OPPORTUNITY ID")
```

#### Update Opportunities
```
update_opportunities = client.update_opportunity(id="OPPORTUNITY ID", name="OPPORTUNITY NAME", description="SOME DESCRIPTION")
```

### Leads Section
- see the documentation https://docs.microsoft.com/es-es/dynamics365/customer-engagement/web-api/lead?view=dynamics-ce-odata-9

#### Get Leads
can receive orderby, filter, select, top, expand
```
list_leads = client.get_leads()
```

#### Create Lead
```
create_leads = client.create_lead(fullname="LEAD NAME", subject="LEAD SUBJECT", mobilephone="123456", websiteurl="WWW.WEBSITE.COM", middlename="MIDDLE LEAD NAME")
```

#### Delete Lead
```
delete_leads = client.delete_lead("ID")
```

#### Update Lead
```
update_leads = client.update_lead(fullname="LEAD NAME", subject="LEAD SUBJECT", mobilephone="123456", websiteurl="WWW.WEBSITE.COM", middlename="MIDDLE LEAD NAME")
```

### Campaign Section
- see the documentation https://docs.microsoft.com/es-es/dynamics365/customer-engagement/web-api/campaign?view=dynamics-ce-odata-9

#### Get Campaigns
can receive orderby, filter, select, top, expand
```
list_campaigns = client.get_campaigns()
```

#### Create Campaign
```
create_campaign = client.create_campaign(name="CAMPAIGN NAME", description="SOME DESCRIPTION")
```

#### Delete Campaign
```
delete_campaign = client.delete_campaign(id="ID")
```

#### Update Campaign
```
update_campaign = client.update_campaign(id="ID", name="CAMPAIGN NAME", description="SOME DESCRIPTION")
```

## Requirements
- requests

## Tests
```
dynamics365crm/test.py
```

## Contributing
We are always grateful for any kind of contribution including but not limited to bug reports, code enhancements, bug fixes, and even functionality suggestions.
#### You can report any bug you find or suggest new functionality with a new [issue](https://github.com/GearPlug/dynamics365crm-python/issues).
#### If you want to add yourself some functionality to the wrapper:
1. Fork it ( https://github.com/GearPlug/dynamics365crm-python )
2. Create your feature branch (git checkout -b my-new-feature)
3. Commit your changes (git commit -am 'Adds my new feature')
4. Push to the branch (git push origin my-new-feature)
5. Create a new Pull Request
