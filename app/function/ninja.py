#coding:utf-8
from ML import Object
from ML import Server
from ML import Log
from ML import Query
from ML import Response


Ninja = Object.extend('Ninja')

@Server.Function
def helloNinja(request):
    #获取param:name
    name = request.json.get('name')

    #产生本体
    ninja = Ninja()
    ninja.set('name',name)
    ninja.save()
    Log.info(u"生成本体，ID为:{}".format(ninja.id))

    #产生50个分身
    clone_ninja_ids = []
    for idx in range(50):
        clone_ninja = Ninja()
        clone_ninja.set('name',u'{0}_{1}'.format(name,idx))
        clone_ninja.save()
        clone_ninja_ids.append(clone_ninja.id)
        Log.info(u"多重影分身:{}".format(clone_ninja.id))

    #找出第50个分身
    query = Query(Ninja)
    query.equal_to('name',u'{}_49'.format(name))
    ninja_50 = query.first()
    clone_ninja_ids.remove(ninja_50.id)
    Log.info(u"找到第50个分身:{}".format(ninja_50.dump()))

    #击杀其余49个分身
    query = Query(Ninja)
    query.contained_in('objectId',clone_ninja_ids)
    count = query.count()
    for item in query.find():
        item.destroy()
    Log.info(u"完成分身击杀数目:{}".format(count))

    #击杀本体
    ninja.destroy()
    Log.info(u"完成本体击杀")

    #让第50分身成为新的本体
    ninja_50.set('name',u'{}_new'.format(name))
    ninja_50.save()
    Log.info(u"第50个分身在{}成为新的本体".format(ninja_50.updated_at));

    #返回新的本体名称
    return Response(ninja_50.get('name'))


#hack
import ML
ML.client.BASE_URL = "http://apiuat.leap.as/2.0"
# ML.client.BASE_URL = "http://10.10.10.193:8080"
