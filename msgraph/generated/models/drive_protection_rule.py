from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .protection_rule_base import ProtectionRuleBase

from .protection_rule_base import ProtectionRuleBase

@dataclass
class DriveProtectionRule(ProtectionRuleBase, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.driveProtectionRule"
    # Contains a drive expression. For examples, see driveExpression examples.
    drive_expression: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DriveProtectionRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DriveProtectionRule
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DriveProtectionRule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .protection_rule_base import ProtectionRuleBase

        from .protection_rule_base import ProtectionRuleBase

        fields: Dict[str, Callable[[Any], None]] = {
            "driveExpression": lambda n : setattr(self, 'drive_expression', n.get_str_value()),
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
        from .protection_rule_base import ProtectionRuleBase

        writer.write_str_value("driveExpression", self.drive_expression)
    

