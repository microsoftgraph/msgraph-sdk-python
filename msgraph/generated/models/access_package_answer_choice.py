from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import access_package_localized_text

class AccessPackageAnswerChoice(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new accessPackageAnswerChoice and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The actual value of the selected choice. This is typically a string value which is understandable by applications. Required.
        self._actual_value: Optional[str] = None
        # The text of the answer choice represented in a format for a specific locale.
        self._localizations: Optional[List[access_package_localized_text.AccessPackageLocalizedText]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The text property
        self._text: Optional[str] = None
    
    @property
    def actual_value(self,) -> Optional[str]:
        """
        Gets the actualValue property value. The actual value of the selected choice. This is typically a string value which is understandable by applications. Required.
        Returns: Optional[str]
        """
        return self._actual_value
    
    @actual_value.setter
    def actual_value(self,value: Optional[str] = None) -> None:
        """
        Sets the actualValue property value. The actual value of the selected choice. This is typically a string value which is understandable by applications. Required.
        Args:
            value: Value to set for the actual_value property.
        """
        self._actual_value = value
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessPackageAnswerChoice:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageAnswerChoice
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AccessPackageAnswerChoice()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import access_package_localized_text

        fields: Dict[str, Callable[[Any], None]] = {
            "actualValue": lambda n : setattr(self, 'actual_value', n.get_str_value()),
            "localizations": lambda n : setattr(self, 'localizations', n.get_collection_of_object_values(access_package_localized_text.AccessPackageLocalizedText)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "text": lambda n : setattr(self, 'text', n.get_str_value()),
        }
        return fields
    
    @property
    def localizations(self,) -> Optional[List[access_package_localized_text.AccessPackageLocalizedText]]:
        """
        Gets the localizations property value. The text of the answer choice represented in a format for a specific locale.
        Returns: Optional[List[access_package_localized_text.AccessPackageLocalizedText]]
        """
        return self._localizations
    
    @localizations.setter
    def localizations(self,value: Optional[List[access_package_localized_text.AccessPackageLocalizedText]] = None) -> None:
        """
        Sets the localizations property value. The text of the answer choice represented in a format for a specific locale.
        Args:
            value: Value to set for the localizations property.
        """
        self._localizations = value
    
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
        writer.write_str_value("actualValue", self.actual_value)
        writer.write_collection_of_object_values("localizations", self.localizations)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("text", self.text)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def text(self,) -> Optional[str]:
        """
        Gets the text property value. The text property
        Returns: Optional[str]
        """
        return self._text
    
    @text.setter
    def text(self,value: Optional[str] = None) -> None:
        """
        Sets the text property value. The text property
        Args:
            value: Value to set for the text property.
        """
        self._text = value
    

