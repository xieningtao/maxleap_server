#coding:utf-8
from ML import Object
from ML import Server
from ML import Log
from ML import Query
from ML import Response

@Server.Job
def test_job(request):
    return Response('test')