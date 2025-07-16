from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .sensitivity_label import SensitivityLabel
    from .tenant_data_security_and_governance import TenantDataSecurityAndGovernance
    from .user_data_security_and_governance import UserDataSecurityAndGovernance

from .entity import Entity

@dataclass
class DataSecurityAndGovernance(Entity, Parsable):
    # The OdataType property
    odata_type: Optional[str] = None
    # The sensitivityLabels property
    sensitivity_labels: Optional[list[SensitivityLabel]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DataSecurityAndGovernance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DataSecurityAndGovernance
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.tenantDataSecurityAndGovernance".casefold():
            from .tenant_data_security_and_governance import TenantDataSecurityAndGovernance

            return TenantDataSecurityAndGovernance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userDataSecurityAndGovernance".casefold():
            from .user_data_security_and_governance import UserDataSecurityAndGovernance

            return UserDataSecurityAndGovernance()
        return DataSecurityAndGovernance()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .sensitivity_label import SensitivityLabel
        from .tenant_data_security_and_governance import TenantDataSecurityAndGovernance
        from .user_data_security_and_governance import UserDataSecurityAndGovernance

        from .entity import Entity
        from .sensitivity_label import SensitivityLabel
        from .tenant_data_security_and_governance import TenantDataSecurityAndGovernance
        from .user_data_security_and_governance import UserDataSecurityAndGovernance

        fields: dict[str, Callable[[Any], None]] = {
            "sensitivityLabels": lambda n : setattr(self, 'sensitivity_labels', n.get_collection_of_object_values(SensitivityLabel)),
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
        writer.write_collection_of_object_values("sensitivityLabels", self.sensitivity_labels)
    

