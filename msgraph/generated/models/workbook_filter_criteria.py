from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .workbook_icon import WorkbookIcon

@dataclass
class WorkbookFilterCriteria(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The color applied to the cell.
    color: Optional[str] = None
    # A custom criterion.
    criterion1: Optional[str] = None
    # A custom criterion.
    criterion2: Optional[str] = None
    # A dynamic formula specified in a custom filter.
    dynamic_criteria: Optional[str] = None
    # Indicates whether a filter is applied to a column.
    filter_on: Optional[str] = None
    # An icon applied to a cell via conditional formatting.
    icon: Optional[WorkbookIcon] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # An operator in a cell; for example, =, >, <, <=, or <>.
    operator: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WorkbookFilterCriteria:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookFilterCriteria
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WorkbookFilterCriteria()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .workbook_icon import WorkbookIcon

        from .workbook_icon import WorkbookIcon

        fields: dict[str, Callable[[Any], None]] = {
            "color": lambda n : setattr(self, 'color', n.get_str_value()),
            "criterion1": lambda n : setattr(self, 'criterion1', n.get_str_value()),
            "criterion2": lambda n : setattr(self, 'criterion2', n.get_str_value()),
            "dynamicCriteria": lambda n : setattr(self, 'dynamic_criteria', n.get_str_value()),
            "filterOn": lambda n : setattr(self, 'filter_on', n.get_str_value()),
            "icon": lambda n : setattr(self, 'icon', n.get_object_value(WorkbookIcon)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "operator": lambda n : setattr(self, 'operator', n.get_str_value()),
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
        writer.write_str_value("color", self.color)
        writer.write_str_value("criterion1", self.criterion1)
        writer.write_str_value("criterion2", self.criterion2)
        writer.write_str_value("dynamicCriteria", self.dynamic_criteria)
        writer.write_str_value("filterOn", self.filter_on)
        writer.write_object_value("icon", self.icon)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("operator", self.operator)
        writer.write_additional_data_value(self.additional_data)
    

