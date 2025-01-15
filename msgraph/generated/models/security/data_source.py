from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from ..identity_set import IdentitySet
    from .data_source_hold_status import DataSourceHoldStatus
    from .site_source import SiteSource
    from .unified_group_source import UnifiedGroupSource
    from .user_source import UserSource

from ..entity import Entity

@dataclass
class DataSource(Entity, Parsable):
    # The user who created the dataSource.
    created_by: Optional[IdentitySet] = None
    # The date and time the dataSource was created.
    created_date_time: Optional[datetime.datetime] = None
    # The display name of the dataSource and is the name of the SharePoint site.
    display_name: Optional[str] = None
    # The hold status of the dataSource.The possible values are: notApplied, applied, applying, removing, partial
    hold_status: Optional[DataSourceHoldStatus] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DataSource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DataSource
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.siteSource".casefold():
            from .site_source import SiteSource

            return SiteSource()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.unifiedGroupSource".casefold():
            from .unified_group_source import UnifiedGroupSource

            return UnifiedGroupSource()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.userSource".casefold():
            from .user_source import UserSource

            return UserSource()
        return DataSource()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from ..identity_set import IdentitySet
        from .data_source_hold_status import DataSourceHoldStatus
        from .site_source import SiteSource
        from .unified_group_source import UnifiedGroupSource
        from .user_source import UserSource

        from ..entity import Entity
        from ..identity_set import IdentitySet
        from .data_source_hold_status import DataSourceHoldStatus
        from .site_source import SiteSource
        from .unified_group_source import UnifiedGroupSource
        from .user_source import UserSource

        fields: dict[str, Callable[[Any], None]] = {
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(IdentitySet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "holdStatus": lambda n : setattr(self, 'hold_status', n.get_enum_value(DataSourceHoldStatus)),
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
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("holdStatus", self.hold_status)
    

