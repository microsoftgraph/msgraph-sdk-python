from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

date_time_time_zone = lazy_import('msgraph.generated.models.date_time_time_zone')
followup_flag_status = lazy_import('msgraph.generated.models.followup_flag_status')

class FollowupFlag(AdditionalDataHolder, Parsable):
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
    def completed_date_time(self,) -> Optional[date_time_time_zone.DateTimeTimeZone]:
        """
        Gets the completedDateTime property value. The date and time that the follow-up was finished.
        Returns: Optional[date_time_time_zone.DateTimeTimeZone]
        """
        return self._completed_date_time
    
    @completed_date_time.setter
    def completed_date_time(self,value: Optional[date_time_time_zone.DateTimeTimeZone] = None) -> None:
        """
        Sets the completedDateTime property value. The date and time that the follow-up was finished.
        Args:
            value: Value to set for the completedDateTime property.
        """
        self._completed_date_time = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new followupFlag and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The date and time that the follow-up was finished.
        self._completed_date_time: Optional[date_time_time_zone.DateTimeTimeZone] = None
        # The date and time that the follow up is to be finished. Note: To set the due date, you must also specify the startDateTime; otherwise, you will get a 400 Bad Request response.
        self._due_date_time: Optional[date_time_time_zone.DateTimeTimeZone] = None
        # The status for follow-up for an item. Possible values are notFlagged, complete, and flagged.
        self._flag_status: Optional[followup_flag_status.FollowupFlagStatus] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The date and time that the follow-up is to begin.
        self._start_date_time: Optional[date_time_time_zone.DateTimeTimeZone] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> FollowupFlag:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: FollowupFlag
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return FollowupFlag()
    
    @property
    def due_date_time(self,) -> Optional[date_time_time_zone.DateTimeTimeZone]:
        """
        Gets the dueDateTime property value. The date and time that the follow up is to be finished. Note: To set the due date, you must also specify the startDateTime; otherwise, you will get a 400 Bad Request response.
        Returns: Optional[date_time_time_zone.DateTimeTimeZone]
        """
        return self._due_date_time
    
    @due_date_time.setter
    def due_date_time(self,value: Optional[date_time_time_zone.DateTimeTimeZone] = None) -> None:
        """
        Sets the dueDateTime property value. The date and time that the follow up is to be finished. Note: To set the due date, you must also specify the startDateTime; otherwise, you will get a 400 Bad Request response.
        Args:
            value: Value to set for the dueDateTime property.
        """
        self._due_date_time = value
    
    @property
    def flag_status(self,) -> Optional[followup_flag_status.FollowupFlagStatus]:
        """
        Gets the flagStatus property value. The status for follow-up for an item. Possible values are notFlagged, complete, and flagged.
        Returns: Optional[followup_flag_status.FollowupFlagStatus]
        """
        return self._flag_status
    
    @flag_status.setter
    def flag_status(self,value: Optional[followup_flag_status.FollowupFlagStatus] = None) -> None:
        """
        Sets the flagStatus property value. The status for follow-up for an item. Possible values are notFlagged, complete, and flagged.
        Args:
            value: Value to set for the flagStatus property.
        """
        self._flag_status = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "completed_date_time": lambda n : setattr(self, 'completed_date_time', n.get_object_value(date_time_time_zone.DateTimeTimeZone)),
            "due_date_time": lambda n : setattr(self, 'due_date_time', n.get_object_value(date_time_time_zone.DateTimeTimeZone)),
            "flag_status": lambda n : setattr(self, 'flag_status', n.get_enum_value(followup_flag_status.FollowupFlagStatus)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "start_date_time": lambda n : setattr(self, 'start_date_time', n.get_object_value(date_time_time_zone.DateTimeTimeZone)),
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
        writer.write_object_value("completedDateTime", self.completed_date_time)
        writer.write_object_value("dueDateTime", self.due_date_time)
        writer.write_enum_value("flagStatus", self.flag_status)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("startDateTime", self.start_date_time)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def start_date_time(self,) -> Optional[date_time_time_zone.DateTimeTimeZone]:
        """
        Gets the startDateTime property value. The date and time that the follow-up is to begin.
        Returns: Optional[date_time_time_zone.DateTimeTimeZone]
        """
        return self._start_date_time
    
    @start_date_time.setter
    def start_date_time(self,value: Optional[date_time_time_zone.DateTimeTimeZone] = None) -> None:
        """
        Sets the startDateTime property value. The date and time that the follow-up is to begin.
        Args:
            value: Value to set for the startDateTime property.
        """
        self._start_date_time = value
    

