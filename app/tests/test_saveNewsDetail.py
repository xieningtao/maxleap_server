import ML
import function.saveNewsDetail
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
    fileName = "/Users/mac/Downloads/newsDetail.json"
    fileObject = open(fileName)
    try:
        newsDetail = fileObject.read()
    except:
        newsDetail = ""
    response = Server.callFunction('saveNewsDetail', data=json.dumps({"content":newsDetail}))
    print "response: "+response.data