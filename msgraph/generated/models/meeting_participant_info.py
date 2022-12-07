from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

identity_set = lazy_import('msgraph.generated.models.identity_set')
online_meeting_role = lazy_import('msgraph.generated.models.online_meeting_role')

class MeetingParticipantInfo(AdditionalDataHolder, Parsable):
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
        Instantiates a new meetingParticipantInfo and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Identity information of the participant.
        self._identity: Optional[identity_set.IdentitySet] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Specifies the participant's role in the meeting.  Possible values are attendee, presenter, producer, and unknownFutureValue.
        self._role: Optional[online_meeting_role.OnlineMeetingRole] = None
        # User principal name of the participant.
        self._upn: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MeetingParticipantInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MeetingParticipantInfo
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MeetingParticipantInfo()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "identity": lambda n : setattr(self, 'identity', n.get_object_value(identity_set.IdentitySet)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "role": lambda n : setattr(self, 'role', n.get_enum_value(online_meeting_role.OnlineMeetingRole)),
            "upn": lambda n : setattr(self, 'upn', n.get_str_value()),
        }
        return fields
    
    @property
    def identity(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the identity property value. Identity information of the participant.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._identity
    
    @identity.setter
    def identity(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the identity property value. Identity information of the participant.
        Args:
            value: Value to set for the identity property.
        """
        self._identity = value
    
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
    def role(self,) -> Optional[online_meeting_role.OnlineMeetingRole]:
        """
        Gets the role property value. Specifies the participant's role in the meeting.  Possible values are attendee, presenter, producer, and unknownFutureValue.
        Returns: Optional[online_meeting_role.OnlineMeetingRole]
        """
        return self._role
    
    @role.setter
    def role(self,value: Optional[online_meeting_role.OnlineMeetingRole] = None) -> None:
        """
        Sets the role property value. Specifies the participant's role in the meeting.  Possible values are attendee, presenter, producer, and unknownFutureValue.
        Args:
            value: Value to set for the role property.
        """
        self._role = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("identity", self.identity)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("role", self.role)
        writer.write_str_value("upn", self.upn)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def upn(self,) -> Optional[str]:
        """
        Gets the upn property value. User principal name of the participant.
        Returns: Optional[str]
        """
        return self._upn
    
    @upn.setter
    def upn(self,value: Optional[str] = None) -> None:
        """
        Sets the upn property value. User principal name of the participant.
        Args:
            value: Value to set for the upn property.
        """
        self._upn = value
    

