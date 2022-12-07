from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

access_package_subject_type = lazy_import('msgraph.generated.models.access_package_subject_type')
connected_organization = lazy_import('msgraph.generated.models.connected_organization')
entity = lazy_import('msgraph.generated.models.entity')

class AccessPackageSubject(entity.Entity):
    @property
    def connected_organization(self,) -> Optional[connected_organization.ConnectedOrganization]:
        """
        Gets the connectedOrganization property value. The connected organization of the subject. Read-only. Nullable.
        Returns: Optional[connected_organization.ConnectedOrganization]
        """
        return self._connected_organization
    
    @connected_organization.setter
    def connected_organization(self,value: Optional[connected_organization.ConnectedOrganization] = None) -> None:
        """
        Sets the connectedOrganization property value. The connected organization of the subject. Read-only. Nullable.
        Args:
            value: Value to set for the connectedOrganization property.
        """
        self._connected_organization = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new accessPackageSubject and sets the default values.
        """
        super().__init__()
        # The connected organization of the subject. Read-only. Nullable.
        self._connected_organization: Optional[connected_organization.ConnectedOrganization] = None
        # The display name of the subject.
        self._display_name: Optional[str] = None
        # The email address of the subject.
        self._email: Optional[str] = None
        # The object identifier of the subject. null if the subject is not yet a user in the tenant.
        self._object_id: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # A string representation of the principal's security identifier, if known, or null if the subject does not have a security identifier.
        self._on_premises_security_identifier: Optional[str] = None
        # The principal name, if known, of the subject.
        self._principal_name: Optional[str] = None
        # The resource type of the subject. The possible values are: notSpecified, user, servicePrincipal, unknownFutureValue.
        self._subject_type: Optional[access_package_subject_type.AccessPackageSubjectType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessPackageSubject:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageSubject
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AccessPackageSubject()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name of the subject.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name of the subject.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def email(self,) -> Optional[str]:
        """
        Gets the email property value. The email address of the subject.
        Returns: Optional[str]
        """
        return self._email
    
    @email.setter
    def email(self,value: Optional[str] = None) -> None:
        """
        Sets the email property value. The email address of the subject.
        Args:
            value: Value to set for the email property.
        """
        self._email = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "connected_organization": lambda n : setattr(self, 'connected_organization', n.get_object_value(connected_organization.ConnectedOrganization)),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "object_id": lambda n : setattr(self, 'object_id', n.get_str_value()),
            "on_premises_security_identifier": lambda n : setattr(self, 'on_premises_security_identifier', n.get_str_value()),
            "principal_name": lambda n : setattr(self, 'principal_name', n.get_str_value()),
            "subject_type": lambda n : setattr(self, 'subject_type', n.get_enum_value(access_package_subject_type.AccessPackageSubjectType)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def object_id(self,) -> Optional[str]:
        """
        Gets the objectId property value. The object identifier of the subject. null if the subject is not yet a user in the tenant.
        Returns: Optional[str]
        """
        return self._object_id
    
    @object_id.setter
    def object_id(self,value: Optional[str] = None) -> None:
        """
        Sets the objectId property value. The object identifier of the subject. null if the subject is not yet a user in the tenant.
        Args:
            value: Value to set for the objectId property.
        """
        self._object_id = value
    
    @property
    def on_premises_security_identifier(self,) -> Optional[str]:
        """
        Gets the onPremisesSecurityIdentifier property value. A string representation of the principal's security identifier, if known, or null if the subject does not have a security identifier.
        Returns: Optional[str]
        """
        return self._on_premises_security_identifier
    
    @on_premises_security_identifier.setter
    def on_premises_security_identifier(self,value: Optional[str] = None) -> None:
        """
        Sets the onPremisesSecurityIdentifier property value. A string representation of the principal's security identifier, if known, or null if the subject does not have a security identifier.
        Args:
            value: Value to set for the onPremisesSecurityIdentifier property.
        """
        self._on_premises_security_identifier = value
    
    @property
    def principal_name(self,) -> Optional[str]:
        """
        Gets the principalName property value. The principal name, if known, of the subject.
        Returns: Optional[str]
        """
        return self._principal_name
    
    @principal_name.setter
    def principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the principalName property value. The principal name, if known, of the subject.
        Args:
            value: Value to set for the principalName property.
        """
        self._principal_name = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("connectedOrganization", self.connected_organization)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("email", self.email)
        writer.write_str_value("objectId", self.object_id)
        writer.write_str_value("onPremisesSecurityIdentifier", self.on_premises_security_identifier)
        writer.write_str_value("principalName", self.principal_name)
        writer.write_enum_value("subjectType", self.subject_type)
    
    @property
    def subject_type(self,) -> Optional[access_package_subject_type.AccessPackageSubjectType]:
        """
        Gets the subjectType property value. The resource type of the subject. The possible values are: notSpecified, user, servicePrincipal, unknownFutureValue.
        Returns: Optional[access_package_subject_type.AccessPackageSubjectType]
        """
        return self._subject_type
    
    @subject_type.setter
    def subject_type(self,value: Optional[access_package_subject_type.AccessPackageSubjectType] = None) -> None:
        """
        Sets the subjectType property value. The resource type of the subject. The possible values are: notSpecified, user, servicePrincipal, unknownFutureValue.
        Args:
            value: Value to set for the subjectType property.
        """
        self._subject_type = value
    

