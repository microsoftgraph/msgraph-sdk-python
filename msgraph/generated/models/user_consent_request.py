from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .approval import Approval
    from .request import Request

from .request import Request

@dataclass
class UserConsentRequest(Request, Parsable):
    # Approval decisions associated with a request.
    approval: Optional[Approval] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The user's justification for requiring access to the app. Supports $filter (eq only) and $orderby.
    reason: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserConsentRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserConsentRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserConsentRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .approval import Approval
        from .request import Request

        from .approval import Approval
        from .request import Request

        fields: dict[str, Callable[[Any], None]] = {
            "approval": lambda n : setattr(self, 'approval', n.get_object_value(Approval)),
            "reason": lambda n : setattr(self, 'reason', n.get_str_value()),
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
        writer.write_object_value("approval", self.approval)
        writer.write_str_value("reason", self.reason)
    

