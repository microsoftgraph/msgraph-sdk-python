from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import education_excel_resource, education_external_resource, education_file_resource, education_link_resource, education_media_resource, education_power_point_resource, education_teams_app_resource, education_word_resource, identity_set

@dataclass
class EducationResource(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The individual who created the resource.
    created_by: Optional[identity_set.IdentitySet] = None
    # Moment in time when the resource was created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    created_date_time: Optional[datetime] = None
    # Display name of resource.
    display_name: Optional[str] = None
    # The last user to modify the resource.
    last_modified_by: Optional[identity_set.IdentitySet] = None
    # Moment in time when the resource was last modified.  The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    last_modified_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EducationResource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EducationResource
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.educationExcelResource":
                from . import education_excel_resource

                return education_excel_resource.EducationExcelResource()
            if mapping_value == "#microsoft.graph.educationExternalResource":
                from . import education_external_resource

                return education_external_resource.EducationExternalResource()
            if mapping_value == "#microsoft.graph.educationFileResource":
                from . import education_file_resource

                return education_file_resource.EducationFileResource()
            if mapping_value == "#microsoft.graph.educationLinkResource":
                from . import education_link_resource

                return education_link_resource.EducationLinkResource()
            if mapping_value == "#microsoft.graph.educationMediaResource":
                from . import education_media_resource

                return education_media_resource.EducationMediaResource()
            if mapping_value == "#microsoft.graph.educationPowerPointResource":
                from . import education_power_point_resource

                return education_power_point_resource.EducationPowerPointResource()
            if mapping_value == "#microsoft.graph.educationTeamsAppResource":
                from . import education_teams_app_resource

                return education_teams_app_resource.EducationTeamsAppResource()
            if mapping_value == "#microsoft.graph.educationWordResource":
                from . import education_word_resource

                return education_word_resource.EducationWordResource()
        return EducationResource()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import education_excel_resource, education_external_resource, education_file_resource, education_link_resource, education_media_resource, education_power_point_resource, education_teams_app_resource, education_word_resource, identity_set

        fields: Dict[str, Callable[[Any], None]] = {
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(identity_set.IdentitySet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(identity_set.IdentitySet)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

