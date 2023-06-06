from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import approval, request

from . import request

@dataclass
class UserConsentRequest(request.Request):
    # Approval decisions associated with a request.
    approval: Optional[approval.Approval] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The user's justification for requiring access to the app. Supports $filter (eq only) and $orderby.
    reason: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserConsentRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserConsentRequest
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserConsentRequest()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import approval, request

        fields: Dict[str, Callable[[Any], None]] = {
            "approval": lambda n : setattr(self, 'approval', n.get_object_value(approval.Approval)),
            "reason": lambda n : setattr(self, 'reason', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("approval", self.approval)
        writer.write_str_value("reason", self.reason)
    

