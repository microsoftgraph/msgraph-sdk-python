from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authentication_method_modes import AuthenticationMethodModes
    from .entity import Entity
    from .fido2_combination_configuration import Fido2CombinationConfiguration
    from .x509_certificate_combination_configuration import X509CertificateCombinationConfiguration

from .entity import Entity

@dataclass
class AuthenticationCombinationConfiguration(Entity):
    # Which authentication method combinations this configuration applies to. Must be an allowedCombinations object, part of the authenticationStrengthPolicy. The only possible value for fido2combinationConfigurations is 'fido2'.
    applies_to_combinations: Optional[List[AuthenticationMethodModes]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AuthenticationCombinationConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticationCombinationConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.fido2CombinationConfiguration".casefold():
            from .fido2_combination_configuration import Fido2CombinationConfiguration

            return Fido2CombinationConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.x509CertificateCombinationConfiguration".casefold():
            from .x509_certificate_combination_configuration import X509CertificateCombinationConfiguration

            return X509CertificateCombinationConfiguration()
        return AuthenticationCombinationConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .authentication_method_modes import AuthenticationMethodModes
        from .entity import Entity
        from .fido2_combination_configuration import Fido2CombinationConfiguration
        from .x509_certificate_combination_configuration import X509CertificateCombinationConfiguration

        from .authentication_method_modes import AuthenticationMethodModes
        from .entity import Entity
        from .fido2_combination_configuration import Fido2CombinationConfiguration
        from .x509_certificate_combination_configuration import X509CertificateCombinationConfiguration

        fields: Dict[str, Callable[[Any], None]] = {
            "appliesToCombinations": lambda n : setattr(self, 'applies_to_combinations', n.get_collection_of_enum_values(AuthenticationMethodModes)),
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
        writer.write_collection_of_enum_values("appliesToCombinations", self.applies_to_combinations)
    

