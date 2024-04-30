from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ....models.custom_extension_authentication_configuration import CustomExtensionAuthenticationConfiguration
    from ....models.custom_extension_endpoint_configuration import CustomExtensionEndpointConfiguration

@dataclass
class ValidateAuthenticationConfigurationPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The authenticationConfiguration property
    authentication_configuration: Optional[CustomExtensionAuthenticationConfiguration] = None
    # The endpointConfiguration property
    endpoint_configuration: Optional[CustomExtensionEndpointConfiguration] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ValidateAuthenticationConfigurationPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ValidateAuthenticationConfigurationPostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ValidateAuthenticationConfigurationPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ....models.custom_extension_authentication_configuration import CustomExtensionAuthenticationConfiguration
        from ....models.custom_extension_endpoint_configuration import CustomExtensionEndpointConfiguration

        from ....models.custom_extension_authentication_configuration import CustomExtensionAuthenticationConfiguration
        from ....models.custom_extension_endpoint_configuration import CustomExtensionEndpointConfiguration

        fields: Dict[str, Callable[[Any], None]] = {
            "authenticationConfiguration": lambda n : setattr(self, 'authentication_configuration', n.get_object_value(CustomExtensionAuthenticationConfiguration)),
            "endpointConfiguration": lambda n : setattr(self, 'endpoint_configuration', n.get_object_value(CustomExtensionEndpointConfiguration)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("authenticationConfiguration", self.authentication_configuration)
        writer.write_object_value("endpointConfiguration", self.endpoint_configuration)
        writer.write_additional_data_value(self.additional_data)
    

