'''
base tools
'''

# -*- coding: utf-8 -*-

import re

def is_ipv4(ip) :
    pattern = r'^(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9]{1,2})(\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9]{1,2})){3}$'
    matcher = re.match(pattern, ip)
    if matcher is None :
        return False
    else :
        return True
