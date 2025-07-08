from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .scope_base import ScopeBase

@dataclass
class PolicyBinding(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Specifies the users or groups to be explicitly excluded from this policy scope. Can be null or empty.
    exclusions: Optional[list[ScopeBase]] = None
    # Specifies the users or groups to be included in this policy scope. Often set to tenantScope for 'All users'.
    inclusions: Optional[list[ScopeBase]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PolicyBinding:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PolicyBinding
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PolicyBinding()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .scope_base import ScopeBase

        from .scope_base import ScopeBase

        fields: dict[str, Callable[[Any], None]] = {
            "exclusions": lambda n : setattr(self, 'exclusions', n.get_collection_of_object_values(ScopeBase)),
            "inclusions": lambda n : setattr(self, 'inclusions', n.get_collection_of_object_values(ScopeBase)),
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
        writer.write_collection_of_object_values("exclusions", self.exclusions)
        writer.write_collection_of_object_values("inclusions", self.inclusions)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

