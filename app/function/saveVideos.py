#coding:utf-8
from ML import Object
from ML import Server
from ML import Response
from ML import Log
import json

NYVideo=Object.extend("NYVideo")
@Server.Function
def saveVideos(request):
    result = request.json
    # print "result: " + str(result)
    detailConent = result.get("content")
    # print detailConent
    video=NYVideo()
    video.set("videoContent",detailConent)
    video.save()
    return Response("save video successful")