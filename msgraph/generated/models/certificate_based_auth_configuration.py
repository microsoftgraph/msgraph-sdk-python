from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, Union

from . import certificate_authority, entity

class CertificateBasedAuthConfiguration(entity.Entity):
    """
    Provides operations to manage the admin singleton.
    """
    @property
    def certificate_authorities(self,) -> Optional[List[certificate_authority.CertificateAuthority]]:
        """
        Gets the certificateAuthorities property value. Collection of certificate authorities which creates a trusted certificate chain.
        Returns: Optional[List[certificate_authority.CertificateAuthority]]
        """
        return self._certificate_authorities

    @certificate_authorities.setter
    def certificate_authorities(self,value: Optional[List[certificate_authority.CertificateAuthority]] = None) -> None:
        """
        Sets the certificateAuthorities property value. Collection of certificate authorities which creates a trusted certificate chain.
        Args:
            value: Value to set for the certificateAuthorities property.
        """
        self._certificate_authorities = value

    def __init__(self,) -> None:
        """
        Instantiates a new certificateBasedAuthConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.certificateBasedAuthConfiguration"
        # Collection of certificate authorities which creates a trusted certificate chain.
        self._certificate_authorities: Optional[List[certificate_authority.CertificateAuthority]] = None

    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CertificateBasedAuthConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CertificateBasedAuthConfiguration
        """
        if not parse_node:
            raise Exception("parse_node cannot be undefined")
        return CertificateBasedAuthConfiguration()

    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "certificate_authorities": lambda n : setattr(self, 'certificate_authorities', n.get_collection_of_object_values(certificate_authority.CertificateAuthority)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields

    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("certificateAuthorities", self.certificate_authorities)


