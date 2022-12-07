from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

windows_device_account = lazy_import('msgraph.generated.models.windows_device_account')

class UpdateWindowsDeviceAccountActionParameter(AdditionalDataHolder, Parsable):
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
    
    @property
    def calendar_sync_enabled(self,) -> Optional[bool]:
        """
        Gets the calendarSyncEnabled property value. Not yet documented
        Returns: Optional[bool]
        """
        return self._calendar_sync_enabled
    
    @calendar_sync_enabled.setter
    def calendar_sync_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the calendarSyncEnabled property value. Not yet documented
        Args:
            value: Value to set for the calendarSyncEnabled property.
        """
        self._calendar_sync_enabled = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new updateWindowsDeviceAccountActionParameter and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Not yet documented
        self._calendar_sync_enabled: Optional[bool] = None
        # Not yet documented
        self._device_account: Optional[windows_device_account.WindowsDeviceAccount] = None
        # Not yet documented
        self._device_account_email: Optional[str] = None
        # Not yet documented
        self._exchange_server: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Not yet documented
        self._password_rotation_enabled: Optional[bool] = None
        # Not yet documented
        self._session_initiation_protocal_address: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UpdateWindowsDeviceAccountActionParameter:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UpdateWindowsDeviceAccountActionParameter
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UpdateWindowsDeviceAccountActionParameter()
    
    @property
    def device_account(self,) -> Optional[windows_device_account.WindowsDeviceAccount]:
        """
        Gets the deviceAccount property value. Not yet documented
        Returns: Optional[windows_device_account.WindowsDeviceAccount]
        """
        return self._device_account
    
    @device_account.setter
    def device_account(self,value: Optional[windows_device_account.WindowsDeviceAccount] = None) -> None:
        """
        Sets the deviceAccount property value. Not yet documented
        Args:
            value: Value to set for the deviceAccount property.
        """
        self._device_account = value
    
    @property
    def device_account_email(self,) -> Optional[str]:
        """
        Gets the deviceAccountEmail property value. Not yet documented
        Returns: Optional[str]
        """
        return self._device_account_email
    
    @device_account_email.setter
    def device_account_email(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceAccountEmail property value. Not yet documented
        Args:
            value: Value to set for the deviceAccountEmail property.
        """
        self._device_account_email = value
    
    @property
    def exchange_server(self,) -> Optional[str]:
        """
        Gets the exchangeServer property value. Not yet documented
        Returns: Optional[str]
        """
        return self._exchange_server
    
    @exchange_server.setter
    def exchange_server(self,value: Optional[str] = None) -> None:
        """
        Sets the exchangeServer property value. Not yet documented
        Args:
            value: Value to set for the exchangeServer property.
        """
        self._exchange_server = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "calendar_sync_enabled": lambda n : setattr(self, 'calendar_sync_enabled', n.get_bool_value()),
            "device_account": lambda n : setattr(self, 'device_account', n.get_object_value(windows_device_account.WindowsDeviceAccount)),
            "device_account_email": lambda n : setattr(self, 'device_account_email', n.get_str_value()),
            "exchange_server": lambda n : setattr(self, 'exchange_server', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "password_rotation_enabled": lambda n : setattr(self, 'password_rotation_enabled', n.get_bool_value()),
            "session_initiation_protocal_address": lambda n : setattr(self, 'session_initiation_protocal_address', n.get_str_value()),
        }
        return fields
    
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
    def password_rotation_enabled(self,) -> Optional[bool]:
        """
        Gets the passwordRotationEnabled property value. Not yet documented
        Returns: Optional[bool]
        """
        return self._password_rotation_enabled
    
    @password_rotation_enabled.setter
    def password_rotation_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the passwordRotationEnabled property value. Not yet documented
        Args:
            value: Value to set for the passwordRotationEnabled property.
        """
        self._password_rotation_enabled = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_bool_value("calendarSyncEnabled", self.calendar_sync_enabled)
        writer.write_object_value("deviceAccount", self.device_account)
        writer.write_str_value("deviceAccountEmail", self.device_account_email)
        writer.write_str_value("exchangeServer", self.exchange_server)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("passwordRotationEnabled", self.password_rotation_enabled)
        writer.write_str_value("sessionInitiationProtocalAddress", self.session_initiation_protocal_address)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def session_initiation_protocal_address(self,) -> Optional[str]:
        """
        Gets the sessionInitiationProtocalAddress property value. Not yet documented
        Returns: Optional[str]
        """
        return self._session_initiation_protocal_address
    
    @session_initiation_protocal_address.setter
    def session_initiation_protocal_address(self,value: Optional[str] = None) -> None:
        """
        Sets the sessionInitiationProtocalAddress property value. Not yet documented
        Args:
            value: Value to set for the sessionInitiationProtocalAddress property.
        """
        self._session_initiation_protocal_address = value
    

