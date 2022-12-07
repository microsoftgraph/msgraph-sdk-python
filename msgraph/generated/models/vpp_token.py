from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
vpp_token_account_type = lazy_import('msgraph.generated.models.vpp_token_account_type')
vpp_token_state = lazy_import('msgraph.generated.models.vpp_token_state')
vpp_token_sync_status = lazy_import('msgraph.generated.models.vpp_token_sync_status')

class VppToken(entity.Entity):
    """
    You purchase multiple licenses for iOS apps through the Apple Volume Purchase Program for Business or Education. This involves setting up an Apple VPP account from the Apple website and uploading the Apple VPP Business or Education token to Intune. You can then synchronize your volume purchase information with Intune and track your volume-purchased app use. You can upload multiple Apple VPP Business or Education tokens.
    """
    @property
    def apple_id(self,) -> Optional[str]:
        """
        Gets the appleId property value. The apple Id associated with the given Apple Volume Purchase Program Token.
        Returns: Optional[str]
        """
        return self._apple_id
    
    @apple_id.setter
    def apple_id(self,value: Optional[str] = None) -> None:
        """
        Sets the appleId property value. The apple Id associated with the given Apple Volume Purchase Program Token.
        Args:
            value: Value to set for the appleId property.
        """
        self._apple_id = value
    
    @property
    def automatically_update_apps(self,) -> Optional[bool]:
        """
        Gets the automaticallyUpdateApps property value. Whether or not apps for the VPP token will be automatically updated.
        Returns: Optional[bool]
        """
        return self._automatically_update_apps
    
    @automatically_update_apps.setter
    def automatically_update_apps(self,value: Optional[bool] = None) -> None:
        """
        Sets the automaticallyUpdateApps property value. Whether or not apps for the VPP token will be automatically updated.
        Args:
            value: Value to set for the automaticallyUpdateApps property.
        """
        self._automatically_update_apps = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new vppToken and sets the default values.
        """
        super().__init__()
        # The apple Id associated with the given Apple Volume Purchase Program Token.
        self._apple_id: Optional[str] = None
        # Whether or not apps for the VPP token will be automatically updated.
        self._automatically_update_apps: Optional[bool] = None
        # Whether or not apps for the VPP token will be automatically updated.
        self._country_or_region: Optional[str] = None
        # The expiration date time of the Apple Volume Purchase Program Token.
        self._expiration_date_time: Optional[datetime] = None
        # Last modification date time associated with the Apple Volume Purchase Program Token.
        self._last_modified_date_time: Optional[datetime] = None
        # The last time when an application sync was done with the Apple volume purchase program service using the the Apple Volume Purchase Program Token.
        self._last_sync_date_time: Optional[datetime] = None
        # Possible sync statuses associated with an Apple Volume Purchase Program token.
        self._last_sync_status: Optional[vpp_token_sync_status.VppTokenSyncStatus] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The organization associated with the Apple Volume Purchase Program Token
        self._organization_name: Optional[str] = None
        # Possible states associated with an Apple Volume Purchase Program token.
        self._state: Optional[vpp_token_state.VppTokenState] = None
        # The Apple Volume Purchase Program Token string downloaded from the Apple Volume Purchase Program.
        self._token: Optional[str] = None
        # Possible types of an Apple Volume Purchase Program token.
        self._vpp_token_account_type: Optional[vpp_token_account_type.VppTokenAccountType] = None
    
    @property
    def country_or_region(self,) -> Optional[str]:
        """
        Gets the countryOrRegion property value. Whether or not apps for the VPP token will be automatically updated.
        Returns: Optional[str]
        """
        return self._country_or_region
    
    @country_or_region.setter
    def country_or_region(self,value: Optional[str] = None) -> None:
        """
        Sets the countryOrRegion property value. Whether or not apps for the VPP token will be automatically updated.
        Args:
            value: Value to set for the countryOrRegion property.
        """
        self._country_or_region = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> VppToken:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: VppToken
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return VppToken()
    
    @property
    def expiration_date_time(self,) -> Optional[datetime]:
        """
        Gets the expirationDateTime property value. The expiration date time of the Apple Volume Purchase Program Token.
        Returns: Optional[datetime]
        """
        return self._expiration_date_time
    
    @expiration_date_time.setter
    def expiration_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the expirationDateTime property value. The expiration date time of the Apple Volume Purchase Program Token.
        Args:
            value: Value to set for the expirationDateTime property.
        """
        self._expiration_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "apple_id": lambda n : setattr(self, 'apple_id', n.get_str_value()),
            "automatically_update_apps": lambda n : setattr(self, 'automatically_update_apps', n.get_bool_value()),
            "country_or_region": lambda n : setattr(self, 'country_or_region', n.get_str_value()),
            "expiration_date_time": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "last_sync_date_time": lambda n : setattr(self, 'last_sync_date_time', n.get_datetime_value()),
            "last_sync_status": lambda n : setattr(self, 'last_sync_status', n.get_enum_value(vpp_token_sync_status.VppTokenSyncStatus)),
            "organization_name": lambda n : setattr(self, 'organization_name', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(vpp_token_state.VppTokenState)),
            "token": lambda n : setattr(self, 'token', n.get_str_value()),
            "vpp_token_account_type": lambda n : setattr(self, 'vpp_token_account_type', n.get_enum_value(vpp_token_account_type.VppTokenAccountType)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. Last modification date time associated with the Apple Volume Purchase Program Token.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. Last modification date time associated with the Apple Volume Purchase Program Token.
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    @property
    def last_sync_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastSyncDateTime property value. The last time when an application sync was done with the Apple volume purchase program service using the the Apple Volume Purchase Program Token.
        Returns: Optional[datetime]
        """
        return self._last_sync_date_time
    
    @last_sync_date_time.setter
    def last_sync_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastSyncDateTime property value. The last time when an application sync was done with the Apple volume purchase program service using the the Apple Volume Purchase Program Token.
        Args:
            value: Value to set for the lastSyncDateTime property.
        """
        self._last_sync_date_time = value
    
    @property
    def last_sync_status(self,) -> Optional[vpp_token_sync_status.VppTokenSyncStatus]:
        """
        Gets the lastSyncStatus property value. Possible sync statuses associated with an Apple Volume Purchase Program token.
        Returns: Optional[vpp_token_sync_status.VppTokenSyncStatus]
        """
        return self._last_sync_status
    
    @last_sync_status.setter
    def last_sync_status(self,value: Optional[vpp_token_sync_status.VppTokenSyncStatus] = None) -> None:
        """
        Sets the lastSyncStatus property value. Possible sync statuses associated with an Apple Volume Purchase Program token.
        Args:
            value: Value to set for the lastSyncStatus property.
        """
        self._last_sync_status = value
    
    @property
    def organization_name(self,) -> Optional[str]:
        """
        Gets the organizationName property value. The organization associated with the Apple Volume Purchase Program Token
        Returns: Optional[str]
        """
        return self._organization_name
    
    @organization_name.setter
    def organization_name(self,value: Optional[str] = None) -> None:
        """
        Sets the organizationName property value. The organization associated with the Apple Volume Purchase Program Token
        Args:
            value: Value to set for the organizationName property.
        """
        self._organization_name = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("appleId", self.apple_id)
        writer.write_bool_value("automaticallyUpdateApps", self.automatically_update_apps)
        writer.write_str_value("countryOrRegion", self.country_or_region)
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_datetime_value("lastSyncDateTime", self.last_sync_date_time)
        writer.write_enum_value("lastSyncStatus", self.last_sync_status)
        writer.write_str_value("organizationName", self.organization_name)
        writer.write_enum_value("state", self.state)
        writer.write_str_value("token", self.token)
        writer.write_enum_value("vppTokenAccountType", self.vpp_token_account_type)
    
    @property
    def state(self,) -> Optional[vpp_token_state.VppTokenState]:
        """
        Gets the state property value. Possible states associated with an Apple Volume Purchase Program token.
        Returns: Optional[vpp_token_state.VppTokenState]
        """
        return self._state
    
    @state.setter
    def state(self,value: Optional[vpp_token_state.VppTokenState] = None) -> None:
        """
        Sets the state property value. Possible states associated with an Apple Volume Purchase Program token.
        Args:
            value: Value to set for the state property.
        """
        self._state = value
    
    @property
    def token(self,) -> Optional[str]:
        """
        Gets the token property value. The Apple Volume Purchase Program Token string downloaded from the Apple Volume Purchase Program.
        Returns: Optional[str]
        """
        return self._token
    
    @token.setter
    def token(self,value: Optional[str] = None) -> None:
        """
        Sets the token property value. The Apple Volume Purchase Program Token string downloaded from the Apple Volume Purchase Program.
        Args:
            value: Value to set for the token property.
        """
        self._token = value
    
    @property
    def vpp_token_account_type(self,) -> Optional[vpp_token_account_type.VppTokenAccountType]:
        """
        Gets the vppTokenAccountType property value. Possible types of an Apple Volume Purchase Program token.
        Returns: Optional[vpp_token_account_type.VppTokenAccountType]
        """
        return self._vpp_token_account_type
    
    @vpp_token_account_type.setter
    def vpp_token_account_type(self,value: Optional[vpp_token_account_type.VppTokenAccountType] = None) -> None:
        """
        Sets the vppTokenAccountType property value. Possible types of an Apple Volume Purchase Program token.
        Args:
            value: Value to set for the vppTokenAccountType property.
        """
        self._vpp_token_account_type = value
    

