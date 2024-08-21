from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .attribute_flow_behavior import AttributeFlowBehavior
    from .attribute_flow_type import AttributeFlowType
    from .attribute_mapping_source import AttributeMappingSource

@dataclass
class AttributeMapping(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Default value to be used in case the source property was evaluated to null. Optional.
    default_value: Optional[str] = None
    # For internal use only.
    export_missing_references: Optional[bool] = None
    # The flowBehavior property
    flow_behavior: Optional[AttributeFlowBehavior] = None
    # The flowType property
    flow_type: Optional[AttributeFlowType] = None
    # If higher than 0, this attribute will be used to perform an initial match of the objects between source and target directories. The synchronization engine will try to find the matching object using attribute with lowest value of matching priority first. If not found, the attribute with the next matching priority will be used, and so on a until match is found or no more matching attributes are left. Only attributes that are expected to have unique values, such as email, should be used as matching attributes.
    matching_priority: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Defines how a value should be extracted (or transformed) from the source object.
    source: Optional[AttributeMappingSource] = None
    # Name of the attribute on the target object.
    target_attribute_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AttributeMapping:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AttributeMapping
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AttributeMapping()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .attribute_flow_behavior import AttributeFlowBehavior
        from .attribute_flow_type import AttributeFlowType
        from .attribute_mapping_source import AttributeMappingSource

        from .attribute_flow_behavior import AttributeFlowBehavior
        from .attribute_flow_type import AttributeFlowType
        from .attribute_mapping_source import AttributeMappingSource

        fields: Dict[str, Callable[[Any], None]] = {
            "defaultValue": lambda n : setattr(self, 'default_value', n.get_str_value()),
            "exportMissingReferences": lambda n : setattr(self, 'export_missing_references', n.get_bool_value()),
            "flowBehavior": lambda n : setattr(self, 'flow_behavior', n.get_enum_value(AttributeFlowBehavior)),
            "flowType": lambda n : setattr(self, 'flow_type', n.get_enum_value(AttributeFlowType)),
            "matchingPriority": lambda n : setattr(self, 'matching_priority', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "source": lambda n : setattr(self, 'source', n.get_object_value(AttributeMappingSource)),
            "targetAttributeName": lambda n : setattr(self, 'target_attribute_name', n.get_str_value()),
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
        writer.write_str_value("defaultValue", self.default_value)
        writer.write_bool_value("exportMissingReferences", self.export_missing_references)
        writer.write_enum_value("flowBehavior", self.flow_behavior)
        writer.write_enum_value("flowType", self.flow_type)
        writer.write_int_value("matchingPriority", self.matching_priority)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("source", self.source)
        writer.write_str_value("targetAttributeName", self.target_attribute_name)
        writer.write_additional_data_value(self.additional_data)
    

