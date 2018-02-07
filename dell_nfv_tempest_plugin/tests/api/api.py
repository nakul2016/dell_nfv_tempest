from dell_nfv_tempest_plugin.tests.api import base
from oslo_log import log as logging

LOG = logging.getLogger(__name__, "dell-nfv-tempest-plugin")


class OpenStackAPI(base.BaseDellNFVTempestTestCase):

    @classmethod
    def resource_setup(self):
        super(OpenStackAPI, self).resource_setup()
	self.param = ''

 
    @classmethod
    def resource_cleanup(self):
        super(OpenStackAPI, self).resource_cleanup()


    def aggregate_list(self):
        return self.cliclient.openstack(action='aggregate list')


    def aggregate_show(self, aggr_name):
        return self.cliclient.openstack(action='aggregate show', params=str(aggr_name))


    def flavor_create(self, flavor_name, ram=4096, vcpu=4, disk=20):
	return self.cliclient.openstack(action='flavor create', params=str(flavor_name) + ' --ram ' + str(ram) + ' --vcpu ' + str(vcpu) + ' --disk ' + str(disk))


    def flavor_set_properties(self, flavor_name, properties):
	self.param = ''
	for property in properties:
	    self.param = self.param + ' --property ' + str(property)
	return self.cliclient.openstack(action='flavor set', params=str(flavor_name) + self.param)	
   

    def flavor_delete(self, flavor_name):
	return self.cliclient.openstack(action='flavor delete', params=str(flavor_name))


    def runTest(self):
        pass
