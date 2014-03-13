'''
begin to get ip address info
'''

# -*- coding: utf-8 -*-

import os
import urllib2
import json
import socket

from tools import is_ipv4
from constants import *

GET_LOCAL_ADDRESS = r'ifconfig.me'
GET_IP_INFO_PREFIX = r'http://ip.taobao.com/service/getIpInfo.php?ip='

class HandlerFactory :

    @staticmethod
    def create(ip, ip_type) :
        res = {
                0 : lambda : LocalHandler(),
                }
        handler = None

        try :
            handler = res[len(ip)]()
        except KeyError, e :
            handler = ForeignHandler(ip, ip_type)

        return handler

class BaseHandler(object) :

    def __init__(self, ip, ip_type) :
        self.ip = ip
        self.ip_type = ip_type

    def catch(self, index) :
        html = urllib2.urlopen(GET_IP_INFO_PREFIX + self.ip[index])
        if html is None :
            print 'U know we need connect Internet, right?'
            exit(-2)

        addressDic = json.loads(html.read())

        return addressDic

class LocalHandler(BaseHandler) :

    def __init__(self) :
        super(LocalHandler, self).__init__([], NONE)

    def __curl(self) :
        address = os.popen('curl ' + GET_LOCAL_ADDRESS).read()
        address = address.replace('\n', '')
        flag = is_ipv4(address)
        if flag :
            self.ip.append(address)
        else :
            print 'Can\'t fetch the public ip address on ur computer, bye'
            exit(-1)

    def catch(self) :
        self.__curl()

        ip_dics = []
        ip_dics.append(super(LocalHandler, self).catch(0))

        return ip_dics

class ForeignHandler(BaseHandler) :

    def __domain_2_ip(self) :
        for res in socket.getaddrinfo(self.ip[0], None, socket.AF_INET, socket.SOCK_STREAM) :
            af, sock_type, proto, canon_name, sa = res
            self.ip.append(sa[0])
            #print self.ip

    def catch(self) :
        ip_dics = []

        if self.ip_type == DOMAIN :
            self.__domain_2_ip()
            if len(self.ip) <= 1 :
                return None

            del self.ip[0]

            index = 0
            for domain_ip in self.ip :
                ip_dics.append(super(ForeignHandler, self).catch(index))
                index += 1

        elif self.ip_type == IPV4 :
            ip_dics.append(super(ForeignHandler, self).catch(0))
        else :
            return None

        return ip_dics
