from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import set, term_group_scope
    from .. import entity

from .. import entity

class Group(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new group and sets the default values.
        """
        super().__init__()
        # Date and time of the group creation. Read-only.
        self._created_date_time: Optional[datetime] = None
        # Description that gives details on the term usage.
        self._description: Optional[str] = None
        # Name of the group.
        self._display_name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # ID of the parent site of this group.
        self._parent_site_id: Optional[str] = None
        # Returns the type of the group. Possible values are: global, system, and siteCollection.
        self._scope: Optional[term_group_scope.TermGroupScope] = None
        # All sets under the group in a term [store].
        self._sets: Optional[List[set.Set]] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. Date and time of the group creation. Read-only.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. Date and time of the group creation. Read-only.
        Args:
            value: Value to set for the created_date_time property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Group:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Group
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Group()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Description that gives details on the term usage.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Description that gives details on the term usage.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Name of the group.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Name of the group.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import set, term_group_scope
        from .. import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "parentSiteId": lambda n : setattr(self, 'parent_site_id', n.get_str_value()),
            "scope": lambda n : setattr(self, 'scope', n.get_enum_value(term_group_scope.TermGroupScope)),
            "sets": lambda n : setattr(self, 'sets', n.get_collection_of_object_values(set.Set)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def parent_site_id(self,) -> Optional[str]:
        """
        Gets the parentSiteId property value. ID of the parent site of this group.
        Returns: Optional[str]
        """
        return self._parent_site_id
    
    @parent_site_id.setter
    def parent_site_id(self,value: Optional[str] = None) -> None:
        """
        Sets the parentSiteId property value. ID of the parent site of this group.
        Args:
            value: Value to set for the parent_site_id property.
        """
        self._parent_site_id = value
    
    @property
    def scope(self,) -> Optional[term_group_scope.TermGroupScope]:
        """
        Gets the scope property value. Returns the type of the group. Possible values are: global, system, and siteCollection.
        Returns: Optional[term_group_scope.TermGroupScope]
        """
        return self._scope
    
    @scope.setter
    def scope(self,value: Optional[term_group_scope.TermGroupScope] = None) -> None:
        """
        Sets the scope property value. Returns the type of the group. Possible values are: global, system, and siteCollection.
        Args:
            value: Value to set for the scope property.
        """
        self._scope = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("parentSiteId", self.parent_site_id)
        writer.write_enum_value("scope", self.scope)
        writer.write_collection_of_object_values("sets", self.sets)
    
    @property
    def sets(self,) -> Optional[List[set.Set]]:
        """
        Gets the sets property value. All sets under the group in a term [store].
        Returns: Optional[List[set.Set]]
        """
        return self._sets
    
    @sets.setter
    def sets(self,value: Optional[List[set.Set]] = None) -> None:
        """
        Sets the sets property value. All sets under the group in a term [store].
        Args:
            value: Value to set for the sets property.
        """
        self._sets = value
    

