from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .generic_error import GenericError

@dataclass
class AuthenticationConfigurationValidation(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Errors in the validation result of a customAuthenticationExtension.
    errors: Optional[List[GenericError]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Warnings in the validation result of a customAuthenticationExtension.
    warnings: Optional[List[GenericError]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AuthenticationConfigurationValidation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticationConfigurationValidation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AuthenticationConfigurationValidation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .generic_error import GenericError

        from .generic_error import GenericError

        fields: Dict[str, Callable[[Any], None]] = {
            "errors": lambda n : setattr(self, 'errors', n.get_collection_of_object_values(GenericError)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "warnings": lambda n : setattr(self, 'warnings', n.get_collection_of_object_values(GenericError)),
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
        writer.write_collection_of_object_values("errors", self.errors)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("warnings", self.warnings)
        writer.write_additional_data_value(self.additional_data)
    

