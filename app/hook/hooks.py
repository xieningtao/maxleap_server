#coding:utf-8
from ML import Object
from ML import Server
from ML import Log
from ML import Query
from ML import Response

@Server.before_save('Ninja')
def test1(obj):
    Log.info("before_save:{}".format(obj.dump()))

@Server.after_save('Ninja')
def test2(obj):
    Log.info("after_save:{}".format(obj.dump()))

@Server.after_update('Ninja')
def test3(obj):
    Log.info("after_update:{}".format(obj.dump()))

@Server.before_delete('Ninja')
def test4(obj):
    Log.info("before_delete:{}".format(obj.dump()))

@Server.after_delete('Ninja')
def test5(obj):
    Log.info("after_delete:{}".format(obj.dump()))
