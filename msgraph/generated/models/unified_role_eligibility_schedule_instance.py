from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

unified_role_schedule_instance_base = lazy_import('msgraph.generated.models.unified_role_schedule_instance_base')

class UnifiedRoleEligibilityScheduleInstance(unified_role_schedule_instance_base.UnifiedRoleScheduleInstanceBase):
    def __init__(self,) -> None:
        """
        Instantiates a new unifiedRoleEligibilityScheduleInstance and sets the default values.
        """
        super().__init__()
        # The end date of the schedule instance.
        self._end_date_time: Optional[datetime] = None
        # How the role eligibility is inherited. It can either be Inherited, Direct, or Group. It can further imply whether the unifiedRoleEligibilitySchedule can be managed by the caller. Supports $filter (eq, ne).
        self._member_type: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The identifier of the unifiedRoleEligibilitySchedule object from which this instance was created. Supports $filter (eq, ne).
        self._role_eligibility_schedule_id: Optional[str] = None
        # When this instance starts.
        self._start_date_time: Optional[datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UnifiedRoleEligibilityScheduleInstance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UnifiedRoleEligibilityScheduleInstance
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UnifiedRoleEligibilityScheduleInstance()
    
    @property
    def end_date_time(self,) -> Optional[datetime]:
        """
        Gets the endDateTime property value. The end date of the schedule instance.
        Returns: Optional[datetime]
        """
        return self._end_date_time
    
    @end_date_time.setter
    def end_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the endDateTime property value. The end date of the schedule instance.
        Args:
            value: Value to set for the endDateTime property.
        """
        self._end_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "end_date_time": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "member_type": lambda n : setattr(self, 'member_type', n.get_str_value()),
            "role_eligibility_schedule_id": lambda n : setattr(self, 'role_eligibility_schedule_id', n.get_str_value()),
            "start_date_time": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def member_type(self,) -> Optional[str]:
        """
        Gets the memberType property value. How the role eligibility is inherited. It can either be Inherited, Direct, or Group. It can further imply whether the unifiedRoleEligibilitySchedule can be managed by the caller. Supports $filter (eq, ne).
        Returns: Optional[str]
        """
        return self._member_type
    
    @member_type.setter
    def member_type(self,value: Optional[str] = None) -> None:
        """
        Sets the memberType property value. How the role eligibility is inherited. It can either be Inherited, Direct, or Group. It can further imply whether the unifiedRoleEligibilitySchedule can be managed by the caller. Supports $filter (eq, ne).
        Args:
            value: Value to set for the memberType property.
        """
        self._member_type = value
    
    @property
    def role_eligibility_schedule_id(self,) -> Optional[str]:
        """
        Gets the roleEligibilityScheduleId property value. The identifier of the unifiedRoleEligibilitySchedule object from which this instance was created. Supports $filter (eq, ne).
        Returns: Optional[str]
        """
        return self._role_eligibility_schedule_id
    
    @role_eligibility_schedule_id.setter
    def role_eligibility_schedule_id(self,value: Optional[str] = None) -> None:
        """
        Sets the roleEligibilityScheduleId property value. The identifier of the unifiedRoleEligibilitySchedule object from which this instance was created. Supports $filter (eq, ne).
        Args:
            value: Value to set for the roleEligibilityScheduleId property.
        """
        self._role_eligibility_schedule_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_datetime_value("endDateTime", self.end_date_time)
        writer.write_str_value("memberType", self.member_type)
        writer.write_str_value("roleEligibilityScheduleId", self.role_eligibility_schedule_id)
        writer.write_datetime_value("startDateTime", self.start_date_time)
    
    @property
    def start_date_time(self,) -> Optional[datetime]:
        """
        Gets the startDateTime property value. When this instance starts.
        Returns: Optional[datetime]
        """
        return self._start_date_time
    
    @start_date_time.setter
    def start_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the startDateTime property value. When this instance starts.
        Args:
            value: Value to set for the startDateTime property.
        """
        self._start_date_time = value
    

