import requests
import json


class Client:
    api_base_url = "api/data/v9.0"
    header = {"Accept": "application/json, */*", "content-type": "application/json; charset=utf-8",
              'OData-MaxVersion': '4.0', 'OData-Version': '4.0'}

    def __init__(self, resource, client_id=None, client_secret=None, token=None):
        self.resource = resource
        self.client_id = client_id
        self.client_secret = client_secret
        self.token = token

    def make_request(self, method, endpoint, expand=None, filter=None, orderby=None, select=None, skip=None, top=None,
                     data=None, json=None, **kwargs):
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
            extra['$expand'] = str(expand)
        if filter is not None and isinstance(filter, str):
            extra['$filter'] = filter
        if orderby is not None and isinstance(orderby, str):
            extra['$orderby'] = orderby
        if select is not None and isinstance(select, str):
            extra['$select'] = select
        if skip is not None and isinstance(skip, str):
            extra['$skip'] = skip
        if top is not None and isinstance(top, str):
            extra['$top'] = str(top)
        extra = '&'.join(['{0}={1}'.format(k, v) for k, v in extra.items()])
        if self.resource != "":
            if self.token:
                self.header["Authorization"] = "Bearer " + self.token
                url = '{0}{1}/{2}?{3}'.format(self.resource, self.api_base_url, endpoint, extra)
                if method == "get":
                    response = requests.request(method, url, headers=self.header, params=kwargs)
                else:
                    response = requests.request(method, url, headers=self.header, data=data, json=json)
                return self.parse_response(response)
            else:
                raise Exception("To make petitions the token is necessary")

    def _get(self, endpoint, data=None, **kwargs):
        return self.make_request('get', endpoint, data=data, **kwargs)

    def _post(self, endpoint, data=None, json=None, **kwargs):
        return self.make_request('post', endpoint, data=data, json=json, **kwargs)

    def _delete(self, endpoint, **kwargs):
        return self.make_request('delete', endpoint, **kwargs)

    def _patch(self, endpoint, data=None, json=None, **kwargs):
        return self.make_request('patch', endpoint, data=data, json=json, **kwargs)

    def parse_response(self, response):
        """
            This method get the response request and returns json data or raise exceptions
            :param response:
            :return:
        """
        if response.status_code == 204 or response.status_code == 201:
            return True
        elif response.status_code == 400:
            raise Exception(
                "The URL {0} retrieved an {1} error. Please check your request body and try again.\nRaw message: {2}".format(
                    response.url, response.status_code, response.text))
        elif response.status_code == 401:
            raise Exception(
                "The URL {0} retrieved and {1} error. Please check your credentials, make sure you have permission to perform this action and try again.".format(
                    response.url, response.status_code))
        elif response.status_code == 403:
            raise Exception(
                "The URL {0} retrieved and {1} error. Please check your credentials, make sure you have permission to perform this action and try again.".format(
                    response.url, response.status_code))
        elif response.status_code == 404:
            raise Exception(
                "The URL {0} retrieved an {1} error. Please check the URL and try again.\nRaw message: {2}".format(
                    response.url, response.status_code, response.text))
        elif response.status_code == 412:
            raise Exception(
                "The URL {0} retrieved an {1} error. Please check the URL and try again.\nRaw message: {2}".format(
                    response.url, response.status_code, response.text))
        elif response.status_code == 413:
            raise Exception(
                "The URL {0} retrieved an {1} error. Please check the URL and try again.\nRaw message: {2}".format(
                    response.url, response.status_code, response.text))
        elif response.status_code == 500:
            raise Exception(
                "The URL {0} retrieved an {1} error. Please check the URL and try again.\nRaw message: {2}".format(
                    response.url, response.status_code, response.text))
        elif response.status_code == 501:
            raise Exception(
                "The URL {0} retrieved an {1} error. Please check the URL and try again.\nRaw message: {2}".format(
                    response.url, response.status_code, response.text))
        elif response.status_code == 503:
            raise Exception(
                "The URL {0} retrieved an {1} error. Please check the URL and try again.\nRaw message: {2}".format(
                    response.url, response.status_code, response.text))
        return response.json()

    def url_petition(self, redirect_uri):
        if self.client_id is not None and redirect_uri is not None and self.resource is not None:
            url = "https://login.microsoftonline.com/{0}/oauth2/authorize?client_id={1}&response_type={2}&redirect_uri={3}&response_mode={4}&resource={5}".format(
                "common", self.client_id, "code", redirect_uri, "query", self.resource)
            return url
        else:
            raise Exception("The attributes necessary to get the url were not obtained.")


    def exchange_code(self, redirect_uri, code):
        if self.client_id is not None and self.client_secret is not None and redirect_uri is not None and code is not None:
            url = 'https://login.microsoftonline.com/common/oauth2/token'
            args = {
                'client_id': self.client_id,
                'redirect_uri': redirect_uri,
                'client_secret': self.client_secret,
                'code': code,
                'grant_type': 'authorization_code',
            }
            response = requests.post(url, data=args)
            return self.parse_response(response)
        else:
            raise Exception("The attributes necessary to exchange the code were not obtained.")

    def refresh_token(self, refresh_token, redirect_uri):
        if self.client_id is not None and self.client_secret is not None and refresh_token is not None and redirect_uri is not None and self.resource is not None:
            url = "https://login.microsoftonline.com/common/oauth2/token"
            args = {"client_id": self.client_id, "grant_type": "refresh_token", "refresh_token": refresh_token,
                    "redirect_uri": redirect_uri, "client_secret": self.client_secret, "resource": self.resource}
            response = requests.post(url, data=args)
            return self.parse_response(response)
        else:
            raise Exception("The attributes necessary to refresh the token were not obtained.")

    def set_token(self, token):
        """
            Sets the Token for its use in this library.
            :param token: A string with the Token.
            :return:
        """
        if token != "":
            self.token = token

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
            url = '{0}({1})'.format(type, id)
            params = {}
            if kwargs is not None:
                params.update(kwargs)
            return self._patch(url, json=params)
        raise Exception("A type is necessary. Example: contacts, leads, accounts, etc... check the library")

    def delete_data(self, type=None, id=None):
        if type is not None and id is not None:
            return self._delete('{0}({1})'.format(type, id))
        raise Exception("A type is necessary. Example: contacts, leads, accounts, etc... check the library")

    # contact section, see the documentation https://docs.microsoft.com/es-es/dynamics365/customer-engagement/web-api/contact?view=dynamics-ce-odata-9
    def get_contacts(self, **kwargs):
        return self._get('contacts', **kwargs)

    def create_contact(self, **kwargs):
        if kwargs is not None:
            params = {}
            params.update(kwargs)
            return self._post('contacts', json=params)

    def delete_contact(self, id):
        if id != "":
            return self._delete('contacts({0})'.format(id))
        raise Exception("To delete a contact is necessary the ID")

    def update_contact(self, id, **kwargs):
        if id != "":
            url = 'contacts({0})'.format(id)
            params = {}
            if kwargs is not None:
                params.update(kwargs)
            return self._patch(url, json=params)
        raise Exception("To update a contact is necessary the ID")

    # account section, see the documentation https://docs.microsoft.com/es-es/dynamics365/customer-engagement/web-api/account?view=dynamics-ce-odata-9
    def get_accounts(self, **kwargs):
        return self._get('accounts', **kwargs)

    def create_account(self, **kwargs):
        if kwargs is not None:
            params = {}
            params.update(kwargs)
            return self._post('accounts', json=params)

    def delete_account(self, id):
        if id != "":
            return self._delete('accounts({0})'.format(id))
        raise Exception("To delete an account is necessary the ID")

    def update_account(self, id, **kwargs):
        if id != "":
            url = 'accounts({0})'.format(id)
            params = {}
            if kwargs is not None:
                params.update(kwargs)
            return self._patch(url, json=params)
        raise Exception("To update an account is necessary the ID")

    # opportunity section, see the documentation https://docs.microsoft.com/es-es/dynamics365/customer-engagement/web-api/opportunity?view=dynamics-ce-odata-9
    def get_opportunities(self, **kwargs):
        return self._get('opportunities', **kwargs)

    def create_opportunity(self, **kwargs):
        if kwargs is not None:
            params = {}
            params.update(kwargs)
            return self._post('opportunities', json=params)

    def delete_opportunity(self, id):
        if id != "":
            return self._delete('opportunities({0})'.format(id))
        raise Exception("To delete an account is necessary the ID")

    def update_opportunity(self, id, **kwargs):
        if id != "":
            url = 'opportunities({0})'.format(id)
            params = {}
            if kwargs is not None:
                params.update(kwargs)
            return self._patch(url, json=params)
        raise Exception("To update an opportunity is necessary the ID")

    # leads section, see the documentation https://docs.microsoft.com/es-es/dynamics365/customer-engagement/web-api/lead?view=dynamics-ce-odata-9
    def get_leads(self, **kwargs):
        return self._get('leads', **kwargs)

    def create_lead(self, **kwargs):
        if kwargs is not None:
            params = {}
            params.update(kwargs)
            return self._post('leads', json=params)

    def update_lead(self, id, **kwargs):
        if id != "":
            url = 'leads({0})'.format(id)
            params = {}
            if kwargs is not None:
                params.update(kwargs)
            return self._patch(url, json=params)
        raise Exception("To update a lead is necessary the ID")

    def delete_lead(self, id):
        if id != "":
            return self._delete('leads({0})'.format(id))
        raise Exception("To delete a lead is necessary the ID")

    # campaign section, see the documentation https://docs.microsoft.com/es-es/dynamics365/customer-engagement/web-api/campaign?view=dynamics-ce-odata-9
    def get_campaigns(self, **kwargs):
        return self._get('campaigns', **kwargs)

    def create_campaign(self, **kwargs):
        if kwargs is not None:
            params = {}
            params.update(kwargs)
            return self._post('campaigns', json=params)

    def update_campaign(self, id, **kwargs):
        if id != "":
            url = 'campaigns({0})'.format(id)
            params = {}
            if kwargs is not None:
                params.update(kwargs)
            return self._patch(url, json=params)
        raise Exception("To update a campaign is necessary the ID")

    def delete_campaign(self, id):
        if id != "":
            return self._delete('campaigns({0})'.format(id))
        raise Exception("To delete a campaign is necessary the ID")
