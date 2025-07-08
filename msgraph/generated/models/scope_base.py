from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .group_scope import GroupScope
    from .tenant_scope import TenantScope
    from .user_scope import UserScope

@dataclass
class ScopeBase(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The identifier for the scope. This could be a user ID, group ID, or a keyword like 'All' for tenant scope.
    identity: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ScopeBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ScopeBase
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupScope".casefold():
            from .group_scope import GroupScope

            return GroupScope()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.tenantScope".casefold():
            from .tenant_scope import TenantScope

            return TenantScope()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userScope".casefold():
            from .user_scope import UserScope

            return UserScope()
        return ScopeBase()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .group_scope import GroupScope
        from .tenant_scope import TenantScope
        from .user_scope import UserScope

        from .group_scope import GroupScope
        from .tenant_scope import TenantScope
        from .user_scope import UserScope

        fields: dict[str, Callable[[Any], None]] = {
            "identity": lambda n : setattr(self, 'identity', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("identity", self.identity)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

