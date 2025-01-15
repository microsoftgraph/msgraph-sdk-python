from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .data_source_container import DataSourceContainer
    from .ediscovery_index_operation import EdiscoveryIndexOperation
    from .site_source import SiteSource
    from .unified_group_source import UnifiedGroupSource
    from .user_source import UserSource

from .data_source_container import DataSourceContainer

@dataclass
class EdiscoveryCustodian(DataSourceContainer, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.ediscoveryCustodian"
    # Date and time the custodian acknowledged a hold notification.
    acknowledged_date_time: Optional[datetime.datetime] = None
    # Email address of the custodian.
    email: Optional[str] = None
    # Operation entity that represents the latest indexing for the custodian.
    last_index_operation: Optional[EdiscoveryIndexOperation] = None
    # Data source entity for SharePoint sites associated with the custodian.
    site_sources: Optional[list[SiteSource]] = None
    # Data source entity for groups associated with the custodian.
    unified_group_sources: Optional[list[UnifiedGroupSource]] = None
    # Data source entity for a the custodian. This is the container for a custodian's mailbox and OneDrive for Business site.
    user_sources: Optional[list[UserSource]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EdiscoveryCustodian:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EdiscoveryCustodian
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EdiscoveryCustodian()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .data_source_container import DataSourceContainer
        from .ediscovery_index_operation import EdiscoveryIndexOperation
        from .site_source import SiteSource
        from .unified_group_source import UnifiedGroupSource
        from .user_source import UserSource

        from .data_source_container import DataSourceContainer
        from .ediscovery_index_operation import EdiscoveryIndexOperation
        from .site_source import SiteSource
        from .unified_group_source import UnifiedGroupSource
        from .user_source import UserSource

        fields: dict[str, Callable[[Any], None]] = {
            "acknowledgedDateTime": lambda n : setattr(self, 'acknowledged_date_time', n.get_datetime_value()),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "lastIndexOperation": lambda n : setattr(self, 'last_index_operation', n.get_object_value(EdiscoveryIndexOperation)),
            "siteSources": lambda n : setattr(self, 'site_sources', n.get_collection_of_object_values(SiteSource)),
            "unifiedGroupSources": lambda n : setattr(self, 'unified_group_sources', n.get_collection_of_object_values(UnifiedGroupSource)),
            "userSources": lambda n : setattr(self, 'user_sources', n.get_collection_of_object_values(UserSource)),
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
        writer.write_datetime_value("acknowledgedDateTime", self.acknowledged_date_time)
        writer.write_str_value("email", self.email)
        writer.write_object_value("lastIndexOperation", self.last_index_operation)
        writer.write_collection_of_object_values("siteSources", self.site_sources)
        writer.write_collection_of_object_values("unifiedGroupSources", self.unified_group_sources)
        writer.write_collection_of_object_values("userSources", self.user_sources)
    

