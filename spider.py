#!/usr/bin/env python
# coding=utf-8
# /home/nightwish/spider.py
# @nightwish

import urllib 
from BeautifulSoup import BeautifulSoup

url      = 'http://www.baozhao.me/p/3_'
pic_save = '/home/nightwish/photo/'
num      = 0

def spider():
  global num
  for i in range(1,16):
    page    = urllib.urlopen(url+str(i))
    content = page.read()
    soup    = BeautifulSoup(content,fromEncoding='utf-8')
    pic_list= soup.findAll('img')
    for i in pic_list[1::]:
      pic_url=i['src'][:-6]+'.jpg'
      urllib.urlretrieve(pic_url,pic_save + str(num) + '.jpg')
      print num,
      num+=1

if '__name__' == '__main__':
  spider()

