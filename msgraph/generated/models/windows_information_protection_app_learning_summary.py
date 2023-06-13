from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import application_type, entity

from . import entity

@dataclass
class WindowsInformationProtectionAppLearningSummary(entity.Entity):
    """
    Windows Information Protection AppLearning Summary entity.
    """
    # Application Name
    application_name: Optional[str] = None
    # Possible types of Application
    application_type: Optional[application_type.ApplicationType] = None
    # Device Count
    device_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsInformationProtectionAppLearningSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsInformationProtectionAppLearningSummary
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsInformationProtectionAppLearningSummary()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import application_type, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "applicationName": lambda n : setattr(self, 'application_name', n.get_str_value()),
            "applicationType": lambda n : setattr(self, 'application_type', n.get_enum_value(application_type.ApplicationType)),
            "deviceCount": lambda n : setattr(self, 'device_count', n.get_int_value()),
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
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("applicationName", self.application_name)
        writer.write_enum_value("applicationType", self.application_type)
        writer.write_int_value("deviceCount", self.device_count)
    

