from __future__ import annotations
from datetime import timedelta
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class AccessPackageAutomaticRequestSettings(AdditionalDataHolder, Parsable):
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new accessPackageAutomaticRequestSettings and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The gracePeriodBeforeAccessRemoval property
        self._grace_period_before_access_removal: Optional[Timedelta] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The removeAccessWhenTargetLeavesAllowedTargets property
        self._remove_access_when_target_leaves_allowed_targets: Optional[bool] = None
        # If set to true, automatic assignments will be created for targets in the allowed target scope.
        self._request_access_for_allowed_targets: Optional[bool] = None
    
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
        fields = {
            "grace_period_before_access_removal": lambda n : setattr(self, 'grace_period_before_access_removal', n.get_object_value(Timedelta)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "remove_access_when_target_leaves_allowed_targets": lambda n : setattr(self, 'remove_access_when_target_leaves_allowed_targets', n.get_bool_value()),
            "request_access_for_allowed_targets": lambda n : setattr(self, 'request_access_for_allowed_targets', n.get_bool_value()),
        }
        return fields
    
    @property
    def grace_period_before_access_removal(self,) -> Optional[Timedelta]:
        """
        Gets the gracePeriodBeforeAccessRemoval property value. The gracePeriodBeforeAccessRemoval property
        Returns: Optional[Timedelta]
        """
        return self._grace_period_before_access_removal
    
    @grace_period_before_access_removal.setter
    def grace_period_before_access_removal(self,value: Optional[Timedelta] = None) -> None:
        """
        Sets the gracePeriodBeforeAccessRemoval property value. The gracePeriodBeforeAccessRemoval property
        Args:
            value: Value to set for the gracePeriodBeforeAccessRemoval property.
        """
        self._grace_period_before_access_removal = value
    
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
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def remove_access_when_target_leaves_allowed_targets(self,) -> Optional[bool]:
        """
        Gets the removeAccessWhenTargetLeavesAllowedTargets property value. The removeAccessWhenTargetLeavesAllowedTargets property
        Returns: Optional[bool]
        """
        return self._remove_access_when_target_leaves_allowed_targets
    
    @remove_access_when_target_leaves_allowed_targets.setter
    def remove_access_when_target_leaves_allowed_targets(self,value: Optional[bool] = None) -> None:
        """
        Sets the removeAccessWhenTargetLeavesAllowedTargets property value. The removeAccessWhenTargetLeavesAllowedTargets property
        Args:
            value: Value to set for the removeAccessWhenTargetLeavesAllowedTargets property.
        """
        self._remove_access_when_target_leaves_allowed_targets = value
    
    @property
    def request_access_for_allowed_targets(self,) -> Optional[bool]:
        """
        Gets the requestAccessForAllowedTargets property value. If set to true, automatic assignments will be created for targets in the allowed target scope.
        Returns: Optional[bool]
        """
        return self._request_access_for_allowed_targets
    
    @request_access_for_allowed_targets.setter
    def request_access_for_allowed_targets(self,value: Optional[bool] = None) -> None:
        """
        Sets the requestAccessForAllowedTargets property value. If set to true, automatic assignments will be created for targets in the allowed target scope.
        Args:
            value: Value to set for the requestAccessForAllowedTargets property.
        """
        self._request_access_for_allowed_targets = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("gracePeriodBeforeAccessRemoval", self.grace_period_before_access_removal)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("removeAccessWhenTargetLeavesAllowedTargets", self.remove_access_when_target_leaves_allowed_targets)
        writer.write_bool_value("requestAccessForAllowedTargets", self.request_access_for_allowed_targets)
        writer.write_additional_data_value(self.additional_data)
    

