from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .compliance_status import ComplianceStatus
    from .setting_source import SettingSource

@dataclass
class DeviceConfigurationSettingState(AdditionalDataHolder, BackedModel, Parsable):
    """
    Device Configuration Setting State for a given device.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Current value of setting on device
    current_value: Optional[str] = None
    # Error code for the setting
    error_code: Optional[int] = None
    # Error description
    error_description: Optional[str] = None
    # Name of setting instance that is being reported.
    instance_display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The setting that is being reported
    setting: Optional[str] = None
    # Localized/user friendly setting name that is being reported
    setting_name: Optional[str] = None
    # Contributing policies
    sources: Optional[list[SettingSource]] = None
    # The state property
    state: Optional[ComplianceStatus] = None
    # UserEmail
    user_email: Optional[str] = None
    # UserId
    user_id: Optional[str] = None
    # UserName
    user_name: Optional[str] = None
    # UserPrincipalName.
    user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceConfigurationSettingState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceConfigurationSettingState
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceConfigurationSettingState()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .compliance_status import ComplianceStatus
        from .setting_source import SettingSource

        from .compliance_status import ComplianceStatus
        from .setting_source import SettingSource

        fields: dict[str, Callable[[Any], None]] = {
            "currentValue": lambda n : setattr(self, 'current_value', n.get_str_value()),
            "errorCode": lambda n : setattr(self, 'error_code', n.get_int_value()),
            "errorDescription": lambda n : setattr(self, 'error_description', n.get_str_value()),
            "instanceDisplayName": lambda n : setattr(self, 'instance_display_name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "setting": lambda n : setattr(self, 'setting', n.get_str_value()),
            "settingName": lambda n : setattr(self, 'setting_name', n.get_str_value()),
            "sources": lambda n : setattr(self, 'sources', n.get_collection_of_object_values(SettingSource)),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(ComplianceStatus)),
            "userEmail": lambda n : setattr(self, 'user_email', n.get_str_value()),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "userName": lambda n : setattr(self, 'user_name', n.get_str_value()),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
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
        writer.write_str_value("currentValue", self.current_value)
        writer.write_int_value("errorCode", self.error_code)
        writer.write_str_value("errorDescription", self.error_description)
        writer.write_str_value("instanceDisplayName", self.instance_display_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("setting", self.setting)
        writer.write_str_value("settingName", self.setting_name)
        writer.write_collection_of_object_values("sources", self.sources)
        writer.write_enum_value("state", self.state)
        writer.write_str_value("userEmail", self.user_email)
        writer.write_str_value("userId", self.user_id)
        writer.write_str_value("userName", self.user_name)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
        writer.write_additional_data_value(self.additional_data)
    

