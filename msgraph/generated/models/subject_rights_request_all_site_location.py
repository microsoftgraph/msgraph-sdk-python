from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .subject_rights_request_site_location import SubjectRightsRequestSiteLocation

from .subject_rights_request_site_location import SubjectRightsRequestSiteLocation

@dataclass
class SubjectRightsRequestAllSiteLocation(SubjectRightsRequestSiteLocation, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.subjectRightsRequestAllSiteLocation"
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SubjectRightsRequestAllSiteLocation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SubjectRightsRequestAllSiteLocation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SubjectRightsRequestAllSiteLocation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .subject_rights_request_site_location import SubjectRightsRequestSiteLocation

        from .subject_rights_request_site_location import SubjectRightsRequestSiteLocation

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
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        from .subject_rights_request_site_location import SubjectRightsRequestSiteLocation

    

