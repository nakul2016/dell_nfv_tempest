from dell_nfv_tempest_plugin.tests.api import base, api
from tempest import test
import tempest.lib.cli.output_parser as output_parser
import re
from oslo_log import log as logging

LOG = logging.getLogger(__name__, "dell-nfv-tempest-plugin")

aggr_metadata = "pinned='true'"

class TestNumaAggregate(base.BaseDellNFVTempestTestCase):

    @classmethod
    def resource_setup(self):
	super(TestNumaAggregate, self).resource_setup()
	self.openstack = api.OpenStackAPI()
	self.openstack.resource_setup()
	self.aggr_name = None


    @test.attr(type='dell_nfv')
    def test_numa_aggregate(self):
	LOG.info("BEGIN: test_verify_numa_aggregate")
	raw_output = self.openstack.aggregate_list()
	regex = r'[|].*\S.*[|](.*)[|].*\S.*[|]'
	regex_res = re.findall(regex, raw_output)
	for item in regex_res:
	    item = re.sub(r'\s+', '', item)
	    if str(item).lower() != 'name':
		self.aggr_name = item
		metadata = self.get_metadata_in_aggregate()
		if str(metadata).lower() == aggr_metadata:
		    hosts = self.get_hosts_in_aggregate()
		    break
	LOG.info("NUMA Aggregate Found - '%s'", self.aggr_name) 
	LOG.info("Hosts present in NUMA aggregate - '%s' are %s", self.aggr_name, hosts)
	LOG.info("Metadata present in NUMA aggregate - '%s' are %s", self.aggr_name, metadata)
	LOG.info("END: test_verify_numa_aggregate")

 
    def get_hosts_in_aggregate(self):
	raw_output = self.openstack.aggregate_show(self.aggr_name)
	aggr_details = output_parser.listing(raw_output)
	hosts = [x['Value'] for x in aggr_details if str(x['Field']).lower() == 'hosts'][0].strip("[]").replace("u'", "").replace("'","")
	return hosts


    def get_metadata_in_aggregate(self):
	raw_output = self.openstack.aggregate_show(self.aggr_name)
        aggr_details = output_parser.listing(raw_output)
	metadata = [x['Value'] for x in aggr_details if str(x['Field']).lower() == 'properties'][0]
	return metadata


    @classmethod
    def resource_cleanup(self):
        super(TestNumaAggregate, self).resource_cleanup()
	self.openstack.resource_cleanup()
	self.openstack = None
