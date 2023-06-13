from __future__ import annotations
from dataclasses import dataclass, field
from datetime import timedelta
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class AccessPackageAutomaticRequestSettings(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The gracePeriodBeforeAccessRemoval property
    grace_period_before_access_removal: Optional[timedelta] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The removeAccessWhenTargetLeavesAllowedTargets property
    remove_access_when_target_leaves_allowed_targets: Optional[bool] = None
    # If set to true, automatic assignments will be created for targets in the allowed target scope.
    request_access_for_allowed_targets: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessPackageAutomaticRequestSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageAutomaticRequestSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
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
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_timedelta_value("gracePeriodBeforeAccessRemoval", self.grace_period_before_access_removal)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("removeAccessWhenTargetLeavesAllowedTargets", self.remove_access_when_target_leaves_allowed_targets)
        writer.write_bool_value("requestAccessForAllowedTargets", self.request_access_for_allowed_targets)
        writer.write_additional_data_value(self.additional_data)
    

