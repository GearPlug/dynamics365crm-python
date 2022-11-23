import msal
from urllib.parse import urlencode
import re

import requests


class Client:
    api_path = "api/data/v9.0"

    def __init__(self, domain, client_id=None, client_secret=None, access_token=None):
        self.domain = domain.strip("/")
        self.scopes = [f"{domain}/user_impersonation"]
        self.client_id = client_id
        self.client_secret = client_secret

        self.headers = {
            "Accept": "application/json, */*",
            "content-type": "application/json; charset=utf-8",
            # "OData-MaxVersion": "4.0",
            # "OData-Version": "4.0",
        }
        if access_token is not None:
            self.set_access_token(access_token)

    def set_access_token(self, token):
        """
        Sets the Token for its use in this library.
        :param token: A string with the Token.
        :return:
        """
        assert token is not None, "The token cannot be None."
        self.access_token = token
        self.headers["Authorization"] = "Bearer " + self.access_token

    def build_msal_client(self, tenant_id):
        return msal.ConfidentialClientApplication(
            self.client_id,
            client_credential=self.client_secret,
            authority=f"https://login.microsoftonline.com/{tenant_id}",
        )

    def make_request(
        self,
        method,
        endpoint,
        expand=None,
        filter=None,
        orderby=None,
        select=None,
        skip=None,
        top=None,
        data=None,
        json=None,
        **kwargs,
    ):
        """
        this method do the request petition, receive the different methods (post, delete, patch, get) that the api allow, see the documentation to check how to use the filters
        https://msdn.microsoft.com/en-us/library/gg309461(v=crm.7).aspx
        :param method:
        :param endpoint:
        :param expand:
        :param filter:
        :param orderby:
        :param select:
        :param skip:
        :param top:
        :param data:
        :param json:
        :param kwargs:
        :return:
        """
        extra = {}
        if expand is not None and isinstance(expand, str):
            extra["$expand"] = str(expand)
        if filter is not None and isinstance(filter, str):
            extra["$filter"] = filter
        if orderby is not None and isinstance(orderby, str):
            extra["$orderby"] = orderby
        if select is not None and isinstance(select, str):
            extra["$select"] = select
        if skip is not None and isinstance(skip, str):
            extra["$skip"] = skip
        if top is not None and isinstance(top, str):
            extra["$top"] = str(top)

        assert self.domain is not None, "'domain' is required"
        assert self.access_token is not None, "You must provide a 'token' to make requests"
        url = f"{self.domain}/{self.api_path}/{endpoint}?" + urlencode(extra)
        if method == "get":
            response = requests.request(method, url, headers=self.headers, params=kwargs)
        else:
            response = requests.request(method, url, headers=self.headers, data=data, json=json)

        return self.parse_response(response)

    def _get(self, endpoint, data=None, **kwargs):
        return self.make_request("get", endpoint, data=data, **kwargs)

    def _post(self, endpoint, data=None, json=None, **kwargs):
        return self.make_request("post", endpoint, data=data, json=json, **kwargs)

    def _delete(self, endpoint, **kwargs):
        return self.make_request("delete", endpoint, **kwargs)

    def _patch(self, endpoint, data=None, json=None, **kwargs):
        return self.make_request("patch", endpoint, data=data, json=json, **kwargs)

    def parse_response(self, response):
        """
        This method get the response request and returns json data or raise exceptions
        :param response:
        :return:
        """
        if response.status_code == 204 or response.status_code == 201:
            if 'OData-EntityId' in response.headers:
                entity_id = response.headers['OData-EntityId']
                if entity_id[-38:-37] == '(' and entity_id[-1:] == ')':  # Check container
                    guid = entity_id[-37:-1]
                    guid_pattern = re.compile(r'^[\da-f]{8}-([\da-f]{4}-){3}[\da-f]{12}$', re.IGNORECASE)
                    if guid_pattern.match(guid):
                        return guid
                    else:
                        return True  # Not all calls return a guid
            else:
                return True
        elif response.status_code == 400:
            raise Exception(
                "The URL {0} retrieved an {1} error. Please check your request body and try again.\nRaw message: {2}".format(
                    response.url, response.status_code, response.text
                )
            )
        elif response.status_code == 401:
            raise Exception(
                "The URL {0} retrieved and {1} error. Please check your credentials, make sure you have permission to perform this action and try again.".format(
                    response.url, response.status_code
                )
            )
        elif response.status_code == 403:
            raise Exception(
                "The URL {0} retrieved and {1} error. Please check your credentials, make sure you have permission to perform this action and try again.".format(
                    response.url, response.status_code
                )
            )
        elif response.status_code == 404:
            raise Exception(
                "The URL {0} retrieved an {1} error. Please check the URL and try again.\nRaw message: {2}".format(
                    response.url, response.status_code, response.text
                )
            )
        elif response.status_code == 412:
            raise Exception(
                "The URL {0} retrieved an {1} error. Please check the URL and try again.\nRaw message: {2}".format(
                    response.url, response.status_code, response.text
                )
            )
        elif response.status_code == 413:
            raise Exception(
                "The URL {0} retrieved an {1} error. Please check the URL and try again.\nRaw message: {2}".format(
                    response.url, response.status_code, response.text
                )
            )
        elif response.status_code == 500:
            raise Exception(
                "The URL {0} retrieved an {1} error. Please check the URL and try again.\nRaw message: {2}".format(
                    response.url, response.status_code, response.text
                )
            )
        elif response.status_code == 501:
            raise Exception(
                "The URL {0} retrieved an {1} error. Please check the URL and try again.\nRaw message: {2}".format(
                    response.url, response.status_code, response.text
                )
            )
        elif response.status_code == 503:
            raise Exception(
                "The URL {0} retrieved an {1} error. Please check the URL and try again.\nRaw message: {2}".format(
                    response.url, response.status_code, response.text
                )
            )
        return response.json()

    def build_authorization_url(self, tenant_id: str, redirect_uri: str, state: str) -> str:
        msal_client = self.build_msal_client(tenant_id)
        return msal_client.get_authorization_request_url(
            self.scopes,
            state=state,
            redirect_uri=redirect_uri,
            prompt="consent",  # Forces microsoft to show the consent page
        )

    def exchange_code(self, tenant_id, redirect_uri, code) -> dict:
        msal_client = self.build_msal_client(tenant_id)
        return msal_client.acquire_token_by_authorization_code(code, self.scopes, redirect_uri)

    def refresh_access_token(self, tenant_id, refresh_token) -> dict:
        """
        This method takes the refresh token and returns a new access token

        If an error ocurred a dict with an error key will be returned
        """
        msal_client = self.build_msal_client(tenant_id)
        return msal_client.acquire_token_by_refresh_token(refresh_token, self.scopes)

    # TODO: four main methods (CRUD)
    def get_data(self, type=None, **kwargs):
        if type is not None:
            return self._get(type, **kwargs)
        raise Exception("A type is necessary. Example: contacts, leads, accounts, etc... check the library")

    def create_data(self, type=None, **kwargs):
        if type is not None and kwargs is not None:
            params = {}
            params.update(kwargs)
            return self._post(type, json=params)
        raise Exception("A type is necessary. Example: contacts, leads, accounts, etc... check the library")

    def update_data(self, type=None, id=None, **kwargs):
        if type is not None and id is not None:
            url = "{0}({1})".format(type, id)
            params = {}
            if kwargs is not None:
                params.update(kwargs)
            return self._patch(url, json=params)
        raise Exception("A type is necessary. Example: contacts, leads, accounts, etc... check the library")

    def delete_data(self, type=None, id=None):
        if type is not None and id is not None:
            return self._delete("{0}({1})".format(type, id))
        raise Exception("A type is necessary. Example: contacts, leads, accounts, etc... check the library")

    # contact section, see the documentation https://docs.microsoft.com/es-es/dynamics365/customer-engagement/web-api/contact?view=dynamics-ce-odata-9
    def get_contacts(self, **kwargs):
        return self._get("contacts", **kwargs)

    def create_contact(self, **kwargs):
        if kwargs is not None:
            params = {}
            params.update(kwargs)
            return self._post("contacts", json=params)

    def delete_contact(self, id):
        if id != "":
            return self._delete("contacts({0})".format(id))
        raise Exception("To delete a contact is necessary the ID")

    def update_contact(self, id, **kwargs):
        if id != "":
            url = "contacts({0})".format(id)
            params = {}
            if kwargs is not None:
                params.update(kwargs)
            return self._patch(url, json=params)
        raise Exception("To update a contact is necessary the ID")

    # account section, see the documentation https://docs.microsoft.com/es-es/dynamics365/customer-engagement/web-api/account?view=dynamics-ce-odata-9
    def get_accounts(self, **kwargs):
        return self._get("accounts", **kwargs)

    def create_account(self, **kwargs):
        if kwargs is not None:
            return self._post("accounts", json=kwargs)

    def delete_account(self, id):
        if id != "":
            return self._delete("accounts({0})".format(id))
        raise Exception("To delete an account is necessary the ID")

    def update_account(self, id, **kwargs):
        if id != "":
            url = "accounts({0})".format(id)
            params = {}
            if kwargs is not None:
                params.update(kwargs)
            return self._patch(url, json=params)
        raise Exception("To update an account is necessary the ID")

    # opportunity section, see the documentation https://docs.microsoft.com/es-es/dynamics365/customer-engagement/web-api/opportunity?view=dynamics-ce-odata-9
    def get_opportunities(self, **kwargs):
        return self._get("opportunities", **kwargs)

    def create_opportunity(self, **kwargs):
        if kwargs is not None:
            params = {}
            params.update(kwargs)
            return self._post("opportunities", json=params)

    def delete_opportunity(self, id):
        if id != "":
            return self._delete("opportunities({0})".format(id))
        raise Exception("To delete an account is necessary the ID")

    def update_opportunity(self, id, **kwargs):
        if id != "":
            url = "opportunities({0})".format(id)
            params = {}
            if kwargs is not None:
                params.update(kwargs)
            return self._patch(url, json=params)
        raise Exception("To update an opportunity is necessary the ID")

    # leads section, see the documentation https://docs.microsoft.com/es-es/dynamics365/customer-engagement/web-api/lead?view=dynamics-ce-odata-9
    def get_leads(self, **kwargs):
        return self._get("leads", **kwargs)

    def create_lead(self, **kwargs):
        if kwargs is not None:
            params = {}
            params.update(kwargs)
            return self._post("leads", json=params)

    def update_lead(self, id, **kwargs):
        if id != "":
            url = "leads({0})".format(id)
            params = {}
            if kwargs is not None:
                params.update(kwargs)
            return self._patch(url, json=params)
        raise Exception("To update a lead is necessary the ID")

    def delete_lead(self, id):
        if id != "":
            return self._delete("leads({0})".format(id))
        raise Exception("To delete a lead is necessary the ID")

    # campaign section, see the documentation https://docs.microsoft.com/es-es/dynamics365/customer-engagement/web-api/campaign?view=dynamics-ce-odata-9
    def get_campaigns(self, **kwargs):
        return self._get("campaigns", **kwargs)

    def create_campaign(self, **kwargs):
        if kwargs is not None:
            params = {}
            params.update(kwargs)
            return self._post("campaigns", json=params)

    def update_campaign(self, id, **kwargs):
        if id != "":
            url = "campaigns({0})".format(id)
            params = {}
            if kwargs is not None:
                params.update(kwargs)
            return self._patch(url, json=params)
        raise Exception("To update a campaign is necessary the ID")

    def delete_campaign(self, id):
        if id != "":
            return self._delete("campaigns({0})".format(id))
        raise Exception("To delete a campaign is necessary the ID")
