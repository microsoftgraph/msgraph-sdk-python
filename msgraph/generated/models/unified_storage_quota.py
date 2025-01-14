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
class UnifiedStorageQuota(Entity, Parsable):
    # The deleted property
    deleted: Optional[int] = None
    # The manageWebUrl property
    manage_web_url: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The remaining property
    remaining: Optional[int] = None
    # The services property
    services: Optional[list[ServiceStorageQuotaBreakdown]] = None
    # The state property
    state: Optional[str] = None
    # The total property
    total: Optional[int] = None
    # The used property
    used: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UnifiedStorageQuota:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UnifiedStorageQuota
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UnifiedStorageQuota()
    
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
            "deleted": lambda n : setattr(self, 'deleted', n.get_int_value()),
            "manageWebUrl": lambda n : setattr(self, 'manage_web_url', n.get_str_value()),
            "remaining": lambda n : setattr(self, 'remaining', n.get_int_value()),
            "services": lambda n : setattr(self, 'services', n.get_collection_of_object_values(ServiceStorageQuotaBreakdown)),
            "state": lambda n : setattr(self, 'state', n.get_str_value()),
            "total": lambda n : setattr(self, 'total', n.get_int_value()),
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
        writer.write_int_value("deleted", self.deleted)
        writer.write_str_value("manageWebUrl", self.manage_web_url)
        writer.write_int_value("remaining", self.remaining)
        writer.write_collection_of_object_values("services", self.services)
        writer.write_str_value("state", self.state)
        writer.write_int_value("total", self.total)
        writer.write_int_value("used", self.used)
    

