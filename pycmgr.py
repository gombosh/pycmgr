#!/usr/bin/env python3
'''
-------------------------------------------------------------------------
File name    : pycmgr.py
Title        : 
Project      : 
Developers   :  dorong
Created      : Sun Nov 14, 2021  02:43PM
Description  : 
Notes        : 
---------------------------------------------------------------------------
---------------------------------------------------------------------------*/
'''
import base64


def encode(s):
    '''
    used to encode the strings (very simple encoding just to hide from plan searches)
    '''
    return base64.b64encode(s.encode("utf-8"))


def gen_creds(name, hostname="", username="", password=""):
    '''
    generate (encode) and return an instance of the credential class
    the output class should be saved into file.
    for your convenience, the instance have a "print_to_file" function.
    '''
    return credential(encode(name), encode(hostname), encode(username),
                      encode(password))


class credential:
    '''
    this class holds a single encoded credential database
    the 'name' is the only mandatory input
    other (optional) inputs are hostname, user name and password
    '''
    def __init__(self, name, hostname, username, password):
        self.name = name
        self.hostname = hostname
        self.username = username
        self.password = password

    def __str__(self):
        '''
        overload the 'print' function to return a string ready to be pasted
        into the credentials file
        '''
        return f"credential({self.name}, {self.hostname}, {self.username}, {self.password})"

    def print_to_file(self, filename, inst_name="dummy", append=True):
        '''
        print the created instance into the secrets file.
        you need to provide the file path (and name), and
        a name for the instance (can be any name as long as it's unique)
        you can choose if you want to append or overwrite the file.
        '''
        with open(filename, "a" if append else "w") as f:
            f.write("from pycmgr import credential\n")
            f.write(f"{inst_name} = " + self.__str__() + "\n")

    # DECODING + ACCESS FUNCTIONS
##########################################################

    def get_name(self):
        return base64.b64decode(self.name).decode("utf-8")

    def get_host(self):
        return base64.b64decode(self.hostname).decode("utf-8")

    def get_user(self):
        return base64.b64decode(self.username).decode("utf-8")

    def get_pass(self):
        return base64.b64decode(self.password).decode("utf-8")


##########################################################
