# Copyright (c) 2017 Orange.
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

from django import test
import mock

from bgpvpn_dashboard.dashboards.admin.bgpvpn import tables as bgpvpn_tables


class TestDeleteBgpvpns(test.TestCase):
    @mock.patch.object(bgpvpn_tables, 'bgpvpn_api')
    def test_delete(self, mock_bgpvpn_api):
        mock_request = mock.Mock()
        delete_bgpvpn = bgpvpn_tables.DeleteBgpvpn()
        delete_bgpvpn.delete(mock_request, "id")
        mock_bgpvpn_api.bgpvpn_delete.assert_called_once_with(mock_request,
                                                              "id")
