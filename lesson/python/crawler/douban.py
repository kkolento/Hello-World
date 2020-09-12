# -*- coding: utf-8 -*-
"""
Spyder Editor @ Python 3.7.3

Create on Sun Aug 16 19:45:07 2020

@Author : YangXu
"""

import sys
import urllib#输入网址，获取网页数据
from bs4 import BeautifulSoup #网页解析，获取数据
import re #正则表达式，进行文字匹配
import xlwt#进行excel操作
import sqlite3#进行数据库操作


def askurl(url):#单页网页数据读取
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"
        }#用户代理，模拟浏览器头部信息
    req=urllib.request.Request(url,headers=headers)
    try:
        response=urllib.request.urlopen(req)
        html=response.read().decode('utf-8')
    except urllib.error.URLError as e:#没有得到正常响应时的处理
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html

        
def getData(baseurl):#爬取网页
    datalist=[]
    for i in range(0,10):
        url=baseurl+str(i*25)+str("&filter=")#调整读取所有页面
        html=askurl(url)#保存数据
        soup=BeautifulSoup(html,"html.parser")#html解析
        for item in soup.find_all("div",class_="item"):#找到所有div,且其中class属性值为item的
            data=[]#保存一部电影的所有信息
            item=str(item)
            #接下来检索各要保存的数据
            title=re.findall(find_Title,item)[0]
            data.append(title)
            othertitle1=re.findall(find_Othertitle1,item)
            if len(othertitle1)!=0:
                othertitle1=othertitle1[0]
                data.append(othertitle1.strip())
            else:
                data.append(" ")
            category=re.findall(find_Category,item)[0]
            category=category.replace("\n","")
            data.append(category.strip())
            rating=re.findall(find_Rating,item)[0]
            data.append(rating)
            judge=re.findall(find_Judge,item)[0]
            data.append(judge)
            link=re.findall(find_Link,item)[0]
            data.append(link)
            director=re.findall(find_Director,item)[0]
            data.append(director.strip())#去掉空格
            actor=re.findall(find_Actor,item)
            if len(actor)!=0:
                actor=actor[0]
                data.append(actor.strip())
            else:
                data.append(" ")
            inq=re.findall(find_Inq,item)
            if len(inq)!=0:
                inq=inq[0]
                data.append(inq)
            else:
                data.append(" ")
            image=re.findall(find_Image,item)[0]
            data.append(image)
            datalist.append(data)#保存至整个数据表
    return datalist
    

def saveData(datalist,savepath):
    book=xlwt.Workbook(encoding='utf-8')
    sheet=book.add_sheet("豆瓣电影TOP250",cell_overwrite_ok=True)
    col=("影片中文名","影片别名","影片类型","影片评分","评价人数","电影链接","导演","主演","概述","图片链接")
    for i in range(0,10):
        sheet.write(0,i,col[i])
    for i in range(0,250):
        data=datalist[i]
        for j in range(0,10):
            sheet.write(i+1,j,data[j])
    book.save(savepath)
      

def init_sql(sqlpath):
    sql1=sqlite3.connect(sqlpath)
    c=sql1.cursor()
    sqlexe='''
        create table douban250
        (
            id integer primary key autoincrement,
            title text,
            other_title text,
            category text,
            rating real,
            comments integer,
            link text,
            director text,
            actor text,
            inq text,
            image text          
            )
    '''
    c.execute(sqlexe)
    sql1.commit()
    sql1.close()
    

def saveSQL(datalist,sqlpath):
    init_sql(sqlpath)
    sql1=sqlite3.connect(sqlpath)
    c=sql1.cursor()
    for data in datalist:
        for index in range(len(data)):
            data[index]='"'+data[index]+'"'
        sqlexe='''
                insert into douban250(title,other_title,category,rating,comments,link,director,actor,inq,image)
                values(%s)'''%",".join(data)
        c.execute(sqlexe)
        sql1.commit()
    c.close()
    sql1.close()
    
    
if __name__=="__main__":#控制程序运行流程
    baseurl='https://movie.douban.com/top250?start='
    savepath='./douban_movies_top250.xls'
    sqlpath='./web crawler/douban250.db'    
    find_Link=re.compile(r'<a href="(.*?)">')#截取链接
    find_Image=re.compile(r'<img.*src="(.*?)"',re.S)#截取图片链接，忽略换行
    find_Title=re.compile(r'<span class="title">(.*?)</span>')#截取标题
    find_Rating=re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
    find_Judge=re.compile(r'<span>(\d*)人评价</span>')#评价人数
    find_Inq=re.compile(r'<span class="inq">(.*?)</span>')#概况
    find_Category=re.compile(r'<p class="">.*\xa0(.*?)</p>',re.S)#影片类型
    find_Director=re.compile(r'<p class="">(.*?)\xa0.*</p>',re.S)#导演
    find_Actor=re.compile(r'主演:(.*?)<br/>',re.S)
    find_Othertitle1=re.compile(r'<span class="other">.*\xa0(.*?)/')#其他名称
    
    datalist=getData(baseurl)
    #saveData(datalist,savepath)
    saveSQL(datalist,sqlpath)
    