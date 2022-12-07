from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
remote_assistance_onboarding_status = lazy_import('msgraph.generated.models.remote_assistance_onboarding_status')

class RemoteAssistancePartner(entity.Entity):
    """
    RemoteAssistPartner resources represent the metadata and status of a given Remote Assistance partner service.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new remoteAssistancePartner and sets the default values.
        """
        super().__init__()
        # Display name of the partner.
        self._display_name: Optional[str] = None
        # Timestamp of the last request sent to Intune by the TEM partner.
        self._last_connection_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The current TeamViewer connector status
        self._onboarding_status: Optional[remote_assistance_onboarding_status.RemoteAssistanceOnboardingStatus] = None
        # URL of the partner's onboarding portal, where an administrator can configure their Remote Assistance service.
        self._onboarding_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RemoteAssistancePartner:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RemoteAssistancePartner
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RemoteAssistancePartner()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Display name of the partner.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Display name of the partner.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "last_connection_date_time": lambda n : setattr(self, 'last_connection_date_time', n.get_datetime_value()),
            "onboarding_status": lambda n : setattr(self, 'onboarding_status', n.get_enum_value(remote_assistance_onboarding_status.RemoteAssistanceOnboardingStatus)),
            "onboarding_url": lambda n : setattr(self, 'onboarding_url', n.get_str_value()),
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
    
    @property
    def onboarding_status(self,) -> Optional[remote_assistance_onboarding_status.RemoteAssistanceOnboardingStatus]:
        """
        Gets the onboardingStatus property value. The current TeamViewer connector status
        Returns: Optional[remote_assistance_onboarding_status.RemoteAssistanceOnboardingStatus]
        """
        return self._onboarding_status
    
    @onboarding_status.setter
    def onboarding_status(self,value: Optional[remote_assistance_onboarding_status.RemoteAssistanceOnboardingStatus] = None) -> None:
        """
        Sets the onboardingStatus property value. The current TeamViewer connector status
        Args:
            value: Value to set for the onboardingStatus property.
        """
        self._onboarding_status = value
    
    @property
    def onboarding_url(self,) -> Optional[str]:
        """
        Gets the onboardingUrl property value. URL of the partner's onboarding portal, where an administrator can configure their Remote Assistance service.
        Returns: Optional[str]
        """
        return self._onboarding_url
    
    @onboarding_url.setter
    def onboarding_url(self,value: Optional[str] = None) -> None:
        """
        Sets the onboardingUrl property value. URL of the partner's onboarding portal, where an administrator can configure their Remote Assistance service.
        Args:
            value: Value to set for the onboardingUrl property.
        """
        self._onboarding_url = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastConnectionDateTime", self.last_connection_date_time)
        writer.write_enum_value("onboardingStatus", self.onboarding_status)
        writer.write_str_value("onboardingUrl", self.onboarding_url)
    

