from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .initiator import Initiator
    from .modified_property import ModifiedProperty
    from .provisioned_identity import ProvisionedIdentity
    from .provisioning_action import ProvisioningAction
    from .provisioning_service_principal import ProvisioningServicePrincipal
    from .provisioning_status_info import ProvisioningStatusInfo
    from .provisioning_step import ProvisioningStep
    from .provisioning_system import ProvisioningSystem

from .entity import Entity

@dataclass
class ProvisioningObjectSummary(Entity, Parsable):
    # Represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.  SUpports $filter (eq, gt, lt) and orderby.
    activity_date_time: Optional[datetime.datetime] = None
    # Unique ID of this change in this cycle. Supports $filter (eq, contains).
    change_id: Optional[str] = None
    # Unique ID per job iteration. Supports $filter (eq, contains).
    cycle_id: Optional[str] = None
    # Indicates how long this provisioning action took to finish. Measured in milliseconds.
    duration_in_milliseconds: Optional[int] = None
    # Details of who initiated this provisioning. Supports $filter (eq, contains).
    initiated_by: Optional[Initiator] = None
    # The unique ID for the whole provisioning job. Supports $filter (eq, contains).
    job_id: Optional[str] = None
    # Details of each property that was modified in this provisioning action on this object.
    modified_properties: Optional[list[ModifiedProperty]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates the activity name or the operation name. The possible values are: create, update, delete, stageddelete, disable, other and unknownFutureValue. For a list of activities logged, refer to Microsoft Entra activity list. Supports $filter (eq, contains).
    provisioning_action: Optional[ProvisioningAction] = None
    # Details of provisioning status.
    provisioning_status_info: Optional[ProvisioningStatusInfo] = None
    # Details of each step in provisioning.
    provisioning_steps: Optional[list[ProvisioningStep]] = None
    # Represents the service principal used for provisioning. Supports $filter (eq) for id and name.
    service_principal: Optional[ProvisioningServicePrincipal] = None
    # Details of source object being provisioned. Supports $filter (eq, contains) for identityType, id, and displayName.
    source_identity: Optional[ProvisionedIdentity] = None
    # Details of source system of the object being provisioned. Supports $filter (eq, contains) for displayName.
    source_system: Optional[ProvisioningSystem] = None
    # Details of target object being provisioned. Supports $filter (eq, contains) for identityType, id, and displayName.
    target_identity: Optional[ProvisionedIdentity] = None
    # Details of target system of the object being provisioned. Supports $filter (eq, contains) for displayName.
    target_system: Optional[ProvisioningSystem] = None
    # Unique Microsoft Entra tenant ID. Supports $filter (eq, contains).
    tenant_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ProvisioningObjectSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ProvisioningObjectSummary
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ProvisioningObjectSummary()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .initiator import Initiator
        from .modified_property import ModifiedProperty
        from .provisioned_identity import ProvisionedIdentity
        from .provisioning_action import ProvisioningAction
        from .provisioning_service_principal import ProvisioningServicePrincipal
        from .provisioning_status_info import ProvisioningStatusInfo
        from .provisioning_step import ProvisioningStep
        from .provisioning_system import ProvisioningSystem

        from .entity import Entity
        from .initiator import Initiator
        from .modified_property import ModifiedProperty
        from .provisioned_identity import ProvisionedIdentity
        from .provisioning_action import ProvisioningAction
        from .provisioning_service_principal import ProvisioningServicePrincipal
        from .provisioning_status_info import ProvisioningStatusInfo
        from .provisioning_step import ProvisioningStep
        from .provisioning_system import ProvisioningSystem

        fields: dict[str, Callable[[Any], None]] = {
            "activityDateTime": lambda n : setattr(self, 'activity_date_time', n.get_datetime_value()),
            "changeId": lambda n : setattr(self, 'change_id', n.get_str_value()),
            "cycleId": lambda n : setattr(self, 'cycle_id', n.get_str_value()),
            "durationInMilliseconds": lambda n : setattr(self, 'duration_in_milliseconds', n.get_int_value()),
            "initiatedBy": lambda n : setattr(self, 'initiated_by', n.get_object_value(Initiator)),
            "jobId": lambda n : setattr(self, 'job_id', n.get_str_value()),
            "modifiedProperties": lambda n : setattr(self, 'modified_properties', n.get_collection_of_object_values(ModifiedProperty)),
            "provisioningAction": lambda n : setattr(self, 'provisioning_action', n.get_enum_value(ProvisioningAction)),
            "provisioningStatusInfo": lambda n : setattr(self, 'provisioning_status_info', n.get_object_value(ProvisioningStatusInfo)),
            "provisioningSteps": lambda n : setattr(self, 'provisioning_steps', n.get_collection_of_object_values(ProvisioningStep)),
            "servicePrincipal": lambda n : setattr(self, 'service_principal', n.get_object_value(ProvisioningServicePrincipal)),
            "sourceIdentity": lambda n : setattr(self, 'source_identity', n.get_object_value(ProvisionedIdentity)),
            "sourceSystem": lambda n : setattr(self, 'source_system', n.get_object_value(ProvisioningSystem)),
            "targetIdentity": lambda n : setattr(self, 'target_identity', n.get_object_value(ProvisionedIdentity)),
            "targetSystem": lambda n : setattr(self, 'target_system', n.get_object_value(ProvisioningSystem)),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
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
        writer.write_datetime_value("activityDateTime", self.activity_date_time)
        writer.write_str_value("changeId", self.change_id)
        writer.write_str_value("cycleId", self.cycle_id)
        writer.write_int_value("durationInMilliseconds", self.duration_in_milliseconds)
        writer.write_object_value("initiatedBy", self.initiated_by)
        writer.write_str_value("jobId", self.job_id)
        writer.write_collection_of_object_values("modifiedProperties", self.modified_properties)
        writer.write_enum_value("provisioningAction", self.provisioning_action)
        writer.write_object_value("provisioningStatusInfo", self.provisioning_status_info)
        writer.write_collection_of_object_values("provisioningSteps", self.provisioning_steps)
        writer.write_object_value("servicePrincipal", self.service_principal)
        writer.write_object_value("sourceIdentity", self.source_identity)
        writer.write_object_value("sourceSystem", self.source_system)
        writer.write_object_value("targetIdentity", self.target_identity)
        writer.write_object_value("targetSystem", self.target_system)
        writer.write_str_value("tenantId", self.tenant_id)
    

