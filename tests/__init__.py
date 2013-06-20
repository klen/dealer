from unittest import TestCase
from os import path as op


class DealerTest(TestCase):

    def test_git(self):

        from dealer.git import git, Backend

        self.assertTrue(git.repo)
        self.assertTrue(git.revision)

        git.path = 'invalid/path/to/git'
        self.assertFalse(git._repo) # nolint

        try:
            assert git.repo
            raise AssertionError('test.failed')
        except TypeError:
            pass

        git.path = op.abspath(op.dirname(op.dirname(__file__)))
        self.assertTrue(git.repo)

        git = Backend('.')
        self.assertTrue(git.repo)

    def test_hg(self):
        try:
            from dealer.mercurial import hg, Backend

            path = op.join(op.dirname(__file__), 'hg')
            hg.path = path
            self.assertTrue(hg.repo)
            self.assertTrue(hg.revision)

            hg.path = 'invalid/path/to/hg'
            self.assertFalse(hg._repo) # nolint

            hg = Backend(path)
            self.assertTrue(hg.repo)

        except TypeError:
            assert True

    def test_simple(self):
        from dealer.simple import simple, Backend

        path = op.join(op.dirname(__file__), 'simple')
        simple.path = path
        self.assertTrue(simple.repo)
        self.assertEqual(simple.revision, 'default')

        simple.path = 'invalid/path/to/hg'
        self.assertFalse(simple._repo) # nolint

        try:
            assert simple.repo
            raise AssertionError('test.failed')
        except TypeError:
            pass

        simple = Backend(op.join(path, 'revision'))
        self.assertEqual(simple.revision, 'test_revision')

        simple = Backend(path, filename='revision2')
        self.assertEqual(simple.revision, 'cap1254')

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
        from flask import Flask, g # nolint
        from dealer.contrib.flask import Dealer

        app = Flask('test')
        Dealer(app)
        self.assertTrue(app.revision)
        app.route('/')(lambda: g.revision)
        with app.test_request_context():
            client = app.test_client()
            response = client.get('/')
            self.assertTrue(app.revision in response.data)

# lint_ignore=C0110
