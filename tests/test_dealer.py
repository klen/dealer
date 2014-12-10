from os import path as op, environ
import pytest
from sys import version_info


def test_git():

    from dealer.git import git, Backend

    assert git.repo
    assert git.revision
    assert git.tag

    git.path = 'invalid/path/to/git'
    assert not git._repo

    with pytest.raises(TypeError):
        assert git.repo

    git.path = op.abspath(op.dirname(op.dirname(__file__)))
    assert git.repo

    git = Backend('.')
    assert git.repo


@pytest.mark.skipif(version_info < (3, 0), reason='requires python3')
def test_hg():
    from dealer.mercurial import hg, Backend

    path = op.join(op.dirname(__file__), 'hg')
    hg.path = path
    assert hg.repo
    assert hg.revision
    assert hg.tag

    hg.path = 'invalid/path/to/hg'
    assert not hg._repo

    hg = Backend(path)
    assert hg.repo


def test_simple():
    from dealer.simple import simple, Backend

    path = op.join(op.dirname(__file__), 'simple')
    simple.path = path
    assert simple.repo
    assert simple.revision == 'default'
    assert simple.tag == 'default'

    simple.path = 'invalid/path/to/hg'
    assert not simple._repo

    with pytest.raises(TypeError):
        assert simple.repo

    simple = Backend(op.join(path, 'revision'))
    assert simple.revision == 'test_revision'

    simple = Backend(path, filename='revision2')
    assert simple.revision == 'cap1254'


def test_env():
    from dealer.env import env, Backend

    environ['DEALER_REVISION'] = '3ffb6b6'
    environ['DEALER_TAG'] = 'v1.0'

    assert env.revision == '3ffb6b6'
    assert env.tag == 'v1.0'

    environ['MY_REVISION'] = '3ffb6b7'
    environ['MY_TAG'] = 'v1.1'

    options = dict(revision_env_keyname='MY_REVISION', tag_env_keyname='MY_TAG')
    env = Backend(**options)
    assert env.revision == '3ffb6b7'
    assert env.tag == 'v1.1'


def test_auto():
    from dealer.auto import auto
    from dealer.git import git

    path = op.join(op.dirname(__file__), 'hg')
    auto.path = path
    assert auto.repo
    assert auto.revision

    auto.path = git.path
    assert auto.repo
    assert auto.revision == git.revision


def test_common():
    from dealer import get_backend

    git = get_backend('git')
    assert git.repo


def test_backends():
    from dealer import get_backend

    path = op.dirname(__file__)
    auto = get_backend('auto', path=path, backends=('simple', 'git'))
    assert auto.repo


def test_null():
    from dealer.null import null

    assert null.repo


def test_flask():
    from flask import Flask, g
    from dealer.contrib.flask import Dealer

    app = Flask('test')
    Dealer(app)
    assert app.revision

    app.route('/')(lambda: "%s - %s" % (g.revision, g.tag))
    with app.test_request_context():
        client = app.test_client()
        response = client.get('/')
        assert app.revision in response.data
        assert app.tag in response.data


def test_django():
    import os
    os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.django_app.settings'

    from django.test import Client

    client = Client()
    revision = client.get('/revision/')
    assert revision.status_code == 200
    assert revision.content

    tag = client.get('/tag/')
    assert tag.status_code == 200
    assert tag.content


def test_pyramid():
    from tests.pyramid_app import revision, config
    from pyramid import testing
    testing.setUp(config.registry)
    r = testing.DummyRequest()
    result = revision(r)
    assert result.status_code == 200
    testing.tearDown()
