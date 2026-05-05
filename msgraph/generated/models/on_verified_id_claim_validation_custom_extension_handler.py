from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .custom_extension_overwrite_configuration import CustomExtensionOverwriteConfiguration
    from .on_verified_id_claim_validation_custom_extension import OnVerifiedIdClaimValidationCustomExtension
    from .on_verified_id_claim_validation_handler import OnVerifiedIdClaimValidationHandler

from .on_verified_id_claim_validation_handler import OnVerifiedIdClaimValidationHandler

@dataclass
class OnVerifiedIdClaimValidationCustomExtensionHandler(OnVerifiedIdClaimValidationHandler, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.onVerifiedIdClaimValidationCustomExtensionHandler"
    # Configuration that overrides the default settings from the referenced custom extension, such as timeout and retry values. Optional.
    configuration: Optional[CustomExtensionOverwriteConfiguration] = None
    # The customExtension property
    custom_extension: Optional[OnVerifiedIdClaimValidationCustomExtension] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OnVerifiedIdClaimValidationCustomExtensionHandler:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OnVerifiedIdClaimValidationCustomExtensionHandler
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OnVerifiedIdClaimValidationCustomExtensionHandler()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .custom_extension_overwrite_configuration import CustomExtensionOverwriteConfiguration
        from .on_verified_id_claim_validation_custom_extension import OnVerifiedIdClaimValidationCustomExtension
        from .on_verified_id_claim_validation_handler import OnVerifiedIdClaimValidationHandler

        from .custom_extension_overwrite_configuration import CustomExtensionOverwriteConfiguration
        from .on_verified_id_claim_validation_custom_extension import OnVerifiedIdClaimValidationCustomExtension
        from .on_verified_id_claim_validation_handler import OnVerifiedIdClaimValidationHandler

        fields: dict[str, Callable[[Any], None]] = {
            "configuration": lambda n : setattr(self, 'configuration', n.get_object_value(CustomExtensionOverwriteConfiguration)),
            "customExtension": lambda n : setattr(self, 'custom_extension', n.get_object_value(OnVerifiedIdClaimValidationCustomExtension)),
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
        writer.write_object_value("configuration", self.configuration)
        writer.write_object_value("customExtension", self.custom_extension)
    

