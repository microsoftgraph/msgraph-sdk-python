from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class TopicModelingSettings(AdditionalDataHolder, Parsable):
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
        Instantiates a new topicModelingSettings and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Indicates whether the themes model should dynamically optimize the number of generated topics. To learn more, see Adjust maximum number of themes dynamically.
        self._dynamically_adjust_topic_count: Optional[bool] = None
        # Indicates whether the themes model should exclude numbers while parsing document texts. To learn more, see Include numbers in themes.
        self._ignore_numbers: Optional[bool] = None
        # Indicates whether themes model is enabled for the case.
        self._is_enabled: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The total number of topics that the themes model will generate for a review set. To learn more, see Maximum number of themes.
        self._topic_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TopicModelingSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TopicModelingSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TopicModelingSettings()
    
    @property
    def dynamically_adjust_topic_count(self,) -> Optional[bool]:
        """
        Gets the dynamicallyAdjustTopicCount property value. Indicates whether the themes model should dynamically optimize the number of generated topics. To learn more, see Adjust maximum number of themes dynamically.
        Returns: Optional[bool]
        """
        return self._dynamically_adjust_topic_count
    
    @dynamically_adjust_topic_count.setter
    def dynamically_adjust_topic_count(self,value: Optional[bool] = None) -> None:
        """
        Sets the dynamicallyAdjustTopicCount property value. Indicates whether the themes model should dynamically optimize the number of generated topics. To learn more, see Adjust maximum number of themes dynamically.
        Args:
            value: Value to set for the dynamicallyAdjustTopicCount property.
        """
        self._dynamically_adjust_topic_count = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "dynamically_adjust_topic_count": lambda n : setattr(self, 'dynamically_adjust_topic_count', n.get_bool_value()),
            "ignore_numbers": lambda n : setattr(self, 'ignore_numbers', n.get_bool_value()),
            "is_enabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "topic_count": lambda n : setattr(self, 'topic_count', n.get_int_value()),
        }
        return fields
    
    @property
    def ignore_numbers(self,) -> Optional[bool]:
        """
        Gets the ignoreNumbers property value. Indicates whether the themes model should exclude numbers while parsing document texts. To learn more, see Include numbers in themes.
        Returns: Optional[bool]
        """
        return self._ignore_numbers
    
    @ignore_numbers.setter
    def ignore_numbers(self,value: Optional[bool] = None) -> None:
        """
        Sets the ignoreNumbers property value. Indicates whether the themes model should exclude numbers while parsing document texts. To learn more, see Include numbers in themes.
        Args:
            value: Value to set for the ignoreNumbers property.
        """
        self._ignore_numbers = value
    
    @property
    def is_enabled(self,) -> Optional[bool]:
        """
        Gets the isEnabled property value. Indicates whether themes model is enabled for the case.
        Returns: Optional[bool]
        """
        return self._is_enabled
    
    @is_enabled.setter
    def is_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isEnabled property value. Indicates whether themes model is enabled for the case.
        Args:
            value: Value to set for the isEnabled property.
        """
        self._is_enabled = value
    
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
        writer.write_bool_value("dynamicallyAdjustTopicCount", self.dynamically_adjust_topic_count)
        writer.write_bool_value("ignoreNumbers", self.ignore_numbers)
        writer.write_bool_value("isEnabled", self.is_enabled)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("topicCount", self.topic_count)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def topic_count(self,) -> Optional[int]:
        """
        Gets the topicCount property value. The total number of topics that the themes model will generate for a review set. To learn more, see Maximum number of themes.
        Returns: Optional[int]
        """
        return self._topic_count
    
    @topic_count.setter
    def topic_count(self,value: Optional[int] = None) -> None:
        """
        Sets the topicCount property value. The total number of topics that the themes model will generate for a review set. To learn more, see Maximum number of themes.
        Args:
            value: Value to set for the topicCount property.
        """
        self._topic_count = value
    

