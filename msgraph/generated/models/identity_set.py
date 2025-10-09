from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .ai_interaction_mentioned_identity_set import AiInteractionMentionedIdentitySet
    from .chat_message_from_identity_set import ChatMessageFromIdentitySet
    from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
    from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
    from .communications_identity_set import CommunicationsIdentitySet
    from .engagement_identity_set import EngagementIdentitySet
    from .identity import Identity
    from .share_point_identity_set import SharePointIdentitySet

@dataclass
class IdentitySet(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Optional. The application associated with this action.
    application: Optional[Identity] = None
    # Optional. The device associated with this action.
    device: Optional[Identity] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Optional. The user associated with this action.
    user: Optional[Identity] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IdentitySet:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IdentitySet
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.aiInteractionMentionedIdentitySet".casefold():
            from .ai_interaction_mentioned_identity_set import AiInteractionMentionedIdentitySet

            return AiInteractionMentionedIdentitySet()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.chatMessageFromIdentitySet".casefold():
            from .chat_message_from_identity_set import ChatMessageFromIdentitySet

            return ChatMessageFromIdentitySet()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.chatMessageMentionedIdentitySet".casefold():
            from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet

            return ChatMessageMentionedIdentitySet()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.chatMessageReactionIdentitySet".casefold():
            from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet

            return ChatMessageReactionIdentitySet()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.communicationsIdentitySet".casefold():
            from .communications_identity_set import CommunicationsIdentitySet

            return CommunicationsIdentitySet()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.engagementIdentitySet".casefold():
            from .engagement_identity_set import EngagementIdentitySet

            return EngagementIdentitySet()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sharePointIdentitySet".casefold():
            from .share_point_identity_set import SharePointIdentitySet

            return SharePointIdentitySet()
        return IdentitySet()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .ai_interaction_mentioned_identity_set import AiInteractionMentionedIdentitySet
        from .chat_message_from_identity_set import ChatMessageFromIdentitySet
        from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
        from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
        from .communications_identity_set import CommunicationsIdentitySet
        from .engagement_identity_set import EngagementIdentitySet
        from .identity import Identity
        from .share_point_identity_set import SharePointIdentitySet

        from .ai_interaction_mentioned_identity_set import AiInteractionMentionedIdentitySet
        from .chat_message_from_identity_set import ChatMessageFromIdentitySet
        from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
        from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
        from .communications_identity_set import CommunicationsIdentitySet
        from .engagement_identity_set import EngagementIdentitySet
        from .identity import Identity
        from .share_point_identity_set import SharePointIdentitySet

        fields: dict[str, Callable[[Any], None]] = {
            "application": lambda n : setattr(self, 'application', n.get_object_value(Identity)),
            "device": lambda n : setattr(self, 'device', n.get_object_value(Identity)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "user": lambda n : setattr(self, 'user', n.get_object_value(Identity)),
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
        writer.write_object_value("application", self.application)
        writer.write_object_value("device", self.device)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("user", self.user)
        writer.write_additional_data_value(self.additional_data)
    

