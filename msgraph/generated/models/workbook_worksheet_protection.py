from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
workbook_worksheet_protection_options = lazy_import('msgraph.generated.models.workbook_worksheet_protection_options')

class WorkbookWorksheetProtection(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new workbookWorksheetProtection and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Sheet protection options. Read-only.
        self._options: Optional[workbook_worksheet_protection_options.WorkbookWorksheetProtectionOptions] = None
        # Indicates if the worksheet is protected.  Read-only.
        self._protected: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WorkbookWorksheetProtection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookWorksheetProtection
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WorkbookWorksheetProtection()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "options": lambda n : setattr(self, 'options', n.get_object_value(workbook_worksheet_protection_options.WorkbookWorksheetProtectionOptions)),
            "protected": lambda n : setattr(self, 'protected', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def options(self,) -> Optional[workbook_worksheet_protection_options.WorkbookWorksheetProtectionOptions]:
        """
        Gets the options property value. Sheet protection options. Read-only.
        Returns: Optional[workbook_worksheet_protection_options.WorkbookWorksheetProtectionOptions]
        """
        return self._options
    
    @options.setter
    def options(self,value: Optional[workbook_worksheet_protection_options.WorkbookWorksheetProtectionOptions] = None) -> None:
        """
        Sets the options property value. Sheet protection options. Read-only.
        Args:
            value: Value to set for the options property.
        """
        self._options = value
    
    @property
    def protected(self,) -> Optional[bool]:
        """
        Gets the protected property value. Indicates if the worksheet is protected.  Read-only.
        Returns: Optional[bool]
        """
        return self._protected
    
    @protected.setter
    def protected(self,value: Optional[bool] = None) -> None:
        """
        Sets the protected property value. Indicates if the worksheet is protected.  Read-only.
        Args:
            value: Value to set for the protected property.
        """
        self._protected = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("options", self.options)
        writer.write_bool_value("protected", self.protected)
    

