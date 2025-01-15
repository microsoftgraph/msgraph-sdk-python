from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class TeamsAppSettings(Entity, Parsable):
    # Indicates whether users are allowed to request access to the unavailable Teams apps.
    allow_user_requests_for_app_access: Optional[bool] = None
    # Indicates whether resource-specific consent for personal scope in Teams apps is enabled for the tenant. True indicates that Teams apps that are allowed in the tenant and require resource-specific permissions can be installed in the personal scope. False blocks the installation of any Teams app that requires resource-specific permissions in the personal scope.
    is_user_personal_scope_resource_specific_consent_enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TeamsAppSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TeamsAppSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TeamsAppSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "allowUserRequestsForAppAccess": lambda n : setattr(self, 'allow_user_requests_for_app_access', n.get_bool_value()),
            "isUserPersonalScopeResourceSpecificConsentEnabled": lambda n : setattr(self, 'is_user_personal_scope_resource_specific_consent_enabled', n.get_bool_value()),
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
        writer.write_bool_value("allowUserRequestsForAppAccess", self.allow_user_requests_for_app_access)
        writer.write_bool_value("isUserPersonalScopeResourceSpecificConsentEnabled", self.is_user_personal_scope_resource_specific_consent_enabled)
    

