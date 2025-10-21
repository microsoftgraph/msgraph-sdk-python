from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .vpp_token_account_type import VppTokenAccountType
    from .vpp_token_state import VppTokenState
    from .vpp_token_sync_status import VppTokenSyncStatus

from .entity import Entity

@dataclass
class VppToken(Entity, Parsable):
    """
    You purchase multiple licenses for iOS apps through the Apple Volume Purchase Program for Business or Education. This involves setting up an Apple VPP account from the Apple website and uploading the Apple VPP Business or Education token to Intune. You can then synchronize your volume purchase information with Intune and track your volume-purchased app use. You can upload multiple Apple VPP Business or Education tokens.
    """
    # The apple Id associated with the given Apple Volume Purchase Program Token.
    apple_id: Optional[str] = None
    # Whether or not apps for the VPP token will be automatically updated.
    automatically_update_apps: Optional[bool] = None
    # Whether or not apps for the VPP token will be automatically updated.
    country_or_region: Optional[str] = None
    # The expiration date time of the Apple Volume Purchase Program Token.
    expiration_date_time: Optional[datetime.datetime] = None
    # Last modification date time associated with the Apple Volume Purchase Program Token.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The last time when an application sync was done with the Apple volume purchase program service using the the Apple Volume Purchase Program Token.
    last_sync_date_time: Optional[datetime.datetime] = None
    # Possible sync statuses associated with an Apple Volume Purchase Program token.
    last_sync_status: Optional[VppTokenSyncStatus] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The organization associated with the Apple Volume Purchase Program Token
    organization_name: Optional[str] = None
    # Possible states associated with an Apple Volume Purchase Program token.
    state: Optional[VppTokenState] = None
    # The Apple Volume Purchase Program Token string downloaded from the Apple Volume Purchase Program.
    token: Optional[str] = None
    # Possible types of an Apple Volume Purchase Program token.
    vpp_token_account_type: Optional[VppTokenAccountType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> VppToken:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: VppToken
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return VppToken()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .vpp_token_account_type import VppTokenAccountType
        from .vpp_token_state import VppTokenState
        from .vpp_token_sync_status import VppTokenSyncStatus

        from .entity import Entity
        from .vpp_token_account_type import VppTokenAccountType
        from .vpp_token_state import VppTokenState
        from .vpp_token_sync_status import VppTokenSyncStatus

        fields: dict[str, Callable[[Any], None]] = {
            "appleId": lambda n : setattr(self, 'apple_id', n.get_str_value()),
            "automaticallyUpdateApps": lambda n : setattr(self, 'automatically_update_apps', n.get_bool_value()),
            "countryOrRegion": lambda n : setattr(self, 'country_or_region', n.get_str_value()),
            "expirationDateTime": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "lastSyncDateTime": lambda n : setattr(self, 'last_sync_date_time', n.get_datetime_value()),
            "lastSyncStatus": lambda n : setattr(self, 'last_sync_status', n.get_enum_value(VppTokenSyncStatus)),
            "organizationName": lambda n : setattr(self, 'organization_name', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(VppTokenState)),
            "token": lambda n : setattr(self, 'token', n.get_str_value()),
            "vppTokenAccountType": lambda n : setattr(self, 'vpp_token_account_type', n.get_enum_value(VppTokenAccountType)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
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
    

