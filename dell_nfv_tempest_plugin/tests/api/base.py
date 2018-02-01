from oslo_log import log as logging
from tempest import config
from tempest import test
import tempest.lib.cli.base as cli
import random
import os

CONF = config.CONF
LOG = logging.getLogger(__name__)


class BaseDellNFVTempestTestCase(test.BaseTestCase):

    @classmethod
    def resource_setup(self):
        super(BaseDellNFVTempestTestCase, self).resource_setup()
        self.os_user_name = os.environ['OS_USERNAME']
        self.os_password = os.environ['OS_PASSWORD']
        self.os_auth_url = os.environ['OS_AUTH_URL']
        self.os_tenant_name = os.environ['OS_USERNAME']
        self.cli_dir = '/bin'
        self.cliclient = cli.CLIClient(username=self.os_user_name, password=self.os_password, tenant_name=self.os_tenant_name,
                                       uri=self.os_auth_url, cli_dir='/bin/')


    def get_random_integer(self, lower=10, upper=5000):
        """ Returns a random integer between upper and lower bounds
        """
        return random.randint(lower, upper)
