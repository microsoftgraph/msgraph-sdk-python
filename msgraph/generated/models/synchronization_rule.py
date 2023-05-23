from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import container_filter, group_filter, object_mapping, string_key_string_value_pair

class SynchronizationRule(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new synchronizationRule and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The containerFilter property
        self._container_filter: Optional[container_filter.ContainerFilter] = None
        # The editable property
        self._editable: Optional[bool] = None
        # The groupFilter property
        self._group_filter: Optional[group_filter.GroupFilter] = None
        # The id property
        self._id: Optional[str] = None
        # The metadata property
        self._metadata: Optional[List[string_key_string_value_pair.StringKeyStringValuePair]] = None
        # The name property
        self._name: Optional[str] = None
        # The objectMappings property
        self._object_mappings: Optional[List[object_mapping.ObjectMapping]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The priority property
        self._priority: Optional[int] = None
        # The sourceDirectoryName property
        self._source_directory_name: Optional[str] = None
        # The targetDirectoryName property
        self._target_directory_name: Optional[str] = None
    
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def container_filter(self,) -> Optional[container_filter.ContainerFilter]:
        """
        Gets the containerFilter property value. The containerFilter property
        Returns: Optional[container_filter.ContainerFilter]
        """
        return self._container_filter
    
    @container_filter.setter
    def container_filter(self,value: Optional[container_filter.ContainerFilter] = None) -> None:
        """
        Sets the containerFilter property value. The containerFilter property
        Args:
            value: Value to set for the container_filter property.
        """
        self._container_filter = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SynchronizationRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SynchronizationRule
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SynchronizationRule()
    
    @property
    def editable(self,) -> Optional[bool]:
        """
        Gets the editable property value. The editable property
        Returns: Optional[bool]
        """
        return self._editable
    
    @editable.setter
    def editable(self,value: Optional[bool] = None) -> None:
        """
        Sets the editable property value. The editable property
        Args:
            value: Value to set for the editable property.
        """
        self._editable = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import container_filter, group_filter, object_mapping, string_key_string_value_pair

        fields: Dict[str, Callable[[Any], None]] = {
            "containerFilter": lambda n : setattr(self, 'container_filter', n.get_object_value(container_filter.ContainerFilter)),
            "editable": lambda n : setattr(self, 'editable', n.get_bool_value()),
            "groupFilter": lambda n : setattr(self, 'group_filter', n.get_object_value(group_filter.GroupFilter)),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "metadata": lambda n : setattr(self, 'metadata', n.get_collection_of_object_values(string_key_string_value_pair.StringKeyStringValuePair)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "objectMappings": lambda n : setattr(self, 'object_mappings', n.get_collection_of_object_values(object_mapping.ObjectMapping)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "priority": lambda n : setattr(self, 'priority', n.get_int_value()),
            "sourceDirectoryName": lambda n : setattr(self, 'source_directory_name', n.get_str_value()),
            "targetDirectoryName": lambda n : setattr(self, 'target_directory_name', n.get_str_value()),
        }
        return fields
    
    @property
    def group_filter(self,) -> Optional[group_filter.GroupFilter]:
        """
        Gets the groupFilter property value. The groupFilter property
        Returns: Optional[group_filter.GroupFilter]
        """
        return self._group_filter
    
    @group_filter.setter
    def group_filter(self,value: Optional[group_filter.GroupFilter] = None) -> None:
        """
        Sets the groupFilter property value. The groupFilter property
        Args:
            value: Value to set for the group_filter property.
        """
        self._group_filter = value
    
    @property
    def id(self,) -> Optional[str]:
        """
        Gets the id property value. The id property
        Returns: Optional[str]
        """
        return self._id
    
    @id.setter
    def id(self,value: Optional[str] = None) -> None:
        """
        Sets the id property value. The id property
        Args:
            value: Value to set for the id property.
        """
        self._id = value
    
    @property
    def metadata(self,) -> Optional[List[string_key_string_value_pair.StringKeyStringValuePair]]:
        """
        Gets the metadata property value. The metadata property
        Returns: Optional[List[string_key_string_value_pair.StringKeyStringValuePair]]
        """
        return self._metadata
    
    @metadata.setter
    def metadata(self,value: Optional[List[string_key_string_value_pair.StringKeyStringValuePair]] = None) -> None:
        """
        Sets the metadata property value. The metadata property
        Args:
            value: Value to set for the metadata property.
        """
        self._metadata = value
    
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
    
    @property
    def object_mappings(self,) -> Optional[List[object_mapping.ObjectMapping]]:
        """
        Gets the objectMappings property value. The objectMappings property
        Returns: Optional[List[object_mapping.ObjectMapping]]
        """
        return self._object_mappings
    
    @object_mappings.setter
    def object_mappings(self,value: Optional[List[object_mapping.ObjectMapping]] = None) -> None:
        """
        Sets the objectMappings property value. The objectMappings property
        Args:
            value: Value to set for the object_mappings property.
        """
        self._object_mappings = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    @property
    def priority(self,) -> Optional[int]:
        """
        Gets the priority property value. The priority property
        Returns: Optional[int]
        """
        return self._priority
    
    @priority.setter
    def priority(self,value: Optional[int] = None) -> None:
        """
        Sets the priority property value. The priority property
        Args:
            value: Value to set for the priority property.
        """
        self._priority = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("containerFilter", self.container_filter)
        writer.write_bool_value("editable", self.editable)
        writer.write_object_value("groupFilter", self.group_filter)
        writer.write_str_value("id", self.id)
        writer.write_collection_of_object_values("metadata", self.metadata)
        writer.write_str_value("name", self.name)
        writer.write_collection_of_object_values("objectMappings", self.object_mappings)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("priority", self.priority)
        writer.write_str_value("sourceDirectoryName", self.source_directory_name)
        writer.write_str_value("targetDirectoryName", self.target_directory_name)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def source_directory_name(self,) -> Optional[str]:
        """
        Gets the sourceDirectoryName property value. The sourceDirectoryName property
        Returns: Optional[str]
        """
        return self._source_directory_name
    
    @source_directory_name.setter
    def source_directory_name(self,value: Optional[str] = None) -> None:
        """
        Sets the sourceDirectoryName property value. The sourceDirectoryName property
        Args:
            value: Value to set for the source_directory_name property.
        """
        self._source_directory_name = value
    
    @property
    def target_directory_name(self,) -> Optional[str]:
        """
        Gets the targetDirectoryName property value. The targetDirectoryName property
        Returns: Optional[str]
        """
        return self._target_directory_name
    
    @target_directory_name.setter
    def target_directory_name(self,value: Optional[str] = None) -> None:
        """
        Sets the targetDirectoryName property value. The targetDirectoryName property
        Args:
            value: Value to set for the target_directory_name property.
        """
        self._target_directory_name = value
    

