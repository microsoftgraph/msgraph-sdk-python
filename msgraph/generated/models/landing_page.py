from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .email_identity import EmailIdentity
    from .entity import Entity
    from .landing_page_detail import LandingPageDetail
    from .simulation_content_source import SimulationContentSource
    from .simulation_content_status import SimulationContentStatus

from .entity import Entity

@dataclass
class LandingPage(Entity, Parsable):
    # Identity of the user who created the landing page.
    created_by: Optional[EmailIdentity] = None
    # Date and time when the landing page was created. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    created_date_time: Optional[datetime.datetime] = None
    # Description of the landing page as defined by the user.
    description: Optional[str] = None
    # The detail information for a landing page associated with a simulation during its creation.
    details: Optional[list[LandingPageDetail]] = None
    # The display name of the landing page.
    display_name: Optional[str] = None
    # Email identity of the user who last modified the landing page.
    last_modified_by: Optional[EmailIdentity] = None
    # Date and time when the landing page was last modified. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    last_modified_date_time: Optional[datetime.datetime] = None
    # Content locale.
    locale: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The source of the content. The possible values are: unknown, global, tenant, unknownFutureValue.
    source: Optional[SimulationContentSource] = None
    # The status of the simulation. The possible values are: unknown, draft, ready, archive, delete, unknownFutureValue.
    status: Optional[SimulationContentStatus] = None
    # Supported locales.
    supported_locales: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LandingPage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LandingPage
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LandingPage()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .email_identity import EmailIdentity
        from .entity import Entity
        from .landing_page_detail import LandingPageDetail
        from .simulation_content_source import SimulationContentSource
        from .simulation_content_status import SimulationContentStatus

        from .email_identity import EmailIdentity
        from .entity import Entity
        from .landing_page_detail import LandingPageDetail
        from .simulation_content_source import SimulationContentSource
        from .simulation_content_status import SimulationContentStatus

        fields: dict[str, Callable[[Any], None]] = {
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(EmailIdentity)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "details": lambda n : setattr(self, 'details', n.get_collection_of_object_values(LandingPageDetail)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(EmailIdentity)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "locale": lambda n : setattr(self, 'locale', n.get_str_value()),
            "source": lambda n : setattr(self, 'source', n.get_enum_value(SimulationContentSource)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(SimulationContentStatus)),
            "supportedLocales": lambda n : setattr(self, 'supported_locales', n.get_collection_of_primitive_values(str)),
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
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_collection_of_object_values("details", self.details)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("locale", self.locale)
        writer.write_enum_value("source", self.source)
        writer.write_enum_value("status", self.status)
        writer.write_collection_of_primitive_values("supportedLocales", self.supported_locales)
    

