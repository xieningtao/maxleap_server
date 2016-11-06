import ML
import function.sayhello
import json
from nose.tools import with_setup
from ML import Server

def setup_func():
    ML.init(
        "57f9edc887d4a7e337b8c231",
        master_key="elhmazJfd29ZTFBhR0M3SmJ0R2N6UQ",
        )

@with_setup(setup_func)
def test_sayhello():
    print "test"
    response = Server.callFunction('sayHello', data=json.dumps({'name': "test"}))
    print "response: " + response.data
    assert response.data != 'test'
    assert response.status_code == 200