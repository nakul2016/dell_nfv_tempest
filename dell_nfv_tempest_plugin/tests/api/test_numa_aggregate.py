from dell_nfv_tempest_plugin.tests.api import base
from tempest import test
import tempest.lib.cli.output_parser as output_parser
import os
from oslo_log import log as logging

LOG = logging.getLogger(__name__, "dell-nfv-tempest-plugin")


class TestNumaAggregate(base.BaseDellNFVTempestTestCase):

    @classmethod
    def resource_setup(self):
	super(TestNumaAggregate, self).resource_setup()
	self.aggr_name = None


    @test.attr(type='dell_nfv')
    def test_numa_aggregate(self):
	LOG.info("BEGIN: verify_numa_aggregate")
	raw_output = self.cliclient.openstack(action='aggregate list')
	all_aggr = output_parser.listing(raw_output)
	aggr_names = [x['Name'] for x in all_aggr]
	LOG.info("Aggregtes present in OverCloud -", ', '.join(aggr_names)) 
	for self.aggr_name in aggr_names:
	    hosts, metadata_tag = self.get_hosts_and_metadata_in_aggregate()
	LOG.info("END: verify_numa_aggregate")

   
    def get_hosts_and_metadata_in_aggregate(self):
	raw_output = self.cliclient.openstack(action='aggregate show', params=self.aggr_name)
	aggr_details = output_parser.listing(raw_output)
	hosts = [x['Value'] for x in aggr_details if str(x['Field']).lower() == 'hosts'][0].strip("[]").replace("u'", "").replace("'","")
	LOG.info("Hosts present in host aggregate - " + self.aggr_name + " are " + hosts)
	metadata_tag = [x['Value'] for x in aggr_details if str(x['Field']).lower() == 'properties'][0]
	LOG.info("Metadata tag present in host aggregate - " + self.aggr_name + " are " + metadata_tag)
	return hosts, metadata_tag


    @classmethod
    def resource_cleanup(cls):
        super(TestNumaAggregate, cls).resource_cleanup()
