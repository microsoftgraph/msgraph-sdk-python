from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .ai_interaction_plugin import AiInteractionPlugin
    from .process_content_metadata_base import ProcessContentMetadataBase

from .process_content_metadata_base import ProcessContentMetadataBase

@dataclass
class ProcessConversationMetadata(ProcessContentMetadataBase, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.processConversationMetadata"
    # List of resources (for example, file URLs, web URLs) accessed during the generation of this message (relevant for bot interactions).
    accessed_resources: Optional[list[str]] = None
    # Identifier of the parent message in a threaded conversation, if applicable.
    parent_message_id: Optional[str] = None
    # List of plugins used during the generation of this message (relevant for AI/bot interactions).
    plugins: Optional[list[AiInteractionPlugin]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ProcessConversationMetadata:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ProcessConversationMetadata
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ProcessConversationMetadata()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .ai_interaction_plugin import AiInteractionPlugin
        from .process_content_metadata_base import ProcessContentMetadataBase

        from .ai_interaction_plugin import AiInteractionPlugin
        from .process_content_metadata_base import ProcessContentMetadataBase

        fields: dict[str, Callable[[Any], None]] = {
            "accessedResources": lambda n : setattr(self, 'accessed_resources', n.get_collection_of_primitive_values(str)),
            "parentMessageId": lambda n : setattr(self, 'parent_message_id', n.get_str_value()),
            "plugins": lambda n : setattr(self, 'plugins', n.get_collection_of_object_values(AiInteractionPlugin)),
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
        writer.write_collection_of_primitive_values("accessedResources", self.accessed_resources)
        writer.write_str_value("parentMessageId", self.parent_message_id)
        writer.write_collection_of_object_values("plugins", self.plugins)
    

