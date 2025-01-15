from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .onenote_patch_action_type import OnenotePatchActionType
    from .onenote_patch_insert_position import OnenotePatchInsertPosition

@dataclass
class OnenotePatchContentCommand(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The action property
    action: Optional[OnenotePatchActionType] = None
    # A string of well-formed HTML to add to the page, and any image or file binary data. If the content contains binary data, the request must be sent using the multipart/form-data content type with a 'Commands' part.
    content: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The location to add the supplied content, relative to the target element. The possible values are: after (default) or before.
    position: Optional[OnenotePatchInsertPosition] = None
    # The element to update. Must be the #<data-id> or the generated <id> of the element, or the body or title keyword.
    target: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OnenotePatchContentCommand:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OnenotePatchContentCommand
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OnenotePatchContentCommand()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .onenote_patch_action_type import OnenotePatchActionType
        from .onenote_patch_insert_position import OnenotePatchInsertPosition

        from .onenote_patch_action_type import OnenotePatchActionType
        from .onenote_patch_insert_position import OnenotePatchInsertPosition

        fields: dict[str, Callable[[Any], None]] = {
            "action": lambda n : setattr(self, 'action', n.get_enum_value(OnenotePatchActionType)),
            "content": lambda n : setattr(self, 'content', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "position": lambda n : setattr(self, 'position', n.get_enum_value(OnenotePatchInsertPosition)),
            "target": lambda n : setattr(self, 'target', n.get_str_value()),
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
        writer.write_enum_value("action", self.action)
        writer.write_str_value("content", self.content)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("position", self.position)
        writer.write_str_value("target", self.target)
        writer.write_additional_data_value(self.additional_data)
    

