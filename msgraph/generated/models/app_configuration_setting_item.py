from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

mdm_app_config_key_type = lazy_import('msgraph.generated.models.mdm_app_config_key_type')

class AppConfigurationSettingItem(AdditionalDataHolder, Parsable):
    """
    Contains properties for App configuration setting item.
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
    
    @property
    def app_config_key(self,) -> Optional[str]:
        """
        Gets the appConfigKey property value. app configuration key.
        Returns: Optional[str]
        """
        return self._app_config_key
    
    @app_config_key.setter
    def app_config_key(self,value: Optional[str] = None) -> None:
        """
        Sets the appConfigKey property value. app configuration key.
        Args:
            value: Value to set for the appConfigKey property.
        """
        self._app_config_key = value
    
    @property
    def app_config_key_type(self,) -> Optional[mdm_app_config_key_type.MdmAppConfigKeyType]:
        """
        Gets the appConfigKeyType property value. App configuration key types.
        Returns: Optional[mdm_app_config_key_type.MdmAppConfigKeyType]
        """
        return self._app_config_key_type
    
    @app_config_key_type.setter
    def app_config_key_type(self,value: Optional[mdm_app_config_key_type.MdmAppConfigKeyType] = None) -> None:
        """
        Sets the appConfigKeyType property value. App configuration key types.
        Args:
            value: Value to set for the appConfigKeyType property.
        """
        self._app_config_key_type = value
    
    @property
    def app_config_key_value(self,) -> Optional[str]:
        """
        Gets the appConfigKeyValue property value. app configuration key value.
        Returns: Optional[str]
        """
        return self._app_config_key_value
    
    @app_config_key_value.setter
    def app_config_key_value(self,value: Optional[str] = None) -> None:
        """
        Sets the appConfigKeyValue property value. app configuration key value.
        Args:
            value: Value to set for the appConfigKeyValue property.
        """
        self._app_config_key_value = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new appConfigurationSettingItem and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # app configuration key.
        self._app_config_key: Optional[str] = None
        # App configuration key types.
        self._app_config_key_type: Optional[mdm_app_config_key_type.MdmAppConfigKeyType] = None
        # app configuration key value.
        self._app_config_key_value: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AppConfigurationSettingItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AppConfigurationSettingItem
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AppConfigurationSettingItem()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "app_config_key": lambda n : setattr(self, 'app_config_key', n.get_str_value()),
            "app_config_key_type": lambda n : setattr(self, 'app_config_key_type', n.get_enum_value(mdm_app_config_key_type.MdmAppConfigKeyType)),
            "app_config_key_value": lambda n : setattr(self, 'app_config_key_value', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("appConfigKey", self.app_config_key)
        writer.write_enum_value("appConfigKeyType", self.app_config_key_type)
        writer.write_str_value("appConfigKeyValue", self.app_config_key_value)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

