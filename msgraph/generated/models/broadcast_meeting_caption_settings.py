from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class BroadcastMeetingCaptionSettings(AdditionalDataHolder, Parsable):
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
        Instantiates a new broadcastMeetingCaptionSettings and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Indicates whether captions are enabled for this Teams live event.
        self._is_caption_enabled: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The spoken language.
        self._spoken_language: Optional[str] = None
        # The translation languages (choose up to 6).
        self._translation_languages: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BroadcastMeetingCaptionSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: BroadcastMeetingCaptionSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return BroadcastMeetingCaptionSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "is_caption_enabled": lambda n : setattr(self, 'is_caption_enabled', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "spoken_language": lambda n : setattr(self, 'spoken_language', n.get_str_value()),
            "translation_languages": lambda n : setattr(self, 'translation_languages', n.get_collection_of_primitive_values(str)),
        }
        return fields
    
    @property
    def is_caption_enabled(self,) -> Optional[bool]:
        """
        Gets the isCaptionEnabled property value. Indicates whether captions are enabled for this Teams live event.
        Returns: Optional[bool]
        """
        return self._is_caption_enabled
    
    @is_caption_enabled.setter
    def is_caption_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isCaptionEnabled property value. Indicates whether captions are enabled for this Teams live event.
        Args:
            value: Value to set for the isCaptionEnabled property.
        """
        self._is_caption_enabled = value
    
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
        writer.write_bool_value("isCaptionEnabled", self.is_caption_enabled)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("spokenLanguage", self.spoken_language)
        writer.write_collection_of_primitive_values("translationLanguages", self.translation_languages)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def spoken_language(self,) -> Optional[str]:
        """
        Gets the spokenLanguage property value. The spoken language.
        Returns: Optional[str]
        """
        return self._spoken_language
    
    @spoken_language.setter
    def spoken_language(self,value: Optional[str] = None) -> None:
        """
        Sets the spokenLanguage property value. The spoken language.
        Args:
            value: Value to set for the spokenLanguage property.
        """
        self._spoken_language = value
    
    @property
    def translation_languages(self,) -> Optional[List[str]]:
        """
        Gets the translationLanguages property value. The translation languages (choose up to 6).
        Returns: Optional[List[str]]
        """
        return self._translation_languages
    
    @translation_languages.setter
    def translation_languages(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the translationLanguages property value. The translation languages (choose up to 6).
        Args:
            value: Value to set for the translationLanguages property.
        """
        self._translation_languages = value
    

