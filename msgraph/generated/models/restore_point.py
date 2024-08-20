from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .protection_unit_base import ProtectionUnitBase
    from .restore_point_tags import RestorePointTags

from .entity import Entity

@dataclass
class RestorePoint(Entity):
    # Expiration date time of the restore point.
    expiration_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Date time when the restore point was created.
    protection_date_time: Optional[datetime.datetime] = None
    # The site, drive, or mailbox units that are protected under a protection policy.
    protection_unit: Optional[ProtectionUnitBase] = None
    # The type of the restore point. The possible values are: none, fastRestore, unknownFutureValue.
    tags: Optional[RestorePointTags] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RestorePoint:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RestorePoint
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RestorePoint()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .protection_unit_base import ProtectionUnitBase
        from .restore_point_tags import RestorePointTags

        from .entity import Entity
        from .protection_unit_base import ProtectionUnitBase
        from .restore_point_tags import RestorePointTags

        fields: Dict[str, Callable[[Any], None]] = {
            "expirationDateTime": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "protectionDateTime": lambda n : setattr(self, 'protection_date_time', n.get_datetime_value()),
            "protectionUnit": lambda n : setattr(self, 'protection_unit', n.get_object_value(ProtectionUnitBase)),
            "tags": lambda n : setattr(self, 'tags', n.get_collection_of_enum_values(RestorePointTags)),
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
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_datetime_value("protectionDateTime", self.protection_date_time)
        writer.write_object_value("protectionUnit", self.protection_unit)
        writer.write_enum_value("tags", self.tags)
    

