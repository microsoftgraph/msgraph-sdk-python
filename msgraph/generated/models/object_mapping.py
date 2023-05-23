from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import attribute_mapping, filter, object_flow_types, object_mapping_metadata_entry

class ObjectMapping(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new objectMapping and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The attributeMappings property
        self._attribute_mappings: Optional[List[attribute_mapping.AttributeMapping]] = None
        # The enabled property
        self._enabled: Optional[bool] = None
        # The flowTypes property
        self._flow_types: Optional[object_flow_types.ObjectFlowTypes] = None
        # The metadata property
        self._metadata: Optional[List[object_mapping_metadata_entry.ObjectMappingMetadataEntry]] = None
        # The name property
        self._name: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The scope property
        self._scope: Optional[filter.Filter] = None
        # The sourceObjectName property
        self._source_object_name: Optional[str] = None
        # The targetObjectName property
        self._target_object_name: Optional[str] = None
    
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
    def attribute_mappings(self,) -> Optional[List[attribute_mapping.AttributeMapping]]:
        """
        Gets the attributeMappings property value. The attributeMappings property
        Returns: Optional[List[attribute_mapping.AttributeMapping]]
        """
        return self._attribute_mappings
    
    @attribute_mappings.setter
    def attribute_mappings(self,value: Optional[List[attribute_mapping.AttributeMapping]] = None) -> None:
        """
        Sets the attributeMappings property value. The attributeMappings property
        Args:
            value: Value to set for the attribute_mappings property.
        """
        self._attribute_mappings = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ObjectMapping:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ObjectMapping
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ObjectMapping()
    
    @property
    def enabled(self,) -> Optional[bool]:
        """
        Gets the enabled property value. The enabled property
        Returns: Optional[bool]
        """
        return self._enabled
    
    @enabled.setter
    def enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the enabled property value. The enabled property
        Args:
            value: Value to set for the enabled property.
        """
        self._enabled = value
    
    @property
    def flow_types(self,) -> Optional[object_flow_types.ObjectFlowTypes]:
        """
        Gets the flowTypes property value. The flowTypes property
        Returns: Optional[object_flow_types.ObjectFlowTypes]
        """
        return self._flow_types
    
    @flow_types.setter
    def flow_types(self,value: Optional[object_flow_types.ObjectFlowTypes] = None) -> None:
        """
        Sets the flowTypes property value. The flowTypes property
        Args:
            value: Value to set for the flow_types property.
        """
        self._flow_types = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import attribute_mapping, filter, object_flow_types, object_mapping_metadata_entry

        fields: Dict[str, Callable[[Any], None]] = {
            "attributeMappings": lambda n : setattr(self, 'attribute_mappings', n.get_collection_of_object_values(attribute_mapping.AttributeMapping)),
            "enabled": lambda n : setattr(self, 'enabled', n.get_bool_value()),
            "flowTypes": lambda n : setattr(self, 'flow_types', n.get_enum_value(object_flow_types.ObjectFlowTypes)),
            "metadata": lambda n : setattr(self, 'metadata', n.get_collection_of_object_values(object_mapping_metadata_entry.ObjectMappingMetadataEntry)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "scope": lambda n : setattr(self, 'scope', n.get_object_value(filter.Filter)),
            "sourceObjectName": lambda n : setattr(self, 'source_object_name', n.get_str_value()),
            "targetObjectName": lambda n : setattr(self, 'target_object_name', n.get_str_value()),
        }
        return fields
    
    @property
    def metadata(self,) -> Optional[List[object_mapping_metadata_entry.ObjectMappingMetadataEntry]]:
        """
        Gets the metadata property value. The metadata property
        Returns: Optional[List[object_mapping_metadata_entry.ObjectMappingMetadataEntry]]
        """
        return self._metadata
    
    @metadata.setter
    def metadata(self,value: Optional[List[object_mapping_metadata_entry.ObjectMappingMetadataEntry]] = None) -> None:
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
    def scope(self,) -> Optional[filter.Filter]:
        """
        Gets the scope property value. The scope property
        Returns: Optional[filter.Filter]
        """
        return self._scope
    
    @scope.setter
    def scope(self,value: Optional[filter.Filter] = None) -> None:
        """
        Sets the scope property value. The scope property
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
        writer.write_collection_of_object_values("attributeMappings", self.attribute_mappings)
        writer.write_bool_value("enabled", self.enabled)
        writer.write_enum_value("flowTypes", self.flow_types)
        writer.write_collection_of_object_values("metadata", self.metadata)
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("scope", self.scope)
        writer.write_str_value("sourceObjectName", self.source_object_name)
        writer.write_str_value("targetObjectName", self.target_object_name)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def source_object_name(self,) -> Optional[str]:
        """
        Gets the sourceObjectName property value. The sourceObjectName property
        Returns: Optional[str]
        """
        return self._source_object_name
    
    @source_object_name.setter
    def source_object_name(self,value: Optional[str] = None) -> None:
        """
        Sets the sourceObjectName property value. The sourceObjectName property
        Args:
            value: Value to set for the source_object_name property.
        """
        self._source_object_name = value
    
    @property
    def target_object_name(self,) -> Optional[str]:
        """
        Gets the targetObjectName property value. The targetObjectName property
        Returns: Optional[str]
        """
        return self._target_object_name
    
    @target_object_name.setter
    def target_object_name(self,value: Optional[str] = None) -> None:
        """
        Sets the targetObjectName property value. The targetObjectName property
        Args:
            value: Value to set for the target_object_name property.
        """
        self._target_object_name = value
    

