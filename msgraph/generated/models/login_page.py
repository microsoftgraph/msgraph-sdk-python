from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .email_identity import EmailIdentity
    from .entity import Entity
    from .simulation_content_source import SimulationContentSource
    from .simulation_content_status import SimulationContentStatus

from .entity import Entity

@dataclass
class LoginPage(Entity, Parsable):
    # The HTML content of the login page.
    content: Optional[str] = None
    # Identity of the user who created the login page.
    created_by: Optional[EmailIdentity] = None
    # Date and time when the login page was created. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    created_date_time: Optional[datetime.datetime] = None
    # Description about the login page.
    description: Optional[str] = None
    # Display name of the login page.
    display_name: Optional[str] = None
    # The content language of the login page.
    language: Optional[str] = None
    # Identity of the user who last modified the login page.
    last_modified_by: Optional[EmailIdentity] = None
    # Date and time when the login page was last modified. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The source of the content. The possible values are: unknown, global, tenant, unknownFutureValue.
    source: Optional[SimulationContentSource] = None
    # The login page status. The possible values are: unknown, draft, ready, archive, delete, unknownFutureValue.
    status: Optional[SimulationContentStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LoginPage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LoginPage
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LoginPage()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .email_identity import EmailIdentity
        from .entity import Entity
        from .simulation_content_source import SimulationContentSource
        from .simulation_content_status import SimulationContentStatus

        from .email_identity import EmailIdentity
        from .entity import Entity
        from .simulation_content_source import SimulationContentSource
        from .simulation_content_status import SimulationContentStatus

        fields: dict[str, Callable[[Any], None]] = {
            "content": lambda n : setattr(self, 'content', n.get_str_value()),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(EmailIdentity)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "language": lambda n : setattr(self, 'language', n.get_str_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(EmailIdentity)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "source": lambda n : setattr(self, 'source', n.get_enum_value(SimulationContentSource)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(SimulationContentStatus)),
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
        writer.write_str_value("content", self.content)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("language", self.language)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_enum_value("source", self.source)
        writer.write_enum_value("status", self.status)
    

