
import requests

api_endpoint = 'https://contactlistrahul.herokuapp.com/phonebook/'
email=['gmail.com',"yahoo.com","hotmail.com", "rediffmail.com", "outlook.com"]
    
start,end=2000,3000

for i in range(start,end):
    data['contact_name']=str(i)+"_"+chr(65+i%26)+chr(66+i%25)
    data['email']=chr(122-i%26)+chr(121-i%25)+"."+email[i%len(email)]
    requests.post(api_endpoint,data=data)
