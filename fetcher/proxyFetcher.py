# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     proxyFetcher
   Description :
   Author :        JHao
   date：          2016/11/25
-------------------------------------------------
   Change Activity:
                   2016/11/25: proxyFetcher
-------------------------------------------------
"""
__author__ = 'JHao'

import re
import json
from time import sleep

from util.webRequest import WebRequest


class ProxyFetcher(object):
    """
    proxy getter
    """

    # @staticmethod
    # def freeProxy01():
    #     """
    #     站大爷 https://www.zdaye.com/dayProxy.html
    #     """
    #     start_url = "https://www.zdaye.com/dayProxy.html"
    #     html_tree = WebRequest().get(start_url, verify=False).tree
    #     latest_page_time = html_tree.xpath("//span[@class='thread_time_info']/text()")[0].strip()
    #     from datetime import datetime
    #     interval = datetime.now() - datetime.strptime(latest_page_time, "%Y/%m/%d %H:%M:%S")
    #     if interval.seconds < 300:  # 只采集5分钟内的更新
    #         target_url = "https://www.zdaye.com/" + html_tree.xpath("//h3[@class='thread_title']/a/@href")[0].strip()
    #         while target_url:
    #             _tree = WebRequest().get(target_url, verify=False).tree
    #             for tr in _tree.xpath("//table//tr"):
    #                 ip = "".join(tr.xpath("./td[1]/text()")).strip()
    #                 port = "".join(tr.xpath("./td[2]/text()")).strip()
    #                 yield "%s:%s" % (ip, port)
    #             next_page = _tree.xpath("//div[@class='page']/a[@title='下一页']/@href")
    #             target_url = "https://www.zdaye.com/" + next_page[0].strip() if next_page else False
    #             sleep(5)
    #
    # @staticmethod
    # def freeProxy02():
    #     """
    #     代理66 http://www.66ip.cn/
    #     """
    #     url = "http://www.66ip.cn/"
    #     resp = WebRequest().get(url, timeout=10).tree
    #     for i, tr in enumerate(resp.xpath("(//table)[3]//tr")):
    #         if i > 0:
    #             ip = "".join(tr.xpath("./td[1]/text()")).strip()
    #             port = "".join(tr.xpath("./td[2]/text()")).strip()
    #             yield "%s:%s" % (ip, port)
    #
    # @staticmethod
    # def freeProxy03():
    #     """ 开心代理 """
    #     target_urls = ["http://www.kxdaili.com/dailiip.html", "http://www.kxdaili.com/dailiip/2/1.html"]
    #     for url in target_urls:
    #         tree = WebRequest().get(url).tree
    #         for tr in tree.xpath("//table[@class='active']//tr")[1:]:
    #             ip = "".join(tr.xpath('./td[1]/text()')).strip()
    #             port = "".join(tr.xpath('./td[2]/text()')).strip()
    #             yield "%s:%s" % (ip, port)
    #
    # @staticmethod
    # def freeProxy04():
    #     """ FreeProxyList https://www.freeproxylists.net/zh/ """
    #     url = "https://www.freeproxylists.net/zh/?c=CN&pt=&pr=&a%5B%5D=0&a%5B%5D=1&a%5B%5D=2&u=50"
    #     tree = WebRequest().get(url, verify=False).tree
    #     from urllib import parse
    #
    #     def parse_ip(input_str):
    #         html_str = parse.unquote(input_str)
    #         ips = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', html_str)
    #         return ips[0] if ips else None
    #
    #     for tr in tree.xpath("//tr[@class='Odd']") + tree.xpath("//tr[@class='Even']"):
    #         ip = parse_ip("".join(tr.xpath('./td[1]/script/text()')).strip())
    #         port = "".join(tr.xpath('./td[2]/text()')).strip()
    #         if ip:
    #             yield "%s:%s" % (ip, port)
    #
    # @staticmethod
    # def freeProxy05(page_count=1):
    #     """ 快代理 https://www.kuaidaili.com """
    #     url_pattern = [
    #         'https://www.kuaidaili.com/free/inha/{}/',
    #         'https://www.kuaidaili.com/free/intr/{}/'
    #     ]
    #     url_list = []
    #     for page_index in range(1, page_count + 1):
    #         for pattern in url_pattern:
    #             url_list.append(pattern.format(page_index))
    #
    #     for url in url_list:
    #         tree = WebRequest().get(url).tree
    #         proxy_list = tree.xpath('.//table//tr')
    #         sleep(1)  # 必须sleep 不然第二条请求不到数据
    #         for tr in proxy_list[1:]:
    #             yield ':'.join(tr.xpath('./td/text()')[0:2])
    #
    # @staticmethod
    # def freeProxy06():
    #     """ FateZero http://proxylist.fatezero.org/ """
    #     url = "http://proxylist.fatezero.org/proxy.list"
    #     try:
    #         resp_text = WebRequest().get(url).text
    #         for each in resp_text.split("\n"):
    #             json_info = json.loads(each)
    #             if json_info.get("country") == "CN":
    #                 yield "%s:%s" % (json_info.get("host", ""), json_info.get("port", ""))
    #     except Exception as e:
    #         print(e)
    #
    # @staticmethod
    # def freeProxy07():
    #     """ 云代理 """
    #     urls = ['http://www.ip3366.net/free/?stype=1', "http://www.ip3366.net/free/?stype=2"]
    #     for url in urls:
    #         r = WebRequest().get(url, timeout=10)
    #         proxies = re.findall(r'<td>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})</td>[\s\S]*?<td>(\d+)</td>', r.text)
    #         for proxy in proxies:
    #             yield ":".join(proxy)
    #
    # @staticmethod
    # def freeProxy08():
    #     """ 小幻代理 """
    #     urls = ['https://ip.ihuan.me/address/5Lit5Zu9.html']
    #     for url in urls:
    #         r = WebRequest().get(url, timeout=10)
    #         proxies = re.findall(r'>\s*?(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s*?</a></td><td>(\d+)</td>', r.text)
    #         for proxy in proxies:
    #             yield ":".join(proxy)
    #
    # @staticmethod
    # def freeProxy09(page_count=1):
    #     """ 免费代理库 """
    #     for i in range(1, page_count + 1):
    #         url = 'http://ip.jiangxianli.com/?country=中国&page={}'.format(i)
    #         html_tree = WebRequest().get(url, verify=False).tree
    #         for index, tr in enumerate(html_tree.xpath("//table//tr")):
    #             if index == 0:
    #                 continue
    #             yield ":".join(tr.xpath("./td/text()")[0:2]).strip()
    #
    # @staticmethod
    # def freeProxy10():
    #     """ 89免费代理 """
    #     r = WebRequest().get("https://www.89ip.cn/index_1.html", timeout=10)
    #     proxies = re.findall(
    #         r'<td.*?>[\s\S]*?(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})[\s\S]*?</td>[\s\S]*?<td.*?>[\s\S]*?(\d+)[\s\S]*?</td>',
    #         r.text)
    #     for proxy in proxies:
    #         yield ':'.join(proxy)


    @staticmethod
    def freeProxy11():
        """ us-proxy """
        r = WebRequest().get("https://us-proxy.org/", timeout=10)
        proxies = re.findall(
            r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5})', r.text)
        for proxy in proxies:
            yield ':'.join(proxy)


    @staticmethod
    def freeProxy13():
        """ geonode """
        url = 'https://proxylist.geonode.com/api/proxy-list?limit=100&page=1&sort_by=lastChecked&sort_type=desc&country=US&protocols=http'
        r = WebRequest().get(url, timeout=50)
        data = json.loads(r.text).get('data')
        for da in data:
            yield da.get('ip') + ':' + da.get('port')


    @staticmethod
    def freeProxy14():
        """ geonode """
        url = 'https://www.freeproxy.world/?anonymity=&country=US&speed=&port=&page=1'
        r = WebRequest().get(url, timeout=50)
        proxies = re.findall(r'<tr>\s*<td.*?>\s*(.*?)\s*</td>\s*<td.*?>\s*<a[^>]*>\s*(\d+)\s*</a>\s*</td>', r.text)
        for proxy in proxies:
            yield ':'.join(proxy)


    @staticmethod
    def freeProxy15():
        """ geonode """
        url = 'https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS.txt'
        r = WebRequest().get(url, timeout=50)
        proxies = re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5})', r.text)
        for proxy in proxies:
            yield ':'.join(proxy)


    @staticmethod
    def freeProxy16():
        """ geonode """
        url = 'https://www.proxy-list.download/HTTPS'
        r = WebRequest().get(url, timeout=50)
        proxies = re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s*</td>\s*<td>\s*(\d{1,5})', r.text)
        for proxy in proxies:
            yield ':'.join(proxy)


    @staticmethod
    def freeProxy17():
        """ geonode """
        # url = 'https://www.proxy-list.download/HTTPS'
        urls = [
        'https://raw.githubusercontent.com/HyperBeats/proxy-list/main/http.txt',
        'https://raw.githubusercontent.com/HyperBeats/proxy-list/main/https.txt',
        'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt',
        'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt',
        'https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt',
        'https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt',
        'https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt',
        'https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/http.txt',
        'https://raw.githubusercontent.com/NotUnko/autoproxies/main/http.txt',
        'https://raw.githubusercontent.com/NotUnko/autoproxies/main/http2.txt',
        'https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt',
        'https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/https/https.txt',
        'https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt',
        'https://raw.githubusercontent.com/proxylist-to/proxy-list/main/http.txt',
        'https://raw.githubusercontent.com/prxchk/proxy-list/main/http.txt',
        'https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt',
        'https://raw.githubusercontent.com/rx4096/proxylist/main/online/http.txt',
        'https://raw.githubusercontent.com/rx4096/proxylist/main/online/https.txt',
        'https://raw.githubusercontent.com/saisuiu/Lionkings-Http-Proxys-Proxies/main/free.txt',
        'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt',
        'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt',
        'https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt',
        'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt',
        'https://raw.githubusercontent.com/ToShukKr/rProxyList/main/proxy-list.txt',
        'https://raw.githubusercontent.com/TylerAmesIsGay/proxy-list/main/http_proxies%20(2).txt',
        'https://raw.githubusercontent.com/TylerAmesIsGay/proxy-list/main/http_proxies%20(3).txt',
        'https://raw.githubusercontent.com/yemixzy/proxy-list/main/proxies/http.txt',
        'https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/http.txt',
        'https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/https.txt',
        'https://raw.githubusercontent.com/zevtyardt/proxy-list/main/http.txt',
        'https://rootjazz.com/proxies/proxies.txt',
        'https://spys.me/proxy.txt',
        'https://www.proxy-list.download/api/v1/get?type=http',
        'https://www.proxy-list.download/api/v1/get?type=https'
        #'https://raw.githubusercontent.com/HyperBeats/proxy-list/main/http.txt'
        ]
        for url in urls:
            r = WebRequest().get(url, timeout=50)
            proxies = re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{2,5})', r.text)
            for proxy in proxies:
                yield ':'.join(proxy)
                
    
    @staticmethod
    def freeProxy18():
        urls = [
            "https://api.proxyscrape.com/?request=displayproxies&proxytype=http",
            "https://www.proxy-list.download/api/v1/get?type=http",
            "https://www.proxyscan.io/download?type=http",
            "http://spys.me/proxy.txt",
            "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt",
            "https://api.openproxylist.xyz/http.txt",
            "https://raw.githubusercontent.com/shiftytr/proxy-list/master/proxy.txt",
            "http://alexa.lr2b.com/proxylist.txt",
            "http://rootjazz.com/proxies/proxies.txt"]
        for url in urls:
            r = WebRequest().get(url, timeout=50)
            proxies = re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{2,5})', r.text)
            for proxy in proxies:
                yield ':'.join(proxy)


    @staticmethod
    def freeProxy19():
        urls = [
            "https://www.freeproxychecker.com/result/http_proxies.txt",
            "http://proxysearcher.sourceforge.net/Proxy%20List.php?type=http",
            "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt",
            "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
            "https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt",
            "https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt",
            "https://proxy-spider.com/api/proxies.example.txt",
            "https://multiproxy.org/txt_all/proxy.txt",
            "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
            "https://raw.githubusercontent.com/UserR3X/proxy-list/main/online/http.txt",
            "https://raw.githubusercontent.com/UserR3X/proxy-list/main/online/https.txt"]
        for url in urls:
            r = WebRequest().get(url, timeout=50)
            proxies = re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{2,5})', r.text)
            for proxy in proxies:
                yield ':'.join(proxy)

    @staticmethod
    def freeProxy20():
        urls = [
            'https://raw.githubusercontent.com/UptimerBot/proxy-list/main/proxies/http.txt',
            'https://openproxy.space/list/http',
            'https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt',
            'https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt',
            'https://raw.githubusercontent.com/hendrikbgr/Free-Proxy-Repo/master/proxy_list.txt',
            'https://raw.githubusercontent.com/almroot/proxylist/master/list.txt',
            'https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt',
            'https://raw.githubusercontent.com/aslisk/proxyhttps/main/https.txt',
            'https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/http.txt',
            'https://raw.githubusercontent.com/saisuiu/uiu/main/free.txt',
            'https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt',
            'https://proxylist.live/nodes/free_1.php?page=1&showall=1',
            'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http',
            'https://openproxy.space/list/http',
            'https://openproxylist.xyz/http.txt',
            'https://proxylist.live/nodes/free_1.php?page=1&showall=1',
            'https://proxysearcher.sourceforge.net/Proxy%20List.php?type=http']
        for url in urls:
            r = WebRequest().get(url, timeout=50)
            proxies = re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{2,5})', r.text)
            for proxy in proxies:
                yield ':'.join(proxy)


    @staticmethod
    def freeProxy21():
        urls = [
            'https://proxyspace.pro/http.txt',
            'https://proxyspace.pro/https.txt',
            'https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/http.txt',
            'https://raw.githubusercontent.com/andigwandi/free-proxy/main/proxy_list.txt',
            'https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/http.txt',
            'https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/https.txt',
            'https://raw.githubusercontent.com/aslisk/proxyhttps/main/https.txt',
            'https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/HTTP.txt',
            'https://raw.githubusercontent.com/caliphdev/Proxy-List/master/http.txt',
            'https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt',
            'https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/http.txt',
            'https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/https.txt',
            'https://raw.githubusercontent.com/hanwayTech/free-proxy-list/main/http.txt',
            'https://raw.githubusercontent.com/hanwayTech/free-proxy-list/main/https.txt',
            'https://raw.githubusercontent.com/hendrikbgr/Free-Proxy-Repo/master/proxy_list.txt'
        ]
        for url in urls:
            r = WebRequest().get(url, timeout=50)
            proxies = re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{2,5})', r.text)
            for proxy in proxies:
                yield ':'.join(proxy)
    # @staticmethod
    # def wallProxy01():
    #     """
    #     PzzQz https://pzzqz.com/
    #     """
    #     from requests import Session
    #     from lxml import etree
    #     session = Session()
    #     try:
    #         index_resp = session.get("https://pzzqz.com/", timeout=20, verify=False).text
    #         x_csrf_token = re.findall('X-CSRFToken": "(.*?)"', index_resp)
    #         if x_csrf_token:
    #             data = {"http": "on", "ping": "3000", "country": "cn", "ports": ""}
    #             proxy_resp = session.post("https://pzzqz.com/", verify=False,
    #                                       headers={"X-CSRFToken": x_csrf_token[0]}, json=data).json()
    #             tree = etree.HTML(proxy_resp["proxy_html"])
    #             for tr in tree.xpath("//tr"):
    #                 ip = "".join(tr.xpath("./td[1]/text()"))
    #                 port = "".join(tr.xpath("./td[2]/text()"))
    #                 yield "%s:%s" % (ip, port)
    #     except Exception as e:
    #         print(e)

    # @staticmethod
    # def freeProxy10():
    #     """
    #     墙外网站 cn-proxy
    #     :return:
    #     """
    #     urls = ['http://cn-proxy.com/', 'http://cn-proxy.com/archives/218']
    #     request = WebRequest()
    #     for url in urls:
    #         r = request.get(url, timeout=10)
    #         proxies = re.findall(r'<td>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})</td>[\w\W]<td>(\d+)</td>', r.text)
    #         for proxy in proxies:
    #             yield ':'.join(proxy)

    # @staticmethod
    # def freeProxy11():
    #     """
    #     https://proxy-list.org/english/index.php
    #     :return:
    #     """
    #     urls = ['https://proxy-list.org/english/index.php?p=%s' % n for n in range(1, 10)]
    #     request = WebRequest()
    #     import base64
    #     for url in urls:
    #         r = request.get(url, timeout=10)
    #         proxies = re.findall(r"Proxy\('(.*?)'\)", r.text)
    #         for proxy in proxies:
    #             yield base64.b64decode(proxy).decode()

    # @staticmethod
    # def freeProxy12():
    #     urls = ['https://list.proxylistplus.com/Fresh-HTTP-Proxy-List-1']
    #     request = WebRequest()
    #     for url in urls:
    #         r = request.get(url, timeout=10)
    #         proxies = re.findall(r'<td>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})</td>[\s\S]*?<td>(\d+)</td>', r.text)
    #         for proxy in proxies:
    #             yield ':'.join(proxy)


if __name__ == '__main__':
    p = ProxyFetcher()
    for _ in p.freeProxy17():
        print(_)

# http://nntime.com/proxy-list-01.htm


# freeProxy04
# freeProxy07
# freeProxy08
