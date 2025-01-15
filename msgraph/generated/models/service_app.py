from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .identity import Identity
    from .identity_set import IdentitySet
    from .service_app_status import ServiceAppStatus

from .entity import Entity

@dataclass
class ServiceApp(Entity, Parsable):
    # The Entra ID application ID.
    application: Optional[Identity] = None
    # Timestamp of the effective activation of the service app.
    effective_date_time: Optional[datetime.datetime] = None
    # Identity of the person who last modified the entity.
    last_modified_by: Optional[IdentitySet] = None
    # Timestamp of the last modification of the entity.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Timestamp of the creation of the service app entity.
    registration_date_time: Optional[datetime.datetime] = None
    # The status of the service app. This value indicates whether or not the application can be used to control the backup service. The possible values are: inactive, active, pendingActive, pendingInactive, unknownFutureValue.
    status: Optional[ServiceAppStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ServiceApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ServiceApp
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ServiceApp()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .identity import Identity
        from .identity_set import IdentitySet
        from .service_app_status import ServiceAppStatus

        from .entity import Entity
        from .identity import Identity
        from .identity_set import IdentitySet
        from .service_app_status import ServiceAppStatus

        fields: dict[str, Callable[[Any], None]] = {
            "application": lambda n : setattr(self, 'application', n.get_object_value(Identity)),
            "effectiveDateTime": lambda n : setattr(self, 'effective_date_time', n.get_datetime_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(IdentitySet)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "registrationDateTime": lambda n : setattr(self, 'registration_date_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(ServiceAppStatus)),
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
        writer.write_object_value("application", self.application)
        writer.write_datetime_value("effectiveDateTime", self.effective_date_time)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_datetime_value("registrationDateTime", self.registration_date_time)
        writer.write_enum_value("status", self.status)
    

