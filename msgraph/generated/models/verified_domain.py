from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class VerifiedDomain(AdditionalDataHolder, Parsable):
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
    def capabilities(self,) -> Optional[str]:
        """
        Gets the capabilities property value. For example, Email, OfficeCommunicationsOnline.
        Returns: Optional[str]
        """
        return self._capabilities
    
    @capabilities.setter
    def capabilities(self,value: Optional[str] = None) -> None:
        """
        Sets the capabilities property value. For example, Email, OfficeCommunicationsOnline.
        Args:
            value: Value to set for the capabilities property.
        """
        self._capabilities = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new verifiedDomain and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # For example, Email, OfficeCommunicationsOnline.
        self._capabilities: Optional[str] = None
        # true if this is the default domain associated with the tenant; otherwise, false.
        self._is_default: Optional[bool] = None
        # true if this is the initial domain associated with the tenant; otherwise, false.
        self._is_initial: Optional[bool] = None
        # The domain name; for example, contoso.onmicrosoft.com.
        self._name: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # For example, Managed.
        self._type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> VerifiedDomain:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: VerifiedDomain
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return VerifiedDomain()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "capabilities": lambda n : setattr(self, 'capabilities', n.get_str_value()),
            "is_default": lambda n : setattr(self, 'is_default', n.get_bool_value()),
            "is_initial": lambda n : setattr(self, 'is_initial', n.get_bool_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
        }
        return fields
    
    @property
    def is_default(self,) -> Optional[bool]:
        """
        Gets the isDefault property value. true if this is the default domain associated with the tenant; otherwise, false.
        Returns: Optional[bool]
        """
        return self._is_default
    
    @is_default.setter
    def is_default(self,value: Optional[bool] = None) -> None:
        """
        Sets the isDefault property value. true if this is the default domain associated with the tenant; otherwise, false.
        Args:
            value: Value to set for the isDefault property.
        """
        self._is_default = value
    
    @property
    def is_initial(self,) -> Optional[bool]:
        """
        Gets the isInitial property value. true if this is the initial domain associated with the tenant; otherwise, false.
        Returns: Optional[bool]
        """
        return self._is_initial
    
    @is_initial.setter
    def is_initial(self,value: Optional[bool] = None) -> None:
        """
        Sets the isInitial property value. true if this is the initial domain associated with the tenant; otherwise, false.
        Args:
            value: Value to set for the isInitial property.
        """
        self._is_initial = value
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. The domain name; for example, contoso.onmicrosoft.com.
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. The domain name; for example, contoso.onmicrosoft.com.
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
        writer.write_str_value("capabilities", self.capabilities)
        writer.write_bool_value("isDefault", self.is_default)
        writer.write_bool_value("isInitial", self.is_initial)
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def type(self,) -> Optional[str]:
        """
        Gets the type property value. For example, Managed.
        Returns: Optional[str]
        """
        return self._type
    
    @type.setter
    def type(self,value: Optional[str] = None) -> None:
        """
        Sets the type property value. For example, Managed.
        Args:
            value: Value to set for the type property.
        """
        self._type = value
    

