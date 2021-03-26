import unittest
import requests
import pytest
from APIDemo import *

class TestAPI(unittest.TestCase):
    def test_create_user_with_valid(self):
        APIDemo.create_user(self,"rabbit","lead")
        
    def test_delete_user_with_vaild(self):
        APIDemo.delete_user(self,2)
 
    def test_get_users_with_valid(self):
        APIDemo.get_user(self,2)

    def test_get_users_with_data_updated(self):
        APIDemo.update_user(self,2,"zion resident")

    def test_user_with_valid_reg(self):
        APIDemo.register_user(self,"eve.holt@reqres.in","pistol")
    
    def test_user_with_invalid_reg(self):
        APIDemo.register_user(self,"rabbit0057@gmail.com","test")
    
if __name__ == "__main__":
    unittest.main()