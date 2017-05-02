#Please download the file in the attachment and use Python to print out its content

#!usr/bin/python
# -*- coding: utf-8 -*-

import json
from pprint import pprint

with open('company1.json', 'r') as f:
    data = json.loads(f.read())
pprint (data)
