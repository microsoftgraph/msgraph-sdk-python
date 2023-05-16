from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import acl, external_activity, external_item_content, properties
    from .. import entity

from .. import entity

class ExternalItem(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new externalItem and sets the default values.
        """
        super().__init__()
        # An array of access control entries. Each entry specifies the access granted to a user or group. Required.
        self._acl: Optional[List[acl.Acl]] = None
        # Returns a list of activities performed on the item. Write-only.
        self._activities: Optional[List[external_activity.ExternalActivity]] = None
        # A plain-text  representation of the contents of the item. The text in this property is full-text indexed. Optional.
        self._content: Optional[external_item_content.ExternalItemContent] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # A property bag with the properties of the item. The properties MUST conform to the schema defined for the externalConnection. Required.
        self._properties: Optional[properties.Properties] = None
    
    @property
    def acl(self,) -> Optional[List[acl.Acl]]:
        """
        Gets the acl property value. An array of access control entries. Each entry specifies the access granted to a user or group. Required.
        Returns: Optional[List[acl.Acl]]
        """
        return self._acl
    
    @acl.setter
    def acl(self,value: Optional[List[acl.Acl]] = None) -> None:
        """
        Sets the acl property value. An array of access control entries. Each entry specifies the access granted to a user or group. Required.
        Args:
            value: Value to set for the acl property.
        """
        self._acl = value
    
    @property
    def activities(self,) -> Optional[List[external_activity.ExternalActivity]]:
        """
        Gets the activities property value. Returns a list of activities performed on the item. Write-only.
        Returns: Optional[List[external_activity.ExternalActivity]]
        """
        return self._activities
    
    @activities.setter
    def activities(self,value: Optional[List[external_activity.ExternalActivity]] = None) -> None:
        """
        Sets the activities property value. Returns a list of activities performed on the item. Write-only.
        Args:
            value: Value to set for the activities property.
        """
        self._activities = value
    
    @property
    def content(self,) -> Optional[external_item_content.ExternalItemContent]:
        """
        Gets the content property value. A plain-text  representation of the contents of the item. The text in this property is full-text indexed. Optional.
        Returns: Optional[external_item_content.ExternalItemContent]
        """
        return self._content
    
    @content.setter
    def content(self,value: Optional[external_item_content.ExternalItemContent] = None) -> None:
        """
        Sets the content property value. A plain-text  representation of the contents of the item. The text in this property is full-text indexed. Optional.
        Args:
            value: Value to set for the content property.
        """
        self._content = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ExternalItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ExternalItem
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ExternalItem()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import acl, external_activity, external_item_content, properties
        from .. import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "acl": lambda n : setattr(self, 'acl', n.get_collection_of_object_values(acl.Acl)),
            "activities": lambda n : setattr(self, 'activities', n.get_collection_of_object_values(external_activity.ExternalActivity)),
            "content": lambda n : setattr(self, 'content', n.get_object_value(external_item_content.ExternalItemContent)),
            "properties": lambda n : setattr(self, 'properties', n.get_object_value(properties.Properties)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def properties(self,) -> Optional[properties.Properties]:
        """
        Gets the properties property value. A property bag with the properties of the item. The properties MUST conform to the schema defined for the externalConnection. Required.
        Returns: Optional[properties.Properties]
        """
        return self._properties
    
    @properties.setter
    def properties(self,value: Optional[properties.Properties] = None) -> None:
        """
        Sets the properties property value. A property bag with the properties of the item. The properties MUST conform to the schema defined for the externalConnection. Required.
        Args:
            value: Value to set for the properties property.
        """
        self._properties = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("acl", self.acl)
        writer.write_collection_of_object_values("activities", self.activities)
        writer.write_object_value("content", self.content)
        writer.write_object_value("properties", self.properties)
    

