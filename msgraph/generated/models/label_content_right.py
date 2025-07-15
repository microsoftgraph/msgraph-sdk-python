from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .sensitivity_label import SensitivityLabel
    from .usage_rights import UsageRights

from .entity import Entity

@dataclass
class LabelContentRight(Entity, Parsable):
    # The content identifier.
    cid: Optional[str] = None
    # The content format.
    format: Optional[str] = None
    # The label property
    label: Optional[SensitivityLabel] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The rights property
    rights: Optional[UsageRights] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LabelContentRight:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LabelContentRight
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LabelContentRight()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .sensitivity_label import SensitivityLabel
        from .usage_rights import UsageRights

        from .entity import Entity
        from .sensitivity_label import SensitivityLabel
        from .usage_rights import UsageRights

        fields: dict[str, Callable[[Any], None]] = {
            "cid": lambda n : setattr(self, 'cid', n.get_str_value()),
            "format": lambda n : setattr(self, 'format', n.get_str_value()),
            "label": lambda n : setattr(self, 'label', n.get_object_value(SensitivityLabel)),
            "rights": lambda n : setattr(self, 'rights', n.get_collection_of_enum_values(UsageRights)),
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
        writer.write_str_value("cid", self.cid)
        writer.write_str_value("format", self.format)
        writer.write_object_value("label", self.label)
        writer.write_enum_value("rights", self.rights)
    

