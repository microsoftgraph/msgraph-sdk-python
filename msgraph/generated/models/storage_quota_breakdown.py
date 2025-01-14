from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .service_storage_quota_breakdown import ServiceStorageQuotaBreakdown

from .entity import Entity

@dataclass
class StorageQuotaBreakdown(Entity, Parsable):
    # The displayName property
    display_name: Optional[str] = None
    # The manageWebUrl property
    manage_web_url: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The used property
    used: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> StorageQuotaBreakdown:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: StorageQuotaBreakdown
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.serviceStorageQuotaBreakdown".casefold():
            from .service_storage_quota_breakdown import ServiceStorageQuotaBreakdown

            return ServiceStorageQuotaBreakdown()
        return StorageQuotaBreakdown()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .service_storage_quota_breakdown import ServiceStorageQuotaBreakdown

        from .entity import Entity
        from .service_storage_quota_breakdown import ServiceStorageQuotaBreakdown

        fields: dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "manageWebUrl": lambda n : setattr(self, 'manage_web_url', n.get_str_value()),
            "used": lambda n : setattr(self, 'used', n.get_int_value()),
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
        writer.write_str_value("manageWebUrl", self.manage_web_url)
        writer.write_int_value("used", self.used)
    

