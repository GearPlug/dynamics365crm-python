# dynamics365crm-python
Dynamics365CRM API wrapper for Dynamics 365 written in Python.
This library works for API version: v9.0

## Installing
```
pip install dynamics365crm-python
```

## Usage

This library provides a client that is initialized with the following arguments

- domain: the dynamics 365 tenant domain (yours or someone else's)
- access_token: the retrieved token after authentication

Arguments for OAuth2 flow
- client_id: your Azure AD application client id
- client_secret: your Azure AD application client secret

```python
from dynamics365crm.client import Client

## Normal use to make calls to the api
client = Client("https://tenant_name.crmX.dynamics.com", access_token="access_token")

## OAuth2 configuration required arguments
client = Client(
    "https://tenant_name.crmX.dynamics.com",
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
)
```

### OAuth2 Protocol
#### Get authorization url

This will return a [MSAL](https://github.com/AzureAD/microsoft-authentication-library-for-python) valid authorization url, the following are required:

- tenant_id: someone else's Azure AD tenant_id
  - Ask the dynamics tenant owner to go to the [Azure Portal](portal.azure.com) and retrieve the Tenant ID from the Azure Active Directory/Overview
  - If your app is configured as multi-tenant (for any enterprise or personal account to use) you could pass "common" instead od the Tenant ID
    - However microsoft azure app configuration is a mess so the Tenant ID is preferable
- redirect_uri: your service callback url
- state: your unique generated state to identify the requester
  - you could also initiate an oauth flow with msal manually with initiate_auth_code_flow method, check the [official example](https://github.com/Azure-Samples/ms-identity-python-webapp)

```python
authorization_url = client.build_authorization_url("tenant_id", "redirect_uri", "state")

>>> "https://login.microsoftonline.com/common/oauth2/v2.0/authorize?client_id=XXXX&response_type=code&redirect_uri=https%3A%2F%your_domain/%2Fcallback%2F&scope=https%3A%2F%2tenant_name.crmX.dynamics.com%2Fuser_impersonation+offline_access+openid+profile&state=XXXX&prompt=consent"
```

#### Exchange the callback code for an access token

To finish the oauth protocol microsoft will redirect to your callback endpoint with a temporal code in the url query params to be exchanged for the full-fledged token (a json with the access_token, refresh_token, expires_in, etc.)

Again the (**tenant_id** or "common") and **redirect_uri** are required, the third argument is the code sent by microsoft

```python
token = client.exchange_code("tenant_id", "redirect_uri", "code")
```

#### Refresh token

If the access token expires you could get a new **access_token** exchanging the long-lived **refresh_token**

Again the **tenant_id** or "common" is required

```python
token = client.refresh_access_token("tenant_id", "refresh_token")
```

#### Set access token

You could pass the access_token in the constructor or set it with

```python
client.set_access_token("access_token")
```

## Dynamics Web API

### Contacts
- See the documentation https://docs.microsoft.com/es-es/dynamics365/customer-engagement/web-api/contact?view=dynamics-ce-odata-9

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

### Accounts
- See the documentation https://docs.microsoft.com/es-es/dynamics365/customer-engagement/web-api/account?view=dynamics-ce-odata-9

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

### Opportunities
- See the documentation https://docs.microsoft.com/es-es/dynamics365/customer-engagement/web-api/opportunity?view=dynamics-ce-odata-9

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

### Leads
- See the documentation https://docs.microsoft.com/es-es/dynamics365/customer-engagement/web-api/lead?view=dynamics-ce-odata-9

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

### Campaigns
- See the documentation https://docs.microsoft.com/es-es/dynamics365/customer-engagement/web-api/campaign?view=dynamics-ce-odata-9

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
- msal

## Contributing
We are always grateful for any kind of contribution including but not limited to bug reports, code enhancements, bug fixes, and even functionality suggestions.
#### You can report any bug you find or suggest new functionality with a new [issue](https://github.com/GearPlug/dynamics365crm-python/issues).
#### If you want to add yourself some functionality to the wrapper:
1. Fork it ( https://github.com/GearPlug/dynamics365crm-python )
2. Create your feature branch (git checkout -b my-new-feature)
3. Commit your changes (git commit -am 'Adds my new feature')
4. Push to the branch (git push origin my-new-feature)
5. Create a new Pull Request
