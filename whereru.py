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

def usage() :
    print 'usage : python whereru.py [<ip address>]'
    exit(1)

def main(argv) :
    if len(argv) > 2 :
        usage()

    ip = None

    if len(argv) == 2 :
        flag = is_ipv4(argv[1])
        if not flag :
            print 'Correct ip address, OK? Now, let\'s just play ipv4'
            usage()
        else :
            ip = argv[1]

    handler = HandlerFactory.create(ip)

    ip_info_dic = handler.catch()

    print ''
    print '====================================='
    print 'ip      :', ip_info_dic['data']['ip']
    print 'isp     :', ip_info_dic['data']['isp']
    print '====================================='
    print 'country :', ip_info_dic['data']['country']
    print 'area    :', ip_info_dic['data']['area']
    print 'region  :', ip_info_dic['data']['region']
    print 'city    :', ip_info_dic['data']['city']
    print 'county  :', ip_info_dic['data']['county']
    print '====================================='

if __name__ == '__main__' :
    argv = sys.argv
    main(argv)
