from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .governance_insight import GovernanceInsight

from .governance_insight import GovernanceInsight

@dataclass
class UserSignInInsight(GovernanceInsight, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.userSignInInsight"
    # Indicates when the user last signed in.
    last_sign_in_date_time: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserSignInInsight:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserSignInInsight
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserSignInInsight()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .governance_insight import GovernanceInsight

        from .governance_insight import GovernanceInsight

        fields: dict[str, Callable[[Any], None]] = {
            "lastSignInDateTime": lambda n : setattr(self, 'last_sign_in_date_time', n.get_datetime_value()),
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
        writer.write_datetime_value("lastSignInDateTime", self.last_sign_in_date_time)
    

