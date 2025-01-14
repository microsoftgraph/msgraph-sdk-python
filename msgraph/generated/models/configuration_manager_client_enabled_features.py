from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class ConfigurationManagerClientEnabledFeatures(AdditionalDataHolder, BackedModel, Parsable):
    """
    configuration Manager client enabled features
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Whether compliance policy is managed by Intune
    compliance_policy: Optional[bool] = None
    # Whether device configuration is managed by Intune
    device_configuration: Optional[bool] = None
    # Whether inventory is managed by Intune
    inventory: Optional[bool] = None
    # Whether modern application is managed by Intune
    modern_apps: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Whether resource access is managed by Intune
    resource_access: Optional[bool] = None
    # Whether Windows Update for Business is managed by Intune
    windows_update_for_business: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ConfigurationManagerClientEnabledFeatures:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ConfigurationManagerClientEnabledFeatures
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ConfigurationManagerClientEnabledFeatures()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "compliancePolicy": lambda n : setattr(self, 'compliance_policy', n.get_bool_value()),
            "deviceConfiguration": lambda n : setattr(self, 'device_configuration', n.get_bool_value()),
            "inventory": lambda n : setattr(self, 'inventory', n.get_bool_value()),
            "modernApps": lambda n : setattr(self, 'modern_apps', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "resourceAccess": lambda n : setattr(self, 'resource_access', n.get_bool_value()),
            "windowsUpdateForBusiness": lambda n : setattr(self, 'windows_update_for_business', n.get_bool_value()),
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
        writer.write_bool_value("compliancePolicy", self.compliance_policy)
        writer.write_bool_value("deviceConfiguration", self.device_configuration)
        writer.write_bool_value("inventory", self.inventory)
        writer.write_bool_value("modernApps", self.modern_apps)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("resourceAccess", self.resource_access)
        writer.write_bool_value("windowsUpdateForBusiness", self.windows_update_for_business)
        writer.write_additional_data_value(self.additional_data)
    

