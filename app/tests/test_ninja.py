#coding:utf-8

import ML
import function.ninja
import hook.hooks
import job.job
import json
from nose.tools import with_setup
from ML import Server

def setup_func():
    ML.init(
        "",
        master_key="",
        )

@with_setup(setup_func)
def test_helloNinja():
    response = Server.callFunction('helloNinja', data=json.dumps({'name':"test"}))
    assert response.data == 'test_new'
    assert response.status_code == 200
