from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .claim_binding import ClaimBinding
    from .claim_binding_source import ClaimBindingSource
    from .claim_validation import ClaimValidation

@dataclass
class VerifiedIdProfileConfiguration(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Trusted Verified ID issuer.
    accepted_issuer: Optional[str] = None
    # The claimBindingSource property
    claim_binding_source: Optional[ClaimBindingSource] = None
    # Claim bindings from Verified ID to source attributes.
    claim_bindings: Optional[list[ClaimBinding]] = None
    # The claimValidation property
    claim_validation: Optional[ClaimValidation] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Verified ID type.
    type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> VerifiedIdProfileConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: VerifiedIdProfileConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return VerifiedIdProfileConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .claim_binding import ClaimBinding
        from .claim_binding_source import ClaimBindingSource
        from .claim_validation import ClaimValidation

        from .claim_binding import ClaimBinding
        from .claim_binding_source import ClaimBindingSource
        from .claim_validation import ClaimValidation

        fields: dict[str, Callable[[Any], None]] = {
            "acceptedIssuer": lambda n : setattr(self, 'accepted_issuer', n.get_str_value()),
            "claimBindingSource": lambda n : setattr(self, 'claim_binding_source', n.get_enum_value(ClaimBindingSource)),
            "claimBindings": lambda n : setattr(self, 'claim_bindings', n.get_collection_of_object_values(ClaimBinding)),
            "claimValidation": lambda n : setattr(self, 'claim_validation', n.get_object_value(ClaimValidation)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
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
        writer.write_str_value("acceptedIssuer", self.accepted_issuer)
        writer.write_enum_value("claimBindingSource", self.claim_binding_source)
        writer.write_collection_of_object_values("claimBindings", self.claim_bindings)
        writer.write_object_value("claimValidation", self.claim_validation)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

