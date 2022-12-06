from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

date_time_time_zone = lazy_import('msgraph.generated.models.date_time_time_zone')
locale_info = lazy_import('msgraph.generated.models.locale_info')

class AutomaticRepliesMailTips(AdditionalDataHolder, Parsable):
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
        Instantiates a new automaticRepliesMailTips and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The automatic reply message.
        self._message: Optional[str] = None
        # The language that the automatic reply message is in.
        self._message_language: Optional[locale_info.LocaleInfo] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The date and time that automatic replies are set to end.
        self._scheduled_end_time: Optional[date_time_time_zone.DateTimeTimeZone] = None
        # The date and time that automatic replies are set to begin.
        self._scheduled_start_time: Optional[date_time_time_zone.DateTimeTimeZone] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AutomaticRepliesMailTips:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AutomaticRepliesMailTips
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AutomaticRepliesMailTips()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "message": lambda n : setattr(self, 'message', n.get_str_value()),
            "message_language": lambda n : setattr(self, 'message_language', n.get_object_value(locale_info.LocaleInfo)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "scheduled_end_time": lambda n : setattr(self, 'scheduled_end_time', n.get_object_value(date_time_time_zone.DateTimeTimeZone)),
            "scheduled_start_time": lambda n : setattr(self, 'scheduled_start_time', n.get_object_value(date_time_time_zone.DateTimeTimeZone)),
        }
        return fields
    
    @property
    def message(self,) -> Optional[str]:
        """
        Gets the message property value. The automatic reply message.
        Returns: Optional[str]
        """
        return self._message
    
    @message.setter
    def message(self,value: Optional[str] = None) -> None:
        """
        Sets the message property value. The automatic reply message.
        Args:
            value: Value to set for the message property.
        """
        self._message = value
    
    @property
    def message_language(self,) -> Optional[locale_info.LocaleInfo]:
        """
        Gets the messageLanguage property value. The language that the automatic reply message is in.
        Returns: Optional[locale_info.LocaleInfo]
        """
        return self._message_language
    
    @message_language.setter
    def message_language(self,value: Optional[locale_info.LocaleInfo] = None) -> None:
        """
        Sets the messageLanguage property value. The language that the automatic reply message is in.
        Args:
            value: Value to set for the messageLanguage property.
        """
        self._message_language = value
    
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
    def scheduled_end_time(self,) -> Optional[date_time_time_zone.DateTimeTimeZone]:
        """
        Gets the scheduledEndTime property value. The date and time that automatic replies are set to end.
        Returns: Optional[date_time_time_zone.DateTimeTimeZone]
        """
        return self._scheduled_end_time
    
    @scheduled_end_time.setter
    def scheduled_end_time(self,value: Optional[date_time_time_zone.DateTimeTimeZone] = None) -> None:
        """
        Sets the scheduledEndTime property value. The date and time that automatic replies are set to end.
        Args:
            value: Value to set for the scheduledEndTime property.
        """
        self._scheduled_end_time = value
    
    @property
    def scheduled_start_time(self,) -> Optional[date_time_time_zone.DateTimeTimeZone]:
        """
        Gets the scheduledStartTime property value. The date and time that automatic replies are set to begin.
        Returns: Optional[date_time_time_zone.DateTimeTimeZone]
        """
        return self._scheduled_start_time
    
    @scheduled_start_time.setter
    def scheduled_start_time(self,value: Optional[date_time_time_zone.DateTimeTimeZone] = None) -> None:
        """
        Sets the scheduledStartTime property value. The date and time that automatic replies are set to begin.
        Args:
            value: Value to set for the scheduledStartTime property.
        """
        self._scheduled_start_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("message", self.message)
        writer.write_object_value("messageLanguage", self.message_language)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("scheduledEndTime", self.scheduled_end_time)
        writer.write_object_value("scheduledStartTime", self.scheduled_start_time)
        writer.write_additional_data_value(self.additional_data)
    

