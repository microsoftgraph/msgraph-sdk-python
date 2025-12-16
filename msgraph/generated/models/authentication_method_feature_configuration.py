from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .advanced_config_state import AdvancedConfigState
    from .feature_target import FeatureTarget

@dataclass
class AuthenticationMethodFeatureConfiguration(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # A single entity that is excluded from this feature.
    exclude_target: Optional[FeatureTarget] = None
    # A single entity that is included in this feature.
    include_target: Optional[FeatureTarget] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Enable or disable the feature. The possible values are: default, enabled, disabled, unknownFutureValue. The default value is used when the configuration hasn't been explicitly set and uses the default behavior of Microsoft Entra ID for the setting. The default value is disabled.
    state: Optional[AdvancedConfigState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AuthenticationMethodFeatureConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticationMethodFeatureConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AuthenticationMethodFeatureConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .advanced_config_state import AdvancedConfigState
        from .feature_target import FeatureTarget

        from .advanced_config_state import AdvancedConfigState
        from .feature_target import FeatureTarget

        fields: dict[str, Callable[[Any], None]] = {
            "excludeTarget": lambda n : setattr(self, 'exclude_target', n.get_object_value(FeatureTarget)),
            "includeTarget": lambda n : setattr(self, 'include_target', n.get_object_value(FeatureTarget)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(AdvancedConfigState)),
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
        writer.write_object_value("excludeTarget", self.exclude_target)
        writer.write_object_value("includeTarget", self.include_target)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("state", self.state)
        writer.write_additional_data_value(self.additional_data)
    

