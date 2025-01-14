from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .app_consent_request_scope import AppConsentRequestScope
    from .entity import Entity
    from .user_consent_request import UserConsentRequest

from .entity import Entity

@dataclass
class AppConsentRequest(Entity, Parsable):
    # The display name of the app for which consent is requested. Required. Supports $filter (eq only) and $orderby.
    app_display_name: Optional[str] = None
    # The identifier of the application. Required. Supports $filter (eq only) and $orderby.
    app_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # A list of pending scopes waiting for approval. Required.
    pending_scopes: Optional[list[AppConsentRequestScope]] = None
    # A list of pending user consent requests. Supports $filter (eq).
    user_consent_requests: Optional[list[UserConsentRequest]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AppConsentRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AppConsentRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AppConsentRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .app_consent_request_scope import AppConsentRequestScope
        from .entity import Entity
        from .user_consent_request import UserConsentRequest

        from .app_consent_request_scope import AppConsentRequestScope
        from .entity import Entity
        from .user_consent_request import UserConsentRequest

        fields: dict[str, Callable[[Any], None]] = {
            "appDisplayName": lambda n : setattr(self, 'app_display_name', n.get_str_value()),
            "appId": lambda n : setattr(self, 'app_id', n.get_str_value()),
            "pendingScopes": lambda n : setattr(self, 'pending_scopes', n.get_collection_of_object_values(AppConsentRequestScope)),
            "userConsentRequests": lambda n : setattr(self, 'user_consent_requests', n.get_collection_of_object_values(UserConsentRequest)),
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
        writer.write_str_value("appDisplayName", self.app_display_name)
        writer.write_str_value("appId", self.app_id)
        writer.write_collection_of_object_values("pendingScopes", self.pending_scopes)
        writer.write_collection_of_object_values("userConsentRequests", self.user_consent_requests)
    

