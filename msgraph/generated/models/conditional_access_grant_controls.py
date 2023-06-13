from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import authentication_strength_policy, conditional_access_grant_control

@dataclass
class ConditionalAccessGrantControls(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The authenticationStrength property
    authentication_strength: Optional[authentication_strength_policy.AuthenticationStrengthPolicy] = None
    # List of values of built-in controls required by the policy. Possible values: block, mfa, compliantDevice, domainJoinedDevice, approvedApplication, compliantApplication, passwordChange, unknownFutureValue.
    built_in_controls: Optional[List[conditional_access_grant_control.ConditionalAccessGrantControl]] = None
    # List of custom controls IDs required by the policy. For more information, see Custom controls.
    custom_authentication_factors: Optional[List[str]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Defines the relationship of the grant controls. Possible values: AND, OR.
    operator: Optional[str] = None
    # List of terms of use IDs required by the policy.
    terms_of_use: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ConditionalAccessGrantControls:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ConditionalAccessGrantControls
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ConditionalAccessGrantControls()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import authentication_strength_policy, conditional_access_grant_control

        fields: Dict[str, Callable[[Any], None]] = {
            "authenticationStrength": lambda n : setattr(self, 'authentication_strength', n.get_object_value(authentication_strength_policy.AuthenticationStrengthPolicy)),
            "builtInControls": lambda n : setattr(self, 'built_in_controls', n.get_collection_of_enum_values(conditional_access_grant_control.ConditionalAccessGrantControl)),
            "customAuthenticationFactors": lambda n : setattr(self, 'custom_authentication_factors', n.get_collection_of_primitive_values(str)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "operator": lambda n : setattr(self, 'operator', n.get_str_value()),
            "termsOfUse": lambda n : setattr(self, 'terms_of_use', n.get_collection_of_primitive_values(str)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("authenticationStrength", self.authentication_strength)
        writer.write_enum_value("builtInControls", self.built_in_controls)
        writer.write_collection_of_primitive_values("customAuthenticationFactors", self.custom_authentication_factors)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("operator", self.operator)
        writer.write_collection_of_primitive_values("termsOfUse", self.terms_of_use)
        writer.write_additional_data_value(self.additional_data)
    

