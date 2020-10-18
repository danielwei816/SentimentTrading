#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 23:17:53 2020

@author: daniel
"""
import pyrebase

# firebase configuration keys
firebase_config = {
  "apiKey": "AIzaSyCmmznsEI68l0AVICMuB5Gm3rRDifJt-xE",
  "authDomain": "sentimenttrading-f5ae7.firebaseapp.com",
  "databaseURL": "https://sentimenttrading-f5ae7.firebaseio.com/",
  "storageBucket": "sentimenttrading-f5ae7.appspot.com",
  "serviceAccount": "firebase_keys.json"
}

# initialize firebase
firebase = pyrebase.initialize_app(firebase_config)

# Get a reference to the auth service
auth = firebase.auth()

# Get a reference to the database service
db = firebase.database()