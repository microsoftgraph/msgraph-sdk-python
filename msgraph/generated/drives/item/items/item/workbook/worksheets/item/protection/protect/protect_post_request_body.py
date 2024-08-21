from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..........models.workbook_worksheet_protection_options import WorkbookWorksheetProtectionOptions

@dataclass
class ProtectPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The options property
    options: Optional[WorkbookWorksheetProtectionOptions] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ProtectPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ProtectPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ProtectPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..........models.workbook_worksheet_protection_options import WorkbookWorksheetProtectionOptions

        from ..........models.workbook_worksheet_protection_options import WorkbookWorksheetProtectionOptions

        fields: Dict[str, Callable[[Any], None]] = {
            "options": lambda n : setattr(self, 'options', n.get_object_value(WorkbookWorksheetProtectionOptions)),
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
        writer.write_object_value("options", self.options)
        writer.write_additional_data_value(self.additional_data)
    

