##############################################################################
# COPYRIGHT Ericsson AB 2013
#
# The copyright to the computer program(s) herein is the property of
# Ericsson AB. The programs may be used and/or copied only with written
# permission from Ericsson AB. or in accordance with the terms and
# conditions stipulated in the agreement/contract under which the
# program(s) have been supplied.
##############################################################################

from litp.core.model_type import ItemType, Property, PropertyType
from litp.core.extension import ModelExtension
from litp.core.model_type import Collection


from litp.core.litp_logging import LitpLogger
log = LitpLogger()


class SysparamsPluginExtension(ModelExtension):
    """
    This model extension defines property and item types that let the user
    specify sysparam-node-config and key/value pairs for the
    sysctl parameters.
    """

    def define_property_types(self):
        property_types = [PropertyType("sysparam_value", regex=r"^.+$")]

        return property_types

    def define_item_types(self):
        item_types = []
        item_types.append(
            ItemType("sysparam-node-config",
                     extend_item="node-config",
                     item_description="A node-level sysctrl parameter "
                     "configuration.",
                     params=Collection("sysparam", min_count=1)
            )
        )
        item_types.append(
            ItemType(
                "sysparam",
                item_description="A sysctl parameter key/value pair.",
                key=Property(
                    "file_path_string",
                    required=True,
                    prop_description="The key of the sysctrl parameter"),
                value=Property(
                    "sysparam_value",
                    required=True,
                    prop_description="The value of the sysctrl parameter")
            )
        )
        return item_types
