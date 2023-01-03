from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
initiator = lazy_import('msgraph.generated.models.initiator')
modified_property = lazy_import('msgraph.generated.models.modified_property')
provisioned_identity = lazy_import('msgraph.generated.models.provisioned_identity')
provisioning_action = lazy_import('msgraph.generated.models.provisioning_action')
provisioning_service_principal = lazy_import('msgraph.generated.models.provisioning_service_principal')
provisioning_status_info = lazy_import('msgraph.generated.models.provisioning_status_info')
provisioning_step = lazy_import('msgraph.generated.models.provisioning_step')
provisioning_system = lazy_import('msgraph.generated.models.provisioning_system')

class ProvisioningObjectSummary(entity.Entity):
    """
    Provides operations to manage the admin singleton.
    """
    @property
    def activity_date_time(self,) -> Optional[datetime]:
        """
        Gets the activityDateTime property value. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Returns: Optional[datetime]
        """
        return self._activity_date_time
    
    @activity_date_time.setter
    def activity_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the activityDateTime property value. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Args:
            value: Value to set for the activityDateTime property.
        """
        self._activity_date_time = value
    
    @property
    def change_id(self,) -> Optional[str]:
        """
        Gets the changeId property value. Unique ID of this change in this cycle.
        Returns: Optional[str]
        """
        return self._change_id
    
    @change_id.setter
    def change_id(self,value: Optional[str] = None) -> None:
        """
        Sets the changeId property value. Unique ID of this change in this cycle.
        Args:
            value: Value to set for the changeId property.
        """
        self._change_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new provisioningObjectSummary and sets the default values.
        """
        super().__init__()
        # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        self._activity_date_time: Optional[datetime] = None
        # Unique ID of this change in this cycle.
        self._change_id: Optional[str] = None
        # Unique ID per job iteration.
        self._cycle_id: Optional[str] = None
        # Indicates how long this provisioning action took to finish. Measured in milliseconds.
        self._duration_in_milliseconds: Optional[int] = None
        # Details of who initiated this provisioning.
        self._initiated_by: Optional[initiator.Initiator] = None
        # The unique ID for the whole provisioning job.
        self._job_id: Optional[str] = None
        # Details of each property that was modified in this provisioning action on this object.
        self._modified_properties: Optional[List[modified_property.ModifiedProperty]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Indicates the activity name or the operation name. Possible values are: create, update, delete, stageddelete, disable, other and unknownFutureValue. For a list of activities logged, refer to Azure AD activity list.
        self._provisioning_action: Optional[provisioning_action.ProvisioningAction] = None
        # Details of provisioning status.
        self._provisioning_status_info: Optional[provisioning_status_info.ProvisioningStatusInfo] = None
        # Details of each step in provisioning.
        self._provisioning_steps: Optional[List[provisioning_step.ProvisioningStep]] = None
        # Represents the service principal used for provisioning.
        self._service_principal: Optional[provisioning_service_principal.ProvisioningServicePrincipal] = None
        # Details of source object being provisioned.
        self._source_identity: Optional[provisioned_identity.ProvisionedIdentity] = None
        # Details of source system of the object being provisioned.
        self._source_system: Optional[provisioning_system.ProvisioningSystem] = None
        # Details of target object being provisioned.
        self._target_identity: Optional[provisioned_identity.ProvisionedIdentity] = None
        # Details of target system of the object being provisioned.
        self._target_system: Optional[provisioning_system.ProvisioningSystem] = None
        # Unique Azure AD tenant ID.
        self._tenant_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ProvisioningObjectSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ProvisioningObjectSummary
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ProvisioningObjectSummary()
    
    @property
    def cycle_id(self,) -> Optional[str]:
        """
        Gets the cycleId property value. Unique ID per job iteration.
        Returns: Optional[str]
        """
        return self._cycle_id
    
    @cycle_id.setter
    def cycle_id(self,value: Optional[str] = None) -> None:
        """
        Sets the cycleId property value. Unique ID per job iteration.
        Args:
            value: Value to set for the cycleId property.
        """
        self._cycle_id = value
    
    @property
    def duration_in_milliseconds(self,) -> Optional[int]:
        """
        Gets the durationInMilliseconds property value. Indicates how long this provisioning action took to finish. Measured in milliseconds.
        Returns: Optional[int]
        """
        return self._duration_in_milliseconds
    
    @duration_in_milliseconds.setter
    def duration_in_milliseconds(self,value: Optional[int] = None) -> None:
        """
        Sets the durationInMilliseconds property value. Indicates how long this provisioning action took to finish. Measured in milliseconds.
        Args:
            value: Value to set for the durationInMilliseconds property.
        """
        self._duration_in_milliseconds = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "activity_date_time": lambda n : setattr(self, 'activity_date_time', n.get_datetime_value()),
            "change_id": lambda n : setattr(self, 'change_id', n.get_str_value()),
            "cycle_id": lambda n : setattr(self, 'cycle_id', n.get_str_value()),
            "duration_in_milliseconds": lambda n : setattr(self, 'duration_in_milliseconds', n.get_int_value()),
            "initiated_by": lambda n : setattr(self, 'initiated_by', n.get_object_value(initiator.Initiator)),
            "job_id": lambda n : setattr(self, 'job_id', n.get_str_value()),
            "modified_properties": lambda n : setattr(self, 'modified_properties', n.get_collection_of_object_values(modified_property.ModifiedProperty)),
            "provisioning_action": lambda n : setattr(self, 'provisioning_action', n.get_enum_value(provisioning_action.ProvisioningAction)),
            "provisioning_status_info": lambda n : setattr(self, 'provisioning_status_info', n.get_object_value(provisioning_status_info.ProvisioningStatusInfo)),
            "provisioning_steps": lambda n : setattr(self, 'provisioning_steps', n.get_collection_of_object_values(provisioning_step.ProvisioningStep)),
            "service_principal": lambda n : setattr(self, 'service_principal', n.get_object_value(provisioning_service_principal.ProvisioningServicePrincipal)),
            "source_identity": lambda n : setattr(self, 'source_identity', n.get_object_value(provisioned_identity.ProvisionedIdentity)),
            "source_system": lambda n : setattr(self, 'source_system', n.get_object_value(provisioning_system.ProvisioningSystem)),
            "target_identity": lambda n : setattr(self, 'target_identity', n.get_object_value(provisioned_identity.ProvisionedIdentity)),
            "target_system": lambda n : setattr(self, 'target_system', n.get_object_value(provisioning_system.ProvisioningSystem)),
            "tenant_id": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def initiated_by(self,) -> Optional[initiator.Initiator]:
        """
        Gets the initiatedBy property value. Details of who initiated this provisioning.
        Returns: Optional[initiator.Initiator]
        """
        return self._initiated_by
    
    @initiated_by.setter
    def initiated_by(self,value: Optional[initiator.Initiator] = None) -> None:
        """
        Sets the initiatedBy property value. Details of who initiated this provisioning.
        Args:
            value: Value to set for the initiatedBy property.
        """
        self._initiated_by = value
    
    @property
    def job_id(self,) -> Optional[str]:
        """
        Gets the jobId property value. The unique ID for the whole provisioning job.
        Returns: Optional[str]
        """
        return self._job_id
    
    @job_id.setter
    def job_id(self,value: Optional[str] = None) -> None:
        """
        Sets the jobId property value. The unique ID for the whole provisioning job.
        Args:
            value: Value to set for the jobId property.
        """
        self._job_id = value
    
    @property
    def modified_properties(self,) -> Optional[List[modified_property.ModifiedProperty]]:
        """
        Gets the modifiedProperties property value. Details of each property that was modified in this provisioning action on this object.
        Returns: Optional[List[modified_property.ModifiedProperty]]
        """
        return self._modified_properties
    
    @modified_properties.setter
    def modified_properties(self,value: Optional[List[modified_property.ModifiedProperty]] = None) -> None:
        """
        Sets the modifiedProperties property value. Details of each property that was modified in this provisioning action on this object.
        Args:
            value: Value to set for the modifiedProperties property.
        """
        self._modified_properties = value
    
    @property
    def provisioning_action(self,) -> Optional[provisioning_action.ProvisioningAction]:
        """
        Gets the provisioningAction property value. Indicates the activity name or the operation name. Possible values are: create, update, delete, stageddelete, disable, other and unknownFutureValue. For a list of activities logged, refer to Azure AD activity list.
        Returns: Optional[provisioning_action.ProvisioningAction]
        """
        return self._provisioning_action
    
    @provisioning_action.setter
    def provisioning_action(self,value: Optional[provisioning_action.ProvisioningAction] = None) -> None:
        """
        Sets the provisioningAction property value. Indicates the activity name or the operation name. Possible values are: create, update, delete, stageddelete, disable, other and unknownFutureValue. For a list of activities logged, refer to Azure AD activity list.
        Args:
            value: Value to set for the provisioningAction property.
        """
        self._provisioning_action = value
    
    @property
    def provisioning_status_info(self,) -> Optional[provisioning_status_info.ProvisioningStatusInfo]:
        """
        Gets the provisioningStatusInfo property value. Details of provisioning status.
        Returns: Optional[provisioning_status_info.ProvisioningStatusInfo]
        """
        return self._provisioning_status_info
    
    @provisioning_status_info.setter
    def provisioning_status_info(self,value: Optional[provisioning_status_info.ProvisioningStatusInfo] = None) -> None:
        """
        Sets the provisioningStatusInfo property value. Details of provisioning status.
        Args:
            value: Value to set for the provisioningStatusInfo property.
        """
        self._provisioning_status_info = value
    
    @property
    def provisioning_steps(self,) -> Optional[List[provisioning_step.ProvisioningStep]]:
        """
        Gets the provisioningSteps property value. Details of each step in provisioning.
        Returns: Optional[List[provisioning_step.ProvisioningStep]]
        """
        return self._provisioning_steps
    
    @provisioning_steps.setter
    def provisioning_steps(self,value: Optional[List[provisioning_step.ProvisioningStep]] = None) -> None:
        """
        Sets the provisioningSteps property value. Details of each step in provisioning.
        Args:
            value: Value to set for the provisioningSteps property.
        """
        self._provisioning_steps = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
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
    
    @property
    def service_principal(self,) -> Optional[provisioning_service_principal.ProvisioningServicePrincipal]:
        """
        Gets the servicePrincipal property value. Represents the service principal used for provisioning.
        Returns: Optional[provisioning_service_principal.ProvisioningServicePrincipal]
        """
        return self._service_principal
    
    @service_principal.setter
    def service_principal(self,value: Optional[provisioning_service_principal.ProvisioningServicePrincipal] = None) -> None:
        """
        Sets the servicePrincipal property value. Represents the service principal used for provisioning.
        Args:
            value: Value to set for the servicePrincipal property.
        """
        self._service_principal = value
    
    @property
    def source_identity(self,) -> Optional[provisioned_identity.ProvisionedIdentity]:
        """
        Gets the sourceIdentity property value. Details of source object being provisioned.
        Returns: Optional[provisioned_identity.ProvisionedIdentity]
        """
        return self._source_identity
    
    @source_identity.setter
    def source_identity(self,value: Optional[provisioned_identity.ProvisionedIdentity] = None) -> None:
        """
        Sets the sourceIdentity property value. Details of source object being provisioned.
        Args:
            value: Value to set for the sourceIdentity property.
        """
        self._source_identity = value
    
    @property
    def source_system(self,) -> Optional[provisioning_system.ProvisioningSystem]:
        """
        Gets the sourceSystem property value. Details of source system of the object being provisioned.
        Returns: Optional[provisioning_system.ProvisioningSystem]
        """
        return self._source_system
    
    @source_system.setter
    def source_system(self,value: Optional[provisioning_system.ProvisioningSystem] = None) -> None:
        """
        Sets the sourceSystem property value. Details of source system of the object being provisioned.
        Args:
            value: Value to set for the sourceSystem property.
        """
        self._source_system = value
    
    @property
    def target_identity(self,) -> Optional[provisioned_identity.ProvisionedIdentity]:
        """
        Gets the targetIdentity property value. Details of target object being provisioned.
        Returns: Optional[provisioned_identity.ProvisionedIdentity]
        """
        return self._target_identity
    
    @target_identity.setter
    def target_identity(self,value: Optional[provisioned_identity.ProvisionedIdentity] = None) -> None:
        """
        Sets the targetIdentity property value. Details of target object being provisioned.
        Args:
            value: Value to set for the targetIdentity property.
        """
        self._target_identity = value
    
    @property
    def target_system(self,) -> Optional[provisioning_system.ProvisioningSystem]:
        """
        Gets the targetSystem property value. Details of target system of the object being provisioned.
        Returns: Optional[provisioning_system.ProvisioningSystem]
        """
        return self._target_system
    
    @target_system.setter
    def target_system(self,value: Optional[provisioning_system.ProvisioningSystem] = None) -> None:
        """
        Sets the targetSystem property value. Details of target system of the object being provisioned.
        Args:
            value: Value to set for the targetSystem property.
        """
        self._target_system = value
    
    @property
    def tenant_id(self,) -> Optional[str]:
        """
        Gets the tenantId property value. Unique Azure AD tenant ID.
        Returns: Optional[str]
        """
        return self._tenant_id
    
    @tenant_id.setter
    def tenant_id(self,value: Optional[str] = None) -> None:
        """
        Sets the tenantId property value. Unique Azure AD tenant ID.
        Args:
            value: Value to set for the tenantId property.
        """
        self._tenant_id = value
    

