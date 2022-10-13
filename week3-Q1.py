import urllib.request as request
import json

src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
    # data=response.read().decode("utf-8")
    data=json.load(response)
# print(data)
firstViewPoint = data["result"]["results"][0]["stitle"]

allViewPointData=data["result"]["results"]
allNeedData=""


for i in range(0,len(allViewPointData)):
    xpostDate=data["result"]["results"][i]["xpostDate"].split("/")[0]
    firstViewPoint = data["result"]["results"][i]["stitle"]
    firsrViewPointArea=data["result"]["results"][i]["address"][5:8]
    firstViewPointLongitude=data["result"]["results"][i]["longitude"]
    firstViewPointLatitude=data["result"]["results"][i]["latitude"]
    firstViewPointFirstPictureUrl=data["result"]["results"][i]["file"]
    firstUrl=firstViewPointFirstPictureUrl.split("https")
    if(int(xpostDate)>=2015):
            needData=firstViewPoint+","+firsrViewPointArea+","+firstViewPointLongitude+","+firstViewPointLatitude+","+"https"+firstUrl[1]
            allNeedData=allNeedData+needData+"\n"
    

    # print(needData)
print(allNeedData)
file = open("data.csv",mode="w")
file.write(allNeedData)
file.close()