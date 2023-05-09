from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import property_rule
    from .. import json

class DisplayTemplate(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new displayTemplate and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The text identifier for the display template; for example, contosoTickets. Maximum 16 characters. Only alphanumeric characters allowed.
        self._id: Optional[str] = None
        # The layout property
        self._layout: Optional[json.Json] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Defines the priority of a display template. A display template with priority 1 is evaluated before a template with priority 4. Gaps in priority values are supported. Must be positive value.
        self._priority: Optional[int] = None
        # Specifies additional rules for selecting this display template based on the item schema. Optional.
        self._rules: Optional[List[property_rule.PropertyRule]] = None
    
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DisplayTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DisplayTemplate
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DisplayTemplate()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import property_rule
        from .. import json

        fields: Dict[str, Callable[[Any], None]] = {
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "layout": lambda n : setattr(self, 'layout', n.get_object_value(json.Json)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "priority": lambda n : setattr(self, 'priority', n.get_int_value()),
            "rules": lambda n : setattr(self, 'rules', n.get_collection_of_object_values(property_rule.PropertyRule)),
        }
        return fields
    
    @property
    def id(self,) -> Optional[str]:
        """
        Gets the id property value. The text identifier for the display template; for example, contosoTickets. Maximum 16 characters. Only alphanumeric characters allowed.
        Returns: Optional[str]
        """
        return self._id
    
    @id.setter
    def id(self,value: Optional[str] = None) -> None:
        """
        Sets the id property value. The text identifier for the display template; for example, contosoTickets. Maximum 16 characters. Only alphanumeric characters allowed.
        Args:
            value: Value to set for the id property.
        """
        self._id = value
    
    @property
    def layout(self,) -> Optional[json.Json]:
        """
        Gets the layout property value. The layout property
        Returns: Optional[json.Json]
        """
        return self._layout
    
    @layout.setter
    def layout(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the layout property value. The layout property
        Args:
            value: Value to set for the layout property.
        """
        self._layout = value
    
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
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    @property
    def priority(self,) -> Optional[int]:
        """
        Gets the priority property value. Defines the priority of a display template. A display template with priority 1 is evaluated before a template with priority 4. Gaps in priority values are supported. Must be positive value.
        Returns: Optional[int]
        """
        return self._priority
    
    @priority.setter
    def priority(self,value: Optional[int] = None) -> None:
        """
        Sets the priority property value. Defines the priority of a display template. A display template with priority 1 is evaluated before a template with priority 4. Gaps in priority values are supported. Must be positive value.
        Args:
            value: Value to set for the priority property.
        """
        self._priority = value
    
    @property
    def rules(self,) -> Optional[List[property_rule.PropertyRule]]:
        """
        Gets the rules property value. Specifies additional rules for selecting this display template based on the item schema. Optional.
        Returns: Optional[List[property_rule.PropertyRule]]
        """
        return self._rules
    
    @rules.setter
    def rules(self,value: Optional[List[property_rule.PropertyRule]] = None) -> None:
        """
        Sets the rules property value. Specifies additional rules for selecting this display template based on the item schema. Optional.
        Args:
            value: Value to set for the rules property.
        """
        self._rules = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("id", self.id)
        writer.write_object_value("layout", self.layout)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("priority", self.priority)
        writer.write_collection_of_object_values("rules", self.rules)
        writer.write_additional_data_value(self.additional_data)
    

