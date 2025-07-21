from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .identity_set import IdentitySet
    from .retention_label_settings import RetentionLabelSettings

from .entity import Entity

@dataclass
class ItemRetentionLabel(Entity, Parsable):
    # Specifies whether the label is applied explicitly on the item. True indicates that the label is applied explicitly; otherwise, the label is inherited from its parent. Read-only.
    is_label_applied_explicitly: Optional[bool] = None
    # Identity of the user who applied the label. Read-only.
    label_applied_by: Optional[IdentitySet] = None
    # The date and time when the label was applied on the item. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    label_applied_date_time: Optional[datetime.datetime] = None
    # The retention label on the document. Read-write.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The retention settings enforced on the item. Read-write.
    retention_settings: Optional[RetentionLabelSettings] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ItemRetentionLabel:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ItemRetentionLabel
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ItemRetentionLabel()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .identity_set import IdentitySet
        from .retention_label_settings import RetentionLabelSettings

        from .entity import Entity
        from .identity_set import IdentitySet
        from .retention_label_settings import RetentionLabelSettings

        fields: dict[str, Callable[[Any], None]] = {
            "isLabelAppliedExplicitly": lambda n : setattr(self, 'is_label_applied_explicitly', n.get_bool_value()),
            "labelAppliedBy": lambda n : setattr(self, 'label_applied_by', n.get_object_value(IdentitySet)),
            "labelAppliedDateTime": lambda n : setattr(self, 'label_applied_date_time', n.get_datetime_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "retentionSettings": lambda n : setattr(self, 'retention_settings', n.get_object_value(RetentionLabelSettings)),
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
        writer.write_bool_value("isLabelAppliedExplicitly", self.is_label_applied_explicitly)
        writer.write_object_value("labelAppliedBy", self.label_applied_by)
        writer.write_datetime_value("labelAppliedDateTime", self.label_applied_date_time)
        writer.write_str_value("name", self.name)
        writer.write_object_value("retentionSettings", self.retention_settings)
    

