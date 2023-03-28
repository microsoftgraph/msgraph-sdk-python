from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity

from . import entity

class WorkbookApplication(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new workbookApplication and sets the default values.
        """
        super().__init__()
        # Returns the calculation mode used in the workbook. Possible values are: Automatic, AutomaticExceptTables, Manual.
        self._calculation_mode: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @property
    def calculation_mode(self,) -> Optional[str]:
        """
        Gets the calculationMode property value. Returns the calculation mode used in the workbook. Possible values are: Automatic, AutomaticExceptTables, Manual.
        Returns: Optional[str]
        """
        return self._calculation_mode
    
    @calculation_mode.setter
    def calculation_mode(self,value: Optional[str] = None) -> None:
        """
        Sets the calculationMode property value. Returns the calculation mode used in the workbook. Possible values are: Automatic, AutomaticExceptTables, Manual.
        Args:
            value: Value to set for the calculation_mode property.
        """
        self._calculation_mode = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WorkbookApplication:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookApplication
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WorkbookApplication()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "calculationMode": lambda n : setattr(self, 'calculation_mode', n.get_str_value()),
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
        writer.write_str_value("calculationMode", self.calculation_mode)
    

