from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import onenote_patch_action_type, onenote_patch_insert_position

@dataclass
class OnenotePatchContentCommand(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The action property
    action: Optional[onenote_patch_action_type.OnenotePatchActionType] = None
    # A string of well-formed HTML to add to the page, and any image or file binary data. If the content contains binary data, the request must be sent using the multipart/form-data content type with a 'Commands' part.
    content: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The location to add the supplied content, relative to the target element. The possible values are: after (default) or before.
    position: Optional[onenote_patch_insert_position.OnenotePatchInsertPosition] = None
    # The element to update. Must be the #<data-id> or the generated <id> of the element, or the body or title keyword.
    target: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OnenotePatchContentCommand:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OnenotePatchContentCommand
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OnenotePatchContentCommand()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import onenote_patch_action_type, onenote_patch_insert_position

        fields: Dict[str, Callable[[Any], None]] = {
            "action": lambda n : setattr(self, 'action', n.get_enum_value(onenote_patch_action_type.OnenotePatchActionType)),
            "content": lambda n : setattr(self, 'content', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "position": lambda n : setattr(self, 'position', n.get_enum_value(onenote_patch_insert_position.OnenotePatchInsertPosition)),
            "target": lambda n : setattr(self, 'target', n.get_str_value()),
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
        writer.write_enum_value("action", self.action)
        writer.write_str_value("content", self.content)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("position", self.position)
        writer.write_str_value("target", self.target)
        writer.write_additional_data_value(self.additional_data)
    

