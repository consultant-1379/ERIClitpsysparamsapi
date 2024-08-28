##############################################################################
# COPYRIGHT Ericsson AB 2013
#
# The copyright to the computer program(s) herein is the property of
# Ericsson AB. The programs may be used and/or copied only with written
# permission from Ericsson AB. or in accordance with the terms and
# conditions stipulated in the agreement/contract under which the
# program(s) have been supplied.
##############################################################################


import unittest
from sysparams_extension.sysparamsextension import SysparamsPluginExtension


class TestsysparamspluginExtension(unittest.TestCase):

    def setUp(self):
        self.ext = SysparamsPluginExtension()

#     def test_property_types_registered(self):
#         # Assert that only extension's property types
#         # are defined.
#         prop_types_expected = ['sysparam',]
#         prop_types = [pt.property_type_id for pt in
#                       self.ext.define_property_types()]
#         self.assertEquals(prop_types_expected, prop_types)

    def test_item_types_registered(self):
        # Assert that only extension's item types
        # are defined.
        item_types_expected = ['sysparam', 'sysparam-node-config']
        item_types = [it.item_type_id for it in
                      self.ext.define_item_types()]
        diff = [x for x in item_types_expected if x not in item_types]
        self.assertEquals(len(diff), 0)

if __name__ == '__main__':
    unittest.main()
