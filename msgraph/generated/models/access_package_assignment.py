from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_package import AccessPackage
    from .access_package_assignment_policy import AccessPackageAssignmentPolicy
    from .access_package_assignment_state import AccessPackageAssignmentState
    from .access_package_subject import AccessPackageSubject
    from .custom_extension_callout_instance import CustomExtensionCalloutInstance
    from .entitlement_management_schedule import EntitlementManagementSchedule
    from .entity import Entity

from .entity import Entity

@dataclass
class AccessPackageAssignment(Entity, Parsable):
    # Read-only. Nullable. Supports $filter (eq) on the id property and $expand query parameters.
    access_package: Optional[AccessPackage] = None
    # Read-only. Supports $filter (eq) on the id property and $expand query parameters.
    assignment_policy: Optional[AccessPackageAssignmentPolicy] = None
    # Information about all the custom extension calls that were made during the access package assignment workflow.
    custom_extension_callout_instances: Optional[list[CustomExtensionCalloutInstance]] = None
    # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    expired_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # When the access assignment is to be in place. Read-only.
    schedule: Optional[EntitlementManagementSchedule] = None
    # The state of the access package assignment. The possible values are: delivering, partiallyDelivered, delivered, expired, deliveryFailed, unknownFutureValue. Read-only. Supports $filter (eq).
    state: Optional[AccessPackageAssignmentState] = None
    # More information about the assignment lifecycle. Possible values include Delivering, Delivered, AutoAssignmentInGracePeriod, NearExpiry1DayNotificationTriggered, or ExpiredNotificationTriggered. Read-only.
    status: Optional[str] = None
    # The subject of the access package assignment. Read-only. Nullable. Supports $expand. Supports $filter (eq) on objectId.
    target: Optional[AccessPackageSubject] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AccessPackageAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageAssignment
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AccessPackageAssignment()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .access_package import AccessPackage
        from .access_package_assignment_policy import AccessPackageAssignmentPolicy
        from .access_package_assignment_state import AccessPackageAssignmentState
        from .access_package_subject import AccessPackageSubject
        from .custom_extension_callout_instance import CustomExtensionCalloutInstance
        from .entitlement_management_schedule import EntitlementManagementSchedule
        from .entity import Entity

        from .access_package import AccessPackage
        from .access_package_assignment_policy import AccessPackageAssignmentPolicy
        from .access_package_assignment_state import AccessPackageAssignmentState
        from .access_package_subject import AccessPackageSubject
        from .custom_extension_callout_instance import CustomExtensionCalloutInstance
        from .entitlement_management_schedule import EntitlementManagementSchedule
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "accessPackage": lambda n : setattr(self, 'access_package', n.get_object_value(AccessPackage)),
            "assignmentPolicy": lambda n : setattr(self, 'assignment_policy', n.get_object_value(AccessPackageAssignmentPolicy)),
            "customExtensionCalloutInstances": lambda n : setattr(self, 'custom_extension_callout_instances', n.get_collection_of_object_values(CustomExtensionCalloutInstance)),
            "expiredDateTime": lambda n : setattr(self, 'expired_date_time', n.get_datetime_value()),
            "schedule": lambda n : setattr(self, 'schedule', n.get_object_value(EntitlementManagementSchedule)),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(AccessPackageAssignmentState)),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
            "target": lambda n : setattr(self, 'target', n.get_object_value(AccessPackageSubject)),
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
        writer.write_object_value("accessPackage", self.access_package)
        writer.write_object_value("assignmentPolicy", self.assignment_policy)
        writer.write_collection_of_object_values("customExtensionCalloutInstances", self.custom_extension_callout_instances)
        writer.write_datetime_value("expiredDateTime", self.expired_date_time)
        writer.write_object_value("schedule", self.schedule)
        writer.write_enum_value("state", self.state)
        writer.write_str_value("status", self.status)
        writer.write_object_value("target", self.target)
    

