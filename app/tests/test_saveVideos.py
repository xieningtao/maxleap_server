import ML
import function.saveVideos
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
def test_saveVideos():
    fileName = "/Users/mac/Downloads/nyvideos.json"
    fileObject = open(fileName)
    try:
        videos = fileObject.read()
    except:
        videos = ""
    response = Server.callFunction('saveVideos', data=json.dumps({"content":videos}))
    print "response: "+response.data