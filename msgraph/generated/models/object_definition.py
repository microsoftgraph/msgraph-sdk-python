from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import attribute_definition, object_definition_metadata_entry

class ObjectDefinition(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new objectDefinition and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The attributes property
        self._attributes: Optional[List[attribute_definition.AttributeDefinition]] = None
        # The metadata property
        self._metadata: Optional[List[object_definition_metadata_entry.ObjectDefinitionMetadataEntry]] = None
        # The name property
        self._name: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The supportedApis property
        self._supported_apis: Optional[List[str]] = None
    
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
    def attributes(self,) -> Optional[List[attribute_definition.AttributeDefinition]]:
        """
        Gets the attributes property value. The attributes property
        Returns: Optional[List[attribute_definition.AttributeDefinition]]
        """
        return self._attributes
    
    @attributes.setter
    def attributes(self,value: Optional[List[attribute_definition.AttributeDefinition]] = None) -> None:
        """
        Sets the attributes property value. The attributes property
        Args:
            value: Value to set for the attributes property.
        """
        self._attributes = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ObjectDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ObjectDefinition
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ObjectDefinition()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import attribute_definition, object_definition_metadata_entry

        fields: Dict[str, Callable[[Any], None]] = {
            "attributes": lambda n : setattr(self, 'attributes', n.get_collection_of_object_values(attribute_definition.AttributeDefinition)),
            "metadata": lambda n : setattr(self, 'metadata', n.get_collection_of_object_values(object_definition_metadata_entry.ObjectDefinitionMetadataEntry)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "supportedApis": lambda n : setattr(self, 'supported_apis', n.get_collection_of_primitive_values(str)),
        }
        return fields
    
    @property
    def metadata(self,) -> Optional[List[object_definition_metadata_entry.ObjectDefinitionMetadataEntry]]:
        """
        Gets the metadata property value. The metadata property
        Returns: Optional[List[object_definition_metadata_entry.ObjectDefinitionMetadataEntry]]
        """
        return self._metadata
    
    @metadata.setter
    def metadata(self,value: Optional[List[object_definition_metadata_entry.ObjectDefinitionMetadataEntry]] = None) -> None:
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_object_values("attributes", self.attributes)
        writer.write_collection_of_object_values("metadata", self.metadata)
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_primitive_values("supportedApis", self.supported_apis)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def supported_apis(self,) -> Optional[List[str]]:
        """
        Gets the supportedApis property value. The supportedApis property
        Returns: Optional[List[str]]
        """
        return self._supported_apis
    
    @supported_apis.setter
    def supported_apis(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the supportedApis property value. The supportedApis property
        Args:
            value: Value to set for the supported_apis property.
        """
        self._supported_apis = value
    

