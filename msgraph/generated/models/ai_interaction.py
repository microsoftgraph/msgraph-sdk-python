from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .ai_interaction_attachment import AiInteractionAttachment
    from .ai_interaction_context import AiInteractionContext
    from .ai_interaction_link import AiInteractionLink
    from .ai_interaction_mention import AiInteractionMention
    from .ai_interaction_type import AiInteractionType
    from .entity import Entity
    from .identity_set import IdentitySet
    from .item_body import ItemBody

from .entity import Entity

@dataclass
class AiInteraction(Entity, Parsable):
    # The data source for Copilot data. For example, IPM.SkypeTeams.Message.Copilot.Excel or IPM.SkypeTeams.Message.Copilot.Loop.
    app_class: Optional[str] = None
    # The collection of documents attached to the interaction, such as cards and images.
    attachments: Optional[list[AiInteractionAttachment]] = None
    # The body of the message, including the text of the body and its body type.
    body: Optional[ItemBody] = None
    # The identifer that maps to all contexts associated with an interaction.
    contexts: Optional[list[AiInteractionContext]] = None
    # The type of the conversation. For example, appchat or bizchat.
    conversation_type: Optional[str] = None
    # The time when the interaction was created.
    created_date_time: Optional[datetime.datetime] = None
    # The timestamp of when the interaction was last modified.
    etag: Optional[str] = None
    # The from property
    from_: Optional[IdentitySet] = None
    # The interactionType property
    interaction_type: Optional[AiInteractionType] = None
    # The collection of links that appear in the interaction.
    links: Optional[list[AiInteractionLink]] = None
    # The locale of the sender.
    locale: Optional[str] = None
    # The collection of the entities that were mentioned in the interaction, including users, bots, and so on.
    mentions: Optional[list[AiInteractionMention]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The identifier that groups a user prompt with its Copilot response.
    request_id: Optional[str] = None
    # The thread ID or conversation identifier that maps to all Copilot sessions for the user.
    session_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AiInteraction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AiInteraction
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AiInteraction()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .ai_interaction_attachment import AiInteractionAttachment
        from .ai_interaction_context import AiInteractionContext
        from .ai_interaction_link import AiInteractionLink
        from .ai_interaction_mention import AiInteractionMention
        from .ai_interaction_type import AiInteractionType
        from .entity import Entity
        from .identity_set import IdentitySet
        from .item_body import ItemBody

        from .ai_interaction_attachment import AiInteractionAttachment
        from .ai_interaction_context import AiInteractionContext
        from .ai_interaction_link import AiInteractionLink
        from .ai_interaction_mention import AiInteractionMention
        from .ai_interaction_type import AiInteractionType
        from .entity import Entity
        from .identity_set import IdentitySet
        from .item_body import ItemBody

        fields: dict[str, Callable[[Any], None]] = {
            "appClass": lambda n : setattr(self, 'app_class', n.get_str_value()),
            "attachments": lambda n : setattr(self, 'attachments', n.get_collection_of_object_values(AiInteractionAttachment)),
            "body": lambda n : setattr(self, 'body', n.get_object_value(ItemBody)),
            "contexts": lambda n : setattr(self, 'contexts', n.get_collection_of_object_values(AiInteractionContext)),
            "conversationType": lambda n : setattr(self, 'conversation_type', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "etag": lambda n : setattr(self, 'etag', n.get_str_value()),
            "from": lambda n : setattr(self, 'from_', n.get_object_value(IdentitySet)),
            "interactionType": lambda n : setattr(self, 'interaction_type', n.get_enum_value(AiInteractionType)),
            "links": lambda n : setattr(self, 'links', n.get_collection_of_object_values(AiInteractionLink)),
            "locale": lambda n : setattr(self, 'locale', n.get_str_value()),
            "mentions": lambda n : setattr(self, 'mentions', n.get_collection_of_object_values(AiInteractionMention)),
            "requestId": lambda n : setattr(self, 'request_id', n.get_str_value()),
            "sessionId": lambda n : setattr(self, 'session_id', n.get_str_value()),
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
        writer.write_str_value("appClass", self.app_class)
        writer.write_collection_of_object_values("attachments", self.attachments)
        writer.write_object_value("body", self.body)
        writer.write_collection_of_object_values("contexts", self.contexts)
        writer.write_str_value("conversationType", self.conversation_type)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("etag", self.etag)
        writer.write_object_value("from", self.from_)
        writer.write_enum_value("interactionType", self.interaction_type)
        writer.write_collection_of_object_values("links", self.links)
        writer.write_str_value("locale", self.locale)
        writer.write_collection_of_object_values("mentions", self.mentions)
        writer.write_str_value("requestId", self.request_id)
        writer.write_str_value("sessionId", self.session_id)
    

