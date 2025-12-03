from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ......models.security.action import Action
    from ......models.security.identity_provider import IdentityProvider

@dataclass
class InvokeActionPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The accountId property
    account_id: Optional[str] = None
    # The action property
    action: Optional[Action] = None
    # The identityProvider property
    identity_provider: Optional[IdentityProvider] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> InvokeActionPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: InvokeActionPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return InvokeActionPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ......models.security.action import Action
        from ......models.security.identity_provider import IdentityProvider

        from ......models.security.action import Action
        from ......models.security.identity_provider import IdentityProvider

        fields: dict[str, Callable[[Any], None]] = {
            "accountId": lambda n : setattr(self, 'account_id', n.get_str_value()),
            "action": lambda n : setattr(self, 'action', n.get_enum_value(Action)),
            "identityProvider": lambda n : setattr(self, 'identity_provider', n.get_enum_value(IdentityProvider)),
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
        writer.write_str_value("accountId", self.account_id)
        writer.write_enum_value("action", self.action)
        writer.write_enum_value("identityProvider", self.identity_provider)
        writer.write_additional_data_value(self.additional_data)
    

