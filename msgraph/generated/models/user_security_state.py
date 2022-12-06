from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

email_role = lazy_import('msgraph.generated.models.email_role')
logon_type = lazy_import('msgraph.generated.models.logon_type')
user_account_security_type = lazy_import('msgraph.generated.models.user_account_security_type')

class UserSecurityState(AdditionalDataHolder, Parsable):
    @property
    def aad_user_id(self,) -> Optional[str]:
        """
        Gets the aadUserId property value. AAD User object identifier (GUID) - represents the physical/multi-account user entity.
        Returns: Optional[str]
        """
        return self._aad_user_id
    
    @aad_user_id.setter
    def aad_user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the aadUserId property value. AAD User object identifier (GUID) - represents the physical/multi-account user entity.
        Args:
            value: Value to set for the aadUserId property.
        """
        self._aad_user_id = value
    
    @property
    def account_name(self,) -> Optional[str]:
        """
        Gets the accountName property value. Account name of user account (without Active Directory domain or DNS domain) - (also called mailNickName).
        Returns: Optional[str]
        """
        return self._account_name
    
    @account_name.setter
    def account_name(self,value: Optional[str] = None) -> None:
        """
        Sets the accountName property value. Account name of user account (without Active Directory domain or DNS domain) - (also called mailNickName).
        Args:
            value: Value to set for the accountName property.
        """
        self._account_name = value
    
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
        Instantiates a new userSecurityState and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # AAD User object identifier (GUID) - represents the physical/multi-account user entity.
        self._aad_user_id: Optional[str] = None
        # Account name of user account (without Active Directory domain or DNS domain) - (also called mailNickName).
        self._account_name: Optional[str] = None
        # NetBIOS/Active Directory domain of user account (that is, domain/account format).
        self._domain_name: Optional[str] = None
        # For email-related alerts - user account's email 'role'. Possible values are: unknown, sender, recipient.
        self._email_role: Optional[email_role.EmailRole] = None
        # Indicates whether the user logged on through a VPN.
        self._is_vpn: Optional[bool] = None
        # Time at which the sign-in occurred. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._logon_date_time: Optional[datetime] = None
        # User sign-in ID.
        self._logon_id: Optional[str] = None
        # IP Address the sign-in request originated from.
        self._logon_ip: Optional[str] = None
        # Location (by IP address mapping) associated with a user sign-in event by this user.
        self._logon_location: Optional[str] = None
        # Method of user sign in. Possible values are: unknown, interactive, remoteInteractive, network, batch, service.
        self._logon_type: Optional[logon_type.LogonType] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Active Directory (on-premises) Security Identifier (SID) of the user.
        self._on_premises_security_identifier: Optional[str] = None
        # Provider-generated/calculated risk score of the user account. Recommended value range of 0-1, which equates to a percentage.
        self._risk_score: Optional[str] = None
        # User account type (group membership), per Windows definition. Possible values are: unknown, standard, power, administrator.
        self._user_account_type: Optional[user_account_security_type.UserAccountSecurityType] = None
        # User sign-in name - internet format: (user account name)@(user account DNS domain name).
        self._user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserSecurityState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserSecurityState
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserSecurityState()
    
    @property
    def domain_name(self,) -> Optional[str]:
        """
        Gets the domainName property value. NetBIOS/Active Directory domain of user account (that is, domain/account format).
        Returns: Optional[str]
        """
        return self._domain_name
    
    @domain_name.setter
    def domain_name(self,value: Optional[str] = None) -> None:
        """
        Sets the domainName property value. NetBIOS/Active Directory domain of user account (that is, domain/account format).
        Args:
            value: Value to set for the domainName property.
        """
        self._domain_name = value
    
    @property
    def email_role(self,) -> Optional[email_role.EmailRole]:
        """
        Gets the emailRole property value. For email-related alerts - user account's email 'role'. Possible values are: unknown, sender, recipient.
        Returns: Optional[email_role.EmailRole]
        """
        return self._email_role
    
    @email_role.setter
    def email_role(self,value: Optional[email_role.EmailRole] = None) -> None:
        """
        Sets the emailRole property value. For email-related alerts - user account's email 'role'. Possible values are: unknown, sender, recipient.
        Args:
            value: Value to set for the emailRole property.
        """
        self._email_role = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "aad_user_id": lambda n : setattr(self, 'aad_user_id', n.get_str_value()),
            "account_name": lambda n : setattr(self, 'account_name', n.get_str_value()),
            "domain_name": lambda n : setattr(self, 'domain_name', n.get_str_value()),
            "email_role": lambda n : setattr(self, 'email_role', n.get_enum_value(email_role.EmailRole)),
            "is_vpn": lambda n : setattr(self, 'is_vpn', n.get_bool_value()),
            "logon_date_time": lambda n : setattr(self, 'logon_date_time', n.get_datetime_value()),
            "logon_id": lambda n : setattr(self, 'logon_id', n.get_str_value()),
            "logon_ip": lambda n : setattr(self, 'logon_ip', n.get_str_value()),
            "logon_location": lambda n : setattr(self, 'logon_location', n.get_str_value()),
            "logon_type": lambda n : setattr(self, 'logon_type', n.get_enum_value(logon_type.LogonType)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "on_premises_security_identifier": lambda n : setattr(self, 'on_premises_security_identifier', n.get_str_value()),
            "risk_score": lambda n : setattr(self, 'risk_score', n.get_str_value()),
            "user_account_type": lambda n : setattr(self, 'user_account_type', n.get_enum_value(user_account_security_type.UserAccountSecurityType)),
            "user_principal_name": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
        }
        return fields
    
    @property
    def is_vpn(self,) -> Optional[bool]:
        """
        Gets the isVpn property value. Indicates whether the user logged on through a VPN.
        Returns: Optional[bool]
        """
        return self._is_vpn
    
    @is_vpn.setter
    def is_vpn(self,value: Optional[bool] = None) -> None:
        """
        Sets the isVpn property value. Indicates whether the user logged on through a VPN.
        Args:
            value: Value to set for the isVpn property.
        """
        self._is_vpn = value
    
    @property
    def logon_date_time(self,) -> Optional[datetime]:
        """
        Gets the logonDateTime property value. Time at which the sign-in occurred. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._logon_date_time
    
    @logon_date_time.setter
    def logon_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the logonDateTime property value. Time at which the sign-in occurred. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the logonDateTime property.
        """
        self._logon_date_time = value
    
    @property
    def logon_id(self,) -> Optional[str]:
        """
        Gets the logonId property value. User sign-in ID.
        Returns: Optional[str]
        """
        return self._logon_id
    
    @logon_id.setter
    def logon_id(self,value: Optional[str] = None) -> None:
        """
        Sets the logonId property value. User sign-in ID.
        Args:
            value: Value to set for the logonId property.
        """
        self._logon_id = value
    
    @property
    def logon_ip(self,) -> Optional[str]:
        """
        Gets the logonIp property value. IP Address the sign-in request originated from.
        Returns: Optional[str]
        """
        return self._logon_ip
    
    @logon_ip.setter
    def logon_ip(self,value: Optional[str] = None) -> None:
        """
        Sets the logonIp property value. IP Address the sign-in request originated from.
        Args:
            value: Value to set for the logonIp property.
        """
        self._logon_ip = value
    
    @property
    def logon_location(self,) -> Optional[str]:
        """
        Gets the logonLocation property value. Location (by IP address mapping) associated with a user sign-in event by this user.
        Returns: Optional[str]
        """
        return self._logon_location
    
    @logon_location.setter
    def logon_location(self,value: Optional[str] = None) -> None:
        """
        Sets the logonLocation property value. Location (by IP address mapping) associated with a user sign-in event by this user.
        Args:
            value: Value to set for the logonLocation property.
        """
        self._logon_location = value
    
    @property
    def logon_type(self,) -> Optional[logon_type.LogonType]:
        """
        Gets the logonType property value. Method of user sign in. Possible values are: unknown, interactive, remoteInteractive, network, batch, service.
        Returns: Optional[logon_type.LogonType]
        """
        return self._logon_type
    
    @logon_type.setter
    def logon_type(self,value: Optional[logon_type.LogonType] = None) -> None:
        """
        Sets the logonType property value. Method of user sign in. Possible values are: unknown, interactive, remoteInteractive, network, batch, service.
        Args:
            value: Value to set for the logonType property.
        """
        self._logon_type = value
    
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
    def on_premises_security_identifier(self,) -> Optional[str]:
        """
        Gets the onPremisesSecurityIdentifier property value. Active Directory (on-premises) Security Identifier (SID) of the user.
        Returns: Optional[str]
        """
        return self._on_premises_security_identifier
    
    @on_premises_security_identifier.setter
    def on_premises_security_identifier(self,value: Optional[str] = None) -> None:
        """
        Sets the onPremisesSecurityIdentifier property value. Active Directory (on-premises) Security Identifier (SID) of the user.
        Args:
            value: Value to set for the onPremisesSecurityIdentifier property.
        """
        self._on_premises_security_identifier = value
    
    @property
    def risk_score(self,) -> Optional[str]:
        """
        Gets the riskScore property value. Provider-generated/calculated risk score of the user account. Recommended value range of 0-1, which equates to a percentage.
        Returns: Optional[str]
        """
        return self._risk_score
    
    @risk_score.setter
    def risk_score(self,value: Optional[str] = None) -> None:
        """
        Sets the riskScore property value. Provider-generated/calculated risk score of the user account. Recommended value range of 0-1, which equates to a percentage.
        Args:
            value: Value to set for the riskScore property.
        """
        self._risk_score = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
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
    
    @property
    def user_account_type(self,) -> Optional[user_account_security_type.UserAccountSecurityType]:
        """
        Gets the userAccountType property value. User account type (group membership), per Windows definition. Possible values are: unknown, standard, power, administrator.
        Returns: Optional[user_account_security_type.UserAccountSecurityType]
        """
        return self._user_account_type
    
    @user_account_type.setter
    def user_account_type(self,value: Optional[user_account_security_type.UserAccountSecurityType] = None) -> None:
        """
        Sets the userAccountType property value. User account type (group membership), per Windows definition. Possible values are: unknown, standard, power, administrator.
        Args:
            value: Value to set for the userAccountType property.
        """
        self._user_account_type = value
    
    @property
    def user_principal_name(self,) -> Optional[str]:
        """
        Gets the userPrincipalName property value. User sign-in name - internet format: (user account name)@(user account DNS domain name).
        Returns: Optional[str]
        """
        return self._user_principal_name
    
    @user_principal_name.setter
    def user_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userPrincipalName property value. User sign-in name - internet format: (user account name)@(user account DNS domain name).
        Args:
            value: Value to set for the userPrincipalName property.
        """
        self._user_principal_name = value
    

