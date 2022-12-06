from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class PrivacyProfile(AdditionalDataHolder, Parsable):
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
        Instantiates a new privacyProfile and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # A valid smtp email address for the privacy statement contact. Not required.
        self._contact_email: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # A valid URL format that begins with http:// or https://. Maximum length is 255 characters. The URL that directs to the company's privacy statement. Not required.
        self._statement_url: Optional[str] = None
    
    @property
    def contact_email(self,) -> Optional[str]:
        """
        Gets the contactEmail property value. A valid smtp email address for the privacy statement contact. Not required.
        Returns: Optional[str]
        """
        return self._contact_email
    
    @contact_email.setter
    def contact_email(self,value: Optional[str] = None) -> None:
        """
        Sets the contactEmail property value. A valid smtp email address for the privacy statement contact. Not required.
        Args:
            value: Value to set for the contactEmail property.
        """
        self._contact_email = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PrivacyProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PrivacyProfile
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PrivacyProfile()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "contact_email": lambda n : setattr(self, 'contact_email', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "statement_url": lambda n : setattr(self, 'statement_url', n.get_str_value()),
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
        writer.write_str_value("contactEmail", self.contact_email)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("statementUrl", self.statement_url)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def statement_url(self,) -> Optional[str]:
        """
        Gets the statementUrl property value. A valid URL format that begins with http:// or https://. Maximum length is 255 characters. The URL that directs to the company's privacy statement. Not required.
        Returns: Optional[str]
        """
        return self._statement_url
    
    @statement_url.setter
    def statement_url(self,value: Optional[str] = None) -> None:
        """
        Sets the statementUrl property value. A valid URL format that begins with http:// or https://. Maximum length is 255 characters. The URL that directs to the company's privacy statement. Not required.
        Args:
            value: Value to set for the statementUrl property.
        """
        self._statement_url = value
    

