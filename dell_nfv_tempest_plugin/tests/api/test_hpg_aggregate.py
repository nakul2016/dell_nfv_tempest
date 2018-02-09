from dell_nfv_tempest_plugin.tests.api import base
from dell_nfv_tempest_plugin.tests.api import api_helper as api
from tempest import config
from tempest import test
import tempest.lib.cli.output_parser as output_parser
import re
from oslo_log import log as logging

CONF = config.CONF
LOG = logging.getLogger(__name__, "dell-nfv-tempest-plugin")


class TestHpgAggregate(base.BaseDellNFVTempestTestCase):

    @classmethod
    def resource_setup(self):
	super(TestHpgAggregate, self).resource_setup()
	self.api_helper = api.APIHelper()
	self.aggr_name = None
	self.hosts = None
	self.metadata = None
	self.aggr_metadata = CONF.hugepage.aggregate_metadata


    @test.attr(type='dell_nfv')
    def test_hpg_aggregate(self):
	LOG.info("BEGIN: test_verify_hugepage_aggregate")
	aggr_list = self.api_helper.get_aggregate_list()
	self.assertNotEmpty(aggr_list)

	for self.aggr_name in aggr_list:
	    self.metadata = self.api_helper.get_metadata_in_aggregate(self.aggr_name)
	    if str(self.metadata).lower() == str(self.aggr_metadata).lower():
		self.hosts = self.api_helper.get_hosts_in_aggregate(self.aggr_name)
		break

	self.assertNotEmpty(self.hosts)
	self.assertNotEmpty(self.metadata)

	LOG.info("Hugepage Aggregate Found - '%s'", self.aggr_name) 
	LOG.info("Hosts present in Hugepage aggregate - '%s' are %s", self.aggr_name, self.hosts)
	LOG.info("Metadata present in Hugepage aggregate - '%s' are %s", self.aggr_name, self.metadata)
	LOG.info("END: test_verify_hugepage_aggregate")

 
    @classmethod
    def resource_cleanup(self):
        super(TestHpgAggregate, self).resource_cleanup()
	self.api_helper = None
