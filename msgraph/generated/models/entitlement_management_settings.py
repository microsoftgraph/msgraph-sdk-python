from __future__ import annotations
from dataclasses import dataclass, field
from datetime import timedelta
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import access_package_external_user_lifecycle_action, entity

from . import entity

@dataclass
class EntitlementManagementSettings(entity.Entity):
    # If externalUserLifecycleAction is blockSignInAndDelete, the duration, typically a number of days, after an external user is blocked from sign in before their account is deleted.
    duration_until_external_user_deleted_after_blocked: Optional[timedelta] = None
    # Automatic action that the service should take when an external user's last access package assignment is removed. The possible values are: none, blockSignIn, blockSignInAndDelete, unknownFutureValue.
    external_user_lifecycle_action: Optional[access_package_external_user_lifecycle_action.AccessPackageExternalUserLifecycleAction] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EntitlementManagementSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EntitlementManagementSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EntitlementManagementSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import access_package_external_user_lifecycle_action, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "durationUntilExternalUserDeletedAfterBlocked": lambda n : setattr(self, 'duration_until_external_user_deleted_after_blocked', n.get_timedelta_value()),
            "externalUserLifecycleAction": lambda n : setattr(self, 'external_user_lifecycle_action', n.get_enum_value(access_package_external_user_lifecycle_action.AccessPackageExternalUserLifecycleAction)),
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
        writer.write_timedelta_value("durationUntilExternalUserDeletedAfterBlocked", self.duration_until_external_user_deleted_after_blocked)
        writer.write_enum_value("externalUserLifecycleAction", self.external_user_lifecycle_action)
    

