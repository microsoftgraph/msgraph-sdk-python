from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

identity_provider_base = lazy_import('msgraph.generated.models.identity_provider_base')

class BuiltInIdentityProvider(identity_provider_base.IdentityProviderBase):
    def __init__(self,) -> None:
        """
        Instantiates a new BuiltInIdentityProvider and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.builtInIdentityProvider"
        # The identity provider type. For a B2B scenario, possible values: AADSignup, MicrosoftAccount, EmailOTP. Required.
        self._identity_provider_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BuiltInIdentityProvider:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: BuiltInIdentityProvider
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return BuiltInIdentityProvider()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "identity_provider_type": lambda n : setattr(self, 'identity_provider_type', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def identity_provider_type(self,) -> Optional[str]:
        """
        Gets the identityProviderType property value. The identity provider type. For a B2B scenario, possible values: AADSignup, MicrosoftAccount, EmailOTP. Required.
        Returns: Optional[str]
        """
        return self._identity_provider_type
    
    @identity_provider_type.setter
    def identity_provider_type(self,value: Optional[str] = None) -> None:
        """
        Sets the identityProviderType property value. The identity provider type. For a B2B scenario, possible values: AADSignup, MicrosoftAccount, EmailOTP. Required.
        Args:
            value: Value to set for the identityProviderType property.
        """
        self._identity_provider_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("identityProviderType", self.identity_provider_type)
    

