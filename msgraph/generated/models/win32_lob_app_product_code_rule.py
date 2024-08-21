from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .win32_lob_app_rule import Win32LobAppRule
    from .win32_lob_app_rule_operator import Win32LobAppRuleOperator

from .win32_lob_app_rule import Win32LobAppRule

@dataclass
class Win32LobAppProductCodeRule(Win32LobAppRule):
    """
    A complex type to store the product code and version rule data for a Win32 LOB app. This rule is not supported as a requirement rule.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.win32LobAppProductCodeRule"
    # The product code of the app.
    product_code: Optional[str] = None
    # The product version comparison value.
    product_version: Optional[str] = None
    # Contains properties for detection operator.
    product_version_operator: Optional[Win32LobAppRuleOperator] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Win32LobAppProductCodeRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Win32LobAppProductCodeRule
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Win32LobAppProductCodeRule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .win32_lob_app_rule import Win32LobAppRule
        from .win32_lob_app_rule_operator import Win32LobAppRuleOperator

        from .win32_lob_app_rule import Win32LobAppRule
        from .win32_lob_app_rule_operator import Win32LobAppRuleOperator

        fields: Dict[str, Callable[[Any], None]] = {
            "productCode": lambda n : setattr(self, 'product_code', n.get_str_value()),
            "productVersion": lambda n : setattr(self, 'product_version', n.get_str_value()),
            "productVersionOperator": lambda n : setattr(self, 'product_version_operator', n.get_enum_value(Win32LobAppRuleOperator)),
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
        writer.write_str_value("productCode", self.product_code)
        writer.write_str_value("productVersion", self.product_version)
        writer.write_enum_value("productVersionOperator", self.product_version_operator)
    

