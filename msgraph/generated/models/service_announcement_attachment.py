from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class ServiceAnnouncementAttachment(entity.Entity):
    """
    Provides operations to manage the admin singleton.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new serviceAnnouncementAttachment and sets the default values.
        """
        super().__init__()
        # The attachment content.
        self._content: Optional[bytes] = None
        # The contentType property
        self._content_type: Optional[str] = None
        # The lastModifiedDateTime property
        self._last_modified_date_time: Optional[datetime] = None
        # The name property
        self._name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The size property
        self._size: Optional[int] = None
    
    @property
    def content(self,) -> Optional[bytes]:
        """
        Gets the content property value. The attachment content.
        Returns: Optional[bytes]
        """
        return self._content
    
    @content.setter
    def content(self,value: Optional[bytes] = None) -> None:
        """
        Sets the content property value. The attachment content.
        Args:
            value: Value to set for the content property.
        """
        self._content = value
    
    @property
    def content_type(self,) -> Optional[str]:
        """
        Gets the contentType property value. The contentType property
        Returns: Optional[str]
        """
        return self._content_type
    
    @content_type.setter
    def content_type(self,value: Optional[str] = None) -> None:
        """
        Sets the contentType property value. The contentType property
        Args:
            value: Value to set for the contentType property.
        """
        self._content_type = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ServiceAnnouncementAttachment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ServiceAnnouncementAttachment
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ServiceAnnouncementAttachment()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "content": lambda n : setattr(self, 'content', n.get_bytes_value()),
            "content_type": lambda n : setattr(self, 'content_type', n.get_str_value()),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "size": lambda n : setattr(self, 'size', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. The lastModifiedDateTime property
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. The lastModifiedDateTime property
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. The name property
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. The name property
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("content", self.content)
        writer.write_str_value("contentType", self.content_type)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("name", self.name)
        writer.write_int_value("size", self.size)
    
    @property
    def size(self,) -> Optional[int]:
        """
        Gets the size property value. The size property
        Returns: Optional[int]
        """
        return self._size
    
    @size.setter
    def size(self,value: Optional[int] = None) -> None:
        """
        Sets the size property value. The size property
        Args:
            value: Value to set for the size property.
        """
        self._size = value
    

