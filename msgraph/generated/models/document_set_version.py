from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

document_set_version_item = lazy_import('msgraph.generated.models.document_set_version_item')
identity_set = lazy_import('msgraph.generated.models.identity_set')
list_item_version = lazy_import('msgraph.generated.models.list_item_version')

class DocumentSetVersion(list_item_version.ListItemVersion):
    @property
    def comment(self,) -> Optional[str]:
        """
        Gets the comment property value. Comment about the captured version.
        Returns: Optional[str]
        """
        return self._comment
    
    @comment.setter
    def comment(self,value: Optional[str] = None) -> None:
        """
        Sets the comment property value. Comment about the captured version.
        Args:
            value: Value to set for the comment property.
        """
        self._comment = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new DocumentSetVersion and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.documentSetVersion"
        # Comment about the captured version.
        self._comment: Optional[str] = None
        # User who captured the version.
        self._created_by: Optional[identity_set.IdentitySet] = None
        # Date and time when this version was created.
        self._created_date_time: Optional[datetime] = None
        # Items within the document set that are captured as part of this version.
        self._items: Optional[List[document_set_version_item.DocumentSetVersionItem]] = None
        # If true, minor versions of items are also captured; otherwise, only major versions will be captured. Default value is false.
        self._should_capture_minor_version: Optional[bool] = None
    
    @property
    def created_by(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the createdBy property value. User who captured the version.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._created_by
    
    @created_by.setter
    def created_by(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the createdBy property value. User who captured the version.
        Args:
            value: Value to set for the createdBy property.
        """
        self._created_by = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. Date and time when this version was created.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. Date and time when this version was created.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DocumentSetVersion:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DocumentSetVersion
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DocumentSetVersion()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "comment": lambda n : setattr(self, 'comment', n.get_str_value()),
            "created_by": lambda n : setattr(self, 'created_by', n.get_object_value(identity_set.IdentitySet)),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "items": lambda n : setattr(self, 'items', n.get_collection_of_object_values(document_set_version_item.DocumentSetVersionItem)),
            "should_capture_minor_version": lambda n : setattr(self, 'should_capture_minor_version', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def items(self,) -> Optional[List[document_set_version_item.DocumentSetVersionItem]]:
        """
        Gets the items property value. Items within the document set that are captured as part of this version.
        Returns: Optional[List[document_set_version_item.DocumentSetVersionItem]]
        """
        return self._items
    
    @items.setter
    def items(self,value: Optional[List[document_set_version_item.DocumentSetVersionItem]] = None) -> None:
        """
        Sets the items property value. Items within the document set that are captured as part of this version.
        Args:
            value: Value to set for the items property.
        """
        self._items = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("comment", self.comment)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_collection_of_object_values("items", self.items)
        writer.write_bool_value("shouldCaptureMinorVersion", self.should_capture_minor_version)
    
    @property
    def should_capture_minor_version(self,) -> Optional[bool]:
        """
        Gets the shouldCaptureMinorVersion property value. If true, minor versions of items are also captured; otherwise, only major versions will be captured. Default value is false.
        Returns: Optional[bool]
        """
        return self._should_capture_minor_version
    
    @should_capture_minor_version.setter
    def should_capture_minor_version(self,value: Optional[bool] = None) -> None:
        """
        Sets the shouldCaptureMinorVersion property value. If true, minor versions of items are also captured; otherwise, only major versions will be captured. Default value is false.
        Args:
            value: Value to set for the shouldCaptureMinorVersion property.
        """
        self._should_capture_minor_version = value
    

