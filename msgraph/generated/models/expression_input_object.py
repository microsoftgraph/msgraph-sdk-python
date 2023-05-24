from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import object_definition, string_key_object_value_pair

class ExpressionInputObject(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new expressionInputObject and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The definition property
        self._definition: Optional[object_definition.ObjectDefinition] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The properties property
        self._properties: Optional[List[string_key_object_value_pair.StringKeyObjectValuePair]] = None
    
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ExpressionInputObject:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ExpressionInputObject
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ExpressionInputObject()
    
    @property
    def definition(self,) -> Optional[object_definition.ObjectDefinition]:
        """
        Gets the definition property value. The definition property
        Returns: Optional[object_definition.ObjectDefinition]
        """
        return self._definition
    
    @definition.setter
    def definition(self,value: Optional[object_definition.ObjectDefinition] = None) -> None:
        """
        Sets the definition property value. The definition property
        Args:
            value: Value to set for the definition property.
        """
        self._definition = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import object_definition, string_key_object_value_pair

        fields: Dict[str, Callable[[Any], None]] = {
            "definition": lambda n : setattr(self, 'definition', n.get_object_value(object_definition.ObjectDefinition)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "properties": lambda n : setattr(self, 'properties', n.get_collection_of_object_values(string_key_object_value_pair.StringKeyObjectValuePair)),
        }
        return fields
    
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
    def properties(self,) -> Optional[List[string_key_object_value_pair.StringKeyObjectValuePair]]:
        """
        Gets the properties property value. The properties property
        Returns: Optional[List[string_key_object_value_pair.StringKeyObjectValuePair]]
        """
        return self._properties
    
    @properties.setter
    def properties(self,value: Optional[List[string_key_object_value_pair.StringKeyObjectValuePair]] = None) -> None:
        """
        Sets the properties property value. The properties property
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
        writer.write_object_value("definition", self.definition)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("properties", self.properties)
        writer.write_additional_data_value(self.additional_data)
    

