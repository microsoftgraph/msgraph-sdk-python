from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models.managed_mobile_app import ManagedMobileApp

@dataclass
class TargetAppsPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The apps property
    apps: Optional[List[ManagedMobileApp]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TargetAppsPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TargetAppsPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TargetAppsPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .....models.managed_mobile_app import ManagedMobileApp

        from .....models.managed_mobile_app import ManagedMobileApp

        fields: Dict[str, Callable[[Any], None]] = {
            "apps": lambda n : setattr(self, 'apps', n.get_collection_of_object_values(ManagedMobileApp)),
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
        writer.write_collection_of_object_values("apps", self.apps)
        writer.write_additional_data_value(self.additional_data)
    

