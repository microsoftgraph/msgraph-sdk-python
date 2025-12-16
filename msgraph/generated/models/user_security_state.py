from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .email_role import EmailRole
    from .logon_type import LogonType
    from .user_account_security_type import UserAccountSecurityType

@dataclass
class UserSecurityState(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # AAD User object identifier (GUID) - represents the physical/multi-account user entity.
    aad_user_id: Optional[str] = None
    # Account name of user account (without Active Directory domain or DNS domain) - (also called mailNickName).
    account_name: Optional[str] = None
    # NetBIOS/Active Directory domain of user account (that is, domain/account format).
    domain_name: Optional[str] = None
    # For email-related alerts - user account's email 'role'. The possible values are: unknown, sender, recipient.
    email_role: Optional[EmailRole] = None
    # Indicates whether the user logged on through a VPN.
    is_vpn: Optional[bool] = None
    # Time at which the sign-in occurred. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    logon_date_time: Optional[datetime.datetime] = None
    # User sign-in ID.
    logon_id: Optional[str] = None
    # IP Address the sign-in request originated from.
    logon_ip: Optional[str] = None
    # Location (by IP address mapping) associated with a user sign-in event by this user.
    logon_location: Optional[str] = None
    # Method of user sign in. The possible values are: unknown, interactive, remoteInteractive, network, batch, service.
    logon_type: Optional[LogonType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Active Directory (on-premises) Security Identifier (SID) of the user.
    on_premises_security_identifier: Optional[str] = None
    # Provider-generated/calculated risk score of the user account. Recommended value range of 0-1, which equates to a percentage.
    risk_score: Optional[str] = None
    # User account type (group membership), per Windows definition. The possible values are: unknown, standard, power, administrator.
    user_account_type: Optional[UserAccountSecurityType] = None
    # User sign-in name - internet format: (user account name)@(user account DNS domain name).
    user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserSecurityState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserSecurityState
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserSecurityState()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .email_role import EmailRole
        from .logon_type import LogonType
        from .user_account_security_type import UserAccountSecurityType

        from .email_role import EmailRole
        from .logon_type import LogonType
        from .user_account_security_type import UserAccountSecurityType

        fields: dict[str, Callable[[Any], None]] = {
            "aadUserId": lambda n : setattr(self, 'aad_user_id', n.get_str_value()),
            "accountName": lambda n : setattr(self, 'account_name', n.get_str_value()),
            "domainName": lambda n : setattr(self, 'domain_name', n.get_str_value()),
            "emailRole": lambda n : setattr(self, 'email_role', n.get_enum_value(EmailRole)),
            "isVpn": lambda n : setattr(self, 'is_vpn', n.get_bool_value()),
            "logonDateTime": lambda n : setattr(self, 'logon_date_time', n.get_datetime_value()),
            "logonId": lambda n : setattr(self, 'logon_id', n.get_str_value()),
            "logonIp": lambda n : setattr(self, 'logon_ip', n.get_str_value()),
            "logonLocation": lambda n : setattr(self, 'logon_location', n.get_str_value()),
            "logonType": lambda n : setattr(self, 'logon_type', n.get_enum_value(LogonType)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "onPremisesSecurityIdentifier": lambda n : setattr(self, 'on_premises_security_identifier', n.get_str_value()),
            "riskScore": lambda n : setattr(self, 'risk_score', n.get_str_value()),
            "userAccountType": lambda n : setattr(self, 'user_account_type', n.get_enum_value(UserAccountSecurityType)),
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
        writer.write_str_value("aadUserId", self.aad_user_id)
        writer.write_str_value("accountName", self.account_name)
        writer.write_str_value("domainName", self.domain_name)
        writer.write_enum_value("emailRole", self.email_role)
        writer.write_bool_value("isVpn", self.is_vpn)
        writer.write_datetime_value("logonDateTime", self.logon_date_time)
        writer.write_str_value("logonId", self.logon_id)
        writer.write_str_value("logonIp", self.logon_ip)
        writer.write_str_value("logonLocation", self.logon_location)
        writer.write_enum_value("logonType", self.logon_type)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("onPremisesSecurityIdentifier", self.on_premises_security_identifier)
        writer.write_str_value("riskScore", self.risk_score)
        writer.write_enum_value("userAccountType", self.user_account_type)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
        writer.write_additional_data_value(self.additional_data)
    

