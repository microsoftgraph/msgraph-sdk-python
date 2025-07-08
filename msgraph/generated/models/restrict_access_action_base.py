from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .dlp_action_info import DlpActionInfo
    from .restriction_action import RestrictionAction
    from .restrict_access_action import RestrictAccessAction

from .dlp_action_info import DlpActionInfo

@dataclass
class RestrictAccessActionBase(DlpActionInfo, Parsable):
    # The OdataType property
    odata_type: Optional[str] = None
    # Action for the app to take. The possible values are: warn, audit, block.
    restriction_action: Optional[RestrictionAction] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RestrictAccessActionBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RestrictAccessActionBase
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.restrictAccessAction".casefold():
            from .restrict_access_action import RestrictAccessAction

            return RestrictAccessAction()
        return RestrictAccessActionBase()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .dlp_action_info import DlpActionInfo
        from .restriction_action import RestrictionAction
        from .restrict_access_action import RestrictAccessAction

        from .dlp_action_info import DlpActionInfo
        from .restriction_action import RestrictionAction
        from .restrict_access_action import RestrictAccessAction

        fields: dict[str, Callable[[Any], None]] = {
            "restrictionAction": lambda n : setattr(self, 'restriction_action', n.get_enum_value(RestrictionAction)),
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
        writer.write_enum_value("restrictionAction", self.restriction_action)
    

