from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import document_set_version, drive_item_version, entity, identity_set, list_item_version, publication_facet

from . import entity

@dataclass
class BaseItemVersion(entity.Entity):
    # Identity of the user which last modified the version. Read-only.
    last_modified_by: Optional[identity_set.IdentitySet] = None
    # Date and time the version was last modified. Read-only.
    last_modified_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates the publication status of this particular version. Read-only.
    publication: Optional[publication_facet.PublicationFacet] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BaseItemVersion:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: BaseItemVersion
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.documentSetVersion".casefold():
            from . import document_set_version

            return document_set_version.DocumentSetVersion()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.driveItemVersion".casefold():
            from . import drive_item_version

            return drive_item_version.DriveItemVersion()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.listItemVersion".casefold():
            from . import list_item_version

            return list_item_version.ListItemVersion()
        return BaseItemVersion()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import document_set_version, drive_item_version, entity, identity_set, list_item_version, publication_facet

        from . import document_set_version, drive_item_version, entity, identity_set, list_item_version, publication_facet

        fields: Dict[str, Callable[[Any], None]] = {
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(identity_set.IdentitySet)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "publication": lambda n : setattr(self, 'publication', n.get_object_value(publication_facet.PublicationFacet)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_object_value("publication", self.publication)
    

