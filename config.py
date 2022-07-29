import os

table_name = "WEB_URL"

# WTF config

WTF_CSRF_ENABLED = True
SECRET_KEY = 'U_Short_Url_just_shorten_it'

# MySQL Config


host = "localhost"
user = "root"
passwrd = "abcd26"
db = "USHORT"

# Domain Host

'''
For now , use http as using https returns a bad error message , 
For https , use a SSL certificate. ( under works)
'''
domain = "http://localhost:5000/"
