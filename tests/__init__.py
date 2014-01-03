from unittest import TestCase
from os import path as op, environ
from sys import version_info


class DealerTest(TestCase):

    def test_git(self):

        from dealer.git import git, Backend

        self.assertTrue(git.repo)
        self.assertTrue(git.revision)
        self.assertTrue(git.tag)

        git.path = 'invalid/path/to/git'
        self.assertFalse(git._repo)  # noqa

        try:
            assert git.repo
            raise AssertionError('test.failed')
        except TypeError:
            pass

        git.path = op.abspath(op.dirname(op.dirname(__file__)))
        self.assertTrue(git.repo)

        git = Backend('.')
        self.assertTrue(git.repo)

    if version_info < (3, 0):
        def test_hg(self):
            from dealer.mercurial import hg, Backend

            path = op.join(op.dirname(__file__), 'hg')
            hg.path = path
            self.assertTrue(hg.repo)
            self.assertTrue(hg.revision)
            self.assertTrue(hg.tag)

            hg.path = 'invalid/path/to/hg'
            self.assertFalse(hg._repo)  # noqa

            hg = Backend(path)
            self.assertTrue(hg.repo)

    def test_simple(self):
        from dealer.simple import simple, Backend

        path = op.join(op.dirname(__file__), 'simple')
        simple.path = path
        self.assertTrue(simple.repo)
        self.assertEqual(simple.revision, 'default')
        self.assertEqual(simple.tag, 'default')

        simple.path = 'invalid/path/to/hg'
        self.assertFalse(simple._repo)  # noqa

        try:
            assert simple.repo
            raise AssertionError('test.failed')
        except TypeError:
            pass

        simple = Backend(op.join(path, 'revision'))
        self.assertEqual(simple.revision, 'test_revision')

        simple = Backend(path, filename='revision2')
        self.assertEqual(simple.revision, 'cap1254')

    def test_env(self):
        from dealer.env import env, Backend
    
        self.assertFalse(env._repo)
    
        environ['DEALER_REVISION'] = '3ffb6b6'
        environ['DEALER_TAG'] = 'v1.0'
    
        self.assertTrue(env.repo)
        self.assertEqual(env.revision, '3ffb6b6')
        self.assertEqual(env.tag, 'v1.0')

        environ['MY_REVISION'] = '3ffb6b7'
        environ['MY_TAG'] = 'v1.1'

        options = dict(revision_env_keyname = 'MY_REVISION', tag_env_keyname = 'MY_TAG')
        env = Backend(**options)
        self.assertEqual(env.revision, '3ffb6b7')
        self.assertEqual(env.tag, 'v1.1')

    def test_auto(self):
        from dealer.auto import auto
        from dealer.git import git

        path = op.join(op.dirname(__file__), 'hg')
        auto.path = path
        self.assertTrue(auto.repo)
        self.assertTrue(auto.revision)

        auto.path = git.path
        self.assertTrue(auto.repo)
        self.assertEqual(auto.revision, git.revision)

    def test_common(self):
        from dealer import get_backend

        git = get_backend('git')
        self.assertTrue(git.repo)

    def test_backends(self):
        from dealer import get_backend

        path = op.dirname(__file__)
        auto = get_backend('auto', path=path, backends=('simple', 'git'))
        self.assertTrue(auto.repo)

    def test_null(self):
        from dealer.null import null

        self.assertTrue(null.repo)

    def test_flask(self):
        from flask import Flask, g
        from dealer.contrib.flask import Dealer

        app = Flask('test')
        Dealer(app)
        self.assertTrue(app.revision)
        app.route('/')(lambda: "%s - %s" % (g.revision, g.tag))
        with app.test_request_context():
            client = app.test_client()
            response = client.get('/')
            self.assertTrue(app.revision in response.data)
            self.assertTrue(app.tag in response.data)

    def test_django(self):
        from django.conf import settings

        settings.configure(
            ROOT_URLCONF='tests.django_app.urls',
            TEMPLATE_CONTEXT_PROCESSORS = ('dealer.contrib.django.staff.context_processor',), # noqa
            MIDDLEWARE_CLASSES = ('dealer.contrib.django.staff.Middleware',),

        )
        from django.test import Client

        client = Client()
        revision = client.get('/revision/')
        self.assertEqual(revision.status_code, 200)
        self.assertTrue(revision.content)

        tag = client.get('/tag/')
        self.assertEqual(tag.status_code, 200)
        self.assertTrue(tag.content)
