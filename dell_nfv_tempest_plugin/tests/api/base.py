from tempest import test
import tempest.lib.cli.base as cli
import os
import random
from oslo_log import log as logging

LOG = logging.getLogger(__name__, "dell-nfv-tempest-plugin")


class BaseDellNFVTempestTestCase(test.BaseTestCase):

    @classmethod
    def resource_setup(self):
        super(BaseDellNFVTempestTestCase, self).resource_setup()
	self.os_user_name = os.environ['OS_USERNAME']
        self.os_password = os.environ['OS_PASSWORD']
        self.os_auth_url = os.environ['OS_AUTH_URL']
        self.os_tenant_name = os.environ['OS_USERNAME']
        self.cli_dir = '/bin'
        self.cliclient = cli.CLIClient(username=self.os_user_name,
                                       password=self.os_password,
                                       tenant_name=self.os_tenant_name,
                                       uri=self.os_auth_url,
                                       cli_dir='/bin/')



    @classmethod
    def resource_cleanup(self):
	super(BaseDellNFVTempestTestCase, self).resource_cleanup()
	self.cliclient = None


    def get_random_integer(self, lower=10, upper=5000):
	return random.randint(lower, upper)    
