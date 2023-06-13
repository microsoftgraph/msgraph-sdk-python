from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import win32_lob_app_rule, win32_lob_app_rule_operator

from . import win32_lob_app_rule

@dataclass
class Win32LobAppProductCodeRule(win32_lob_app_rule.Win32LobAppRule):
    odata_type = "#microsoft.graph.win32LobAppProductCodeRule"
    # The product code of the app.
    product_code: Optional[str] = None
    # The product version comparison value.
    product_version: Optional[str] = None
    # Contains properties for detection operator.
    product_version_operator: Optional[win32_lob_app_rule_operator.Win32LobAppRuleOperator] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Win32LobAppProductCodeRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Win32LobAppProductCodeRule
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Win32LobAppProductCodeRule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import win32_lob_app_rule, win32_lob_app_rule_operator

        fields: Dict[str, Callable[[Any], None]] = {
            "productCode": lambda n : setattr(self, 'product_code', n.get_str_value()),
            "productVersion": lambda n : setattr(self, 'product_version', n.get_str_value()),
            "productVersionOperator": lambda n : setattr(self, 'product_version_operator', n.get_enum_value(win32_lob_app_rule_operator.Win32LobAppRuleOperator)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("productCode", self.product_code)
        writer.write_str_value("productVersion", self.product_version)
        writer.write_enum_value("productVersionOperator", self.product_version_operator)
    

