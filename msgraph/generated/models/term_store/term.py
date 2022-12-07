from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
key_value = lazy_import('msgraph.generated.models.key_value')
localized_description = lazy_import('msgraph.generated.models.term_store.localized_description')
localized_label = lazy_import('msgraph.generated.models.term_store.localized_label')
relation = lazy_import('msgraph.generated.models.term_store.relation')
set = lazy_import('msgraph.generated.models.term_store.set')

class Term(entity.Entity):
    @property
    def children(self,) -> Optional[List[Term]]:
        """
        Gets the children property value. Children of current term.
        Returns: Optional[List[Term]]
        """
        return self._children
    
    @children.setter
    def children(self,value: Optional[List[Term]] = None) -> None:
        """
        Sets the children property value. Children of current term.
        Args:
            value: Value to set for the children property.
        """
        self._children = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new term and sets the default values.
        """
        super().__init__()
        # Children of current term.
        self._children: Optional[List[Term]] = None
        # Date and time of term creation. Read-only.
        self._created_date_time: Optional[datetime] = None
        # Description about term that is dependent on the languageTag.
        self._descriptions: Optional[List[localized_description.LocalizedDescription]] = None
        # Label metadata for a term.
        self._labels: Optional[List[localized_label.LocalizedLabel]] = None
        # Last date and time of term modification. Read-only.
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Collection of properties on the term.
        self._properties: Optional[List[key_value.KeyValue]] = None
        # To indicate which terms are related to the current term as either pinned or reused.
        self._relations: Optional[List[relation.Relation]] = None
        # The [set] in which the term is created.
        self._set: Optional[set.Set] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. Date and time of term creation. Read-only.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. Date and time of term creation. Read-only.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Term:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Term
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Term()
    
    @property
    def descriptions(self,) -> Optional[List[localized_description.LocalizedDescription]]:
        """
        Gets the descriptions property value. Description about term that is dependent on the languageTag.
        Returns: Optional[List[localized_description.LocalizedDescription]]
        """
        return self._descriptions
    
    @descriptions.setter
    def descriptions(self,value: Optional[List[localized_description.LocalizedDescription]] = None) -> None:
        """
        Sets the descriptions property value. Description about term that is dependent on the languageTag.
        Args:
            value: Value to set for the descriptions property.
        """
        self._descriptions = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "children": lambda n : setattr(self, 'children', n.get_collection_of_object_values(Term)),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "descriptions": lambda n : setattr(self, 'descriptions', n.get_collection_of_object_values(localized_description.LocalizedDescription)),
            "labels": lambda n : setattr(self, 'labels', n.get_collection_of_object_values(localized_label.LocalizedLabel)),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "properties": lambda n : setattr(self, 'properties', n.get_collection_of_object_values(key_value.KeyValue)),
            "relations": lambda n : setattr(self, 'relations', n.get_collection_of_object_values(relation.Relation)),
            "set": lambda n : setattr(self, 'set', n.get_object_value(set.Set)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def labels(self,) -> Optional[List[localized_label.LocalizedLabel]]:
        """
        Gets the labels property value. Label metadata for a term.
        Returns: Optional[List[localized_label.LocalizedLabel]]
        """
        return self._labels
    
    @labels.setter
    def labels(self,value: Optional[List[localized_label.LocalizedLabel]] = None) -> None:
        """
        Sets the labels property value. Label metadata for a term.
        Args:
            value: Value to set for the labels property.
        """
        self._labels = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. Last date and time of term modification. Read-only.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. Last date and time of term modification. Read-only.
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    @property
    def properties(self,) -> Optional[List[key_value.KeyValue]]:
        """
        Gets the properties property value. Collection of properties on the term.
        Returns: Optional[List[key_value.KeyValue]]
        """
        return self._properties
    
    @properties.setter
    def properties(self,value: Optional[List[key_value.KeyValue]] = None) -> None:
        """
        Sets the properties property value. Collection of properties on the term.
        Args:
            value: Value to set for the properties property.
        """
        self._properties = value
    
    @property
    def relations(self,) -> Optional[List[relation.Relation]]:
        """
        Gets the relations property value. To indicate which terms are related to the current term as either pinned or reused.
        Returns: Optional[List[relation.Relation]]
        """
        return self._relations
    
    @relations.setter
    def relations(self,value: Optional[List[relation.Relation]] = None) -> None:
        """
        Sets the relations property value. To indicate which terms are related to the current term as either pinned or reused.
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
        writer.write_collection_of_object_values("descriptions", self.descriptions)
        writer.write_collection_of_object_values("labels", self.labels)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_collection_of_object_values("properties", self.properties)
        writer.write_collection_of_object_values("relations", self.relations)
        writer.write_object_value("set", self.set)
    
    @property
    def set(self,) -> Optional[set.Set]:
        """
        Gets the set property value. The [set] in which the term is created.
        Returns: Optional[set.Set]
        """
        return self._set
    
    @set.setter
    def set(self,value: Optional[set.Set] = None) -> None:
        """
        Sets the set property value. The [set] in which the term is created.
        Args:
            value: Value to set for the set property.
        """
        self._set = value
    

