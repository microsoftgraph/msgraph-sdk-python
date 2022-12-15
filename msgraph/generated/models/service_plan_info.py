from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class ServicePlanInfo(AdditionalDataHolder, Parsable):
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
    def applies_to(self,) -> Optional[str]:
        """
        Gets the appliesTo property value. The object the service plan can be assigned to. The possible values are:User - service plan can be assigned to individual users.Company - service plan can be assigned to the entire tenant.
        Returns: Optional[str]
        """
        return self._applies_to
    
    @applies_to.setter
    def applies_to(self,value: Optional[str] = None) -> None:
        """
        Sets the appliesTo property value. The object the service plan can be assigned to. The possible values are:User - service plan can be assigned to individual users.Company - service plan can be assigned to the entire tenant.
        Args:
            value: Value to set for the appliesTo property.
        """
        self._applies_to = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new servicePlanInfo and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The object the service plan can be assigned to. The possible values are:User - service plan can be assigned to individual users.Company - service plan can be assigned to the entire tenant.
        self._applies_to: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The provisioning status of the service plan. The possible values are:Success - Service is fully provisioned.Disabled - Service has been disabled.ErrorStatus - The service plan has not been provisioned and is in an error state.PendingInput - Service is not yet provisioned; awaiting service confirmation.PendingActivation - Service is provisioned but requires explicit activation by administrator (for example, Intune_O365 service plan)PendingProvisioning - Microsoft has added a new service to the product SKU and it has not been activated in the tenant, yet.
        self._provisioning_status: Optional[str] = None
        # The unique identifier of the service plan.
        self._service_plan_id: Optional[Guid] = None
        # The name of the service plan.
        self._service_plan_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ServicePlanInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ServicePlanInfo
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ServicePlanInfo()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "applies_to": lambda n : setattr(self, 'applies_to', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "provisioning_status": lambda n : setattr(self, 'provisioning_status', n.get_str_value()),
            "service_plan_id": lambda n : setattr(self, 'service_plan_id', n.get_object_value(Guid)),
            "service_plan_name": lambda n : setattr(self, 'service_plan_name', n.get_str_value()),
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
    
    @property
    def provisioning_status(self,) -> Optional[str]:
        """
        Gets the provisioningStatus property value. The provisioning status of the service plan. The possible values are:Success - Service is fully provisioned.Disabled - Service has been disabled.ErrorStatus - The service plan has not been provisioned and is in an error state.PendingInput - Service is not yet provisioned; awaiting service confirmation.PendingActivation - Service is provisioned but requires explicit activation by administrator (for example, Intune_O365 service plan)PendingProvisioning - Microsoft has added a new service to the product SKU and it has not been activated in the tenant, yet.
        Returns: Optional[str]
        """
        return self._provisioning_status
    
    @provisioning_status.setter
    def provisioning_status(self,value: Optional[str] = None) -> None:
        """
        Sets the provisioningStatus property value. The provisioning status of the service plan. The possible values are:Success - Service is fully provisioned.Disabled - Service has been disabled.ErrorStatus - The service plan has not been provisioned and is in an error state.PendingInput - Service is not yet provisioned; awaiting service confirmation.PendingActivation - Service is provisioned but requires explicit activation by administrator (for example, Intune_O365 service plan)PendingProvisioning - Microsoft has added a new service to the product SKU and it has not been activated in the tenant, yet.
        Args:
            value: Value to set for the provisioningStatus property.
        """
        self._provisioning_status = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("appliesTo", self.applies_to)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("provisioningStatus", self.provisioning_status)
        writer.write_object_value("servicePlanId", self.service_plan_id)
        writer.write_str_value("servicePlanName", self.service_plan_name)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def service_plan_id(self,) -> Optional[Guid]:
        """
        Gets the servicePlanId property value. The unique identifier of the service plan.
        Returns: Optional[Guid]
        """
        return self._service_plan_id
    
    @service_plan_id.setter
    def service_plan_id(self,value: Optional[Guid] = None) -> None:
        """
        Sets the servicePlanId property value. The unique identifier of the service plan.
        Args:
            value: Value to set for the servicePlanId property.
        """
        self._service_plan_id = value
    
    @property
    def service_plan_name(self,) -> Optional[str]:
        """
        Gets the servicePlanName property value. The name of the service plan.
        Returns: Optional[str]
        """
        return self._service_plan_name
    
    @service_plan_name.setter
    def service_plan_name(self,value: Optional[str] = None) -> None:
        """
        Sets the servicePlanName property value. The name of the service plan.
        Args:
            value: Value to set for the servicePlanName property.
        """
        self._service_plan_name = value
    

