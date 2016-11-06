from ML import Server
from ML import Response

@Server.Function
def sayHello(request):
    return Response("hello! my name is xie ning tao ")
