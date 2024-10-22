from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .mobile_app_identifier import MobileAppIdentifier

@dataclass
class ManagedAppPolicyDeploymentSummaryPerApp(AdditionalDataHolder, BackedModel, Parsable):
    """
    Represents policy deployment summary per app.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Number of users the policy is applied.
    configuration_applied_user_count: Optional[int] = None
    # Deployment of an app.
    mobile_app_identifier: Optional[MobileAppIdentifier] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ManagedAppPolicyDeploymentSummaryPerApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ManagedAppPolicyDeploymentSummaryPerApp
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ManagedAppPolicyDeploymentSummaryPerApp()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .mobile_app_identifier import MobileAppIdentifier

        from .mobile_app_identifier import MobileAppIdentifier

        fields: Dict[str, Callable[[Any], None]] = {
            "configurationAppliedUserCount": lambda n : setattr(self, 'configuration_applied_user_count', n.get_int_value()),
            "mobileAppIdentifier": lambda n : setattr(self, 'mobile_app_identifier', n.get_object_value(MobileAppIdentifier)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        from .mobile_app_identifier import MobileAppIdentifier

        writer.write_int_value("configurationAppliedUserCount", self.configuration_applied_user_count)
        writer.write_object_value("mobileAppIdentifier", self.mobile_app_identifier)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

