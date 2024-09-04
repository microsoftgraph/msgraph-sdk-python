from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .resource_reference import ResourceReference
    from .resource_visualization import ResourceVisualization

from .entity import Entity

@dataclass
class Trending(Entity):
    # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Used for navigating to the trending document.
    resource: Optional[Entity] = None
    # Reference properties of the trending document, such as the url and type of the document.
    resource_reference: Optional[ResourceReference] = None
    # Properties that you can use to visualize the document in your experience.
    resource_visualization: Optional[ResourceVisualization] = None
    # Value indicating how much the document is currently trending. The larger the number, the more the document is currently trending around the user (the more relevant it is). Returned documents are sorted by this value.
    weight: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Trending:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Trending
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Trending()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .resource_reference import ResourceReference
        from .resource_visualization import ResourceVisualization

        from .entity import Entity
        from .resource_reference import ResourceReference
        from .resource_visualization import ResourceVisualization

        fields: Dict[str, Callable[[Any], None]] = {
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "resource": lambda n : setattr(self, 'resource', n.get_object_value(Entity)),
            "resourceReference": lambda n : setattr(self, 'resource_reference', n.get_object_value(ResourceReference)),
            "resourceVisualization": lambda n : setattr(self, 'resource_visualization', n.get_object_value(ResourceVisualization)),
            "weight": lambda n : setattr(self, 'weight', n.get_float_value()),
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
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_object_value("resource", self.resource)
        writer.write_float_value("weight", self.weight)
    

