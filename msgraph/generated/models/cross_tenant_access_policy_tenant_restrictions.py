from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cross_tenant_access_policy_b2_b_setting import CrossTenantAccessPolicyB2BSetting
    from .devices_filter import DevicesFilter

from .cross_tenant_access_policy_b2_b_setting import CrossTenantAccessPolicyB2BSetting

@dataclass
class CrossTenantAccessPolicyTenantRestrictions(CrossTenantAccessPolicyB2BSetting, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.crossTenantAccessPolicyTenantRestrictions"
    # Defines the rule for filtering devices and whether devices that satisfy the rule should be allowed or blocked. This property isn't supported on the server side yet.
    devices: Optional[DevicesFilter] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CrossTenantAccessPolicyTenantRestrictions:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CrossTenantAccessPolicyTenantRestrictions
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CrossTenantAccessPolicyTenantRestrictions()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .cross_tenant_access_policy_b2_b_setting import CrossTenantAccessPolicyB2BSetting
        from .devices_filter import DevicesFilter

        from .cross_tenant_access_policy_b2_b_setting import CrossTenantAccessPolicyB2BSetting
        from .devices_filter import DevicesFilter

        fields: Dict[str, Callable[[Any], None]] = {
            "devices": lambda n : setattr(self, 'devices', n.get_object_value(DevicesFilter)),
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
        from .cross_tenant_access_policy_b2_b_setting import CrossTenantAccessPolicyB2BSetting
        from .devices_filter import DevicesFilter

        writer.write_object_value("devices", self.devices)
    

