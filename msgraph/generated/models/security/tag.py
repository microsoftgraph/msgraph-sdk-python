from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import ediscovery_review_tag
    from .. import entity, identity_set

from .. import entity

class Tag(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new tag and sets the default values.
        """
        super().__init__()
        # The createdBy property
        self._created_by: Optional[identity_set.IdentitySet] = None
        # The description property
        self._description: Optional[str] = None
        # The displayName property
        self._display_name: Optional[str] = None
        # The lastModifiedDateTime property
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @property
    def created_by(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the createdBy property value. The createdBy property
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._created_by
    
    @created_by.setter
    def created_by(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the createdBy property value. The createdBy property
        Args:
            value: Value to set for the created_by property.
        """
        self._created_by = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Tag:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Tag
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.security.ediscoveryReviewTag":
                from . import ediscovery_review_tag

                return ediscovery_review_tag.EdiscoveryReviewTag()
        return Tag()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The description property
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The description property
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The displayName property
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The displayName property
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import ediscovery_review_tag
        from .. import entity, identity_set

        fields: Dict[str, Callable[[Any], None]] = {
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(identity_set.IdentitySet)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
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
            value: Value to set for the last_modified_date_time property.
        """
        self._last_modified_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
    

