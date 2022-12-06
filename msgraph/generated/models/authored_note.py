from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
identity = lazy_import('msgraph.generated.models.identity')
item_body = lazy_import('msgraph.generated.models.item_body')

class AuthoredNote(entity.Entity):
    @property
    def author(self,) -> Optional[identity.Identity]:
        """
        Gets the author property value. Identity information about the note's author.
        Returns: Optional[identity.Identity]
        """
        return self._author
    
    @author.setter
    def author(self,value: Optional[identity.Identity] = None) -> None:
        """
        Sets the author property value. Identity information about the note's author.
        Args:
            value: Value to set for the author property.
        """
        self._author = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new AuthoredNote and sets the default values.
        """
        super().__init__()
        # Identity information about the note's author.
        self._author: Optional[identity.Identity] = None
        # The content of the note.
        self._content: Optional[item_body.ItemBody] = None
        # The date and time when the entity was created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._created_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @property
    def content(self,) -> Optional[item_body.ItemBody]:
        """
        Gets the content property value. The content of the note.
        Returns: Optional[item_body.ItemBody]
        """
        return self._content
    
    @content.setter
    def content(self,value: Optional[item_body.ItemBody] = None) -> None:
        """
        Sets the content property value. The content of the note.
        Args:
            value: Value to set for the content property.
        """
        self._content = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The date and time when the entity was created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The date and time when the entity was created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AuthoredNote:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AuthoredNote
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AuthoredNote()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "author": lambda n : setattr(self, 'author', n.get_object_value(identity.Identity)),
            "content": lambda n : setattr(self, 'content', n.get_object_value(item_body.ItemBody)),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
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
        writer.write_object_value("author", self.author)
        writer.write_object_value("content", self.content)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
    

