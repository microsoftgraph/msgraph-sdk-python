from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .workbook_worksheet_protection_options import WorkbookWorksheetProtectionOptions

from .entity import Entity

@dataclass
class WorkbookWorksheetProtection(Entity, Parsable):
    # The OdataType property
    odata_type: Optional[str] = None
    # Worksheet protection options. Read-only.
    options: Optional[WorkbookWorksheetProtectionOptions] = None
    # Indicates whether the worksheet is protected.  Read-only.
    protected: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WorkbookWorksheetProtection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookWorksheetProtection
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WorkbookWorksheetProtection()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .workbook_worksheet_protection_options import WorkbookWorksheetProtectionOptions

        from .entity import Entity
        from .workbook_worksheet_protection_options import WorkbookWorksheetProtectionOptions

        fields: dict[str, Callable[[Any], None]] = {
            "options": lambda n : setattr(self, 'options', n.get_object_value(WorkbookWorksheetProtectionOptions)),
            "protected": lambda n : setattr(self, 'protected', n.get_bool_value()),
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
        writer.write_object_value("options", self.options)
        writer.write_bool_value("protected", self.protected)
    

