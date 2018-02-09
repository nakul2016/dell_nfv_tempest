from dell_nfv_tempest_plugin.tests.api import api
from oslo_log import log as logging
import tempest.lib.cli.base as cli
import tempest.lib.cli.output_parser as output_parser
import os
import re

LOG = logging.getLogger(__name__, "dell-nfv-tempest-plugin")


class APIHelper():

    def __init__(self):
	self.openstack_api = api.OpenStackAPI()


    def __del__(self):
        self.openstack_api = None


    def get_aggregate_list(self):
	raw_output = self.openstack_api.aggregate_list()
	regex = r'[|].*\S.*[|](.*)[|].*\S.*[|]'
	regex_res = re.findall(regex, raw_output)
        aggr_list = [x.strip(' ') for x in regex_res][1:]
	return aggr_list


    def get_hosts_in_aggregate(self, aggr_name):
	raw_output = self.openstack_api.aggregate_show(aggr_name)
        aggr_details = output_parser.listing(raw_output)
        raw_hosts_output = [x['Value'] for x in aggr_details if str(x['Field']).lower() == 'hosts'][0]
        hosts = raw_hosts_output.strip("[]").replace("u'", "").replace("'","")
   	return hosts


    def get_metadata_in_aggregate(self, aggr_name):
	raw_output = self.openstack_api.aggregate_show(aggr_name)
        aggr_details = output_parser.listing(raw_output)
        metadata = [x['Value'] for x in aggr_details if str(x['Field']).lower() == 'properties'][0]
	return metadata
