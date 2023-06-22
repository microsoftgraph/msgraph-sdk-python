from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_and_app_management_assignment_target, entity, install_intent, mobile_app_assignment_settings

from . import entity

@dataclass
class MobileAppAssignment(entity.Entity):
    """
    A class containing the properties used for Group Assignment of a Mobile App.
    """
    # Possible values for the install intent chosen by the admin.
    intent: Optional[install_intent.InstallIntent] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The settings for target assignment defined by the admin.
    settings: Optional[mobile_app_assignment_settings.MobileAppAssignmentSettings] = None
    # The target group assignment defined by the admin.
    target: Optional[device_and_app_management_assignment_target.DeviceAndAppManagementAssignmentTarget] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MobileAppAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MobileAppAssignment
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return MobileAppAssignment()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_and_app_management_assignment_target, entity, install_intent, mobile_app_assignment_settings

        from . import device_and_app_management_assignment_target, entity, install_intent, mobile_app_assignment_settings

        fields: Dict[str, Callable[[Any], None]] = {
            "intent": lambda n : setattr(self, 'intent', n.get_enum_value(install_intent.InstallIntent)),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(mobile_app_assignment_settings.MobileAppAssignmentSettings)),
            "target": lambda n : setattr(self, 'target', n.get_object_value(device_and_app_management_assignment_target.DeviceAndAppManagementAssignmentTarget)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_enum_value("intent", self.intent)
        writer.write_object_value("settings", self.settings)
        writer.write_object_value("target", self.target)
    

