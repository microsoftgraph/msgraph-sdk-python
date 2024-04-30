from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .custom_callout_extension import CustomCalloutExtension
    from .on_token_issuance_start_custom_extension import OnTokenIssuanceStartCustomExtension

from .custom_callout_extension import CustomCalloutExtension

@dataclass
class CustomAuthenticationExtension(CustomCalloutExtension):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.customAuthenticationExtension"
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CustomAuthenticationExtension:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomAuthenticationExtension
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onTokenIssuanceStartCustomExtension".casefold():
            from .on_token_issuance_start_custom_extension import OnTokenIssuanceStartCustomExtension

            return OnTokenIssuanceStartCustomExtension()
        return CustomAuthenticationExtension()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .custom_callout_extension import CustomCalloutExtension
        from .on_token_issuance_start_custom_extension import OnTokenIssuanceStartCustomExtension

        from .custom_callout_extension import CustomCalloutExtension
        from .on_token_issuance_start_custom_extension import OnTokenIssuanceStartCustomExtension

        fields: Dict[str, Callable[[Any], None]] = {
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
    

