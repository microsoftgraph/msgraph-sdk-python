from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ......models.teamwork_user_identity import TeamworkUserIdentity

@dataclass
class MarkChatUnreadForUserPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The lastMessageReadDateTime property
    last_message_read_date_time: Optional[datetime.datetime] = None
    # The user property
    user: Optional[TeamworkUserIdentity] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MarkChatUnreadForUserPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MarkChatUnreadForUserPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MarkChatUnreadForUserPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ......models.teamwork_user_identity import TeamworkUserIdentity

        from ......models.teamwork_user_identity import TeamworkUserIdentity

        fields: dict[str, Callable[[Any], None]] = {
            "lastMessageReadDateTime": lambda n : setattr(self, 'last_message_read_date_time', n.get_datetime_value()),
            "user": lambda n : setattr(self, 'user', n.get_object_value(TeamworkUserIdentity)),
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
        writer.write_datetime_value("lastMessageReadDateTime", self.last_message_read_date_time)
        writer.write_object_value("user", self.user)
        writer.write_additional_data_value(self.additional_data)
    

