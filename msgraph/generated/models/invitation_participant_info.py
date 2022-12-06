from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

identity_set = lazy_import('msgraph.generated.models.identity_set')

class InvitationParticipantInfo(AdditionalDataHolder, Parsable):
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
        Instantiates a new invitationParticipantInfo and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Optional. Whether to hide the participant from the roster.
        self._hidden: Optional[bool] = None
        # The identity property
        self._identity: Optional[identity_set.IdentitySet] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Optional. The ID of the target participant.
        self._participant_id: Optional[str] = None
        # Optional. Whether to remove them from the main mixer.
        self._remove_from_default_audio_routing_group: Optional[bool] = None
        # Optional. The call which the target identity is currently a part of. For peer-to-peer case, the call will be dropped once the participant is added successfully.
        self._replaces_call_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> InvitationParticipantInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: InvitationParticipantInfo
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return InvitationParticipantInfo()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "hidden": lambda n : setattr(self, 'hidden', n.get_bool_value()),
            "identity": lambda n : setattr(self, 'identity', n.get_object_value(identity_set.IdentitySet)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "participant_id": lambda n : setattr(self, 'participant_id', n.get_str_value()),
            "remove_from_default_audio_routing_group": lambda n : setattr(self, 'remove_from_default_audio_routing_group', n.get_bool_value()),
            "replaces_call_id": lambda n : setattr(self, 'replaces_call_id', n.get_str_value()),
        }
        return fields
    
    @property
    def hidden(self,) -> Optional[bool]:
        """
        Gets the hidden property value. Optional. Whether to hide the participant from the roster.
        Returns: Optional[bool]
        """
        return self._hidden
    
    @hidden.setter
    def hidden(self,value: Optional[bool] = None) -> None:
        """
        Sets the hidden property value. Optional. Whether to hide the participant from the roster.
        Args:
            value: Value to set for the hidden property.
        """
        self._hidden = value
    
    @property
    def identity(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the identity property value. The identity property
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._identity
    
    @identity.setter
    def identity(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the identity property value. The identity property
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
    def participant_id(self,) -> Optional[str]:
        """
        Gets the participantId property value. Optional. The ID of the target participant.
        Returns: Optional[str]
        """
        return self._participant_id
    
    @participant_id.setter
    def participant_id(self,value: Optional[str] = None) -> None:
        """
        Sets the participantId property value. Optional. The ID of the target participant.
        Args:
            value: Value to set for the participantId property.
        """
        self._participant_id = value
    
    @property
    def remove_from_default_audio_routing_group(self,) -> Optional[bool]:
        """
        Gets the removeFromDefaultAudioRoutingGroup property value. Optional. Whether to remove them from the main mixer.
        Returns: Optional[bool]
        """
        return self._remove_from_default_audio_routing_group
    
    @remove_from_default_audio_routing_group.setter
    def remove_from_default_audio_routing_group(self,value: Optional[bool] = None) -> None:
        """
        Sets the removeFromDefaultAudioRoutingGroup property value. Optional. Whether to remove them from the main mixer.
        Args:
            value: Value to set for the removeFromDefaultAudioRoutingGroup property.
        """
        self._remove_from_default_audio_routing_group = value
    
    @property
    def replaces_call_id(self,) -> Optional[str]:
        """
        Gets the replacesCallId property value. Optional. The call which the target identity is currently a part of. For peer-to-peer case, the call will be dropped once the participant is added successfully.
        Returns: Optional[str]
        """
        return self._replaces_call_id
    
    @replaces_call_id.setter
    def replaces_call_id(self,value: Optional[str] = None) -> None:
        """
        Sets the replacesCallId property value. Optional. The call which the target identity is currently a part of. For peer-to-peer case, the call will be dropped once the participant is added successfully.
        Args:
            value: Value to set for the replacesCallId property.
        """
        self._replaces_call_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_bool_value("hidden", self.hidden)
        writer.write_object_value("identity", self.identity)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("participantId", self.participant_id)
        writer.write_bool_value("removeFromDefaultAudioRoutingGroup", self.remove_from_default_audio_routing_group)
        writer.write_str_value("replacesCallId", self.replaces_call_id)
        writer.write_additional_data_value(self.additional_data)
    

