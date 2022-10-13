from math import e
import urllib.request as req
def getData(url,listFirst,listSecond,listThird):
        # url="https://www.ptt.cc/bbs/movie/index.html"
        request=req.Request(url,headers={
                "user-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36"
        })
        with req.urlopen(request) as response:
                data=response.read().decode("utf-8")
        import bs4
        root=bs4.BeautifulSoup(data,"html.parser")
        titles=root.find_all("div",class_="title")
        for title in titles:
                if(title.a!=None):
                        if(title.a.string[0:4]=="[好雷]"):
                                listFirst.append(title.a.string)
                                pass
                        if(title.a.string[0:4]=="[普雷]"):
                                listSecond.append(title.a.string)
                        if(title.a.string[0:4]=="[負雷]"):
                                listThird.append(title.a.string)
        nextLink=root.find("a",string="‹ 上頁")
        return nextLink["href"]
url="https://www.ptt.cc/bbs/movie/index.html"
# 清單分別存好雷1、普雷2、負雷3
# 輸出的形式需要式字串，存入outputData
listFirst=[]
listSecond=[]
listThird=[]
outputData=""
for i in range(10):
        url="https://www.ptt.cc"+getData(url,listFirst,listSecond,listThird)
for i in range(len(listFirst)):
        outputData=outputData+listFirst[i]+"\n"
for i in range(len(listSecond)):
        outputData=outputData+listSecond[i]+"\n"
for i in range(len(listThird)):
        outputData=outputData+listThird[i]+"\n"
print(outputData)
file = open("movie.txt",mode="w",encoding="utf-8")
file.write(outputData)
file.close()