from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class AlternativeSecurityId(AdditionalDataHolder, Parsable):
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new alternativeSecurityId and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # For internal use only
        self._identity_provider: Optional[str] = None
        # For internal use only
        self._key: Optional[bytes] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # For internal use only
        self._type: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AlternativeSecurityId:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AlternativeSecurityId
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AlternativeSecurityId()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "identity_provider": lambda n : setattr(self, 'identity_provider', n.get_str_value()),
            "key": lambda n : setattr(self, 'key', n.get_bytes_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_int_value()),
        }
        return fields
    
    @property
    def identity_provider(self,) -> Optional[str]:
        """
        Gets the identityProvider property value. For internal use only
        Returns: Optional[str]
        """
        return self._identity_provider
    
    @identity_provider.setter
    def identity_provider(self,value: Optional[str] = None) -> None:
        """
        Sets the identityProvider property value. For internal use only
        Args:
            value: Value to set for the identityProvider property.
        """
        self._identity_provider = value
    
    @property
    def key(self,) -> Optional[bytes]:
        """
        Gets the key property value. For internal use only
        Returns: Optional[bytes]
        """
        return self._key
    
    @key.setter
    def key(self,value: Optional[bytes] = None) -> None:
        """
        Sets the key property value. For internal use only
        Args:
            value: Value to set for the key property.
        """
        self._key = value
    
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
        writer.write_str_value("identityProvider", self.identity_provider)
        writer.write_object_value("key", self.key)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def type(self,) -> Optional[int]:
        """
        Gets the type property value. For internal use only
        Returns: Optional[int]
        """
        return self._type
    
    @type.setter
    def type(self,value: Optional[int] = None) -> None:
        """
        Sets the type property value. For internal use only
        Args:
            value: Value to set for the type property.
        """
        self._type = value
    

