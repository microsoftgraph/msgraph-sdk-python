from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
json = lazy_import('msgraph.generated.models.json')
workbook_worksheet = lazy_import('msgraph.generated.models.workbook_worksheet')

class WorkbookNamedItem(entity.Entity):
    """
    Provides operations to manage the collection of agreement entities.
    """
    @property
    def comment(self,) -> Optional[str]:
        """
        Gets the comment property value. Represents the comment associated with this name.
        Returns: Optional[str]
        """
        return self._comment
    
    @comment.setter
    def comment(self,value: Optional[str] = None) -> None:
        """
        Sets the comment property value. Represents the comment associated with this name.
        Args:
            value: Value to set for the comment property.
        """
        self._comment = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new workbookNamedItem and sets the default values.
        """
        super().__init__()
        # Represents the comment associated with this name.
        self._comment: Optional[str] = None
        # The name of the object. Read-only.
        self._name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Indicates whether the name is scoped to the workbook or to a specific worksheet. Read-only.
        self._scope: Optional[str] = None
        # Indicates what type of reference is associated with the name. The possible values are: String, Integer, Double, Boolean, Range. Read-only.
        self._type: Optional[str] = None
        # Represents the formula that the name is defined to refer to. E.g. =Sheet14!$B$2:$H$12, =4.75, etc. Read-only.
        self._value: Optional[json.Json] = None
        # Specifies whether the object is visible or not.
        self._visible: Optional[bool] = None
        # Returns the worksheet on which the named item is scoped to. Available only if the item is scoped to the worksheet. Read-only.
        self._worksheet: Optional[workbook_worksheet.WorkbookWorksheet] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WorkbookNamedItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookNamedItem
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WorkbookNamedItem()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "comment": lambda n : setattr(self, 'comment', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "scope": lambda n : setattr(self, 'scope', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
            "value": lambda n : setattr(self, 'value', n.get_object_value(json.Json)),
            "visible": lambda n : setattr(self, 'visible', n.get_bool_value()),
            "worksheet": lambda n : setattr(self, 'worksheet', n.get_object_value(workbook_worksheet.WorkbookWorksheet)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. The name of the object. Read-only.
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. The name of the object. Read-only.
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
    @property
    def scope(self,) -> Optional[str]:
        """
        Gets the scope property value. Indicates whether the name is scoped to the workbook or to a specific worksheet. Read-only.
        Returns: Optional[str]
        """
        return self._scope
    
    @scope.setter
    def scope(self,value: Optional[str] = None) -> None:
        """
        Sets the scope property value. Indicates whether the name is scoped to the workbook or to a specific worksheet. Read-only.
        Args:
            value: Value to set for the scope property.
        """
        self._scope = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("comment", self.comment)
        writer.write_str_value("name", self.name)
        writer.write_str_value("scope", self.scope)
        writer.write_str_value("type", self.type)
        writer.write_object_value("value", self.value)
        writer.write_bool_value("visible", self.visible)
        writer.write_object_value("worksheet", self.worksheet)
    
    @property
    def type(self,) -> Optional[str]:
        """
        Gets the type property value. Indicates what type of reference is associated with the name. The possible values are: String, Integer, Double, Boolean, Range. Read-only.
        Returns: Optional[str]
        """
        return self._type
    
    @type.setter
    def type(self,value: Optional[str] = None) -> None:
        """
        Sets the type property value. Indicates what type of reference is associated with the name. The possible values are: String, Integer, Double, Boolean, Range. Read-only.
        Args:
            value: Value to set for the type property.
        """
        self._type = value
    
    @property
    def value(self,) -> Optional[json.Json]:
        """
        Gets the value property value. Represents the formula that the name is defined to refer to. E.g. =Sheet14!$B$2:$H$12, =4.75, etc. Read-only.
        Returns: Optional[json.Json]
        """
        return self._value
    
    @value.setter
    def value(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the value property value. Represents the formula that the name is defined to refer to. E.g. =Sheet14!$B$2:$H$12, =4.75, etc. Read-only.
        Args:
            value: Value to set for the value property.
        """
        self._value = value
    
    @property
    def visible(self,) -> Optional[bool]:
        """
        Gets the visible property value. Specifies whether the object is visible or not.
        Returns: Optional[bool]
        """
        return self._visible
    
    @visible.setter
    def visible(self,value: Optional[bool] = None) -> None:
        """
        Sets the visible property value. Specifies whether the object is visible or not.
        Args:
            value: Value to set for the visible property.
        """
        self._visible = value
    
    @property
    def worksheet(self,) -> Optional[workbook_worksheet.WorkbookWorksheet]:
        """
        Gets the worksheet property value. Returns the worksheet on which the named item is scoped to. Available only if the item is scoped to the worksheet. Read-only.
        Returns: Optional[workbook_worksheet.WorkbookWorksheet]
        """
        return self._worksheet
    
    @worksheet.setter
    def worksheet(self,value: Optional[workbook_worksheet.WorkbookWorksheet] = None) -> None:
        """
        Sets the worksheet property value. Returns the worksheet on which the named item is scoped to. Available only if the item is scoped to the worksheet. Read-only.
        Args:
            value: Value to set for the worksheet property.
        """
        self._worksheet = value
    

