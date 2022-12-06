from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

app_list_item = lazy_import('msgraph.generated.models.app_list_item')

class IosNetworkUsageRule(AdditionalDataHolder, Parsable):
    """
    Network Usage Rules allow enterprises to specify how managed apps use networks, such as cellular data networks.
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
    def cellular_data_blocked(self,) -> Optional[bool]:
        """
        Gets the cellularDataBlocked property value. If set to true, corresponding managed apps will not be allowed to use cellular data at any time.
        Returns: Optional[bool]
        """
        return self._cellular_data_blocked
    
    @cellular_data_blocked.setter
    def cellular_data_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the cellularDataBlocked property value. If set to true, corresponding managed apps will not be allowed to use cellular data at any time.
        Args:
            value: Value to set for the cellularDataBlocked property.
        """
        self._cellular_data_blocked = value
    
    @property
    def cellular_data_block_when_roaming(self,) -> Optional[bool]:
        """
        Gets the cellularDataBlockWhenRoaming property value. If set to true, corresponding managed apps will not be allowed to use cellular data when roaming.
        Returns: Optional[bool]
        """
        return self._cellular_data_block_when_roaming
    
    @cellular_data_block_when_roaming.setter
    def cellular_data_block_when_roaming(self,value: Optional[bool] = None) -> None:
        """
        Sets the cellularDataBlockWhenRoaming property value. If set to true, corresponding managed apps will not be allowed to use cellular data when roaming.
        Args:
            value: Value to set for the cellularDataBlockWhenRoaming property.
        """
        self._cellular_data_block_when_roaming = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new iosNetworkUsageRule and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # If set to true, corresponding managed apps will not be allowed to use cellular data at any time.
        self._cellular_data_blocked: Optional[bool] = None
        # If set to true, corresponding managed apps will not be allowed to use cellular data when roaming.
        self._cellular_data_block_when_roaming: Optional[bool] = None
        # Information about the managed apps that this rule is going to apply to. This collection can contain a maximum of 500 elements.
        self._managed_apps: Optional[List[app_list_item.AppListItem]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosNetworkUsageRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IosNetworkUsageRule
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IosNetworkUsageRule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "cellular_data_blocked": lambda n : setattr(self, 'cellular_data_blocked', n.get_bool_value()),
            "cellular_data_block_when_roaming": lambda n : setattr(self, 'cellular_data_block_when_roaming', n.get_bool_value()),
            "managed_apps": lambda n : setattr(self, 'managed_apps', n.get_collection_of_object_values(app_list_item.AppListItem)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def managed_apps(self,) -> Optional[List[app_list_item.AppListItem]]:
        """
        Gets the managedApps property value. Information about the managed apps that this rule is going to apply to. This collection can contain a maximum of 500 elements.
        Returns: Optional[List[app_list_item.AppListItem]]
        """
        return self._managed_apps
    
    @managed_apps.setter
    def managed_apps(self,value: Optional[List[app_list_item.AppListItem]] = None) -> None:
        """
        Sets the managedApps property value. Information about the managed apps that this rule is going to apply to. This collection can contain a maximum of 500 elements.
        Args:
            value: Value to set for the managedApps property.
        """
        self._managed_apps = value
    
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
        writer.write_bool_value("cellularDataBlocked", self.cellular_data_blocked)
        writer.write_bool_value("cellularDataBlockWhenRoaming", self.cellular_data_block_when_roaming)
        writer.write_collection_of_object_values("managedApps", self.managed_apps)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

