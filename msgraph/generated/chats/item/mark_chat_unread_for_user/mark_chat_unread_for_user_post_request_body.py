from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

teamwork_user_identity = lazy_import('msgraph.generated.models.teamwork_user_identity')

class MarkChatUnreadForUserPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the markChatUnreadForUser method.
    """
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
        Instantiates a new markChatUnreadForUserPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The lastMessageReadDateTime property
        self._last_message_read_date_time: Optional[datetime] = None
        # The user property
        self._user: Optional[teamwork_user_identity.TeamworkUserIdentity] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MarkChatUnreadForUserPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MarkChatUnreadForUserPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MarkChatUnreadForUserPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "last_message_read_date_time": lambda n : setattr(self, 'last_message_read_date_time', n.get_datetime_value()),
            "user": lambda n : setattr(self, 'user', n.get_object_value(teamwork_user_identity.TeamworkUserIdentity)),
        }
        return fields
    
    @property
    def last_message_read_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastMessageReadDateTime property value. The lastMessageReadDateTime property
        Returns: Optional[datetime]
        """
        return self._last_message_read_date_time
    
    @last_message_read_date_time.setter
    def last_message_read_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastMessageReadDateTime property value. The lastMessageReadDateTime property
        Args:
            value: Value to set for the lastMessageReadDateTime property.
        """
        self._last_message_read_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_datetime_value("lastMessageReadDateTime", self.last_message_read_date_time)
        writer.write_object_value("user", self.user)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def user(self,) -> Optional[teamwork_user_identity.TeamworkUserIdentity]:
        """
        Gets the user property value. The user property
        Returns: Optional[teamwork_user_identity.TeamworkUserIdentity]
        """
        return self._user
    
    @user.setter
    def user(self,value: Optional[teamwork_user_identity.TeamworkUserIdentity] = None) -> None:
        """
        Sets the user property value. The user property
        Args:
            value: Value to set for the user property.
        """
        self._user = value
    

