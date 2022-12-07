from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
key_value = lazy_import('msgraph.generated.models.key_value')
group = lazy_import('msgraph.generated.models.term_store.group')
localized_name = lazy_import('msgraph.generated.models.term_store.localized_name')
relation = lazy_import('msgraph.generated.models.term_store.relation')
term = lazy_import('msgraph.generated.models.term_store.term')

class Set(entity.Entity):
    @property
    def children(self,) -> Optional[List[term.Term]]:
        """
        Gets the children property value. Children terms of set in term [store].
        Returns: Optional[List[term.Term]]
        """
        return self._children
    
    @children.setter
    def children(self,value: Optional[List[term.Term]] = None) -> None:
        """
        Sets the children property value. Children terms of set in term [store].
        Args:
            value: Value to set for the children property.
        """
        self._children = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new set and sets the default values.
        """
        super().__init__()
        # Children terms of set in term [store].
        self._children: Optional[List[term.Term]] = None
        # Date and time of set creation. Read-only.
        self._created_date_time: Optional[datetime] = None
        # Description that gives details on the term usage.
        self._description: Optional[str] = None
        # Name of the set for each languageTag.
        self._localized_names: Optional[List[localized_name.LocalizedName]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The parentGroup property
        self._parent_group: Optional[group.Group] = None
        # Custom properties for the set.
        self._properties: Optional[List[key_value.KeyValue]] = None
        # Indicates which terms have been pinned or reused directly under the set.
        self._relations: Optional[List[relation.Relation]] = None
        # All the terms under the set.
        self._terms: Optional[List[term.Term]] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. Date and time of set creation. Read-only.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. Date and time of set creation. Read-only.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Set:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Set
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Set()
    
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
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "children": lambda n : setattr(self, 'children', n.get_collection_of_object_values(term.Term)),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "localized_names": lambda n : setattr(self, 'localized_names', n.get_collection_of_object_values(localized_name.LocalizedName)),
            "parent_group": lambda n : setattr(self, 'parent_group', n.get_object_value(group.Group)),
            "properties": lambda n : setattr(self, 'properties', n.get_collection_of_object_values(key_value.KeyValue)),
            "relations": lambda n : setattr(self, 'relations', n.get_collection_of_object_values(relation.Relation)),
            "terms": lambda n : setattr(self, 'terms', n.get_collection_of_object_values(term.Term)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def localized_names(self,) -> Optional[List[localized_name.LocalizedName]]:
        """
        Gets the localizedNames property value. Name of the set for each languageTag.
        Returns: Optional[List[localized_name.LocalizedName]]
        """
        return self._localized_names
    
    @localized_names.setter
    def localized_names(self,value: Optional[List[localized_name.LocalizedName]] = None) -> None:
        """
        Sets the localizedNames property value. Name of the set for each languageTag.
        Args:
            value: Value to set for the localizedNames property.
        """
        self._localized_names = value
    
    @property
    def parent_group(self,) -> Optional[group.Group]:
        """
        Gets the parentGroup property value. The parentGroup property
        Returns: Optional[group.Group]
        """
        return self._parent_group
    
    @parent_group.setter
    def parent_group(self,value: Optional[group.Group] = None) -> None:
        """
        Sets the parentGroup property value. The parentGroup property
        Args:
            value: Value to set for the parentGroup property.
        """
        self._parent_group = value
    
    @property
    def properties(self,) -> Optional[List[key_value.KeyValue]]:
        """
        Gets the properties property value. Custom properties for the set.
        Returns: Optional[List[key_value.KeyValue]]
        """
        return self._properties
    
    @properties.setter
    def properties(self,value: Optional[List[key_value.KeyValue]] = None) -> None:
        """
        Sets the properties property value. Custom properties for the set.
        Args:
            value: Value to set for the properties property.
        """
        self._properties = value
    
    @property
    def relations(self,) -> Optional[List[relation.Relation]]:
        """
        Gets the relations property value. Indicates which terms have been pinned or reused directly under the set.
        Returns: Optional[List[relation.Relation]]
        """
        return self._relations
    
    @relations.setter
    def relations(self,value: Optional[List[relation.Relation]] = None) -> None:
        """
        Sets the relations property value. Indicates which terms have been pinned or reused directly under the set.
        Args:
            value: Value to set for the relations property.
        """
        self._relations = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("children", self.children)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_collection_of_object_values("localizedNames", self.localized_names)
        writer.write_object_value("parentGroup", self.parent_group)
        writer.write_collection_of_object_values("properties", self.properties)
        writer.write_collection_of_object_values("relations", self.relations)
        writer.write_collection_of_object_values("terms", self.terms)
    
    @property
    def terms(self,) -> Optional[List[term.Term]]:
        """
        Gets the terms property value. All the terms under the set.
        Returns: Optional[List[term.Term]]
        """
        return self._terms
    
    @terms.setter
    def terms(self,value: Optional[List[term.Term]] = None) -> None:
        """
        Sets the terms property value. All the terms under the set.
        Args:
            value: Value to set for the terms property.
        """
        self._terms = value
    

