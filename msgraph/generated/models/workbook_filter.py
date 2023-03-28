from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, workbook_filter_criteria

from . import entity

class WorkbookFilter(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new workbookFilter and sets the default values.
        """
        super().__init__()
        # The currently applied filter on the given column. Read-only.
        self._criteria: Optional[workbook_filter_criteria.WorkbookFilterCriteria] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WorkbookFilter:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookFilter
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WorkbookFilter()
    
    @property
    def criteria(self,) -> Optional[workbook_filter_criteria.WorkbookFilterCriteria]:
        """
        Gets the criteria property value. The currently applied filter on the given column. Read-only.
        Returns: Optional[workbook_filter_criteria.WorkbookFilterCriteria]
        """
        return self._criteria
    
    @criteria.setter
    def criteria(self,value: Optional[workbook_filter_criteria.WorkbookFilterCriteria] = None) -> None:
        """
        Sets the criteria property value. The currently applied filter on the given column. Read-only.
        Args:
            value: Value to set for the criteria property.
        """
        self._criteria = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, workbook_filter_criteria

        fields: Dict[str, Callable[[Any], None]] = {
            "criteria": lambda n : setattr(self, 'criteria', n.get_object_value(workbook_filter_criteria.WorkbookFilterCriteria)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("criteria", self.criteria)
    

