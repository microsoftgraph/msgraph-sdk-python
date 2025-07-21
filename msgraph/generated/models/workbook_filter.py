from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .workbook_filter_criteria import WorkbookFilterCriteria

from .entity import Entity

@dataclass
class WorkbookFilter(Entity, Parsable):
    # The currently applied filter on the given column. Read-only.
    criteria: Optional[WorkbookFilterCriteria] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WorkbookFilter:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookFilter
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WorkbookFilter()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .workbook_filter_criteria import WorkbookFilterCriteria

        from .entity import Entity
        from .workbook_filter_criteria import WorkbookFilterCriteria

        fields: dict[str, Callable[[Any], None]] = {
            "criteria": lambda n : setattr(self, 'criteria', n.get_object_value(WorkbookFilterCriteria)),
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
        writer.write_object_value("criteria", self.criteria)
    

