from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .health_issue import HealthIssue
    from .sensor import Sensor

from ..entity import Entity

@dataclass
class IdentityContainer(Entity, Parsable):
    # Represents potential issues identified by Microsoft Defender for Identity within a customer's Microsoft Defender for Identity configuration.
    health_issues: Optional[list[HealthIssue]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents a customer's Microsoft Defender for Identity sensors.
    sensors: Optional[list[Sensor]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IdentityContainer:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IdentityContainer
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return IdentityContainer()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .health_issue import HealthIssue
        from .sensor import Sensor

        from ..entity import Entity
        from .health_issue import HealthIssue
        from .sensor import Sensor

        fields: dict[str, Callable[[Any], None]] = {
            "healthIssues": lambda n : setattr(self, 'health_issues', n.get_collection_of_object_values(HealthIssue)),
            "sensors": lambda n : setattr(self, 'sensors', n.get_collection_of_object_values(Sensor)),
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
        writer.write_collection_of_object_values("healthIssues", self.health_issues)
        writer.write_collection_of_object_values("sensors", self.sensors)
    

