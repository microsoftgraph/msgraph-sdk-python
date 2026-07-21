from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class CloudPcServicePlan(Entity, Parsable):
    # The name for the service plan. Read-only.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The size of the RAM in GB. Read-only.
    ram_in_g_b: Optional[int] = None
    # The size of the operating system disk in GB. Read-only.
    storage_in_g_b: Optional[int] = None
    # The number of vCPUs. Read-only.
    v_cpu_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudPcServicePlan:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcServicePlan
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudPcServicePlan()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "ramInGB": lambda n : setattr(self, 'ram_in_g_b', n.get_int_value()),
            "storageInGB": lambda n : setattr(self, 'storage_in_g_b', n.get_int_value()),
            "vCpuCount": lambda n : setattr(self, 'v_cpu_count', n.get_int_value()),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_int_value("ramInGB", self.ram_in_g_b)
        writer.write_int_value("storageInGB", self.storage_in_g_b)
        writer.write_int_value("vCpuCount", self.v_cpu_count)
    

