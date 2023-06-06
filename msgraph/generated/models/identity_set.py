from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import chat_message_from_identity_set, chat_message_mentioned_identity_set, chat_message_reaction_identity_set, identity, share_point_identity_set

@dataclass
class IdentitySet(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Optional. The application associated with this action.
    application: Optional[identity.Identity] = None
    # Optional. The device associated with this action.
    device: Optional[identity.Identity] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Optional. The user associated with this action.
    user: Optional[identity.Identity] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IdentitySet:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IdentitySet
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.chatMessageFromIdentitySet":
                from . import chat_message_from_identity_set

                return chat_message_from_identity_set.ChatMessageFromIdentitySet()
            if mapping_value == "#microsoft.graph.chatMessageMentionedIdentitySet":
                from . import chat_message_mentioned_identity_set

                return chat_message_mentioned_identity_set.ChatMessageMentionedIdentitySet()
            if mapping_value == "#microsoft.graph.chatMessageReactionIdentitySet":
                from . import chat_message_reaction_identity_set

                return chat_message_reaction_identity_set.ChatMessageReactionIdentitySet()
            if mapping_value == "#microsoft.graph.sharePointIdentitySet":
                from . import share_point_identity_set

                return share_point_identity_set.SharePointIdentitySet()
        return IdentitySet()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import chat_message_from_identity_set, chat_message_mentioned_identity_set, chat_message_reaction_identity_set, identity, share_point_identity_set

        fields: Dict[str, Callable[[Any], None]] = {
            "application": lambda n : setattr(self, 'application', n.get_object_value(identity.Identity)),
            "device": lambda n : setattr(self, 'device', n.get_object_value(identity.Identity)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "user": lambda n : setattr(self, 'user', n.get_object_value(identity.Identity)),
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
        writer.write_object_value("application", self.application)
        writer.write_object_value("device", self.device)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("user", self.user)
        writer.write_additional_data_value(self.additional_data)
    

