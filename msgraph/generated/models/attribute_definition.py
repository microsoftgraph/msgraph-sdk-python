from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .attribute_definition_metadata_entry import AttributeDefinitionMetadataEntry
    from .attribute_type import AttributeType
    from .mutability import Mutability
    from .referenced_object import ReferencedObject
    from .string_key_string_value_pair import StringKeyStringValuePair

@dataclass
class AttributeDefinition(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # true if the attribute should be used as the anchor for the object. Anchor attributes must have a unique value identifying an object, and must be immutable. Default is false. One, and only one, of the object's attributes must be designated as the anchor to support synchronization.
    anchor: Optional[bool] = None
    # The apiExpressions property
    api_expressions: Optional[List[StringKeyStringValuePair]] = None
    # true if value of this attribute should be treated as case-sensitive. This setting affects how the synchronization engine detects changes for the attribute.
    case_exact: Optional[bool] = None
    # The default value of the attribute.
    default_value: Optional[str] = None
    # 'true' to allow null values for attributes.
    flow_null_values: Optional[bool] = None
    # Metadata for the given object.
    metadata: Optional[List[AttributeDefinitionMetadataEntry]] = None
    # true if an attribute can have multiple values. Default is false.
    multivalued: Optional[bool] = None
    # The mutability property
    mutability: Optional[Mutability] = None
    # Name of the attribute. Must be unique within the object definition. Not nullable.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # For attributes with reference type, lists referenced objects (for example, the manager attribute would list User as the referenced object).
    referenced_objects: Optional[List[ReferencedObject]] = None
    # true if attribute is required. Object can not be created if any of the required attributes are missing. If during synchronization, the required attribute has no value, the default value will be used. If default the value was not set, synchronization will record an error.
    required: Optional[bool] = None
    # The type property
    type: Optional[AttributeType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AttributeDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AttributeDefinition
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AttributeDefinition()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .attribute_definition_metadata_entry import AttributeDefinitionMetadataEntry
        from .attribute_type import AttributeType
        from .mutability import Mutability
        from .referenced_object import ReferencedObject
        from .string_key_string_value_pair import StringKeyStringValuePair

        from .attribute_definition_metadata_entry import AttributeDefinitionMetadataEntry
        from .attribute_type import AttributeType
        from .mutability import Mutability
        from .referenced_object import ReferencedObject
        from .string_key_string_value_pair import StringKeyStringValuePair

        fields: Dict[str, Callable[[Any], None]] = {
            "anchor": lambda n : setattr(self, 'anchor', n.get_bool_value()),
            "apiExpressions": lambda n : setattr(self, 'api_expressions', n.get_collection_of_object_values(StringKeyStringValuePair)),
            "caseExact": lambda n : setattr(self, 'case_exact', n.get_bool_value()),
            "defaultValue": lambda n : setattr(self, 'default_value', n.get_str_value()),
            "flowNullValues": lambda n : setattr(self, 'flow_null_values', n.get_bool_value()),
            "metadata": lambda n : setattr(self, 'metadata', n.get_collection_of_object_values(AttributeDefinitionMetadataEntry)),
            "multivalued": lambda n : setattr(self, 'multivalued', n.get_bool_value()),
            "mutability": lambda n : setattr(self, 'mutability', n.get_enum_value(Mutability)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "referencedObjects": lambda n : setattr(self, 'referenced_objects', n.get_collection_of_object_values(ReferencedObject)),
            "required": lambda n : setattr(self, 'required', n.get_bool_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(AttributeType)),
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
        writer.write_bool_value("anchor", self.anchor)
        writer.write_collection_of_object_values("apiExpressions", self.api_expressions)
        writer.write_bool_value("caseExact", self.case_exact)
        writer.write_str_value("defaultValue", self.default_value)
        writer.write_bool_value("flowNullValues", self.flow_null_values)
        writer.write_collection_of_object_values("metadata", self.metadata)
        writer.write_bool_value("multivalued", self.multivalued)
        writer.write_enum_value("mutability", self.mutability)
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("referencedObjects", self.referenced_objects)
        writer.write_bool_value("required", self.required)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

