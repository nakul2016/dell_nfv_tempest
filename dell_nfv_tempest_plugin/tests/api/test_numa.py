from dell_nfv_tempest_plugin.tests.api import base
from tempest import test
import os
from oslo_log import log as logging

LOG = logging.getLogger(__name__, "dell-tempest-plugin")


class CreateNumaFlavor(base.BaseDellNFVTempestTestCase)

    @classmethod
    def resource_setup(self):
        super(CreateNumaFlavor, self).resource_setup()
	self.os_user_name = os.environ['OS_USERNAME']
        self.os_password = os.environ['OS_PASSWORD']
        self.os_auth_url = os.environ['OS_AUTH_URL']
        self.os_tenant_name = os.environ['OS_TENANT_NAME']
        self.cli_dir = '/bin'
        self.cliclient = cli.CLIClient(username=self.os_user_name, password=self.os_password, tenant_name=self.os_tenant_name,
                                       uri=self.os_auth_url, cli_dir='/bin/')


    def create_flavor(self, flavor_name=""):
	if not flavor_name:
	    flavor_name = 'NumaFlavor' + str(self..getUniqueInteger()) + str(self.get_random_integer())
	raw_output = self.cliclient.openstack(action='flavor create', params='--ram 4096' + ' --vcpu 4' + ' --disk 40' + flavor_name)
	LOG.info("create_flavor() raw output %s", raw_output)
	new_flavor = output_parser.listing(raw_output)
        self.assertNotEmpty(new_flavor)
	add_metadata_to_flavor(flavor_name)


    def add_metadata_to_flavor(self, flavor_name)
	raw_output = self.cliclient.openstack(action='flavor set', params=flavor_name + 
						' --property aggregate_instance_extra_specs:pinned=True' +
						' --property hw:cpu_policy=dedicated' +
						' --property hw:cpu_thread_policy=require')
	parsed_output = output_parser.listing(raw_output)
	self.assertIsEmpty(parsed_output)
