from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .alert_evidence import AlertEvidence
    from .google_cloud_location_type import GoogleCloudLocationType

from .alert_evidence import AlertEvidence

@dataclass
class GoogleCloudResourceEvidence(AlertEvidence):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.googleCloudResourceEvidence"
    # The fullResourceName property
    full_resource_name: Optional[str] = None
    # The zone or region where the resource is located.
    location: Optional[str] = None
    # The type of location. Possible values are: unknown, regional, zonal, global, unknownFutureValue.
    location_type: Optional[GoogleCloudLocationType] = None
    # The Google project ID as defined by the user.
    project_id: Optional[str] = None
    # The project number assigned by Google.
    project_number: Optional[int] = None
    # The name of the resource.
    resource_name: Optional[str] = None
    # The type of the resource.
    resource_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GoogleCloudResourceEvidence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GoogleCloudResourceEvidence
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return GoogleCloudResourceEvidence()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .alert_evidence import AlertEvidence
        from .google_cloud_location_type import GoogleCloudLocationType

        from .alert_evidence import AlertEvidence
        from .google_cloud_location_type import GoogleCloudLocationType

        fields: Dict[str, Callable[[Any], None]] = {
            "fullResourceName": lambda n : setattr(self, 'full_resource_name', n.get_str_value()),
            "location": lambda n : setattr(self, 'location', n.get_str_value()),
            "locationType": lambda n : setattr(self, 'location_type', n.get_enum_value(GoogleCloudLocationType)),
            "projectId": lambda n : setattr(self, 'project_id', n.get_str_value()),
            "projectNumber": lambda n : setattr(self, 'project_number', n.get_int_value()),
            "resourceName": lambda n : setattr(self, 'resource_name', n.get_str_value()),
            "resourceType": lambda n : setattr(self, 'resource_type', n.get_str_value()),
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
        writer.write_str_value("fullResourceName", self.full_resource_name)
        writer.write_str_value("location", self.location)
        writer.write_enum_value("locationType", self.location_type)
        writer.write_str_value("projectId", self.project_id)
        writer.write_int_value("projectNumber", self.project_number)
        writer.write_str_value("resourceName", self.resource_name)
        writer.write_str_value("resourceType", self.resource_type)
    

