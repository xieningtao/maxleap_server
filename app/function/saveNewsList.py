#coding:utf-8
from ML import Object
from ML import Server
from ML import Response
from ML import Log
import json
import sys

NYNews = Object.extend('NYNews')
@Server.Function
def saveNewsList(request):
    reload(sys)
    sys.setdefaultencoding("utf-8")
    result = request.json
    detailConent=result.get("content")

    detailConentJson=json.loads(detailConent)
    results=detailConentJson["results"]
    for i in range(0,len(results)):
        news=results[i];
        newsStr=json.dumps(news,ensure_ascii=False)
        print "new: "+str(i)+"--->"+newsStr
        news=NYNews()

        news.set("content",newsStr)
        news.save()
        Log.info(u"id为:{}".format(news.id))


    return Response("thanks")
