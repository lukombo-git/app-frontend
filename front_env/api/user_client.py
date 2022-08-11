import requests
from flask import session
from requests.api import head
from front_env.api.__init__ import USER_API_URL

class UserClient:
    @staticmethod
    def login(form):
        api_key_final= ""
        payload = {
            'username':form.username.data,
            'password':form.password.data
        }
        url = USER_API_URL +'/api/user/login'
        response = requests.post(url, data=payload)
        if response:
            api_key = response.json()
            api_key_final = api_key.get('api_key')
        return api_key_final
    
    @staticmethod
    def get_user():
        headers = {
            'Authorization':session['user_api_key']
        }
        url = USER_API_URL +'/api/user'
        response = requests.get(url, headers = headers)
        return response.json()


    @staticmethod
    def get_user_id(id_user):
        id_user = str(id_user)
        response = requests.get(USER_API_URL +"/api/user/"+ id_user)
        return response.json()

    @staticmethod
    def create_user(form):
        user= None
        payload = {
            'username':form.username.data,
            'first_name': form.first_name.data,
            'last_name': form.last_name.data,
            'address': form.address.data,
            'city': form.city.data,
            'country': form.country.data,
            'post_code': form.post_code.data,
            'password':form.password.data
        }
        url = USER_API_URL +'/api/user/create'
        response = requests.request("POST", url=url, data=payload)
        if response:
            user = response.json()
        return user
    
    @staticmethod
    def user_exists(username):
        url = USER_API_URL+'/api/user/'+username+'/exists'
        response = requests.get(url)
        return response

    @staticmethod
    def count_users():
        response = requests.get(USER_API_URL+'/api/user/count_users')
        return response.json()
    
    @staticmethod
    def get_users():
        response = requests.get(USER_API_URL+'/api/user/all')
        return response.json()


    @staticmethod
    def update_user(form,id_user):
        user = None
        url = USER_API_URL +"/api/user/update/"+id_user
        response = requests.request("PUT", url=url, data=form)
        if response:
            user = response.json()
        return user

    @staticmethod
    def delete_user_id(id_user):
        response = requests.delete(USER_API_URL+'/api/user/delete/'+id_user)
        return response.json()


