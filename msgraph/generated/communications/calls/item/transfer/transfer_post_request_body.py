from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models.invitation_participant_info import InvitationParticipantInfo
    from .....models.participant_info import ParticipantInfo

@dataclass
class TransferPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The transferTarget property
    transfer_target: Optional[InvitationParticipantInfo] = None
    # The transferee property
    transferee: Optional[ParticipantInfo] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TransferPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TransferPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TransferPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .....models.invitation_participant_info import InvitationParticipantInfo
        from .....models.participant_info import ParticipantInfo

        from .....models.invitation_participant_info import InvitationParticipantInfo
        from .....models.participant_info import ParticipantInfo

        fields: Dict[str, Callable[[Any], None]] = {
            "transferTarget": lambda n : setattr(self, 'transfer_target', n.get_object_value(InvitationParticipantInfo)),
            "transferee": lambda n : setattr(self, 'transferee', n.get_object_value(ParticipantInfo)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("transferTarget", self.transfer_target)
        writer.write_object_value("transferee", self.transferee)
        writer.write_additional_data_value(self.additional_data)
    

