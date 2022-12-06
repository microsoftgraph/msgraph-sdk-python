from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

invitation_participant_info = lazy_import('msgraph.generated.models.invitation_participant_info')
participant_info = lazy_import('msgraph.generated.models.participant_info')

class TransferPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the transfer method.
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
        Instantiates a new transferPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The transferee property
        self._transferee: Optional[participant_info.ParticipantInfo] = None
        # The transferTarget property
        self._transfer_target: Optional[invitation_participant_info.InvitationParticipantInfo] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TransferPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TransferPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TransferPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "transferee": lambda n : setattr(self, 'transferee', n.get_object_value(participant_info.ParticipantInfo)),
            "transfer_target": lambda n : setattr(self, 'transfer_target', n.get_object_value(invitation_participant_info.InvitationParticipantInfo)),
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
        writer.write_object_value("transferee", self.transferee)
        writer.write_object_value("transferTarget", self.transfer_target)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def transferee(self,) -> Optional[participant_info.ParticipantInfo]:
        """
        Gets the transferee property value. The transferee property
        Returns: Optional[participant_info.ParticipantInfo]
        """
        return self._transferee
    
    @transferee.setter
    def transferee(self,value: Optional[participant_info.ParticipantInfo] = None) -> None:
        """
        Sets the transferee property value. The transferee property
        Args:
            value: Value to set for the transferee property.
        """
        self._transferee = value
    
    @property
    def transfer_target(self,) -> Optional[invitation_participant_info.InvitationParticipantInfo]:
        """
        Gets the transferTarget property value. The transferTarget property
        Returns: Optional[invitation_participant_info.InvitationParticipantInfo]
        """
        return self._transfer_target
    
    @transfer_target.setter
    def transfer_target(self,value: Optional[invitation_participant_info.InvitationParticipantInfo] = None) -> None:
        """
        Sets the transferTarget property value. The transferTarget property
        Args:
            value: Value to set for the transferTarget property.
        """
        self._transfer_target = value
    

