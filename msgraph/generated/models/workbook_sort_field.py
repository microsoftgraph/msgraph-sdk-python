from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .workbook_icon import WorkbookIcon

@dataclass
class WorkbookSortField(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Represents whether the sorting is done in an ascending fashion.
    ascending: Optional[bool] = None
    # Represents the color that is the target of the condition if the sorting is on font or cell color.
    color: Optional[str] = None
    # Represents additional sorting options for this field. The possible values are: Normal, TextAsNumber.
    data_option: Optional[str] = None
    # Represents the icon that is the target of the condition if the sorting is on the cell's icon.
    icon: Optional[WorkbookIcon] = None
    # Represents the column (or row, depending on the sort orientation) that the condition is on. Represented as an offset from the first column (or row).
    key: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents the type of sorting of this condition. The possible values are: Value, CellColor, FontColor, Icon.
    sort_on: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WorkbookSortField:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookSortField
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WorkbookSortField()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .workbook_icon import WorkbookIcon

        from .workbook_icon import WorkbookIcon

        fields: dict[str, Callable[[Any], None]] = {
            "ascending": lambda n : setattr(self, 'ascending', n.get_bool_value()),
            "color": lambda n : setattr(self, 'color', n.get_str_value()),
            "dataOption": lambda n : setattr(self, 'data_option', n.get_str_value()),
            "icon": lambda n : setattr(self, 'icon', n.get_object_value(WorkbookIcon)),
            "key": lambda n : setattr(self, 'key', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "sortOn": lambda n : setattr(self, 'sort_on', n.get_str_value()),
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
        writer.write_bool_value("ascending", self.ascending)
        writer.write_str_value("color", self.color)
        writer.write_str_value("dataOption", self.data_option)
        writer.write_object_value("icon", self.icon)
        writer.write_int_value("key", self.key)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("sortOn", self.sort_on)
        writer.write_additional_data_value(self.additional_data)
    

