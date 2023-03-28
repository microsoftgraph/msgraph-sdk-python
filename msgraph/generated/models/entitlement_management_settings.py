from __future__ import annotations
from datetime import timedelta
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import access_package_external_user_lifecycle_action, entity

from . import entity

class EntitlementManagementSettings(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new entitlementManagementSettings and sets the default values.
        """
        super().__init__()
        # If externalUserLifecycleAction is blockSignInAndDelete, the duration, typically a number of days, after an external user is blocked from sign in before their account is deleted.
        self._duration_until_external_user_deleted_after_blocked: Optional[timedelta] = None
        # Automatic action that the service should take when an external user's last access package assignment is removed. The possible values are: none, blockSignIn, blockSignInAndDelete, unknownFutureValue.
        self._external_user_lifecycle_action: Optional[access_package_external_user_lifecycle_action.AccessPackageExternalUserLifecycleAction] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
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
    
    @property
    def duration_until_external_user_deleted_after_blocked(self,) -> Optional[timedelta]:
        """
        Gets the durationUntilExternalUserDeletedAfterBlocked property value. If externalUserLifecycleAction is blockSignInAndDelete, the duration, typically a number of days, after an external user is blocked from sign in before their account is deleted.
        Returns: Optional[timedelta]
        """
        return self._duration_until_external_user_deleted_after_blocked
    
    @duration_until_external_user_deleted_after_blocked.setter
    def duration_until_external_user_deleted_after_blocked(self,value: Optional[timedelta] = None) -> None:
        """
        Sets the durationUntilExternalUserDeletedAfterBlocked property value. If externalUserLifecycleAction is blockSignInAndDelete, the duration, typically a number of days, after an external user is blocked from sign in before their account is deleted.
        Args:
            value: Value to set for the duration_until_external_user_deleted_after_blocked property.
        """
        self._duration_until_external_user_deleted_after_blocked = value
    
    @property
    def external_user_lifecycle_action(self,) -> Optional[access_package_external_user_lifecycle_action.AccessPackageExternalUserLifecycleAction]:
        """
        Gets the externalUserLifecycleAction property value. Automatic action that the service should take when an external user's last access package assignment is removed. The possible values are: none, blockSignIn, blockSignInAndDelete, unknownFutureValue.
        Returns: Optional[access_package_external_user_lifecycle_action.AccessPackageExternalUserLifecycleAction]
        """
        return self._external_user_lifecycle_action
    
    @external_user_lifecycle_action.setter
    def external_user_lifecycle_action(self,value: Optional[access_package_external_user_lifecycle_action.AccessPackageExternalUserLifecycleAction] = None) -> None:
        """
        Sets the externalUserLifecycleAction property value. Automatic action that the service should take when an external user's last access package assignment is removed. The possible values are: none, blockSignIn, blockSignInAndDelete, unknownFutureValue.
        Args:
            value: Value to set for the external_user_lifecycle_action property.
        """
        self._external_user_lifecycle_action = value
    
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
    

