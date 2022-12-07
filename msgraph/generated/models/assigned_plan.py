from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class AssignedPlan(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def assigned_date_time(self,) -> Optional[datetime]:
        """
        Gets the assignedDateTime property value. The date and time at which the plan was assigned. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._assigned_date_time
    
    @assigned_date_time.setter
    def assigned_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the assignedDateTime property value. The date and time at which the plan was assigned. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the assignedDateTime property.
        """
        self._assigned_date_time = value
    
    @property
    def capability_status(self,) -> Optional[str]:
        """
        Gets the capabilityStatus property value. Condition of the capability assignment. The possible values are Enabled, Warning, Suspended, Deleted, LockedOut. See a detailed description of each value.
        Returns: Optional[str]
        """
        return self._capability_status
    
    @capability_status.setter
    def capability_status(self,value: Optional[str] = None) -> None:
        """
        Sets the capabilityStatus property value. Condition of the capability assignment. The possible values are Enabled, Warning, Suspended, Deleted, LockedOut. See a detailed description of each value.
        Args:
            value: Value to set for the capabilityStatus property.
        """
        self._capability_status = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new assignedPlan and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The date and time at which the plan was assigned. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._assigned_date_time: Optional[datetime] = None
        # Condition of the capability assignment. The possible values are Enabled, Warning, Suspended, Deleted, LockedOut. See a detailed description of each value.
        self._capability_status: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The name of the service; for example, exchange.
        self._service: Optional[str] = None
        # A GUID that identifies the service plan. For a complete list of GUIDs and their equivalent friendly service names, see Product names and service plan identifiers for licensing.
        self._service_plan_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AssignedPlan:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AssignedPlan
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AssignedPlan()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "assigned_date_time": lambda n : setattr(self, 'assigned_date_time', n.get_datetime_value()),
            "capability_status": lambda n : setattr(self, 'capability_status', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "service": lambda n : setattr(self, 'service', n.get_str_value()),
            "service_plan_id": lambda n : setattr(self, 'service_plan_id', n.get_str_value()),
        }
        return fields
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_datetime_value("assignedDateTime", self.assigned_date_time)
        writer.write_str_value("capabilityStatus", self.capability_status)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("service", self.service)
        writer.write_str_value("servicePlanId", self.service_plan_id)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def service(self,) -> Optional[str]:
        """
        Gets the service property value. The name of the service; for example, exchange.
        Returns: Optional[str]
        """
        return self._service
    
    @service.setter
    def service(self,value: Optional[str] = None) -> None:
        """
        Sets the service property value. The name of the service; for example, exchange.
        Args:
            value: Value to set for the service property.
        """
        self._service = value
    
    @property
    def service_plan_id(self,) -> Optional[str]:
        """
        Gets the servicePlanId property value. A GUID that identifies the service plan. For a complete list of GUIDs and their equivalent friendly service names, see Product names and service plan identifiers for licensing.
        Returns: Optional[str]
        """
        return self._service_plan_id
    
    @service_plan_id.setter
    def service_plan_id(self,value: Optional[str] = None) -> None:
        """
        Sets the servicePlanId property value. A GUID that identifies the service plan. For a complete list of GUIDs and their equivalent friendly service names, see Product names and service plan identifiers for licensing.
        Args:
            value: Value to set for the servicePlanId property.
        """
        self._service_plan_id = value
    

