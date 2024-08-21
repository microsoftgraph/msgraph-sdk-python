from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .document_set_version_item import DocumentSetVersionItem
    from .identity_set import IdentitySet
    from .list_item_version import ListItemVersion

from .list_item_version import ListItemVersion

@dataclass
class DocumentSetVersion(ListItemVersion):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.documentSetVersion"
    # Comment about the captured version.
    comment: Optional[str] = None
    # User who captured the version.
    created_by: Optional[IdentitySet] = None
    # Date and time when this version was created.
    created_date_time: Optional[datetime.datetime] = None
    # Items within the document set that are captured as part of this version.
    items: Optional[List[DocumentSetVersionItem]] = None
    # If true, minor versions of items are also captured; otherwise, only major versions are captured. The default value is false.
    should_capture_minor_version: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DocumentSetVersion:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DocumentSetVersion
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DocumentSetVersion()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .document_set_version_item import DocumentSetVersionItem
        from .identity_set import IdentitySet
        from .list_item_version import ListItemVersion

        from .document_set_version_item import DocumentSetVersionItem
        from .identity_set import IdentitySet
        from .list_item_version import ListItemVersion

        fields: Dict[str, Callable[[Any], None]] = {
            "comment": lambda n : setattr(self, 'comment', n.get_str_value()),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(IdentitySet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "items": lambda n : setattr(self, 'items', n.get_collection_of_object_values(DocumentSetVersionItem)),
            "shouldCaptureMinorVersion": lambda n : setattr(self, 'should_capture_minor_version', n.get_bool_value()),
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
        writer.write_str_value("comment", self.comment)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_collection_of_object_values("items", self.items)
        writer.write_bool_value("shouldCaptureMinorVersion", self.should_capture_minor_version)
    

