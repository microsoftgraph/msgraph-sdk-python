from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import data_source_container, ediscovery_index_operation, site_source, unified_group_source, user_source

from . import data_source_container

@dataclass
class EdiscoveryCustodian(data_source_container.DataSourceContainer):
    odata_type = "#microsoft.graph.security.ediscoveryCustodian"
    # Date and time the custodian acknowledged a hold notification.
    acknowledged_date_time: Optional[datetime] = None
    # Email address of the custodian.
    email: Optional[str] = None
    # Operation entity that represents the latest indexing for the custodian.
    last_index_operation: Optional[ediscovery_index_operation.EdiscoveryIndexOperation] = None
    # Data source entity for SharePoint sites associated with the custodian.
    site_sources: Optional[List[site_source.SiteSource]] = None
    # Data source entity for groups associated with the custodian.
    unified_group_sources: Optional[List[unified_group_source.UnifiedGroupSource]] = None
    # Data source entity for a the custodian. This is the container for a custodian's mailbox and OneDrive for Business site.
    user_sources: Optional[List[user_source.UserSource]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EdiscoveryCustodian:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EdiscoveryCustodian
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EdiscoveryCustodian()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import data_source_container, ediscovery_index_operation, site_source, unified_group_source, user_source

        fields: Dict[str, Callable[[Any], None]] = {
            "acknowledgedDateTime": lambda n : setattr(self, 'acknowledged_date_time', n.get_datetime_value()),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "lastIndexOperation": lambda n : setattr(self, 'last_index_operation', n.get_object_value(ediscovery_index_operation.EdiscoveryIndexOperation)),
            "siteSources": lambda n : setattr(self, 'site_sources', n.get_collection_of_object_values(site_source.SiteSource)),
            "unifiedGroupSources": lambda n : setattr(self, 'unified_group_sources', n.get_collection_of_object_values(unified_group_source.UnifiedGroupSource)),
            "userSources": lambda n : setattr(self, 'user_sources', n.get_collection_of_object_values(user_source.UserSource)),
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
        writer.write_datetime_value("acknowledgedDateTime", self.acknowledged_date_time)
        writer.write_str_value("email", self.email)
        writer.write_object_value("lastIndexOperation", self.last_index_operation)
        writer.write_collection_of_object_values("siteSources", self.site_sources)
        writer.write_collection_of_object_values("unifiedGroupSources", self.unified_group_sources)
        writer.write_collection_of_object_values("userSources", self.user_sources)
    

