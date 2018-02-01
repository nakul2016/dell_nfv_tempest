from oslo_log import log as logging
from tempest import config
from tempest import test
import random


CONF = config.CONF
LOG = logging.getLogger(__name__)


class BaseDellNFVTempestTestCase(test.BaseTestCase):

    @classmethod
    def skip_checks(cls):
	pass

    def get_random_integer(self, lower=10, upper=5000):
        """ Returns a random integer between upper and lower bounds
        """
        return random.randint(lower, upper)
