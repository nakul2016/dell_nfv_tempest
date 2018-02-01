from dell_nfv_tempest_plugin.tests.api import base
from tempest import test
import tempest.lib.cli.base as cli
import tempest.lib.cli.output_parser as output_parser
import os
from oslo_log import log as logging

LOG = logging.getLogger(__name__, "dell-nfv-tempest-plugin")


class VerifyNumaAggregate(base.BaseDellNFVTempestTestCase)

    @classmethod
    def resource_setup(self):
	
	super(VerifyNumaAggregate, self).resource_setup()
	self.os_user_name = os.environ['OS_USERNAME']
        self.os_password = os.environ['OS_PASSWORD']
        self.os_auth_url = os.environ['OS_AUTH_URL']
        self.os_tenant_name = os.environ['OS_USERNAME']
        self.cli_dir = '/bin'
        self.cliclient = cli.CLIClient(username=self.os_user_name, password=self.os_password, tenant_name=self.os_tenant_name,
                                       uri=self.os_auth_url, cli_dir='/bin/')


    @test.attr(type='dell_nfv')
    def verify_numa_aggregate(self):
	LOG.info("BEGIN: verify_numa_aggregate")
	raw_output = self.cliclient.openstack(action='aggregate list')
	all_aggr = output_parser.listing(raw_output)
	aggr_names = [x['Name'] for x in all_aggr]
	LOG.info("Aggregtes present in OverCloud -", ', '.join(aggr_names)) 
	for aggr_name in aggr_names:
	    self.get_hosts_and_metadata_in_aggregate(aggr_name)

   
    def get_hosts_and_metadata_in_aggregate(self, aggr_name):
	raw_output = self.cliclient.openstack(action='aggregate show', params=aggr_name)
	aggr_details = output_parser.listing(raw_output)
	hosts = [x['Value'] for x in aggr_details if str(x['Field']).lower() == 'hosts'][0].strip("[]").replace("u'", "").replace("'","")
	LOG.info("Hosts present in host aggregate - " + aggr_name + " are " + hosts)
	metadata_tag = [x['Value'] for x in aggr_details if str(x['Field']).lower() == 'properties'][0]
	LOG.info("Metadata tag present in host aggregate - " + aggr_name + " are " + metadata_tag)
