from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

alert_evidence = lazy_import('msgraph.generated.models.security.alert_evidence')
user_account = lazy_import('msgraph.generated.models.security.user_account')

class MailboxEvidence(alert_evidence.AlertEvidence):
    def __init__(self,) -> None:
        """
        Instantiates a new MailboxEvidence and sets the default values.
        """
        super().__init__()
        # The name associated with the mailbox.
        self._display_name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The primary email address of the mailbox.
        self._primary_address: Optional[str] = None
        # The user account of the mailbox.
        self._user_account: Optional[user_account.UserAccount] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MailboxEvidence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MailboxEvidence
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MailboxEvidence()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The name associated with the mailbox.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The name associated with the mailbox.
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
            "primary_address": lambda n : setattr(self, 'primary_address', n.get_str_value()),
            "user_account": lambda n : setattr(self, 'user_account', n.get_object_value(user_account.UserAccount)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def primary_address(self,) -> Optional[str]:
        """
        Gets the primaryAddress property value. The primary email address of the mailbox.
        Returns: Optional[str]
        """
        return self._primary_address
    
    @primary_address.setter
    def primary_address(self,value: Optional[str] = None) -> None:
        """
        Sets the primaryAddress property value. The primary email address of the mailbox.
        Args:
            value: Value to set for the primaryAddress property.
        """
        self._primary_address = value
    
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
        writer.write_str_value("primaryAddress", self.primary_address)
        writer.write_object_value("userAccount", self.user_account)
    
    @property
    def user_account(self,) -> Optional[user_account.UserAccount]:
        """
        Gets the userAccount property value. The user account of the mailbox.
        Returns: Optional[user_account.UserAccount]
        """
        return self._user_account
    
    @user_account.setter
    def user_account(self,value: Optional[user_account.UserAccount] = None) -> None:
        """
        Sets the userAccount property value. The user account of the mailbox.
        Args:
            value: Value to set for the userAccount property.
        """
        self._user_account = value
    

