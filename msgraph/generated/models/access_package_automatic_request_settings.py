from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class AccessPackageAutomaticRequestSettings(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The duration for which access must be retained before the target's access is revoked once they leave the allowed target scope.
    grace_period_before_access_removal: Optional[datetime.timedelta] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates whether automatic assignment must be removed for targets who move out of the allowed target scope.
    remove_access_when_target_leaves_allowed_targets: Optional[bool] = None
    # If set to true, automatic assignments will be created for targets in the allowed target scope.
    request_access_for_allowed_targets: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AccessPackageAutomaticRequestSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageAutomaticRequestSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AccessPackageAutomaticRequestSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "gracePeriodBeforeAccessRemoval": lambda n : setattr(self, 'grace_period_before_access_removal', n.get_timedelta_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "removeAccessWhenTargetLeavesAllowedTargets": lambda n : setattr(self, 'remove_access_when_target_leaves_allowed_targets', n.get_bool_value()),
            "requestAccessForAllowedTargets": lambda n : setattr(self, 'request_access_for_allowed_targets', n.get_bool_value()),
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
        writer.write_timedelta_value("gracePeriodBeforeAccessRemoval", self.grace_period_before_access_removal)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("removeAccessWhenTargetLeavesAllowedTargets", self.remove_access_when_target_leaves_allowed_targets)
        writer.write_bool_value("requestAccessForAllowedTargets", self.request_access_for_allowed_targets)
        writer.write_additional_data_value(self.additional_data)
    

