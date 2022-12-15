from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class EmailSender(AdditionalDataHolder, Parsable):
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
        Instantiates a new emailSender and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The name of the sender.
        self._display_name: Optional[str] = None
        # Sender domain.
        self._domain_name: Optional[str] = None
        # Sender email address.
        self._email_address: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EmailSender:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EmailSender
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EmailSender()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The name of the sender.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The name of the sender.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def domain_name(self,) -> Optional[str]:
        """
        Gets the domainName property value. Sender domain.
        Returns: Optional[str]
        """
        return self._domain_name
    
    @domain_name.setter
    def domain_name(self,value: Optional[str] = None) -> None:
        """
        Sets the domainName property value. Sender domain.
        Args:
            value: Value to set for the domainName property.
        """
        self._domain_name = value
    
    @property
    def email_address(self,) -> Optional[str]:
        """
        Gets the emailAddress property value. Sender email address.
        Returns: Optional[str]
        """
        return self._email_address
    
    @email_address.setter
    def email_address(self,value: Optional[str] = None) -> None:
        """
        Sets the emailAddress property value. Sender email address.
        Args:
            value: Value to set for the emailAddress property.
        """
        self._email_address = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "domain_name": lambda n : setattr(self, 'domain_name', n.get_str_value()),
            "email_address": lambda n : setattr(self, 'email_address', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("domainName", self.domain_name)
        writer.write_str_value("emailAddress", self.email_address)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

