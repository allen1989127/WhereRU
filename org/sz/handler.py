'''
begin to get ip address info
'''

# -*- coding: utf-8 -*-

import os
import urllib2
import json

from tools import is_ipv4

GET_LOCAL_ADDRESS = r'ifconfig.me'
GET_IP_INFO_PREFIX = r'http://ip.taobao.com/service/getIpInfo.php?ip='

class HandlerFactory :

    @staticmethod
    def create(ip) :
        if ip is None :
            return LocalHandler()
        else :
            return ForeignHandler(ip)

class BaseHandler(object) :

    def __init__(self, ip) :
        self.ip = ip

    def catch(self) :
        html = urllib2.urlopen(GET_IP_INFO_PREFIX + self.ip)
        if html is None :
            print 'U know we need connect Internet, right?'
            exit(-2)

        addressDic = json.loads(html.read())

        return addressDic

class LocalHandler(BaseHandler) :

    def __init__(self) :
        super(LocalHandler, self).__init__(None)

    def __curl(self) :
        address = os.popen('curl ' + GET_LOCAL_ADDRESS).read()
        address = address.replace('\n', '')
        flag = is_ipv4(address)
        if flag :
            self.ip = address
        else :
            print 'Can\'t fetch the public ip address on ur computer, bye'
            exit(-1)

    def catch(self):
        self.__curl()
        return super(LocalHandler, self).catch()

class ForeignHandler(BaseHandler) :
    pass
