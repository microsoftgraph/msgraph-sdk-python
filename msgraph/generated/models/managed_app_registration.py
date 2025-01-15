from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .android_managed_app_registration import AndroidManagedAppRegistration
    from .entity import Entity
    from .ios_managed_app_registration import IosManagedAppRegistration
    from .managed_app_flagged_reason import ManagedAppFlaggedReason
    from .managed_app_operation import ManagedAppOperation
    from .managed_app_policy import ManagedAppPolicy
    from .mobile_app_identifier import MobileAppIdentifier

from .entity import Entity

@dataclass
class ManagedAppRegistration(Entity, Parsable):
    """
    The ManagedAppEntity is the base entity type for all other entity types under app management workflow.
    """
    # The app package Identifier
    app_identifier: Optional[MobileAppIdentifier] = None
    # App version
    application_version: Optional[str] = None
    # Zero or more policys already applied on the registered app when it last synchronized with managment service.
    applied_policies: Optional[list[ManagedAppPolicy]] = None
    # Date and time of creation
    created_date_time: Optional[datetime.datetime] = None
    # Host device name
    device_name: Optional[str] = None
    # App management SDK generated tag, which helps relate apps hosted on the same device. Not guaranteed to relate apps in all conditions.
    device_tag: Optional[str] = None
    # Host device type
    device_type: Optional[str] = None
    # Zero or more reasons an app registration is flagged. E.g. app running on rooted device
    flagged_reasons: Optional[list[ManagedAppFlaggedReason]] = None
    # Zero or more policies admin intended for the app as of now.
    intended_policies: Optional[list[ManagedAppPolicy]] = None
    # Date and time of last the app synced with management service.
    last_sync_date_time: Optional[datetime.datetime] = None
    # App management SDK version
    management_sdk_version: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Zero or more long running operations triggered on the app registration.
    operations: Optional[list[ManagedAppOperation]] = None
    # Operating System version
    platform_version: Optional[str] = None
    # The user Id to who this app registration belongs.
    user_id: Optional[str] = None
    # Version of the entity.
    version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ManagedAppRegistration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ManagedAppRegistration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidManagedAppRegistration".casefold():
            from .android_managed_app_registration import AndroidManagedAppRegistration

            return AndroidManagedAppRegistration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosManagedAppRegistration".casefold():
            from .ios_managed_app_registration import IosManagedAppRegistration

            return IosManagedAppRegistration()
        return ManagedAppRegistration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .android_managed_app_registration import AndroidManagedAppRegistration
        from .entity import Entity
        from .ios_managed_app_registration import IosManagedAppRegistration
        from .managed_app_flagged_reason import ManagedAppFlaggedReason
        from .managed_app_operation import ManagedAppOperation
        from .managed_app_policy import ManagedAppPolicy
        from .mobile_app_identifier import MobileAppIdentifier

        from .android_managed_app_registration import AndroidManagedAppRegistration
        from .entity import Entity
        from .ios_managed_app_registration import IosManagedAppRegistration
        from .managed_app_flagged_reason import ManagedAppFlaggedReason
        from .managed_app_operation import ManagedAppOperation
        from .managed_app_policy import ManagedAppPolicy
        from .mobile_app_identifier import MobileAppIdentifier

        fields: dict[str, Callable[[Any], None]] = {
            "appIdentifier": lambda n : setattr(self, 'app_identifier', n.get_object_value(MobileAppIdentifier)),
            "applicationVersion": lambda n : setattr(self, 'application_version', n.get_str_value()),
            "appliedPolicies": lambda n : setattr(self, 'applied_policies', n.get_collection_of_object_values(ManagedAppPolicy)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "deviceName": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "deviceTag": lambda n : setattr(self, 'device_tag', n.get_str_value()),
            "deviceType": lambda n : setattr(self, 'device_type', n.get_str_value()),
            "flaggedReasons": lambda n : setattr(self, 'flagged_reasons', n.get_collection_of_enum_values(ManagedAppFlaggedReason)),
            "intendedPolicies": lambda n : setattr(self, 'intended_policies', n.get_collection_of_object_values(ManagedAppPolicy)),
            "lastSyncDateTime": lambda n : setattr(self, 'last_sync_date_time', n.get_datetime_value()),
            "managementSdkVersion": lambda n : setattr(self, 'management_sdk_version', n.get_str_value()),
            "operations": lambda n : setattr(self, 'operations', n.get_collection_of_object_values(ManagedAppOperation)),
            "platformVersion": lambda n : setattr(self, 'platform_version', n.get_str_value()),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
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
        writer.write_object_value("appIdentifier", self.app_identifier)
        writer.write_str_value("applicationVersion", self.application_version)
        writer.write_collection_of_object_values("appliedPolicies", self.applied_policies)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("deviceName", self.device_name)
        writer.write_str_value("deviceTag", self.device_tag)
        writer.write_str_value("deviceType", self.device_type)
        writer.write_collection_of_enum_values("flaggedReasons", self.flagged_reasons)
        writer.write_collection_of_object_values("intendedPolicies", self.intended_policies)
        writer.write_datetime_value("lastSyncDateTime", self.last_sync_date_time)
        writer.write_str_value("managementSdkVersion", self.management_sdk_version)
        writer.write_collection_of_object_values("operations", self.operations)
        writer.write_str_value("platformVersion", self.platform_version)
        writer.write_str_value("userId", self.user_id)
        writer.write_str_value("version", self.version)
    

