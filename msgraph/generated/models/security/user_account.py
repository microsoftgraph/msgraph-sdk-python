from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class UserAccount(AdditionalDataHolder, Parsable):
    @property
    def account_name(self,) -> Optional[str]:
        """
        Gets the accountName property value. The user account's displayed name.
        Returns: Optional[str]
        """
        return self._account_name
    
    @account_name.setter
    def account_name(self,value: Optional[str] = None) -> None:
        """
        Sets the accountName property value. The user account's displayed name.
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
    
    @property
    def azure_ad_user_id(self,) -> Optional[str]:
        """
        Gets the azureAdUserId property value. The user object identifier in Azure AD.
        Returns: Optional[str]
        """
        return self._azure_ad_user_id
    
    @azure_ad_user_id.setter
    def azure_ad_user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the azureAdUserId property value. The user object identifier in Azure AD.
        Args:
            value: Value to set for the azureAdUserId property.
        """
        self._azure_ad_user_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new userAccount and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The user account's displayed name.
        self._account_name: Optional[str] = None
        # The user object identifier in Azure AD.
        self._azure_ad_user_id: Optional[str] = None
        # The name of the Active Directory domain of which the user is a member.
        self._domain_name: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The user principal name of the account in Azure AD.
        self._user_principal_name: Optional[str] = None
        # The local security identifier of the user account.
        self._user_sid: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserAccount:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserAccount
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserAccount()
    
    @property
    def domain_name(self,) -> Optional[str]:
        """
        Gets the domainName property value. The name of the Active Directory domain of which the user is a member.
        Returns: Optional[str]
        """
        return self._domain_name
    
    @domain_name.setter
    def domain_name(self,value: Optional[str] = None) -> None:
        """
        Sets the domainName property value. The name of the Active Directory domain of which the user is a member.
        Args:
            value: Value to set for the domainName property.
        """
        self._domain_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "account_name": lambda n : setattr(self, 'account_name', n.get_str_value()),
            "azure_ad_user_id": lambda n : setattr(self, 'azure_ad_user_id', n.get_str_value()),
            "domain_name": lambda n : setattr(self, 'domain_name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "user_principal_name": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
            "user_sid": lambda n : setattr(self, 'user_sid', n.get_str_value()),
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
        writer.write_str_value("accountName", self.account_name)
        writer.write_str_value("azureAdUserId", self.azure_ad_user_id)
        writer.write_str_value("domainName", self.domain_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
        writer.write_str_value("userSid", self.user_sid)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def user_principal_name(self,) -> Optional[str]:
        """
        Gets the userPrincipalName property value. The user principal name of the account in Azure AD.
        Returns: Optional[str]
        """
        return self._user_principal_name
    
    @user_principal_name.setter
    def user_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userPrincipalName property value. The user principal name of the account in Azure AD.
        Args:
            value: Value to set for the userPrincipalName property.
        """
        self._user_principal_name = value
    
    @property
    def user_sid(self,) -> Optional[str]:
        """
        Gets the userSid property value. The local security identifier of the user account.
        Returns: Optional[str]
        """
        return self._user_sid
    
    @user_sid.setter
    def user_sid(self,value: Optional[str] = None) -> None:
        """
        Sets the userSid property value. The local security identifier of the user account.
        Args:
            value: Value to set for the userSid property.
        """
        self._user_sid = value
    

