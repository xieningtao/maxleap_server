import ML
import function.saveNewsList
import hook.hooks
import job
import json
from nose.tools import with_setup
from ML import Server


def setup_func():
    ML.init(
        "57f9edc887d4a7e337b8c231",
        master_key="elhmazJfd29ZTFBhR0M3SmJ0R2N6UQ",
        )

@with_setup(setup_func)
def test_saveNewsDetail():
    fileName = "/Users/mac/Downloads/newslist.json"
    fileObject = open(fileName)
    try:
        news = fileObject.read()
    except:
        news = ""
    response = Server.callFunction('saveNewsList', data=json.dumps({"content":news}))
    print "response: "+response.data