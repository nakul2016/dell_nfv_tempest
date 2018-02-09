# Copyright 2015
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from oslo_config import cfg
from tempest import config

numa_group = cfg.OptGroup(
    name="numa",
    title="NUMA Service Options"
)

NumaGroup = [
    cfg.StrOpt("aggregate_metadata", 
                help="Metadata for Numa Aggregate to be used in tests. " 
		     "This is a required option"),
    cfg.ListOpt("flavor_metadata",
		help="Metadata for Numa Flavor to be used in tests. "
		     "This is a required option")
]

hugepage_group = cfg.OptGroup(
    name="hugepage",
    title="Hugepage Service Options"
)

HugepageGroup = [
    cfg.StrOpt("aggregate_metadata",
               help="Metadata for Hugepage Aggregate to be used in tests. "
		     "This is a required option")
]
