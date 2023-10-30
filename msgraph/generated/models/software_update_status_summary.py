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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SoftwareUpdateStatusSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SoftwareUpdateStatusSummary
        """
        if not parse_node:
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
            "compliant_device_count": lambda n : setattr(self, 'compliant_device_count', n.get_int_value()),
            "compliant_user_count": lambda n : setattr(self, 'compliant_user_count', n.get_int_value()),
            "conflict_device_count": lambda n : setattr(self, 'conflict_device_count', n.get_int_value()),
            "conflict_user_count": lambda n : setattr(self, 'conflict_user_count', n.get_int_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "error_device_count": lambda n : setattr(self, 'error_device_count', n.get_int_value()),
            "error_user_count": lambda n : setattr(self, 'error_user_count', n.get_int_value()),
            "non_compliant_device_count": lambda n : setattr(self, 'non_compliant_device_count', n.get_int_value()),
            "non_compliant_user_count": lambda n : setattr(self, 'non_compliant_user_count', n.get_int_value()),
            "not_applicable_device_count": lambda n : setattr(self, 'not_applicable_device_count', n.get_int_value()),
            "not_applicable_user_count": lambda n : setattr(self, 'not_applicable_user_count', n.get_int_value()),
            "remediated_device_count": lambda n : setattr(self, 'remediated_device_count', n.get_int_value()),
            "remediated_user_count": lambda n : setattr(self, 'remediated_user_count', n.get_int_value()),
            "unknown_device_count": lambda n : setattr(self, 'unknown_device_count', n.get_int_value()),
            "unknown_user_count": lambda n : setattr(self, 'unknown_user_count', n.get_int_value()),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_int_value("compliant_device_count", self.compliant_device_count)
        writer.write_int_value("compliant_user_count", self.compliant_user_count)
        writer.write_int_value("conflict_device_count", self.conflict_device_count)
        writer.write_int_value("conflict_user_count", self.conflict_user_count)
        writer.write_str_value("display_name", self.display_name)
        writer.write_int_value("error_device_count", self.error_device_count)
        writer.write_int_value("error_user_count", self.error_user_count)
        writer.write_int_value("non_compliant_device_count", self.non_compliant_device_count)
        writer.write_int_value("non_compliant_user_count", self.non_compliant_user_count)
        writer.write_int_value("not_applicable_device_count", self.not_applicable_device_count)
        writer.write_int_value("not_applicable_user_count", self.not_applicable_user_count)
        writer.write_int_value("remediated_device_count", self.remediated_device_count)
        writer.write_int_value("remediated_user_count", self.remediated_user_count)
        writer.write_int_value("unknown_device_count", self.unknown_device_count)
        writer.write_int_value("unknown_user_count", self.unknown_user_count)
    

