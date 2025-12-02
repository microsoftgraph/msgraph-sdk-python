from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .account import Account
    from .user import User

from ..entity import Entity

@dataclass
class IdentityAccounts(Entity, Parsable):
    # Collection of accounts of the identity in different identity providers.
    accounts: Optional[list[Account]] = None
    # The cloud security identifier of the identityAccount.
    cloud_security_identifier: Optional[str] = None
    # The  Active Directory display name of the identityAccount.
    display_name: Optional[str] = None
    # The Active Directory domain name of the identityAccount.
    domain: Optional[str] = None
    # Boolean indicating if the identityAccounts is enabled.
    is_enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The on-premises security identifier of the identityAccount.
    on_premises_security_identifier: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IdentityAccounts:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IdentityAccounts
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.user".casefold():
            from .user import User

            return User()
        return IdentityAccounts()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .account import Account
        from .user import User

        from ..entity import Entity
        from .account import Account
        from .user import User

        fields: dict[str, Callable[[Any], None]] = {
            "accounts": lambda n : setattr(self, 'accounts', n.get_collection_of_object_values(Account)),
            "cloudSecurityIdentifier": lambda n : setattr(self, 'cloud_security_identifier', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "domain": lambda n : setattr(self, 'domain', n.get_str_value()),
            "isEnabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
            "onPremisesSecurityIdentifier": lambda n : setattr(self, 'on_premises_security_identifier', n.get_str_value()),
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
        writer.write_collection_of_object_values("accounts", self.accounts)
        writer.write_str_value("cloudSecurityIdentifier", self.cloud_security_identifier)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("domain", self.domain)
        writer.write_bool_value("isEnabled", self.is_enabled)
        writer.write_str_value("onPremisesSecurityIdentifier", self.on_premises_security_identifier)
    

