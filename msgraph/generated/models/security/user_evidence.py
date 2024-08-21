from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .alert_evidence import AlertEvidence
    from .stream import Stream
    from .user_account import UserAccount

from .alert_evidence import AlertEvidence

@dataclass
class UserEvidence(AlertEvidence):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.userEvidence"
    # The stream property
    stream: Optional[Stream] = None
    # The user account details.
    user_account: Optional[UserAccount] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserEvidence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserEvidence
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserEvidence()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .alert_evidence import AlertEvidence
        from .stream import Stream
        from .user_account import UserAccount

        from .alert_evidence import AlertEvidence
        from .stream import Stream
        from .user_account import UserAccount

        fields: Dict[str, Callable[[Any], None]] = {
            "stream": lambda n : setattr(self, 'stream', n.get_object_value(Stream)),
            "userAccount": lambda n : setattr(self, 'user_account', n.get_object_value(UserAccount)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("stream", self.stream)
        writer.write_object_value("userAccount", self.user_account)
    

