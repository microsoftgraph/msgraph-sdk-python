from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cross_tenant_user_sync_inbound import CrossTenantUserSyncInbound
    from .entity import Entity
    from .template_application_level import TemplateApplicationLevel

from .entity import Entity

@dataclass
class MultiTenantOrganizationIdentitySyncPolicyTemplate(Entity):
    # The OdataType property
    odata_type: Optional[str] = None
    # The templateApplicationLevel property
    template_application_level: Optional[TemplateApplicationLevel] = None
    # Defines whether users can be synchronized from the partner tenant.
    user_sync_inbound: Optional[CrossTenantUserSyncInbound] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MultiTenantOrganizationIdentitySyncPolicyTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MultiTenantOrganizationIdentitySyncPolicyTemplate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MultiTenantOrganizationIdentitySyncPolicyTemplate()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .cross_tenant_user_sync_inbound import CrossTenantUserSyncInbound
        from .entity import Entity
        from .template_application_level import TemplateApplicationLevel

        from .cross_tenant_user_sync_inbound import CrossTenantUserSyncInbound
        from .entity import Entity
        from .template_application_level import TemplateApplicationLevel

        fields: Dict[str, Callable[[Any], None]] = {
            "templateApplicationLevel": lambda n : setattr(self, 'template_application_level', n.get_collection_of_enum_values(TemplateApplicationLevel)),
            "userSyncInbound": lambda n : setattr(self, 'user_sync_inbound', n.get_object_value(CrossTenantUserSyncInbound)),
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
        writer.write_enum_value("templateApplicationLevel", self.template_application_level)
        writer.write_object_value("userSyncInbound", self.user_sync_inbound)
    

