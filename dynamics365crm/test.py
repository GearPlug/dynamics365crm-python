from client import Client

petition = Client(
    "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Ino0NHdNZEh1OHdLc3VtcmJmYUs5OHF4czVZSSIsImtpZCI6Ino0NHdNZEh1OHdLc3VtcmJmYUs5OHF4czVZSSJ9.eyJhdWQiOiJodHRwczovL2dycGx1Zy5jcm0yLmR5bmFtaWNzLmNvbSIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0L2EwNDY5NTVkLWNkNmYtNDU1YS05MTk1LWI2ODQ0ZjA1ZTNlMC8iLCJpYXQiOjE1MTY5NzU4NDcsIm5iZiI6MTUxNjk3NTg0NywiZXhwIjoxNTE2OTc5NzQ3LCJhY3IiOiIxIiwiYWlvIjoiWTJOZ1lEQmxWdWRJTDl5c3Jud3J5U3FZdFMxblQ1M0Z1N1h0L0gxdlQ4VWVxVzl6ZUFnQSIsImFtciI6WyJwd2QiXSwiYXBwaWQiOiI5NDRhOTk4Ni03N2I3LTQ1YTItYjVmMS1kYjE3YWMyOTg1ODUiLCJhcHBpZGFjciI6IjEiLCJmYW1pbHlfbmFtZSI6IkdlbHZleiIsImdpdmVuX25hbWUiOiJZb3JkeSIsImlwYWRkciI6IjE4Ni4zMS43LjIzOCIsIm5hbWUiOiJZb3JkeSBHZWx2ZXoiLCJvaWQiOiJkZDZkYWMyNy03ZTIxLTRkOGMtYjc4NC0xMWQ4ZThhZjU4YmEiLCJwdWlkIjoiMTAwMzAwMDBBN0I4RjU3RCIsInNjcCI6InVzZXJfaW1wZXJzb25hdGlvbiIsInN1YiI6Img5SHA4OFpVTGdidXRtTjUtWUVkbmlJZTUzRHZWSm8tYmloN0VyYUkzUlkiLCJ0aWQiOiJhMDQ2OTU1ZC1jZDZmLTQ1NWEtOTE5NS1iNjg0NGYwNWUzZTAiLCJ1bmlxdWVfbmFtZSI6InlvZ2VsdmV6QGdycGx1Zy5jb20iLCJ1cG4iOiJ5b2dlbHZlekBncnBsdWcuY29tIiwidXRpIjoiWlJVYURKLS1Ta3VpaUJUV2dTTUlBQSIsInZlciI6IjEuMCIsIndpZHMiOlsiNjJlOTAzOTQtNjlmNS00MjM3LTkxOTAtMDEyMTc3MTQ1ZTEwIl19.elOf7r_FXit3snTqb8eQ9YdMMxpF75KMRKaapF1ZyNi6C7xCQzsrD-hqw3z3WldCvTACaPXFgQ4K0SR91zG1yt0cFuZdtp6VSNvYieY4A1AuEnMIYTmxsoMZHwrlN25XVY8s36mXZScaaEBuyddCxjvxTxixDtBGyLkKwm57DB2759Uh8gxaKubNngr5Ql_0aAkw5prOhPr9COknhi-GgpBWKZQeTOUlfMDKsVdETyDOhBmOQEffZDLk_ZHJBoIqblSSv19ms0YAxyQhiR5WWfL9WO8fYLcJ9QRim17sw6aqZ2WMofEhOL7FNMUdbnRrW4C6foAWSOjjT-jZupxOdw")

# result = petition.create_contact(firstname="PRUEBA", lastname="ES UNA PRUEBA", middlename="MEDIO", emailaddress1="prueba@test.com")
# result = petition.update_contact("b935b503-5901-e811-a834-000d3ac0a338", firstname="AQUILES YA NO BAILA")
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
# result = petition.get_data('')
# result = petition.get_data('serviceendpoints', filter="contract eq 8", select="serviceendpointid,name,authtype,url")
# result = petition.create_data('contacts', firstname="PRUEBA", lastname="ES UNA PRUEBA", middlename="MEDIO", emailaddress1="prueba@test.com")
# print(result)
