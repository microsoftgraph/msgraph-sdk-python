from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import attribute_definition_metadata_entry, attribute_type, mutability, referenced_object, string_key_string_value_pair

class AttributeDefinition(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new attributeDefinition and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The anchor property
        self._anchor: Optional[bool] = None
        # The apiExpressions property
        self._api_expressions: Optional[List[string_key_string_value_pair.StringKeyStringValuePair]] = None
        # The caseExact property
        self._case_exact: Optional[bool] = None
        # The defaultValue property
        self._default_value: Optional[str] = None
        # The flowNullValues property
        self._flow_null_values: Optional[bool] = None
        # The metadata property
        self._metadata: Optional[List[attribute_definition_metadata_entry.AttributeDefinitionMetadataEntry]] = None
        # The multivalued property
        self._multivalued: Optional[bool] = None
        # The mutability property
        self._mutability: Optional[mutability.Mutability] = None
        # The name property
        self._name: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The referencedObjects property
        self._referenced_objects: Optional[List[referenced_object.ReferencedObject]] = None
        # The required property
        self._required: Optional[bool] = None
        # The type property
        self._type: Optional[attribute_type.AttributeType] = None
    
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
    def anchor(self,) -> Optional[bool]:
        """
        Gets the anchor property value. The anchor property
        Returns: Optional[bool]
        """
        return self._anchor
    
    @anchor.setter
    def anchor(self,value: Optional[bool] = None) -> None:
        """
        Sets the anchor property value. The anchor property
        Args:
            value: Value to set for the anchor property.
        """
        self._anchor = value
    
    @property
    def api_expressions(self,) -> Optional[List[string_key_string_value_pair.StringKeyStringValuePair]]:
        """
        Gets the apiExpressions property value. The apiExpressions property
        Returns: Optional[List[string_key_string_value_pair.StringKeyStringValuePair]]
        """
        return self._api_expressions
    
    @api_expressions.setter
    def api_expressions(self,value: Optional[List[string_key_string_value_pair.StringKeyStringValuePair]] = None) -> None:
        """
        Sets the apiExpressions property value. The apiExpressions property
        Args:
            value: Value to set for the api_expressions property.
        """
        self._api_expressions = value
    
    @property
    def case_exact(self,) -> Optional[bool]:
        """
        Gets the caseExact property value. The caseExact property
        Returns: Optional[bool]
        """
        return self._case_exact
    
    @case_exact.setter
    def case_exact(self,value: Optional[bool] = None) -> None:
        """
        Sets the caseExact property value. The caseExact property
        Args:
            value: Value to set for the case_exact property.
        """
        self._case_exact = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AttributeDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AttributeDefinition
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AttributeDefinition()
    
    @property
    def default_value(self,) -> Optional[str]:
        """
        Gets the defaultValue property value. The defaultValue property
        Returns: Optional[str]
        """
        return self._default_value
    
    @default_value.setter
    def default_value(self,value: Optional[str] = None) -> None:
        """
        Sets the defaultValue property value. The defaultValue property
        Args:
            value: Value to set for the default_value property.
        """
        self._default_value = value
    
    @property
    def flow_null_values(self,) -> Optional[bool]:
        """
        Gets the flowNullValues property value. The flowNullValues property
        Returns: Optional[bool]
        """
        return self._flow_null_values
    
    @flow_null_values.setter
    def flow_null_values(self,value: Optional[bool] = None) -> None:
        """
        Sets the flowNullValues property value. The flowNullValues property
        Args:
            value: Value to set for the flow_null_values property.
        """
        self._flow_null_values = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import attribute_definition_metadata_entry, attribute_type, mutability, referenced_object, string_key_string_value_pair

        fields: Dict[str, Callable[[Any], None]] = {
            "anchor": lambda n : setattr(self, 'anchor', n.get_bool_value()),
            "apiExpressions": lambda n : setattr(self, 'api_expressions', n.get_collection_of_object_values(string_key_string_value_pair.StringKeyStringValuePair)),
            "caseExact": lambda n : setattr(self, 'case_exact', n.get_bool_value()),
            "defaultValue": lambda n : setattr(self, 'default_value', n.get_str_value()),
            "flowNullValues": lambda n : setattr(self, 'flow_null_values', n.get_bool_value()),
            "metadata": lambda n : setattr(self, 'metadata', n.get_collection_of_object_values(attribute_definition_metadata_entry.AttributeDefinitionMetadataEntry)),
            "multivalued": lambda n : setattr(self, 'multivalued', n.get_bool_value()),
            "mutability": lambda n : setattr(self, 'mutability', n.get_enum_value(mutability.Mutability)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "referencedObjects": lambda n : setattr(self, 'referenced_objects', n.get_collection_of_object_values(referenced_object.ReferencedObject)),
            "required": lambda n : setattr(self, 'required', n.get_bool_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(attribute_type.AttributeType)),
        }
        return fields
    
    @property
    def metadata(self,) -> Optional[List[attribute_definition_metadata_entry.AttributeDefinitionMetadataEntry]]:
        """
        Gets the metadata property value. The metadata property
        Returns: Optional[List[attribute_definition_metadata_entry.AttributeDefinitionMetadataEntry]]
        """
        return self._metadata
    
    @metadata.setter
    def metadata(self,value: Optional[List[attribute_definition_metadata_entry.AttributeDefinitionMetadataEntry]] = None) -> None:
        """
        Sets the metadata property value. The metadata property
        Args:
            value: Value to set for the metadata property.
        """
        self._metadata = value
    
    @property
    def multivalued(self,) -> Optional[bool]:
        """
        Gets the multivalued property value. The multivalued property
        Returns: Optional[bool]
        """
        return self._multivalued
    
    @multivalued.setter
    def multivalued(self,value: Optional[bool] = None) -> None:
        """
        Sets the multivalued property value. The multivalued property
        Args:
            value: Value to set for the multivalued property.
        """
        self._multivalued = value
    
    @property
    def mutability(self,) -> Optional[mutability.Mutability]:
        """
        Gets the mutability property value. The mutability property
        Returns: Optional[mutability.Mutability]
        """
        return self._mutability
    
    @mutability.setter
    def mutability(self,value: Optional[mutability.Mutability] = None) -> None:
        """
        Sets the mutability property value. The mutability property
        Args:
            value: Value to set for the mutability property.
        """
        self._mutability = value
    
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
    def referenced_objects(self,) -> Optional[List[referenced_object.ReferencedObject]]:
        """
        Gets the referencedObjects property value. The referencedObjects property
        Returns: Optional[List[referenced_object.ReferencedObject]]
        """
        return self._referenced_objects
    
    @referenced_objects.setter
    def referenced_objects(self,value: Optional[List[referenced_object.ReferencedObject]] = None) -> None:
        """
        Sets the referencedObjects property value. The referencedObjects property
        Args:
            value: Value to set for the referenced_objects property.
        """
        self._referenced_objects = value
    
    @property
    def required(self,) -> Optional[bool]:
        """
        Gets the required property value. The required property
        Returns: Optional[bool]
        """
        return self._required
    
    @required.setter
    def required(self,value: Optional[bool] = None) -> None:
        """
        Sets the required property value. The required property
        Args:
            value: Value to set for the required property.
        """
        self._required = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_bool_value("anchor", self.anchor)
        writer.write_collection_of_object_values("apiExpressions", self.api_expressions)
        writer.write_bool_value("caseExact", self.case_exact)
        writer.write_str_value("defaultValue", self.default_value)
        writer.write_bool_value("flowNullValues", self.flow_null_values)
        writer.write_collection_of_object_values("metadata", self.metadata)
        writer.write_bool_value("multivalued", self.multivalued)
        writer.write_enum_value("mutability", self.mutability)
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("referencedObjects", self.referenced_objects)
        writer.write_bool_value("required", self.required)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def type(self,) -> Optional[attribute_type.AttributeType]:
        """
        Gets the type property value. The type property
        Returns: Optional[attribute_type.AttributeType]
        """
        return self._type
    
    @type.setter
    def type(self,value: Optional[attribute_type.AttributeType] = None) -> None:
        """
        Sets the type property value. The type property
        Args:
            value: Value to set for the type property.
        """
        self._type = value
    

