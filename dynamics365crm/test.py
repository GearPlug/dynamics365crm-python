from client import Client
import pprint

"""
MAIN INSTANCE
obligatory send the access_token
"""
petition = Client(
    "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Ino0NHdNZEh1OHdLc3VtcmJmYUs5OHF4czVZSSIsImtpZCI6Ino0NHdNZEh1OHdLc3VtcmJmYUs5OHF4czVZSSJ9.eyJhdWQiOiJodHRwczovL2dycGx1Zy5jcm0yLmR5bmFtaWNzLmNvbSIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0L2EwNDY5NTVkLWNkNmYtNDU1YS05MTk1LWI2ODQ0ZjA1ZTNlMC8iLCJpYXQiOjE1MTgwMTkwNDUsIm5iZiI6MTUxODAxOTA0NSwiZXhwIjoxNTE4MDIyOTQ1LCJhY3IiOiIxIiwiYWlvIjoiQVNRQTIvOEdBQUFBSWFRY2M0amsrM0dOTitHMTRmRDBHLytrNGhLUjA4V1FQays4YVUrZXA0Yz0iLCJhbXIiOlsicHdkIl0sImFwcGlkIjoiOTQ0YTk5ODYtNzdiNy00NWEyLWI1ZjEtZGIxN2FjMjk4NTg1IiwiYXBwaWRhY3IiOiIxIiwiZmFtaWx5X25hbWUiOiJHZWx2ZXoiLCJnaXZlbl9uYW1lIjoiWW9yZHkiLCJpcGFkZHIiOiIxODYuMzEuNy4yMzgiLCJuYW1lIjoiWW9yZHkgR2VsdmV6Iiwib2lkIjoiZGQ2ZGFjMjctN2UyMS00ZDhjLWI3ODQtMTFkOGU4YWY1OGJhIiwicHVpZCI6IjEwMDMwMDAwQTdCOEY1N0QiLCJzY3AiOiJ1c2VyX2ltcGVyc29uYXRpb24iLCJzdWIiOiJoOUhwODhaVUxnYnV0bU41LVlFZG5pSWU1M0R2VkpvLWJpaDdFcmFJM1JZIiwidGlkIjoiYTA0Njk1NWQtY2Q2Zi00NTVhLTkxOTUtYjY4NDRmMDVlM2UwIiwidW5pcXVlX25hbWUiOiJ5b2dlbHZlekBncnBsdWcuY29tIiwidXBuIjoieW9nZWx2ZXpAZ3JwbHVnLmNvbSIsInV0aSI6IjNBb1VjMXQwSDAyamlOYWRqZFJCQUEiLCJ2ZXIiOiIxLjAiLCJ3aWRzIjpbIjYyZTkwMzk0LTY5ZjUtNDIzNy05MTkwLTAxMjE3NzE0NWUxMCJdfQ.hI2NO0TiY3TNIig4z7FEBuB5jmFeHe-hO8i7-1RVg8ASlgPxiwstQU3POuM6CQ6xQw6nMbNKunHFX7MB7FAFFPX9Wr932XfqsppNvAWAv88s4YTEFZLV0tfxCm3fP0YzelIqJRqnp1pUTwvd8-Lnu-hwxiOWD5k5Ry3Y1aECnCSTwWwXncJdMBHQ6EedNWDwANggfYCJKioVcWXJfZM6ssKXCaZYCYUdyuz0birwVNzfPCHxFVdC8jG_cCVU6a0uvsM24M0-c3NJrS1zRkbZQEy9JmcUOC9C0rHXgFOyTCID96wWwJhr9ggDy6yG-0kVKUzHRN0uTXrFqYTM8OXoew")
refresh_token = "AQABAAAAAABHh4kmS_aKT5XrjzxRAtHzeeroM8I_s30g1SZHpO5rpBiZEWvj6-2bA2iHSseKDfPXX4eP9uw5nOD9Lt71NVdTve1ZGNlNvRV64Vm2WK2sCEKI3kkayTwDdoSkftI_Eo0WIIuyUdlwm0ratAR6kMErgbegLm7dPBKBonIgsciQtnL5EkzNJmqhUOK_xXDxz7vX2nie9rx4ooJk_O1g9Korj_LvRxcqbesV3BbcojLsrWwpc_J0IxuCrerXcGHkj20vjze8Cx14hQSIUrE3ne3ry5HtP5xqqyZLx7a5Kkvex90RPHqeF27h1ArA0TUJx1zWjKRa6GNdJv5Z1bMO_wUBlnUYCWszxuweCftEJovwytjIbZHr2d9nS6rnxCRcMIM-PTPigSD9W__xL8eq011rYGxWS6hCaI3n-SFiqAm2JyR_Ja7uNZjZpaEN9q9gPuhOgkfDd9FPH2RlgoUTWj_I-yuqoerU3GT7VX8H6BFD-eepmLCqfnsyOf6rTEiAFH4_4xw5IbiYBHolJ6ZZ5-DM8xk-JtEGeTC0d4VaXsL3iWXPiPE0AduoHq9YSmGhAR2is8tyFWUcvfXbo4_V-z_7i09HRGOxe6bvH-tMW99c5XCEd3SKzry0mkqKaOeRsNyF4IP9Dp1IbYm_oEqH2LhzUkFE9AzgEZvPBqMhYoQPZu8cVUFMsxxa4hnZ-R8aIgGcVvtwk324pvPzUFdu2865-xivSc4J3-uidNRkjZH1XatSB5EP7xg6lmOitLnNqEJ-znayGJ2ANhwLaYFeQcFCo3cN6QcyQXyu8_pJYz9ZECAA"

"""
API ENDPOINTS EXAMPLES
"contacts", "accounts", "opportunities", "leads", "campaigns", "EntityDefinitions(LogicalName='contact')/Attributes"
"""

"""
REFRESH TOKEN
to refresh the token you have to send the client_id, the client_secret, the refresh_token, the redirect_uri, and the resource
Example:
    refresh = petition.refresh_token("CLIENT ID", "CLIENT SECRET", 
                                    refresh_token, "REDIRECT URI",
                                    "RESOURCE")
    pprint.pprint(refresh)
"""
# result = petition.refresh_token("944a9986-77b7-45a2-b5f1-db17ac298585", "5JcKFcmaY3uWUPpdynL1aDwoSFnGMOlOnEa4bKLYtvQ=",
#                                 refresh_token, "https://54b8571a.ngrok.io/dynamic/oauth",
#                                 "https://grplug.crm2.dynamics.com")
# pprint.pprint(result)

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

# result = petition.create_contact(firstname="PRUEBA", lastname="ES UNA PRUEBA", middlename="MEDIO", emailaddress1="prueba@test.com")
# result = petition.update_contact("b935b503-5901-e811-a834-000d3ac0a338", firstname="AQUILES YA NO BAILA")
# print(result)
# result = petition.delete_contact("3555421c-f501-e811-a834-000d3ac085f9")
# result = petition.get_contacts()

# result = petition.create_account(name="Google", websiteurl="www.google.com")
# result = petition.update_account(id="3b596d9c-0c02-e811-a836-000d3ac0bc58", name="CAMBIONAME")
# result = petition.delete_account(id="3b596d9c-0c02-e811-a836-000d3ac0bc58")
# result = petition.get_accounts()

# result = petition.create_opportunity(name="OPORTUNIDAD PRUEBA")
# result = petition.update_opportunity(id="e3816f1b-1502-e811-a836-000d3ac09c3f", name="LE CAMBIO A LA PRUEBA", description="No se que decir, pero es relleno")
# result = petition.delete_opportunity("e3816f1b-1502-e811-a836-000d3ac09c3f")
# result = petition.get_opportunities()

# result = petition.create_lead(fullname="LEAD TEST", subject="LEAD TEST", mobilephone="12346", websiteurl="youporn.com", middlename="MIDDLE LEAD TEST")
# result = petition.update_lead("07e92783-1902-e811-a834-000d3ac085f9", mobilephone="3144773197", websiteurl="example.com")
# result = petition.delete_lead("07e92783-1902-e811-a834-000d3ac085f9")
# result = petition.get_leads()

# result = petition.create_campaign(name="CAMPAIGN TEST", description="I just know, that i don´t know a shit")
# result = petition.update_campaign("4dda96e7-1c02-e811-a836-000d3ac09c3f", name="CAMPAIGN TEST CORRECTION", description="I just know, that i know everything")
# result = petition.delete_campaign("4dda96e7-1c02-e811-a836-000d3ac09c3f")
# result = petition.get_campaigns()

# contacts, accounts, opportunities, leads, campaigns
# at = datetime.datetime.now()
# result = petition.get_data("EntityDefinitions(LogicalName='contact')/Attributes")
# result = petition.get_data('serviceendpoints', filter="contract eq 8", select="serviceendpointid,name,authtype,url")
# result = petition.create_data('contacts', firstname="YORDY", lastname="GELVEZ", middlename="ALEJANDRO", emailaddress1="yordy.gelvez@test.com")

# GET LAST
# result = petition.get_data(type="contacts", select="fullname, emailaddress1, createdon", orderby="createdon desc")
# r = result['value']
# print(len(r))
# print(r[0]['createdon'])

# GET FROM DATE
# date_from = "2018-01-30T16:06:55Z"
# result = petition.get_data(type="contacts", filter="createdon ge {0}".format(date_from), select="firstname, createdon", orderby="createdon asc")
