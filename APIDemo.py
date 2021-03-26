import requests
import json
from datetime import datetime
from urllib.request import HTTPError

class APIDemo(object):

    def __init__(self):

        self.result_structure = None # return response for the requests
        self.created_at = "DAY, dd mm YYYY hh:mm:ss" # timestamp the requests are processed
        self.user_id = "" # user id of the specific user
        
        # response definition
        self.response_content_type = "" # content type value returned in request response
        self.server_name = ""   # name of the server where the request executes
        self.response_code = "" # return code of the request response


    def create_user(self, user_name, job):
        """
        Action : Create a new user from given parameters.Overwrite values of instance data members.
        Reference API : https://reqres.in/ (create)
        
        Important note on overwriting instance data attributes:
        response_code : an integer type     
        result_structure : a dictionary type
        created_at : a string type with the format DAY, dd mm YYYY hh:mm:ss( ex: Mon, 15 Feb 2021 06:08:22)
        server_name  : a string type .
   
        Parameters and Return values
        :param user_name: name of the user 
        :param job: job of the user
        :return:In case of successful user creation , it should be True else False """

        payload = {
            "name":user_name,
            "job":job
        }
        url = "https://reqres.in/api/users"
        resp = requests.post(url,data=payload)
        print("response_code:",resp.status_code)
        print("result_structure:",resp.json()) 
        createdat = resp.json() ['createdAt']  
        coverttime = datetime.fromisoformat(createdat[:-1])    
        convertedtime = coverttime.strftime('%a, %d %b %Y %H:%M:%S') 
        print("createdAt:",convertedtime)
        print("server_url:",url)
        print("user_name:",resp.json() ['name'])
        print("job:",resp.json() ['job']) 
        print("create_user_status is:",resp.ok)
        assert resp.status_code == 201 , "User creation failed"
        assert resp.json() ['name'] == user_name
        assert resp.json() ['job'] == job
        


    



    def delete_user(self, user_id):
        """
        Action : Create a new user from given parameters.Overwrite values of instance data members.
        Reference API : https://reqres.in/ (delete)
        
        Important note on overwriting instance data attributes:
        response_code : an integer type
        result_structure : a dictionary type
        response_content_type : a string type
        server_name  : a string type
   
        Parameters and Return values
        :param user_id: id of the user 
        :return:In case of successful user delete action , it should be True else False
        """
        url = "https://reqres.in/api/user/%s" % user_id
        resp = requests.delete(url)
        print("response_code:",resp.status_code)
        # print("result_structure:",resp.json()) 
        # print("response_content_type:", resp.text)
        print("server_url:",url)
        print("id:",user_id)
        print("delete_user_status is:",resp.ok)
        assert resp.status_code == 204 ,"User deletion failed"

    def get_user(self, user_id):
        """
        Action : Get the specific user(single user) definition from given parameters.Overwrite values of instance data members.
        Reference API : https://reqres.in/ (single user)
        
        Important note on overwriting instance data attributes:
        response_code : an integer type
        result_structure : a list type , only "data" value with [[key1,value1],[key2, value2]...[key n, value n]] with sorted key order.
        ex: result_structure = [["avatar" ,"http://.."], ["email","tst@tst.com"],["first_name","tst"],["",""]..]
        response_content_type : a string type
        server_name  : a string type
   
        Parameters and Return values
        :param user_id: id of the user 
        :return:In case user is present , it should be True else False
        """
        url = "https://reqres.in/api/users?page=%s" % user_id
        resp = requests.get(url)
        print("response_code:",resp.status_code)
        result = json.loads(resp.text)
        print("result_structure:",result['data'])
        print("response_content_type:",resp.text)
        print("server_name:",url)
        print("id:",user_id)
        print("get_user_status is:",resp.ok)
        assert resp.status_code == 200 , "Failed to get user data"

    def update_user(self, user_id, job):
        """
        Action : update the user's specific definition from given parameters.Overwrite values of instance data members.
        Reference API : https://reqres.in/ (update)

        Important note on overwriting instance data attributes:
        response_code : an integer type
        result_structure : a dictionary type
        response_content_type : a string type

        Parameters and Return values
        :param user_id: name of the user you want to update
        :param job: job of the user to be changed
        :return: In case user is updated , it should be True else False
        """
        payload = {
            "name":"API",
            "job":"API testing"
        }
        url = "https://reqres.in/api/users/%s" % user_id
        resp_1 = requests.get(url)
        resp = requests.put(url,data=payload)
        print("response_code:",resp.status_code)
        print("result_structure:",resp.json()) 
        print("response_content_type:",resp.text)
        print("user_id:",resp_1.json()['data']['first_name'])
        print("job:",job)
        print("update_user_status is:",resp.ok)

        assert resp.status_code == 200 , "User data failed updated"
        assert resp.json() ['job'] == "API testing"
        
    def register_user(self, email_id, password):
        """
        Action : register the user's specific definition from given parameters.Overwrite values of instance data members.

        Important note on overwriting instance data attributes:
        response_code : an integer type
        result_structure : a dictionary type
        response_content_type : a string type

        Parameters and Return values
        :param email_id: email_id of user
        :param password: password for the user
        :return:  In case of successful user registration , it should be True else False
        """

        payload = {
            "email":email_id,
            "password":password
        }
        url = "https://reqres.in/api/register"
        resp = requests.post(url,data=payload)
        print("response_code:",resp.status_code)
        print("result_structure:",resp.json())
        print("response_content_type:",resp.text)
        print("email_id:",email_id)
        print("password:",password)
        print("registration_status is:",resp.ok)
        assert resp.status_code == 200 , "User registeration failed "


       
       
        

