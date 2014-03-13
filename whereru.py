#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
A bored day, just for fun!
'''

import sys
import urllib2
import re
from org.sz.handler import HandlerFactory
from org.sz.tools import is_ipv4
from org.sz.tools import is_domain
from org.sz.constants import *

def usage() :
    print 'usage : python whereru.py [<ip address|domain>]'
    exit(1)

def main(argv) :
    if len(argv) > 2 :
        usage()

    ip = []
    ip_type = NONE

    if len(argv) == 2 :
        flag_ip = is_ipv4(argv[1])
        flag_domain = is_domain(argv[1])
        if not (flag_ip or flag_domain) :
            print 'Correct ip address, OK? Now, let\'s play ipv4 and domain'
            usage()
        else :
            if flag_ip :
                ip_type = IPV4
            elif flag_domain :
                ip_type = DOMAIN
            ip.append(argv[1])

    handler = HandlerFactory.create(ip, ip_type)

    ip_info_dic = handler.catch()

    if ip_info_dic is None :
        print 'R u kidding, bye!!!'
        exit(-2)

    for ip_info in ip_info_dic :
        print ''
        print '====================================='
        print 'ip      :', ip_info['data']['ip']
        print 'isp     :', ip_info['data']['isp']
        print '====================================='
        print 'country :', ip_info['data']['country']
        print 'area    :', ip_info['data']['area']
        print 'region  :', ip_info['data']['region']
        print 'city    :', ip_info['data']['city']
        print 'county  :', ip_info['data']['county']
        print '====================================='

if __name__ == '__main__' :
    argv = sys.argv
    main(argv)
