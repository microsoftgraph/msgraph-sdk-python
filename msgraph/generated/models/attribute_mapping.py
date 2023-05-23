from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import attribute_flow_behavior, attribute_flow_type, attribute_mapping_source

class AttributeMapping(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new attributeMapping and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The defaultValue property
        self._default_value: Optional[str] = None
        # The exportMissingReferences property
        self._export_missing_references: Optional[bool] = None
        # The flowBehavior property
        self._flow_behavior: Optional[attribute_flow_behavior.AttributeFlowBehavior] = None
        # The flowType property
        self._flow_type: Optional[attribute_flow_type.AttributeFlowType] = None
        # The matchingPriority property
        self._matching_priority: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The source property
        self._source: Optional[attribute_mapping_source.AttributeMappingSource] = None
        # The targetAttributeName property
        self._target_attribute_name: Optional[str] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AttributeMapping:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AttributeMapping
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AttributeMapping()
    
    @property
    def default_value(self,) -> Optional[str]:
        """
        Gets the defaultValue property value. The defaultValue property
        Returns: Optional[str]
        """
        return self._default_value
    
    @default_value.setter
    def default_value(self,value: Optional[str] = None) -> None:
        """
        Sets the defaultValue property value. The defaultValue property
        Args:
            value: Value to set for the default_value property.
        """
        self._default_value = value
    
    @property
    def export_missing_references(self,) -> Optional[bool]:
        """
        Gets the exportMissingReferences property value. The exportMissingReferences property
        Returns: Optional[bool]
        """
        return self._export_missing_references
    
    @export_missing_references.setter
    def export_missing_references(self,value: Optional[bool] = None) -> None:
        """
        Sets the exportMissingReferences property value. The exportMissingReferences property
        Args:
            value: Value to set for the export_missing_references property.
        """
        self._export_missing_references = value
    
    @property
    def flow_behavior(self,) -> Optional[attribute_flow_behavior.AttributeFlowBehavior]:
        """
        Gets the flowBehavior property value. The flowBehavior property
        Returns: Optional[attribute_flow_behavior.AttributeFlowBehavior]
        """
        return self._flow_behavior
    
    @flow_behavior.setter
    def flow_behavior(self,value: Optional[attribute_flow_behavior.AttributeFlowBehavior] = None) -> None:
        """
        Sets the flowBehavior property value. The flowBehavior property
        Args:
            value: Value to set for the flow_behavior property.
        """
        self._flow_behavior = value
    
    @property
    def flow_type(self,) -> Optional[attribute_flow_type.AttributeFlowType]:
        """
        Gets the flowType property value. The flowType property
        Returns: Optional[attribute_flow_type.AttributeFlowType]
        """
        return self._flow_type
    
    @flow_type.setter
    def flow_type(self,value: Optional[attribute_flow_type.AttributeFlowType] = None) -> None:
        """
        Sets the flowType property value. The flowType property
        Args:
            value: Value to set for the flow_type property.
        """
        self._flow_type = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import attribute_flow_behavior, attribute_flow_type, attribute_mapping_source

        fields: Dict[str, Callable[[Any], None]] = {
            "defaultValue": lambda n : setattr(self, 'default_value', n.get_str_value()),
            "exportMissingReferences": lambda n : setattr(self, 'export_missing_references', n.get_bool_value()),
            "flowBehavior": lambda n : setattr(self, 'flow_behavior', n.get_enum_value(attribute_flow_behavior.AttributeFlowBehavior)),
            "flowType": lambda n : setattr(self, 'flow_type', n.get_enum_value(attribute_flow_type.AttributeFlowType)),
            "matchingPriority": lambda n : setattr(self, 'matching_priority', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "source": lambda n : setattr(self, 'source', n.get_object_value(attribute_mapping_source.AttributeMappingSource)),
            "targetAttributeName": lambda n : setattr(self, 'target_attribute_name', n.get_str_value()),
        }
        return fields
    
    @property
    def matching_priority(self,) -> Optional[int]:
        """
        Gets the matchingPriority property value. The matchingPriority property
        Returns: Optional[int]
        """
        return self._matching_priority
    
    @matching_priority.setter
    def matching_priority(self,value: Optional[int] = None) -> None:
        """
        Sets the matchingPriority property value. The matchingPriority property
        Args:
            value: Value to set for the matching_priority property.
        """
        self._matching_priority = value
    
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("defaultValue", self.default_value)
        writer.write_bool_value("exportMissingReferences", self.export_missing_references)
        writer.write_enum_value("flowBehavior", self.flow_behavior)
        writer.write_enum_value("flowType", self.flow_type)
        writer.write_int_value("matchingPriority", self.matching_priority)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("source", self.source)
        writer.write_str_value("targetAttributeName", self.target_attribute_name)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def source(self,) -> Optional[attribute_mapping_source.AttributeMappingSource]:
        """
        Gets the source property value. The source property
        Returns: Optional[attribute_mapping_source.AttributeMappingSource]
        """
        return self._source
    
    @source.setter
    def source(self,value: Optional[attribute_mapping_source.AttributeMappingSource] = None) -> None:
        """
        Sets the source property value. The source property
        Args:
            value: Value to set for the source property.
        """
        self._source = value
    
    @property
    def target_attribute_name(self,) -> Optional[str]:
        """
        Gets the targetAttributeName property value. The targetAttributeName property
        Returns: Optional[str]
        """
        return self._target_attribute_name
    
    @target_attribute_name.setter
    def target_attribute_name(self,value: Optional[str] = None) -> None:
        """
        Sets the targetAttributeName property value. The targetAttributeName property
        Args:
            value: Value to set for the target_attribute_name property.
        """
        self._target_attribute_name = value
    

