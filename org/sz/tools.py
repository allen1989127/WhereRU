'''
base tools
'''

# -*- coding: utf-8 -*-

import re

def is_ipv4(ip) :
    pattern = r'^(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9]{1,2})(\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9]{1,2})){3}$'
    matcher = re.match(pattern, ip)
    if matcher is not None :
        return True

    return False

def is_domain(domain) :
    pattern = r'[a-zA-Z0-9][-a-zA-Z0-9]{0,62}(\.[a-zA-Z0-9][-a-zA-Z0-9]{0,62})+\.?'
    matcher = re.match(pattern, domain)
    if matcher is not None :
        return True

    return False
