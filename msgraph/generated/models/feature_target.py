from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .feature_target_type import FeatureTargetType

@dataclass
class FeatureTarget(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The ID of the entity that's targeted in the include or exclude rule, or all_users to target all users.
    id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The kind of entity that's targeted. The possible values are: group, administrativeUnit, role, unknownFutureValue.
    target_type: Optional[FeatureTargetType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FeatureTarget:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FeatureTarget
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FeatureTarget()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .feature_target_type import FeatureTargetType

        from .feature_target_type import FeatureTargetType

        fields: Dict[str, Callable[[Any], None]] = {
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "targetType": lambda n : setattr(self, 'target_type', n.get_enum_value(FeatureTargetType)),
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
        from .feature_target_type import FeatureTargetType

        writer.write_str_value("id", self.id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("targetType", self.target_type)
        writer.write_additional_data_value(self.additional_data)
    

