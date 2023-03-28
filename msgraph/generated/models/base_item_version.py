from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import document_set_version, drive_item_version, entity, identity_set, list_item_version, publication_facet

from . import entity

class BaseItemVersion(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new baseItemVersion and sets the default values.
        """
        super().__init__()
        # Identity of the user which last modified the version. Read-only.
        self._last_modified_by: Optional[identity_set.IdentitySet] = None
        # Date and time the version was last modified. Read-only.
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Indicates the publication status of this particular version. Read-only.
        self._publication: Optional[publication_facet.PublicationFacet] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BaseItemVersion:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: BaseItemVersion
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.documentSetVersion":
                from . import document_set_version

                return document_set_version.DocumentSetVersion()
            if mapping_value == "#microsoft.graph.driveItemVersion":
                from . import drive_item_version

                return drive_item_version.DriveItemVersion()
            if mapping_value == "#microsoft.graph.listItemVersion":
                from . import list_item_version

                return list_item_version.ListItemVersion()
        return BaseItemVersion()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import document_set_version, drive_item_version, entity, identity_set, list_item_version, publication_facet

        fields: Dict[str, Callable[[Any], None]] = {
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(identity_set.IdentitySet)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "publication": lambda n : setattr(self, 'publication', n.get_object_value(publication_facet.PublicationFacet)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_modified_by(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the lastModifiedBy property value. Identity of the user which last modified the version. Read-only.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._last_modified_by
    
    @last_modified_by.setter
    def last_modified_by(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the lastModifiedBy property value. Identity of the user which last modified the version. Read-only.
        Args:
            value: Value to set for the last_modified_by property.
        """
        self._last_modified_by = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. Date and time the version was last modified. Read-only.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. Date and time the version was last modified. Read-only.
        Args:
            value: Value to set for the last_modified_date_time property.
        """
        self._last_modified_date_time = value
    
    @property
    def publication(self,) -> Optional[publication_facet.PublicationFacet]:
        """
        Gets the publication property value. Indicates the publication status of this particular version. Read-only.
        Returns: Optional[publication_facet.PublicationFacet]
        """
        return self._publication
    
    @publication.setter
    def publication(self,value: Optional[publication_facet.PublicationFacet] = None) -> None:
        """
        Sets the publication property value. Indicates the publication status of this particular version. Read-only.
        Args:
            value: Value to set for the publication property.
        """
        self._publication = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_object_value("publication", self.publication)
    

