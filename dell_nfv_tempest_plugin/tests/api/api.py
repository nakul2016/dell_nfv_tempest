from oslo_log import log as logging
import tempest.lib.cli.base as cli
import os

LOG = logging.getLogger(__name__, "dell-nfv-tempest-plugin")


class Resources(object):

    def __init__(self):
	self.os_user_name = os.environ['OS_USERNAME']
        self.os_password = os.environ['OS_PASSWORD']
        self.os_auth_url = os.environ['OS_AUTH_URL']
        self.os_tenant_name = os.environ['OS_USERNAME']
        self.cli_dir = '/bin'
        self.cliclient = cli.CLIClient(username=self.os_user_name,
                                       password=self.os_password,
                                       tenant_name=self.os_tenant_name,
                                       uri=self.os_auth_url,
                                       cli_dir='/bin/')


    def __del__(self):
	self.cliclient = None



class OpenStackAPI(Resources):

    def __init__(self):
	super(OpenStackAPI, self).__init__()
	self.param = ''

 
    def __del__(self):
	super(OpenStackAPI, self).__del__()


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
