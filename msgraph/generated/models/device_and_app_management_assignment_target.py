from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import all_devices_assignment_target, all_licensed_users_assignment_target, configuration_manager_collection_assignment_target, exclusion_group_assignment_target, group_assignment_target

@dataclass
class DeviceAndAppManagementAssignmentTarget(AdditionalDataHolder, Parsable):
    """
    Base type for assignment targets.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceAndAppManagementAssignmentTarget:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceAndAppManagementAssignmentTarget
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.allDevicesAssignmentTarget":
                from . import all_devices_assignment_target

                return all_devices_assignment_target.AllDevicesAssignmentTarget()
            if mapping_value == "#microsoft.graph.allLicensedUsersAssignmentTarget":
                from . import all_licensed_users_assignment_target

                return all_licensed_users_assignment_target.AllLicensedUsersAssignmentTarget()
            if mapping_value == "#microsoft.graph.configurationManagerCollectionAssignmentTarget":
                from . import configuration_manager_collection_assignment_target

                return configuration_manager_collection_assignment_target.ConfigurationManagerCollectionAssignmentTarget()
            if mapping_value == "#microsoft.graph.exclusionGroupAssignmentTarget":
                from . import exclusion_group_assignment_target

                return exclusion_group_assignment_target.ExclusionGroupAssignmentTarget()
            if mapping_value == "#microsoft.graph.groupAssignmentTarget":
                from . import group_assignment_target

                return group_assignment_target.GroupAssignmentTarget()
        return DeviceAndAppManagementAssignmentTarget()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import all_devices_assignment_target, all_licensed_users_assignment_target, configuration_manager_collection_assignment_target, exclusion_group_assignment_target, group_assignment_target

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

