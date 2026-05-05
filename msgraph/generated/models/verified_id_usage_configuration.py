from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .verified_id_usage_configuration_purpose import VerifiedIdUsageConfigurationPurpose

@dataclass
class VerifiedIdUsageConfiguration(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Sets profile usage for evaluation (test-only) or production.
    is_enabled_for_test_only: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The purpose property
    purpose: Optional[VerifiedIdUsageConfigurationPurpose] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> VerifiedIdUsageConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: VerifiedIdUsageConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return VerifiedIdUsageConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .verified_id_usage_configuration_purpose import VerifiedIdUsageConfigurationPurpose

        from .verified_id_usage_configuration_purpose import VerifiedIdUsageConfigurationPurpose

        fields: dict[str, Callable[[Any], None]] = {
            "isEnabledForTestOnly": lambda n : setattr(self, 'is_enabled_for_test_only', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "purpose": lambda n : setattr(self, 'purpose', n.get_enum_value(VerifiedIdUsageConfigurationPurpose)),
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
        writer.write_bool_value("isEnabledForTestOnly", self.is_enabled_for_test_only)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("purpose", self.purpose)
        writer.write_additional_data_value(self.additional_data)
    

