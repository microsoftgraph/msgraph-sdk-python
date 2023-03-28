from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

meeting_info = lazy_import('msgraph.generated.models.meeting_info')

class TokenMeetingInfo(meeting_info.MeetingInfo):
    def __init__(self,) -> None:
        """
        Instantiates a new TokenMeetingInfo and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.tokenMeetingInfo"
        # The token used to join the call.
        self._token: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TokenMeetingInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TokenMeetingInfo
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TokenMeetingInfo()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "token": lambda n : setattr(self, 'token', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("token", self.token)
    
    @property
    def token(self,) -> Optional[str]:
        """
        Gets the token property value. The token used to join the call.
        Returns: Optional[str]
        """
        return self._token
    
    @token.setter
    def token(self,value: Optional[str] = None) -> None:
        """
        Sets the token property value. The token used to join the call.
        Args:
            value: Value to set for the token property.
        """
        self._token = value
    

