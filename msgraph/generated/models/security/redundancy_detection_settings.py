from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class RedundancyDetectionSettings(AdditionalDataHolder, Parsable):
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
        Instantiates a new redundancyDetectionSettings and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Indicates whether email threading and near duplicate detection are enabled.
        self._is_enabled: Optional[bool] = None
        # Specifies the maximum number of words used for email threading and near duplicate detection. To learn more, see Minimum/maximum number of words.
        self._max_words: Optional[int] = None
        # Specifies the minimum number of words used for email threading and near duplicate detection. To learn more, see Minimum/maximum number of words.
        self._min_words: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Specifies the similarity level for documents to be put in the same near duplicate set. To learn more, see Document and email similarity threshold.
        self._similarity_threshold: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RedundancyDetectionSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RedundancyDetectionSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RedundancyDetectionSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "is_enabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
            "max_words": lambda n : setattr(self, 'max_words', n.get_int_value()),
            "min_words": lambda n : setattr(self, 'min_words', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "similarity_threshold": lambda n : setattr(self, 'similarity_threshold', n.get_int_value()),
        }
        return fields
    
    @property
    def is_enabled(self,) -> Optional[bool]:
        """
        Gets the isEnabled property value. Indicates whether email threading and near duplicate detection are enabled.
        Returns: Optional[bool]
        """
        return self._is_enabled
    
    @is_enabled.setter
    def is_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isEnabled property value. Indicates whether email threading and near duplicate detection are enabled.
        Args:
            value: Value to set for the isEnabled property.
        """
        self._is_enabled = value
    
    @property
    def max_words(self,) -> Optional[int]:
        """
        Gets the maxWords property value. Specifies the maximum number of words used for email threading and near duplicate detection. To learn more, see Minimum/maximum number of words.
        Returns: Optional[int]
        """
        return self._max_words
    
    @max_words.setter
    def max_words(self,value: Optional[int] = None) -> None:
        """
        Sets the maxWords property value. Specifies the maximum number of words used for email threading and near duplicate detection. To learn more, see Minimum/maximum number of words.
        Args:
            value: Value to set for the maxWords property.
        """
        self._max_words = value
    
    @property
    def min_words(self,) -> Optional[int]:
        """
        Gets the minWords property value. Specifies the minimum number of words used for email threading and near duplicate detection. To learn more, see Minimum/maximum number of words.
        Returns: Optional[int]
        """
        return self._min_words
    
    @min_words.setter
    def min_words(self,value: Optional[int] = None) -> None:
        """
        Sets the minWords property value. Specifies the minimum number of words used for email threading and near duplicate detection. To learn more, see Minimum/maximum number of words.
        Args:
            value: Value to set for the minWords property.
        """
        self._min_words = value
    
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
        writer.write_bool_value("isEnabled", self.is_enabled)
        writer.write_int_value("maxWords", self.max_words)
        writer.write_int_value("minWords", self.min_words)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("similarityThreshold", self.similarity_threshold)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def similarity_threshold(self,) -> Optional[int]:
        """
        Gets the similarityThreshold property value. Specifies the similarity level for documents to be put in the same near duplicate set. To learn more, see Document and email similarity threshold.
        Returns: Optional[int]
        """
        return self._similarity_threshold
    
    @similarity_threshold.setter
    def similarity_threshold(self,value: Optional[int] = None) -> None:
        """
        Sets the similarityThreshold property value. Specifies the similarity level for documents to be put in the same near duplicate set. To learn more, see Document and email similarity threshold.
        Args:
            value: Value to set for the similarityThreshold property.
        """
        self._similarity_threshold = value
    

