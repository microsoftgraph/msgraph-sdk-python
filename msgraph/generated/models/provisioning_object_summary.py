from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, initiator, modified_property, provisioned_identity, provisioning_action, provisioning_service_principal, provisioning_status_info, provisioning_step, provisioning_system

from . import entity

@dataclass
class ProvisioningObjectSummary(entity.Entity):
    # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    activity_date_time: Optional[datetime] = None
    # Unique ID of this change in this cycle.
    change_id: Optional[str] = None
    # Unique ID per job iteration.
    cycle_id: Optional[str] = None
    # Indicates how long this provisioning action took to finish. Measured in milliseconds.
    duration_in_milliseconds: Optional[int] = None
    # Details of who initiated this provisioning.
    initiated_by: Optional[initiator.Initiator] = None
    # The unique ID for the whole provisioning job.
    job_id: Optional[str] = None
    # Details of each property that was modified in this provisioning action on this object.
    modified_properties: Optional[List[modified_property.ModifiedProperty]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates the activity name or the operation name. Possible values are: create, update, delete, stageddelete, disable, other and unknownFutureValue. For a list of activities logged, refer to Azure AD activity list.
    provisioning_action: Optional[provisioning_action.ProvisioningAction] = None
    # Details of provisioning status.
    provisioning_status_info: Optional[provisioning_status_info.ProvisioningStatusInfo] = None
    # Details of each step in provisioning.
    provisioning_steps: Optional[List[provisioning_step.ProvisioningStep]] = None
    # Represents the service principal used for provisioning.
    service_principal: Optional[provisioning_service_principal.ProvisioningServicePrincipal] = None
    # Details of source object being provisioned.
    source_identity: Optional[provisioned_identity.ProvisionedIdentity] = None
    # Details of source system of the object being provisioned.
    source_system: Optional[provisioning_system.ProvisioningSystem] = None
    # Details of target object being provisioned.
    target_identity: Optional[provisioned_identity.ProvisionedIdentity] = None
    # Details of target system of the object being provisioned.
    target_system: Optional[provisioning_system.ProvisioningSystem] = None
    # Unique Azure AD tenant ID.
    tenant_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ProvisioningObjectSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ProvisioningObjectSummary
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ProvisioningObjectSummary()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, initiator, modified_property, provisioned_identity, provisioning_action, provisioning_service_principal, provisioning_status_info, provisioning_step, provisioning_system

        from . import entity, initiator, modified_property, provisioned_identity, provisioning_action, provisioning_service_principal, provisioning_status_info, provisioning_step, provisioning_system

        fields: Dict[str, Callable[[Any], None]] = {
            "activityDateTime": lambda n : setattr(self, 'activity_date_time', n.get_datetime_value()),
            "changeId": lambda n : setattr(self, 'change_id', n.get_str_value()),
            "cycleId": lambda n : setattr(self, 'cycle_id', n.get_str_value()),
            "durationInMilliseconds": lambda n : setattr(self, 'duration_in_milliseconds', n.get_int_value()),
            "initiatedBy": lambda n : setattr(self, 'initiated_by', n.get_object_value(initiator.Initiator)),
            "jobId": lambda n : setattr(self, 'job_id', n.get_str_value()),
            "modifiedProperties": lambda n : setattr(self, 'modified_properties', n.get_collection_of_object_values(modified_property.ModifiedProperty)),
            "provisioningAction": lambda n : setattr(self, 'provisioning_action', n.get_enum_value(provisioning_action.ProvisioningAction)),
            "provisioningStatusInfo": lambda n : setattr(self, 'provisioning_status_info', n.get_object_value(provisioning_status_info.ProvisioningStatusInfo)),
            "provisioningSteps": lambda n : setattr(self, 'provisioning_steps', n.get_collection_of_object_values(provisioning_step.ProvisioningStep)),
            "servicePrincipal": lambda n : setattr(self, 'service_principal', n.get_object_value(provisioning_service_principal.ProvisioningServicePrincipal)),
            "sourceIdentity": lambda n : setattr(self, 'source_identity', n.get_object_value(provisioned_identity.ProvisionedIdentity)),
            "sourceSystem": lambda n : setattr(self, 'source_system', n.get_object_value(provisioning_system.ProvisioningSystem)),
            "targetIdentity": lambda n : setattr(self, 'target_identity', n.get_object_value(provisioned_identity.ProvisionedIdentity)),
            "targetSystem": lambda n : setattr(self, 'target_system', n.get_object_value(provisioning_system.ProvisioningSystem)),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
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
        if not writer:
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
    

