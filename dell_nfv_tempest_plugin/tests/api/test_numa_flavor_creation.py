from dell_nfv_tempest_plugin.tests.api import base
from tempest import test
import tempest.lib.cli.base as cli
import tempest.lib.cli.output_parser as output_parser
import os
from oslo_log import log as logging

LOG = logging.getLogger(__name__, "dell-nfv-tempest-plugin")


class TestNumaFlavorCreation(base.BaseDellNFVTempestTestCase):

    @classmethod
    def resource_setup(self):
        super(TestNumaFlavorCreation, self).resource_setup()
	self.os_user_name = os.environ['OS_USERNAME']
        self.os_password = os.environ['OS_PASSWORD']
        self.os_auth_url = os.environ['OS_AUTH_URL']
        self.os_tenant_name = os.environ['OS_TENANT_NAME']
        self.cli_dir = '/bin'
        self.cliclient = cli.CLIClient(username=self.os_user_name, password=self.os_password, tenant_name=self.os_tenant_name,
                                       uri=self.os_auth_url, cli_dir='/bin/')
	self.flavor_name = None

    
    @test.attr(type="dell_nfv")
    def test_numa_flavor_creation(self):
	LOG.info("BEGIN: test_numa_flavor_creation()")
	if not self.flavor_name:
	    self.flavor_name = 'NumaFlavor' + str(self.getUniqueInteger()) + str(self.get_random_integer())
	raw_output = self.cliclient.openstack(action='flavor create', params='--ram 4096' + ' --vcpu 4' + ' --disk 40' + self.flavor_name)
	LOG.info("create_flavor() raw output %s", raw_output)
	new_flavor = output_parser.listing(raw_output)
        self.assertNotEmpty(new_flavor)
	add_metadata_to_flavor()
	
	# Delete the Flavor
        self.delete_flavor()
        LOG.info("END: test_numa_flavor_creation")



    def add_metadata_to_flavor(self):
	ret_val = self.cliclient.openstack(action='flavor set', params=self.flavor_name + 
						' --property aggregate_instance_extra_specs:pinned=True' +
						' --property hw:cpu_policy=dedicated' +
						' --property hw:cpu_thread_policy=require')
	self.assertIsEmpty(ret_val)

   
    def delete_flavor(self):
	ret_val = self.cliclient.openstack(action='flavor delete', params=self.flavor_name)
	self.assertIsEmpty(ret_val) 
