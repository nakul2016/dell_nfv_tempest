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


    @classmethod
    def resource_cleanup(self):
	super(BaseDellNFVTempestTestCase, self).resource_cleanup()


    def get_random_integer(self, lower=10, upper=5000):
	return random.randint(lower, upper)    
