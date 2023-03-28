from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class AccessPackageLocalizedText(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new accessPackageLocalizedText and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The language code that text is in. For example, 'en-us'. The language component follows 2-letter codes as defined in ISO 639-1, and the country component follows 2-letter codes as defined in ISO 3166-1 alpha-2. Required.
        self._language_code: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The question in the specific language. Required.
        self._text: Optional[str] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessPackageLocalizedText:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageLocalizedText
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AccessPackageLocalizedText()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "languageCode": lambda n : setattr(self, 'language_code', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "text": lambda n : setattr(self, 'text', n.get_str_value()),
        }
        return fields
    
    @property
    def language_code(self,) -> Optional[str]:
        """
        Gets the languageCode property value. The language code that text is in. For example, 'en-us'. The language component follows 2-letter codes as defined in ISO 639-1, and the country component follows 2-letter codes as defined in ISO 3166-1 alpha-2. Required.
        Returns: Optional[str]
        """
        return self._language_code
    
    @language_code.setter
    def language_code(self,value: Optional[str] = None) -> None:
        """
        Sets the languageCode property value. The language code that text is in. For example, 'en-us'. The language component follows 2-letter codes as defined in ISO 639-1, and the country component follows 2-letter codes as defined in ISO 3166-1 alpha-2. Required.
        Args:
            value: Value to set for the language_code property.
        """
        self._language_code = value
    
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
        writer.write_str_value("languageCode", self.language_code)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("text", self.text)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def text(self,) -> Optional[str]:
        """
        Gets the text property value. The question in the specific language. Required.
        Returns: Optional[str]
        """
        return self._text
    
    @text.setter
    def text(self,value: Optional[str] = None) -> None:
        """
        Sets the text property value. The question in the specific language. Required.
        Args:
            value: Value to set for the text property.
        """
        self._text = value
    

