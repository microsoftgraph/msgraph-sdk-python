from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import app_management_configuration, policy_base

from . import policy_base

class TenantAppManagementPolicy(policy_base.PolicyBase):
    def __init__(self,) -> None:
        """
        Instantiates a new TenantAppManagementPolicy and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.tenantAppManagementPolicy"
        # Restrictions that apply as default to all application objects in the tenant.
        self._application_restrictions: Optional[app_management_configuration.AppManagementConfiguration] = None
        # Denotes whether the policy is enabled. Default value is false.
        self._is_enabled: Optional[bool] = None
        # Restrictions that apply as default to all service principal objects in the tenant.
        self._service_principal_restrictions: Optional[app_management_configuration.AppManagementConfiguration] = None
    
    @property
    def application_restrictions(self,) -> Optional[app_management_configuration.AppManagementConfiguration]:
        """
        Gets the applicationRestrictions property value. Restrictions that apply as default to all application objects in the tenant.
        Returns: Optional[app_management_configuration.AppManagementConfiguration]
        """
        return self._application_restrictions
    
    @application_restrictions.setter
    def application_restrictions(self,value: Optional[app_management_configuration.AppManagementConfiguration] = None) -> None:
        """
        Sets the applicationRestrictions property value. Restrictions that apply as default to all application objects in the tenant.
        Args:
            value: Value to set for the application_restrictions property.
        """
        self._application_restrictions = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TenantAppManagementPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TenantAppManagementPolicy
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TenantAppManagementPolicy()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import app_management_configuration, policy_base

        fields: Dict[str, Callable[[Any], None]] = {
            "applicationRestrictions": lambda n : setattr(self, 'application_restrictions', n.get_object_value(app_management_configuration.AppManagementConfiguration)),
            "isEnabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
            "servicePrincipalRestrictions": lambda n : setattr(self, 'service_principal_restrictions', n.get_object_value(app_management_configuration.AppManagementConfiguration)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_enabled(self,) -> Optional[bool]:
        """
        Gets the isEnabled property value. Denotes whether the policy is enabled. Default value is false.
        Returns: Optional[bool]
        """
        return self._is_enabled
    
    @is_enabled.setter
    def is_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isEnabled property value. Denotes whether the policy is enabled. Default value is false.
        Args:
            value: Value to set for the is_enabled property.
        """
        self._is_enabled = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("applicationRestrictions", self.application_restrictions)
        writer.write_bool_value("isEnabled", self.is_enabled)
        writer.write_object_value("servicePrincipalRestrictions", self.service_principal_restrictions)
    
    @property
    def service_principal_restrictions(self,) -> Optional[app_management_configuration.AppManagementConfiguration]:
        """
        Gets the servicePrincipalRestrictions property value. Restrictions that apply as default to all service principal objects in the tenant.
        Returns: Optional[app_management_configuration.AppManagementConfiguration]
        """
        return self._service_principal_restrictions
    
    @service_principal_restrictions.setter
    def service_principal_restrictions(self,value: Optional[app_management_configuration.AppManagementConfiguration] = None) -> None:
        """
        Sets the servicePrincipalRestrictions property value. Restrictions that apply as default to all service principal objects in the tenant.
        Args:
            value: Value to set for the service_principal_restrictions property.
        """
        self._service_principal_restrictions = value
    

