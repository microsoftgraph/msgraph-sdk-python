from __future__ import annotations
from datetime import timedelta
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class SetPresencePostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new setPresencePostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The activity property
        self._activity: Optional[str] = None
        # The availability property
        self._availability: Optional[str] = None
        # The expirationDuration property
        self._expiration_duration: Optional[timedelta] = None
        # The sessionId property
        self._session_id: Optional[str] = None
    
    @property
    def activity(self,) -> Optional[str]:
        """
        Gets the activity property value. The activity property
        Returns: Optional[str]
        """
        return self._activity
    
    @activity.setter
    def activity(self,value: Optional[str] = None) -> None:
        """
        Sets the activity property value. The activity property
        Args:
            value: Value to set for the activity property.
        """
        self._activity = value
    
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
    def availability(self,) -> Optional[str]:
        """
        Gets the availability property value. The availability property
        Returns: Optional[str]
        """
        return self._availability
    
    @availability.setter
    def availability(self,value: Optional[str] = None) -> None:
        """
        Sets the availability property value. The availability property
        Args:
            value: Value to set for the availability property.
        """
        self._availability = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SetPresencePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SetPresencePostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SetPresencePostRequestBody()
    
    @property
    def expiration_duration(self,) -> Optional[timedelta]:
        """
        Gets the expirationDuration property value. The expirationDuration property
        Returns: Optional[timedelta]
        """
        return self._expiration_duration
    
    @expiration_duration.setter
    def expiration_duration(self,value: Optional[timedelta] = None) -> None:
        """
        Sets the expirationDuration property value. The expirationDuration property
        Args:
            value: Value to set for the expiration_duration property.
        """
        self._expiration_duration = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "activity": lambda n : setattr(self, 'activity', n.get_str_value()),
            "availability": lambda n : setattr(self, 'availability', n.get_str_value()),
            "expirationDuration": lambda n : setattr(self, 'expiration_duration', n.get_timedelta_value()),
            "sessionId": lambda n : setattr(self, 'session_id', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("activity", self.activity)
        writer.write_str_value("availability", self.availability)
        writer.write_timedelta_value("expirationDuration", self.expiration_duration)
        writer.write_str_value("sessionId", self.session_id)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def session_id(self,) -> Optional[str]:
        """
        Gets the sessionId property value. The sessionId property
        Returns: Optional[str]
        """
        return self._session_id
    
    @session_id.setter
    def session_id(self,value: Optional[str] = None) -> None:
        """
        Sets the sessionId property value. The sessionId property
        Args:
            value: Value to set for the session_id property.
        """
        self._session_id = value
    

