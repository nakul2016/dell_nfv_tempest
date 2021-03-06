from dell_nfv_tempest_plugin.tests.api import base, api
from tempest import test
from tempest import config
import tempest.lib.cli.output_parser as output_parser
import os
from oslo_log import log as logging

CONF = config.CONF
LOG = logging.getLogger(__name__, "dell-nfv-tempest-plugin")


class TestNumaFlavorCreation(base.BaseDellNFVTempestTestCase):

    @classmethod
    def resource_setup(self):
        super(TestNumaFlavorCreation, self).resource_setup()
	self.openstack = api.OpenStackAPI()
	self.flavor_name = None
	self.flavor_metadata = CONF.numa.flavor_metadata

 
    @test.attr(type="dell_nfv")
    def test_numa_flavor_creation(self):
	LOG.info("BEGIN: test_numa_flavor_creation()")
	if not self.flavor_name:
	    self.flavor_name = 'NumaFlavor' + str(self.get_random_integer())
	raw_output = self.openstack.flavor_create(self.flavor_name)
	LOG.info("create_flavor() raw output \n%s", raw_output)
	new_flavor = output_parser.listing(raw_output)
        self.assertNotEmpty(new_flavor)
	
	#Add metadata to flavor
	self.add_metadata_to_flavor()
	
	# Delete the Flavor
        self.delete_flavor()
        LOG.info("END: test_numa_flavor_creation")


    def add_metadata_to_flavor(self):
	ret_val = self.openstack.flavor_set_properties(self.flavor_name, self.flavor_metadata) 
	self.assertEmpty(ret_val)
	LOG.info("NUMA Metadata added to flavor %s", self.flavor_name)

   
    def delete_flavor(self):
	ret_val = self.openstack.flavor_delete(self.flavor_name)
	self.assertEmpty(ret_val) 
	LOG.info("Flavor - %s is deleted.", self.flavor_name)

   
    @classmethod
    def resource_cleanup(cls):
        super(TestNumaFlavorCreation, cls).resource_cleanup()
