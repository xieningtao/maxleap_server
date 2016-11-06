#coding:utf-8

import ML
import function.ninja
import hook.hooks
import job
import json
from nose.tools import with_setup
from ML import Server

def setup_func():
    ML.init(
        "55924bc260b2a70e2a54ae2f",
        master_key="NE85TkVObThsWmk2OW5hcHpKcG5ldw",
        )

@with_setup(setup_func)
def test_helloNinja():
    print "test"
    response = Server.callFunction('helloNinja', data=json.dumps({'name':"test"}))
    print "response: "+response.data
    assert response.data == 'test_new'
    assert response.status_code == 200

