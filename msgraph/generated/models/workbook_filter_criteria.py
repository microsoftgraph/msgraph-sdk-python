from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

json = lazy_import('msgraph.generated.models.json')
workbook_icon = lazy_import('msgraph.generated.models.workbook_icon')

class WorkbookFilterCriteria(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def color(self,) -> Optional[str]:
        """
        Gets the color property value. The color property
        Returns: Optional[str]
        """
        return self._color
    
    @color.setter
    def color(self,value: Optional[str] = None) -> None:
        """
        Sets the color property value. The color property
        Args:
            value: Value to set for the color property.
        """
        self._color = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new workbookFilterCriteria and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The color property
        self._color: Optional[str] = None
        # The criterion1 property
        self._criterion1: Optional[str] = None
        # The criterion2 property
        self._criterion2: Optional[str] = None
        # The dynamicCriteria property
        self._dynamic_criteria: Optional[str] = None
        # The filterOn property
        self._filter_on: Optional[str] = None
        # The icon property
        self._icon: Optional[workbook_icon.WorkbookIcon] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The operator property
        self._operator: Optional[str] = None
        # The values property
        self._values: Optional[json.Json] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WorkbookFilterCriteria:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookFilterCriteria
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WorkbookFilterCriteria()
    
    @property
    def criterion1(self,) -> Optional[str]:
        """
        Gets the criterion1 property value. The criterion1 property
        Returns: Optional[str]
        """
        return self._criterion1
    
    @criterion1.setter
    def criterion1(self,value: Optional[str] = None) -> None:
        """
        Sets the criterion1 property value. The criterion1 property
        Args:
            value: Value to set for the criterion1 property.
        """
        self._criterion1 = value
    
    @property
    def criterion2(self,) -> Optional[str]:
        """
        Gets the criterion2 property value. The criterion2 property
        Returns: Optional[str]
        """
        return self._criterion2
    
    @criterion2.setter
    def criterion2(self,value: Optional[str] = None) -> None:
        """
        Sets the criterion2 property value. The criterion2 property
        Args:
            value: Value to set for the criterion2 property.
        """
        self._criterion2 = value
    
    @property
    def dynamic_criteria(self,) -> Optional[str]:
        """
        Gets the dynamicCriteria property value. The dynamicCriteria property
        Returns: Optional[str]
        """
        return self._dynamic_criteria
    
    @dynamic_criteria.setter
    def dynamic_criteria(self,value: Optional[str] = None) -> None:
        """
        Sets the dynamicCriteria property value. The dynamicCriteria property
        Args:
            value: Value to set for the dynamicCriteria property.
        """
        self._dynamic_criteria = value
    
    @property
    def filter_on(self,) -> Optional[str]:
        """
        Gets the filterOn property value. The filterOn property
        Returns: Optional[str]
        """
        return self._filter_on
    
    @filter_on.setter
    def filter_on(self,value: Optional[str] = None) -> None:
        """
        Sets the filterOn property value. The filterOn property
        Args:
            value: Value to set for the filterOn property.
        """
        self._filter_on = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "color": lambda n : setattr(self, 'color', n.get_str_value()),
            "criterion1": lambda n : setattr(self, 'criterion1', n.get_str_value()),
            "criterion2": lambda n : setattr(self, 'criterion2', n.get_str_value()),
            "dynamic_criteria": lambda n : setattr(self, 'dynamic_criteria', n.get_str_value()),
            "filter_on": lambda n : setattr(self, 'filter_on', n.get_str_value()),
            "icon": lambda n : setattr(self, 'icon', n.get_object_value(workbook_icon.WorkbookIcon)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "operator": lambda n : setattr(self, 'operator', n.get_str_value()),
            "values": lambda n : setattr(self, 'values', n.get_object_value(json.Json)),
        }
        return fields
    
    @property
    def icon(self,) -> Optional[workbook_icon.WorkbookIcon]:
        """
        Gets the icon property value. The icon property
        Returns: Optional[workbook_icon.WorkbookIcon]
        """
        return self._icon
    
    @icon.setter
    def icon(self,value: Optional[workbook_icon.WorkbookIcon] = None) -> None:
        """
        Sets the icon property value. The icon property
        Args:
            value: Value to set for the icon property.
        """
        self._icon = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def operator(self,) -> Optional[str]:
        """
        Gets the operator property value. The operator property
        Returns: Optional[str]
        """
        return self._operator
    
    @operator.setter
    def operator(self,value: Optional[str] = None) -> None:
        """
        Sets the operator property value. The operator property
        Args:
            value: Value to set for the operator property.
        """
        self._operator = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("color", self.color)
        writer.write_str_value("criterion1", self.criterion1)
        writer.write_str_value("criterion2", self.criterion2)
        writer.write_str_value("dynamicCriteria", self.dynamic_criteria)
        writer.write_str_value("filterOn", self.filter_on)
        writer.write_object_value("icon", self.icon)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("operator", self.operator)
        writer.write_object_value("values", self.values)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def values(self,) -> Optional[json.Json]:
        """
        Gets the values property value. The values property
        Returns: Optional[json.Json]
        """
        return self._values
    
    @values.setter
    def values(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the values property value. The values property
        Args:
            value: Value to set for the values property.
        """
        self._values = value
    

