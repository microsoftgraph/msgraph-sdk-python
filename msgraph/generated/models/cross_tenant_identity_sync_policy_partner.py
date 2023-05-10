from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import cross_tenant_user_sync_inbound

class CrossTenantIdentitySyncPolicyPartner(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new crossTenantIdentitySyncPolicyPartner and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The displayName property
        self._display_name: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The tenantId property
        self._tenant_id: Optional[str] = None
        # The userSyncInbound property
        self._user_sync_inbound: Optional[cross_tenant_user_sync_inbound.CrossTenantUserSyncInbound] = None
    
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CrossTenantIdentitySyncPolicyPartner:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CrossTenantIdentitySyncPolicyPartner
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CrossTenantIdentitySyncPolicyPartner()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The displayName property
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The displayName property
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import cross_tenant_user_sync_inbound

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
            "userSyncInbound": lambda n : setattr(self, 'user_sync_inbound', n.get_object_value(cross_tenant_user_sync_inbound.CrossTenantUserSyncInbound)),
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
            value: Value to set for the odata_type property.
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_object_value("userSyncInbound", self.user_sync_inbound)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def tenant_id(self,) -> Optional[str]:
        """
        Gets the tenantId property value. The tenantId property
        Returns: Optional[str]
        """
        return self._tenant_id
    
    @tenant_id.setter
    def tenant_id(self,value: Optional[str] = None) -> None:
        """
        Sets the tenantId property value. The tenantId property
        Args:
            value: Value to set for the tenant_id property.
        """
        self._tenant_id = value
    
    @property
    def user_sync_inbound(self,) -> Optional[cross_tenant_user_sync_inbound.CrossTenantUserSyncInbound]:
        """
        Gets the userSyncInbound property value. The userSyncInbound property
        Returns: Optional[cross_tenant_user_sync_inbound.CrossTenantUserSyncInbound]
        """
        return self._user_sync_inbound
    
    @user_sync_inbound.setter
    def user_sync_inbound(self,value: Optional[cross_tenant_user_sync_inbound.CrossTenantUserSyncInbound] = None) -> None:
        """
        Sets the userSyncInbound property value. The userSyncInbound property
        Args:
            value: Value to set for the user_sync_inbound property.
        """
        self._user_sync_inbound = value
    

