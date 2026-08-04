from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .service_provider_constraints import ServiceProviderConstraints

from .service_provider_constraints import ServiceProviderConstraints

@dataclass
class DelegatedAdminServiceProviderConstraints(ServiceProviderConstraints, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.delegatedAdminServiceProviderConstraints"
    # The allowedRoleTemplateIds property
    allowed_role_template_ids: Optional[list[str]] = None
    # The createdDateTime property
    created_date_time: Optional[datetime.datetime] = None
    # The lastModifiedDateTime property
    last_modified_date_time: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DelegatedAdminServiceProviderConstraints:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DelegatedAdminServiceProviderConstraints
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DelegatedAdminServiceProviderConstraints()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .service_provider_constraints import ServiceProviderConstraints

        from .service_provider_constraints import ServiceProviderConstraints

        fields: dict[str, Callable[[Any], None]] = {
            "allowedRoleTemplateIds": lambda n : setattr(self, 'allowed_role_template_ids', n.get_collection_of_primitive_values(str)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
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
        writer.write_collection_of_primitive_values("allowedRoleTemplateIds", self.allowed_role_template_ids)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
    

