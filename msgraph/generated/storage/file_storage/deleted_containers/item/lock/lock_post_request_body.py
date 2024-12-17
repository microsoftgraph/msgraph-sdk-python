from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ......models.site_lock_state import SiteLockState

@dataclass
class LockPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The lockState property
    lock_state: Optional[SiteLockState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LockPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LockPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LockPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ......models.site_lock_state import SiteLockState

        from ......models.site_lock_state import SiteLockState

        fields: Dict[str, Callable[[Any], None]] = {
            "lockState": lambda n : setattr(self, 'lock_state', n.get_enum_value(SiteLockState)),
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
        from ......models.site_lock_state import SiteLockState

        writer.write_enum_value("lockState", self.lock_state)
        writer.write_additional_data_value(self.additional_data)
    

