# JSON stands for JavaScript Object Notation.

# It's basically a way to store and share data using key value pairs, kind of like a Python dictionary.

# The cool thing about JSON is that it's lightweight, human readable, and language independent.

# That means it doesn't matter what programming language you're using Python, JavaScript, Java you can

# all read and write JSON in the same format.

# Most of the time, JSON is used when applications send data to each other, like when a website talks

# to a server, or when you work with an API.

import json
import os
file_name = 'test.json'
data_list = json.load(open(file_name)) if os.path.exists(file_name) and os.path.getsize(file_name) > 0 else []
with open(file_name,'w') as file:
    data_list.append({"id": 1, "name":"Negede","email":"nege1221@gmail.com"})
    json.dump(data_list, file, indent=4)

