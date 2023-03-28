from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

approval = lazy_import('msgraph.generated.models.approval')
request = lazy_import('msgraph.generated.models.request')

class UserConsentRequest(request.Request):
    @property
    def approval(self,) -> Optional[approval.Approval]:
        """
        Gets the approval property value. Approval decisions associated with a request.
        Returns: Optional[approval.Approval]
        """
        return self._approval
    
    @approval.setter
    def approval(self,value: Optional[approval.Approval] = None) -> None:
        """
        Sets the approval property value. Approval decisions associated with a request.
        Args:
            value: Value to set for the approval property.
        """
        self._approval = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new UserConsentRequest and sets the default values.
        """
        super().__init__()
        # Approval decisions associated with a request.
        self._approval: Optional[approval.Approval] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The user's justification for requiring access to the app. Supports $filter (eq only) and $orderby.
        self._reason: Optional[str] = None
    
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
        fields = {
            "approval": lambda n : setattr(self, 'approval', n.get_object_value(approval.Approval)),
            "reason": lambda n : setattr(self, 'reason', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def reason(self,) -> Optional[str]:
        """
        Gets the reason property value. The user's justification for requiring access to the app. Supports $filter (eq only) and $orderby.
        Returns: Optional[str]
        """
        return self._reason
    
    @reason.setter
    def reason(self,value: Optional[str] = None) -> None:
        """
        Sets the reason property value. The user's justification for requiring access to the app. Supports $filter (eq only) and $orderby.
        Args:
            value: Value to set for the reason property.
        """
        self._reason = value
    
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
    

