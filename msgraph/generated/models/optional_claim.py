from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class OptionalClaim(AdditionalDataHolder, Parsable):
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
    def additional_properties(self,) -> Optional[List[str]]:
        """
        Gets the additionalProperties property value. Additional properties of the claim. If a property exists in this collection, it modifies the behavior of the optional claim specified in the name property.
        Returns: Optional[List[str]]
        """
        return self._additional_properties
    
    @additional_properties.setter
    def additional_properties(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the additionalProperties property value. Additional properties of the claim. If a property exists in this collection, it modifies the behavior of the optional claim specified in the name property.
        Args:
            value: Value to set for the additionalProperties property.
        """
        self._additional_properties = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new optionalClaim and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Additional properties of the claim. If a property exists in this collection, it modifies the behavior of the optional claim specified in the name property.
        self._additional_properties: Optional[List[str]] = None
        # If the value is true, the claim specified by the client is necessary to ensure a smooth authorization experience for the specific task requested by the end user. The default value is false.
        self._essential: Optional[bool] = None
        # The name of the optional claim.
        self._name: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The source (directory object) of the claim. There are predefined claims and user-defined claims from extension properties. If the source value is null, the claim is a predefined optional claim. If the source value is user, the value in the name property is the extension property from the user object.
        self._source: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OptionalClaim:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OptionalClaim
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OptionalClaim()
    
    @property
    def essential(self,) -> Optional[bool]:
        """
        Gets the essential property value. If the value is true, the claim specified by the client is necessary to ensure a smooth authorization experience for the specific task requested by the end user. The default value is false.
        Returns: Optional[bool]
        """
        return self._essential
    
    @essential.setter
    def essential(self,value: Optional[bool] = None) -> None:
        """
        Sets the essential property value. If the value is true, the claim specified by the client is necessary to ensure a smooth authorization experience for the specific task requested by the end user. The default value is false.
        Args:
            value: Value to set for the essential property.
        """
        self._essential = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "additional_properties": lambda n : setattr(self, 'additional_properties', n.get_collection_of_primitive_values(str)),
            "essential": lambda n : setattr(self, 'essential', n.get_bool_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "source": lambda n : setattr(self, 'source', n.get_str_value()),
        }
        return fields
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. The name of the optional claim.
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. The name of the optional claim.
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
            value: Value to set for the OdataType property.
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
        writer.write_collection_of_primitive_values("additionalProperties", self.additional_properties)
        writer.write_bool_value("essential", self.essential)
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("source", self.source)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def source(self,) -> Optional[str]:
        """
        Gets the source property value. The source (directory object) of the claim. There are predefined claims and user-defined claims from extension properties. If the source value is null, the claim is a predefined optional claim. If the source value is user, the value in the name property is the extension property from the user object.
        Returns: Optional[str]
        """
        return self._source
    
    @source.setter
    def source(self,value: Optional[str] = None) -> None:
        """
        Sets the source property value. The source (directory object) of the claim. There are predefined claims and user-defined claims from extension properties. If the source value is null, the claim is a predefined optional claim. If the source value is user, the value in the name property is the extension property from the user object.
        Args:
            value: Value to set for the source property.
        """
        self._source = value
    

