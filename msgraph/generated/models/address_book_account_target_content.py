from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .account_target_content import AccountTargetContent

from .account_target_content import AccountTargetContent

@dataclass
class AddressBookAccountTargetContent(AccountTargetContent, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.addressBookAccountTargetContent"
    # List of user emails targeted for an attack simulation training campaign.
    account_target_emails: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AddressBookAccountTargetContent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AddressBookAccountTargetContent
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AddressBookAccountTargetContent()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .account_target_content import AccountTargetContent

        from .account_target_content import AccountTargetContent

        fields: dict[str, Callable[[Any], None]] = {
            "accountTargetEmails": lambda n : setattr(self, 'account_target_emails', n.get_collection_of_primitive_values(str)),
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
        writer.write_collection_of_primitive_values("accountTargetEmails", self.account_target_emails)
    

