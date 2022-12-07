from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

request_schedule = lazy_import('msgraph.generated.models.request_schedule')
unified_role_schedule_base = lazy_import('msgraph.generated.models.unified_role_schedule_base')

class UnifiedRoleEligibilitySchedule(unified_role_schedule_base.UnifiedRoleScheduleBase):
    def __init__(self,) -> None:
        """
        Instantiates a new unifiedRoleEligibilitySchedule and sets the default values.
        """
        super().__init__()
        # How the role eligibility is inherited. It can either be Inherited, Direct, or Group. It can further imply whether the unifiedRoleEligibilitySchedule can be managed by the caller. Supports $filter (eq, ne).
        self._member_type: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The period of the role eligibility.
        self._schedule_info: Optional[request_schedule.RequestSchedule] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UnifiedRoleEligibilitySchedule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UnifiedRoleEligibilitySchedule
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UnifiedRoleEligibilitySchedule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "member_type": lambda n : setattr(self, 'member_type', n.get_str_value()),
            "schedule_info": lambda n : setattr(self, 'schedule_info', n.get_object_value(request_schedule.RequestSchedule)),
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
    def schedule_info(self,) -> Optional[request_schedule.RequestSchedule]:
        """
        Gets the scheduleInfo property value. The period of the role eligibility.
        Returns: Optional[request_schedule.RequestSchedule]
        """
        return self._schedule_info
    
    @schedule_info.setter
    def schedule_info(self,value: Optional[request_schedule.RequestSchedule] = None) -> None:
        """
        Sets the scheduleInfo property value. The period of the role eligibility.
        Args:
            value: Value to set for the scheduleInfo property.
        """
        self._schedule_info = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("memberType", self.member_type)
        writer.write_object_value("scheduleInfo", self.schedule_info)
    

