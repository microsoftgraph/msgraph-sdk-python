from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

teamwork_user_identity = lazy_import('msgraph.generated.models.teamwork_user_identity')

class TeamworkOnlineMeetingInfo(AdditionalDataHolder, Parsable):
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
    def calendar_event_id(self,) -> Optional[str]:
        """
        Gets the calendarEventId property value. The identifier of the calendar event associated with the meeting.
        Returns: Optional[str]
        """
        return self._calendar_event_id
    
    @calendar_event_id.setter
    def calendar_event_id(self,value: Optional[str] = None) -> None:
        """
        Sets the calendarEventId property value. The identifier of the calendar event associated with the meeting.
        Args:
            value: Value to set for the calendarEventId property.
        """
        self._calendar_event_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new teamworkOnlineMeetingInfo and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The identifier of the calendar event associated with the meeting.
        self._calendar_event_id: Optional[str] = None
        # The URL that users click to join or uniquely identify the meeting.
        self._join_web_url: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The organizer of the meeting.
        self._organizer: Optional[teamwork_user_identity.TeamworkUserIdentity] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamworkOnlineMeetingInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkOnlineMeetingInfo
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TeamworkOnlineMeetingInfo()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "calendar_event_id": lambda n : setattr(self, 'calendar_event_id', n.get_str_value()),
            "join_web_url": lambda n : setattr(self, 'join_web_url', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "organizer": lambda n : setattr(self, 'organizer', n.get_object_value(teamwork_user_identity.TeamworkUserIdentity)),
        }
        return fields
    
    @property
    def join_web_url(self,) -> Optional[str]:
        """
        Gets the joinWebUrl property value. The URL that users click to join or uniquely identify the meeting.
        Returns: Optional[str]
        """
        return self._join_web_url
    
    @join_web_url.setter
    def join_web_url(self,value: Optional[str] = None) -> None:
        """
        Sets the joinWebUrl property value. The URL that users click to join or uniquely identify the meeting.
        Args:
            value: Value to set for the joinWebUrl property.
        """
        self._join_web_url = value
    
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
    def organizer(self,) -> Optional[teamwork_user_identity.TeamworkUserIdentity]:
        """
        Gets the organizer property value. The organizer of the meeting.
        Returns: Optional[teamwork_user_identity.TeamworkUserIdentity]
        """
        return self._organizer
    
    @organizer.setter
    def organizer(self,value: Optional[teamwork_user_identity.TeamworkUserIdentity] = None) -> None:
        """
        Sets the organizer property value. The organizer of the meeting.
        Args:
            value: Value to set for the organizer property.
        """
        self._organizer = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("calendarEventId", self.calendar_event_id)
        writer.write_str_value("joinWebUrl", self.join_web_url)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("organizer", self.organizer)
        writer.write_additional_data_value(self.additional_data)
    

