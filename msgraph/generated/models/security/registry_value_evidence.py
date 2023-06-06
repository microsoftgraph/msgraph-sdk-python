from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import alert_evidence

from . import alert_evidence

@dataclass
class RegistryValueEvidence(alert_evidence.AlertEvidence):
    # The mdeDeviceId property
    mde_device_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Registry hive of the key that the recorded action was applied to.
    registry_hive: Optional[str] = None
    # Registry key that the recorded action was applied to.
    registry_key: Optional[str] = None
    # Data of the registry value that the recorded action was applied to.
    registry_value: Optional[str] = None
    # Name of the registry value that the recorded action was applied to.
    registry_value_name: Optional[str] = None
    # Data type, such as binary or string, of the registry value that the recorded action was applied to.
    registry_value_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RegistryValueEvidence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RegistryValueEvidence
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RegistryValueEvidence()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import alert_evidence

        fields: Dict[str, Callable[[Any], None]] = {
            "mdeDeviceId": lambda n : setattr(self, 'mde_device_id', n.get_str_value()),
            "registryHive": lambda n : setattr(self, 'registry_hive', n.get_str_value()),
            "registryKey": lambda n : setattr(self, 'registry_key', n.get_str_value()),
            "registryValue": lambda n : setattr(self, 'registry_value', n.get_str_value()),
            "registryValueName": lambda n : setattr(self, 'registry_value_name', n.get_str_value()),
            "registryValueType": lambda n : setattr(self, 'registry_value_type', n.get_str_value()),
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
        writer.write_str_value("mdeDeviceId", self.mde_device_id)
        writer.write_str_value("registryHive", self.registry_hive)
        writer.write_str_value("registryKey", self.registry_key)
        writer.write_str_value("registryValue", self.registry_value)
        writer.write_str_value("registryValueName", self.registry_value_name)
        writer.write_str_value("registryValueType", self.registry_value_type)
    

