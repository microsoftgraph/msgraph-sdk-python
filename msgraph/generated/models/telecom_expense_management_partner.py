from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class TelecomExpenseManagementPartner(entity.Entity):
    """
    telecomExpenseManagementPartner resources represent the metadata and status of a given TEM service. Once your organization has onboarded with a partner, the partner can be enabled or disabled to switch TEM functionality on or off.
    """
    @property
    def app_authorized(self,) -> Optional[bool]:
        """
        Gets the appAuthorized property value. Whether the partner's AAD app has been authorized to access Intune.
        Returns: Optional[bool]
        """
        return self._app_authorized
    
    @app_authorized.setter
    def app_authorized(self,value: Optional[bool] = None) -> None:
        """
        Sets the appAuthorized property value. Whether the partner's AAD app has been authorized to access Intune.
        Args:
            value: Value to set for the appAuthorized property.
        """
        self._app_authorized = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new telecomExpenseManagementPartner and sets the default values.
        """
        super().__init__()
        # Whether the partner's AAD app has been authorized to access Intune.
        self._app_authorized: Optional[bool] = None
        # Display name of the TEM partner.
        self._display_name: Optional[str] = None
        # Whether Intune's connection to the TEM service is currently enabled or disabled.
        self._enabled: Optional[bool] = None
        # Timestamp of the last request sent to Intune by the TEM partner.
        self._last_connection_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # URL of the TEM partner's administrative control panel, where an administrator can configure their TEM service.
        self._url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TelecomExpenseManagementPartner:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TelecomExpenseManagementPartner
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TelecomExpenseManagementPartner()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Display name of the TEM partner.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Display name of the TEM partner.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def enabled(self,) -> Optional[bool]:
        """
        Gets the enabled property value. Whether Intune's connection to the TEM service is currently enabled or disabled.
        Returns: Optional[bool]
        """
        return self._enabled
    
    @enabled.setter
    def enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the enabled property value. Whether Intune's connection to the TEM service is currently enabled or disabled.
        Args:
            value: Value to set for the enabled property.
        """
        self._enabled = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "app_authorized": lambda n : setattr(self, 'app_authorized', n.get_bool_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "enabled": lambda n : setattr(self, 'enabled', n.get_bool_value()),
            "last_connection_date_time": lambda n : setattr(self, 'last_connection_date_time', n.get_datetime_value()),
            "url": lambda n : setattr(self, 'url', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_connection_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastConnectionDateTime property value. Timestamp of the last request sent to Intune by the TEM partner.
        Returns: Optional[datetime]
        """
        return self._last_connection_date_time
    
    @last_connection_date_time.setter
    def last_connection_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastConnectionDateTime property value. Timestamp of the last request sent to Intune by the TEM partner.
        Args:
            value: Value to set for the lastConnectionDateTime property.
        """
        self._last_connection_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("appAuthorized", self.app_authorized)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("enabled", self.enabled)
        writer.write_datetime_value("lastConnectionDateTime", self.last_connection_date_time)
        writer.write_str_value("url", self.url)
    
    @property
    def url(self,) -> Optional[str]:
        """
        Gets the url property value. URL of the TEM partner's administrative control panel, where an administrator can configure their TEM service.
        Returns: Optional[str]
        """
        return self._url
    
    @url.setter
    def url(self,value: Optional[str] = None) -> None:
        """
        Sets the url property value. URL of the TEM partner's administrative control panel, where an administrator can configure their TEM service.
        Args:
            value: Value to set for the url property.
        """
        self._url = value
    

