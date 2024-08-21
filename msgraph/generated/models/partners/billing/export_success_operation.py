from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .manifest import Manifest
    from .operation import Operation

from .operation import Operation

@dataclass
class ExportSuccessOperation(Operation):
    # The OdataType property
    odata_type: Optional[str] = None
    # The resourceLocation property
    resource_location: Optional[Manifest] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ExportSuccessOperation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ExportSuccessOperation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ExportSuccessOperation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .manifest import Manifest
        from .operation import Operation

        from .manifest import Manifest
        from .operation import Operation

        fields: Dict[str, Callable[[Any], None]] = {
            "resourceLocation": lambda n : setattr(self, 'resource_location', n.get_object_value(Manifest)),
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
        writer.write_object_value("resourceLocation", self.resource_location)
    

