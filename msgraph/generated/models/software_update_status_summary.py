from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class SoftwareUpdateStatusSummary(Entity):
    # Number of compliant devices.
    compliant_device_count: Optional[int] = None
    # Number of compliant users.
    compliant_user_count: Optional[int] = None
    # Number of conflict devices.
    conflict_device_count: Optional[int] = None
    # Number of conflict users.
    conflict_user_count: Optional[int] = None
    # The name of the policy.
    display_name: Optional[str] = None
    # Number of devices had error.
    error_device_count: Optional[int] = None
    # Number of users had error.
    error_user_count: Optional[int] = None
    # Number of non compliant devices.
    non_compliant_device_count: Optional[int] = None
    # Number of non compliant users.
    non_compliant_user_count: Optional[int] = None
    # Number of not applicable devices.
    not_applicable_device_count: Optional[int] = None
    # Number of not applicable users.
    not_applicable_user_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Number of remediated devices.
    remediated_device_count: Optional[int] = None
    # Number of remediated users.
    remediated_user_count: Optional[int] = None
    # Number of unknown devices.
    unknown_device_count: Optional[int] = None
    # Number of unknown users.
    unknown_user_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SoftwareUpdateStatusSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SoftwareUpdateStatusSummary
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SoftwareUpdateStatusSummary()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "compliantDeviceCount": lambda n : setattr(self, 'compliant_device_count', n.get_int_value()),
            "compliantUserCount": lambda n : setattr(self, 'compliant_user_count', n.get_int_value()),
            "conflictDeviceCount": lambda n : setattr(self, 'conflict_device_count', n.get_int_value()),
            "conflictUserCount": lambda n : setattr(self, 'conflict_user_count', n.get_int_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "errorDeviceCount": lambda n : setattr(self, 'error_device_count', n.get_int_value()),
            "errorUserCount": lambda n : setattr(self, 'error_user_count', n.get_int_value()),
            "nonCompliantDeviceCount": lambda n : setattr(self, 'non_compliant_device_count', n.get_int_value()),
            "nonCompliantUserCount": lambda n : setattr(self, 'non_compliant_user_count', n.get_int_value()),
            "notApplicableDeviceCount": lambda n : setattr(self, 'not_applicable_device_count', n.get_int_value()),
            "notApplicableUserCount": lambda n : setattr(self, 'not_applicable_user_count', n.get_int_value()),
            "remediatedDeviceCount": lambda n : setattr(self, 'remediated_device_count', n.get_int_value()),
            "remediatedUserCount": lambda n : setattr(self, 'remediated_user_count', n.get_int_value()),
            "unknownDeviceCount": lambda n : setattr(self, 'unknown_device_count', n.get_int_value()),
            "unknownUserCount": lambda n : setattr(self, 'unknown_user_count', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_int_value("compliantDeviceCount", self.compliant_device_count)
        writer.write_int_value("compliantUserCount", self.compliant_user_count)
        writer.write_int_value("conflictDeviceCount", self.conflict_device_count)
        writer.write_int_value("conflictUserCount", self.conflict_user_count)
        writer.write_str_value("displayName", self.display_name)
        writer.write_int_value("errorDeviceCount", self.error_device_count)
        writer.write_int_value("errorUserCount", self.error_user_count)
        writer.write_int_value("nonCompliantDeviceCount", self.non_compliant_device_count)
        writer.write_int_value("nonCompliantUserCount", self.non_compliant_user_count)
        writer.write_int_value("notApplicableDeviceCount", self.not_applicable_device_count)
        writer.write_int_value("notApplicableUserCount", self.not_applicable_user_count)
        writer.write_int_value("remediatedDeviceCount", self.remediated_device_count)
        writer.write_int_value("remediatedUserCount", self.remediated_user_count)
        writer.write_int_value("unknownDeviceCount", self.unknown_device_count)
        writer.write_int_value("unknownUserCount", self.unknown_user_count)
    

