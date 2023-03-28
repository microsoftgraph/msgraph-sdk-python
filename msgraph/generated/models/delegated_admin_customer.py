from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import delegated_admin_service_management_detail, entity

from . import entity

class DelegatedAdminCustomer(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new DelegatedAdminCustomer and sets the default values.
        """
        super().__init__()
        # The Azure AD display name of the customer tenant. Read-only. Supports $orderBy.
        self._display_name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Contains the management details of a service in the customer tenant that's managed by delegated administration.
        self._service_management_details: Optional[List[delegated_admin_service_management_detail.DelegatedAdminServiceManagementDetail]] = None
        # The Azure AD-assigned tenant ID of the customer. Read-only.
        self._tenant_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DelegatedAdminCustomer:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DelegatedAdminCustomer
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DelegatedAdminCustomer()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The Azure AD display name of the customer tenant. Read-only. Supports $orderBy.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The Azure AD display name of the customer tenant. Read-only. Supports $orderBy.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import delegated_admin_service_management_detail, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "serviceManagementDetails": lambda n : setattr(self, 'service_management_details', n.get_collection_of_object_values(delegated_admin_service_management_detail.DelegatedAdminServiceManagementDetail)),
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
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("serviceManagementDetails", self.service_management_details)
        writer.write_str_value("tenantId", self.tenant_id)
    
    @property
    def service_management_details(self,) -> Optional[List[delegated_admin_service_management_detail.DelegatedAdminServiceManagementDetail]]:
        """
        Gets the serviceManagementDetails property value. Contains the management details of a service in the customer tenant that's managed by delegated administration.
        Returns: Optional[List[delegated_admin_service_management_detail.DelegatedAdminServiceManagementDetail]]
        """
        return self._service_management_details
    
    @service_management_details.setter
    def service_management_details(self,value: Optional[List[delegated_admin_service_management_detail.DelegatedAdminServiceManagementDetail]] = None) -> None:
        """
        Sets the serviceManagementDetails property value. Contains the management details of a service in the customer tenant that's managed by delegated administration.
        Args:
            value: Value to set for the service_management_details property.
        """
        self._service_management_details = value
    
    @property
    def tenant_id(self,) -> Optional[str]:
        """
        Gets the tenantId property value. The Azure AD-assigned tenant ID of the customer. Read-only.
        Returns: Optional[str]
        """
        return self._tenant_id
    
    @tenant_id.setter
    def tenant_id(self,value: Optional[str] = None) -> None:
        """
        Sets the tenantId property value. The Azure AD-assigned tenant ID of the customer. Read-only.
        Args:
            value: Value to set for the tenant_id property.
        """
        self._tenant_id = value
    

