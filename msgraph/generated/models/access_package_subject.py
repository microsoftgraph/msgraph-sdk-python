from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_package_subject_type import AccessPackageSubjectType
    from .connected_organization import ConnectedOrganization
    from .entity import Entity

from .entity import Entity

@dataclass
class AccessPackageSubject(Entity, Parsable):
    # The connected organization of the subject. Read-only. Nullable.
    connected_organization: Optional[ConnectedOrganization] = None
    # The display name of the subject.
    display_name: Optional[str] = None
    # The email address of the subject.
    email: Optional[str] = None
    # The object identifier of the subject. null if the subject isn't yet a user in the tenant.
    object_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # A string representation of the principal's security identifier, if known, or null if the subject doesn't have a security identifier.
    on_premises_security_identifier: Optional[str] = None
    # The principal name, if known, of the subject.
    principal_name: Optional[str] = None
    # The resource type of the subject. The possible values are: notSpecified, user, servicePrincipal, unknownFutureValue.
    subject_type: Optional[AccessPackageSubjectType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AccessPackageSubject:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageSubject
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AccessPackageSubject()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .access_package_subject_type import AccessPackageSubjectType
        from .connected_organization import ConnectedOrganization
        from .entity import Entity

        from .access_package_subject_type import AccessPackageSubjectType
        from .connected_organization import ConnectedOrganization
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "connectedOrganization": lambda n : setattr(self, 'connected_organization', n.get_object_value(ConnectedOrganization)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "objectId": lambda n : setattr(self, 'object_id', n.get_str_value()),
            "onPremisesSecurityIdentifier": lambda n : setattr(self, 'on_premises_security_identifier', n.get_str_value()),
            "principalName": lambda n : setattr(self, 'principal_name', n.get_str_value()),
            "subjectType": lambda n : setattr(self, 'subject_type', n.get_enum_value(AccessPackageSubjectType)),
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
        writer.write_object_value("connectedOrganization", self.connected_organization)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("email", self.email)
        writer.write_str_value("objectId", self.object_id)
        writer.write_str_value("onPremisesSecurityIdentifier", self.on_premises_security_identifier)
        writer.write_str_value("principalName", self.principal_name)
        writer.write_enum_value("subjectType", self.subject_type)
    

