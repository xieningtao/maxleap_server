#coding:utf-8
from ML import Object
from ML import Server
from ML import Response
from ML import Log
import json
import sys

NYNewsDetail = Object.extend('NYNewsDetail')
@Server.Function
def saveNewsDetail(request):
    reload(sys)
    sys.setdefaultencoding("utf-8")
    result = request.json
    print "result: "+str(result)
    detailConent=result.get("content")

    detailConentJson=json.loads(detailConent)
    finalDetailContent=json.dumps(detailConentJson["results"][0]["detailConent"],ensure_ascii=False)
    newsId=detailConentJson["results"][0]["newsId"]
    print "------->results detail: "+finalDetailContent+" newsId: "+newsId
    newsDeatail=NYNewsDetail()

    newsDeatail.set("detailContent",finalDetailContent)
    newsDeatail.set("newsId",newsId)
    newsDeatail.save()
    Log.info(u"id为:{}".format(newsDeatail.id))


    return Response("thanks")
