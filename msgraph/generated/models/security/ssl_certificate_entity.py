from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..physical_address import PhysicalAddress

@dataclass
class SslCertificateEntity(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # A physical address of the entity.
    address: Optional[PhysicalAddress] = None
    # Alternate names for this entity that are part of the certificate.
    alternate_names: Optional[List[str]] = None
    # A common name for this entity.
    common_name: Optional[str] = None
    # An email for this entity.
    email: Optional[str] = None
    # If the entity is a person, this is the person's given name (first name).
    given_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # If the entity is an organization, this is the name of the organization.
    organization_name: Optional[str] = None
    # If the entity is an organization, this communicates if a unit in the organization is named on the entity.
    organization_unit_name: Optional[str] = None
    # A serial number assigned to the entity; usually only available if the entity is the issuer.
    serial_number: Optional[str] = None
    # If the entity is a person, this is the person's surname (last name).
    surname: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SslCertificateEntity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SslCertificateEntity
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SslCertificateEntity()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..physical_address import PhysicalAddress

        from ..physical_address import PhysicalAddress

        fields: Dict[str, Callable[[Any], None]] = {
            "address": lambda n : setattr(self, 'address', n.get_object_value(PhysicalAddress)),
            "alternateNames": lambda n : setattr(self, 'alternate_names', n.get_collection_of_primitive_values(str)),
            "commonName": lambda n : setattr(self, 'common_name', n.get_str_value()),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "givenName": lambda n : setattr(self, 'given_name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "organizationName": lambda n : setattr(self, 'organization_name', n.get_str_value()),
            "organizationUnitName": lambda n : setattr(self, 'organization_unit_name', n.get_str_value()),
            "serialNumber": lambda n : setattr(self, 'serial_number', n.get_str_value()),
            "surname": lambda n : setattr(self, 'surname', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("address", self.address)
        writer.write_collection_of_primitive_values("alternateNames", self.alternate_names)
        writer.write_str_value("commonName", self.common_name)
        writer.write_str_value("email", self.email)
        writer.write_str_value("givenName", self.given_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("organizationName", self.organization_name)
        writer.write_str_value("organizationUnitName", self.organization_unit_name)
        writer.write_str_value("serialNumber", self.serial_number)
        writer.write_str_value("surname", self.surname)
        writer.write_additional_data_value(self.additional_data)
    

