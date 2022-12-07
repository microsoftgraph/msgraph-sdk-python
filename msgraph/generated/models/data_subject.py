from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class DataSubject(AdditionalDataHolder, Parsable):
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
        Instantiates a new dataSubject and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Email of the data subject.
        self._email: Optional[str] = None
        # First name of the data subject.
        self._first_name: Optional[str] = None
        # Last Name of the data subject.
        self._last_name: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The country/region of residency. The residency information is uesed only for internal reporting but not for the content search.
        self._residency: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DataSubject:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DataSubject
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DataSubject()
    
    @property
    def email(self,) -> Optional[str]:
        """
        Gets the email property value. Email of the data subject.
        Returns: Optional[str]
        """
        return self._email
    
    @email.setter
    def email(self,value: Optional[str] = None) -> None:
        """
        Sets the email property value. Email of the data subject.
        Args:
            value: Value to set for the email property.
        """
        self._email = value
    
    @property
    def first_name(self,) -> Optional[str]:
        """
        Gets the firstName property value. First name of the data subject.
        Returns: Optional[str]
        """
        return self._first_name
    
    @first_name.setter
    def first_name(self,value: Optional[str] = None) -> None:
        """
        Sets the firstName property value. First name of the data subject.
        Args:
            value: Value to set for the firstName property.
        """
        self._first_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "first_name": lambda n : setattr(self, 'first_name', n.get_str_value()),
            "last_name": lambda n : setattr(self, 'last_name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "residency": lambda n : setattr(self, 'residency', n.get_str_value()),
        }
        return fields
    
    @property
    def last_name(self,) -> Optional[str]:
        """
        Gets the lastName property value. Last Name of the data subject.
        Returns: Optional[str]
        """
        return self._last_name
    
    @last_name.setter
    def last_name(self,value: Optional[str] = None) -> None:
        """
        Sets the lastName property value. Last Name of the data subject.
        Args:
            value: Value to set for the lastName property.
        """
        self._last_name = value
    
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
    
    @property
    def residency(self,) -> Optional[str]:
        """
        Gets the residency property value. The country/region of residency. The residency information is uesed only for internal reporting but not for the content search.
        Returns: Optional[str]
        """
        return self._residency
    
    @residency.setter
    def residency(self,value: Optional[str] = None) -> None:
        """
        Sets the residency property value. The country/region of residency. The residency information is uesed only for internal reporting but not for the content search.
        Args:
            value: Value to set for the residency property.
        """
        self._residency = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("email", self.email)
        writer.write_str_value("firstName", self.first_name)
        writer.write_str_value("lastName", self.last_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("residency", self.residency)
        writer.write_additional_data_value(self.additional_data)
    

