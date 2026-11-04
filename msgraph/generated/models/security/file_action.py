from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .automated_action import AutomatedAction

from .automated_action import AutomatedAction

@dataclass
class FileAction(AutomatedAction, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.fileAction"
    # Names of the device groups where the file action applies.
    device_group_names: Optional[list[str]] = None
    # Name of the hunting-query result column that contains the SHA-1 hash of the targeted file.
    sha1_column: Optional[str] = None
    # Name of the hunting-query result column that contains the SHA-256 hash of the targeted file.
    sha256_column: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FileAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FileAction
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FileAction()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .automated_action import AutomatedAction

        from .automated_action import AutomatedAction

        fields: dict[str, Callable[[Any], None]] = {
            "deviceGroupNames": lambda n : setattr(self, 'device_group_names', n.get_collection_of_primitive_values(str)),
            "sha1Column": lambda n : setattr(self, 'sha1_column', n.get_str_value()),
            "sha256Column": lambda n : setattr(self, 'sha256_column', n.get_str_value()),
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
        writer.write_collection_of_primitive_values("deviceGroupNames", self.device_group_names)
        writer.write_str_value("sha1Column", self.sha1_column)
        writer.write_str_value("sha256Column", self.sha256_column)
    

