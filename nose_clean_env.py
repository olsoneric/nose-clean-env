
"""The nose_clean_env plugin resets the contents of os.environ after running
each test.  Use it by setting ``--with-cleanenv`` or the NOSE_WITH_CLEANENV
environment variable.

The effects are similar to wrapping the following functions around the
import and execution of each test module::

    def setup(module):
        module._orig_environ = dict(os.environ)

    def teardown(module):
        os.environ = module._orig_environ

"""

import os
import logging

from nose.plugins import Plugin


log = logging.getLogger('nose.plugins.nose_env')


class NoseCleanEnv(Plugin):
    """
    Activate the Clean Env plugin to backup and restore os.environ
    between each test.
    """
    score = 10  # I want to be last
    name = 'cleanenv'

    def configure(self, options, conf):
        """Configure plugin."""
        Plugin.configure(self, options, conf)

    def beforeTest(self, test):
        """Make a copy of os.environ."""
        self._orig_environ = dict(os.environ)

    def afterTest(self, test):
        """Restore os.environ from the one we saved."""
        os.environ = self._orig_environ