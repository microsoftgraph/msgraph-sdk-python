from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

run_as_account_type = lazy_import('msgraph.generated.models.run_as_account_type')
win32_lob_app_restart_behavior = lazy_import('msgraph.generated.models.win32_lob_app_restart_behavior')

class Win32LobAppInstallExperience(AdditionalDataHolder, Parsable):
    """
    Contains installation experience properties for a Win32 App
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
        Instantiates a new win32LobAppInstallExperience and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Indicates the type of restart action.
        self._device_restart_behavior: Optional[win32_lob_app_restart_behavior.Win32LobAppRestartBehavior] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Indicates the type of execution context the app runs in.
        self._run_as_account: Optional[run_as_account_type.RunAsAccountType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Win32LobAppInstallExperience:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Win32LobAppInstallExperience
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Win32LobAppInstallExperience()
    
    @property
    def device_restart_behavior(self,) -> Optional[win32_lob_app_restart_behavior.Win32LobAppRestartBehavior]:
        """
        Gets the deviceRestartBehavior property value. Indicates the type of restart action.
        Returns: Optional[win32_lob_app_restart_behavior.Win32LobAppRestartBehavior]
        """
        return self._device_restart_behavior
    
    @device_restart_behavior.setter
    def device_restart_behavior(self,value: Optional[win32_lob_app_restart_behavior.Win32LobAppRestartBehavior] = None) -> None:
        """
        Sets the deviceRestartBehavior property value. Indicates the type of restart action.
        Args:
            value: Value to set for the deviceRestartBehavior property.
        """
        self._device_restart_behavior = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "device_restart_behavior": lambda n : setattr(self, 'device_restart_behavior', n.get_enum_value(win32_lob_app_restart_behavior.Win32LobAppRestartBehavior)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "run_as_account": lambda n : setattr(self, 'run_as_account', n.get_enum_value(run_as_account_type.RunAsAccountType)),
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
    def run_as_account(self,) -> Optional[run_as_account_type.RunAsAccountType]:
        """
        Gets the runAsAccount property value. Indicates the type of execution context the app runs in.
        Returns: Optional[run_as_account_type.RunAsAccountType]
        """
        return self._run_as_account
    
    @run_as_account.setter
    def run_as_account(self,value: Optional[run_as_account_type.RunAsAccountType] = None) -> None:
        """
        Sets the runAsAccount property value. Indicates the type of execution context the app runs in.
        Args:
            value: Value to set for the runAsAccount property.
        """
        self._run_as_account = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("deviceRestartBehavior", self.device_restart_behavior)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("runAsAccount", self.run_as_account)
        writer.write_additional_data_value(self.additional_data)
    

