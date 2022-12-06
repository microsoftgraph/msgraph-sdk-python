from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

compliance_status = lazy_import('msgraph.generated.models.compliance_status')
setting_source = lazy_import('msgraph.generated.models.setting_source')

class DeviceCompliancePolicySettingState(AdditionalDataHolder, Parsable):
    """
    Device Compilance Policy Setting State for a given device.
    """
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
        Instantiates a new deviceCompliancePolicySettingState and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Current value of setting on device
        self._current_value: Optional[str] = None
        # Error code for the setting
        self._error_code: Optional[int] = None
        # Error description
        self._error_description: Optional[str] = None
        # Name of setting instance that is being reported.
        self._instance_display_name: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The setting that is being reported
        self._setting: Optional[str] = None
        # Localized/user friendly setting name that is being reported
        self._setting_name: Optional[str] = None
        # Contributing policies
        self._sources: Optional[List[setting_source.SettingSource]] = None
        # The state property
        self._state: Optional[compliance_status.ComplianceStatus] = None
        # UserEmail
        self._user_email: Optional[str] = None
        # UserId
        self._user_id: Optional[str] = None
        # UserName
        self._user_name: Optional[str] = None
        # UserPrincipalName.
        self._user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceCompliancePolicySettingState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceCompliancePolicySettingState
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceCompliancePolicySettingState()
    
    @property
    def current_value(self,) -> Optional[str]:
        """
        Gets the currentValue property value. Current value of setting on device
        Returns: Optional[str]
        """
        return self._current_value
    
    @current_value.setter
    def current_value(self,value: Optional[str] = None) -> None:
        """
        Sets the currentValue property value. Current value of setting on device
        Args:
            value: Value to set for the currentValue property.
        """
        self._current_value = value
    
    @property
    def error_code(self,) -> Optional[int]:
        """
        Gets the errorCode property value. Error code for the setting
        Returns: Optional[int]
        """
        return self._error_code
    
    @error_code.setter
    def error_code(self,value: Optional[int] = None) -> None:
        """
        Sets the errorCode property value. Error code for the setting
        Args:
            value: Value to set for the errorCode property.
        """
        self._error_code = value
    
    @property
    def error_description(self,) -> Optional[str]:
        """
        Gets the errorDescription property value. Error description
        Returns: Optional[str]
        """
        return self._error_description
    
    @error_description.setter
    def error_description(self,value: Optional[str] = None) -> None:
        """
        Sets the errorDescription property value. Error description
        Args:
            value: Value to set for the errorDescription property.
        """
        self._error_description = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "current_value": lambda n : setattr(self, 'current_value', n.get_str_value()),
            "error_code": lambda n : setattr(self, 'error_code', n.get_int_value()),
            "error_description": lambda n : setattr(self, 'error_description', n.get_str_value()),
            "instance_display_name": lambda n : setattr(self, 'instance_display_name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "setting": lambda n : setattr(self, 'setting', n.get_str_value()),
            "setting_name": lambda n : setattr(self, 'setting_name', n.get_str_value()),
            "sources": lambda n : setattr(self, 'sources', n.get_collection_of_object_values(setting_source.SettingSource)),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(compliance_status.ComplianceStatus)),
            "user_email": lambda n : setattr(self, 'user_email', n.get_str_value()),
            "user_id": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "user_name": lambda n : setattr(self, 'user_name', n.get_str_value()),
            "user_principal_name": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
        }
        return fields
    
    @property
    def instance_display_name(self,) -> Optional[str]:
        """
        Gets the instanceDisplayName property value. Name of setting instance that is being reported.
        Returns: Optional[str]
        """
        return self._instance_display_name
    
    @instance_display_name.setter
    def instance_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the instanceDisplayName property value. Name of setting instance that is being reported.
        Args:
            value: Value to set for the instanceDisplayName property.
        """
        self._instance_display_name = value
    
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
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
    
    @property
    def setting(self,) -> Optional[str]:
        """
        Gets the setting property value. The setting that is being reported
        Returns: Optional[str]
        """
        return self._setting
    
    @setting.setter
    def setting(self,value: Optional[str] = None) -> None:
        """
        Sets the setting property value. The setting that is being reported
        Args:
            value: Value to set for the setting property.
        """
        self._setting = value
    
    @property
    def setting_name(self,) -> Optional[str]:
        """
        Gets the settingName property value. Localized/user friendly setting name that is being reported
        Returns: Optional[str]
        """
        return self._setting_name
    
    @setting_name.setter
    def setting_name(self,value: Optional[str] = None) -> None:
        """
        Sets the settingName property value. Localized/user friendly setting name that is being reported
        Args:
            value: Value to set for the settingName property.
        """
        self._setting_name = value
    
    @property
    def sources(self,) -> Optional[List[setting_source.SettingSource]]:
        """
        Gets the sources property value. Contributing policies
        Returns: Optional[List[setting_source.SettingSource]]
        """
        return self._sources
    
    @sources.setter
    def sources(self,value: Optional[List[setting_source.SettingSource]] = None) -> None:
        """
        Sets the sources property value. Contributing policies
        Args:
            value: Value to set for the sources property.
        """
        self._sources = value
    
    @property
    def state(self,) -> Optional[compliance_status.ComplianceStatus]:
        """
        Gets the state property value. The state property
        Returns: Optional[compliance_status.ComplianceStatus]
        """
        return self._state
    
    @state.setter
    def state(self,value: Optional[compliance_status.ComplianceStatus] = None) -> None:
        """
        Sets the state property value. The state property
        Args:
            value: Value to set for the state property.
        """
        self._state = value
    
    @property
    def user_email(self,) -> Optional[str]:
        """
        Gets the userEmail property value. UserEmail
        Returns: Optional[str]
        """
        return self._user_email
    
    @user_email.setter
    def user_email(self,value: Optional[str] = None) -> None:
        """
        Sets the userEmail property value. UserEmail
        Args:
            value: Value to set for the userEmail property.
        """
        self._user_email = value
    
    @property
    def user_id(self,) -> Optional[str]:
        """
        Gets the userId property value. UserId
        Returns: Optional[str]
        """
        return self._user_id
    
    @user_id.setter
    def user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the userId property value. UserId
        Args:
            value: Value to set for the userId property.
        """
        self._user_id = value
    
    @property
    def user_name(self,) -> Optional[str]:
        """
        Gets the userName property value. UserName
        Returns: Optional[str]
        """
        return self._user_name
    
    @user_name.setter
    def user_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userName property value. UserName
        Args:
            value: Value to set for the userName property.
        """
        self._user_name = value
    
    @property
    def user_principal_name(self,) -> Optional[str]:
        """
        Gets the userPrincipalName property value. UserPrincipalName.
        Returns: Optional[str]
        """
        return self._user_principal_name
    
    @user_principal_name.setter
    def user_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userPrincipalName property value. UserPrincipalName.
        Args:
            value: Value to set for the userPrincipalName property.
        """
        self._user_principal_name = value
    

