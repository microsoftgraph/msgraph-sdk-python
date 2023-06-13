from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import attestation_level, authentication_method

from . import authentication_method

@dataclass
class Fido2AuthenticationMethod(authentication_method.AuthenticationMethod):
    odata_type = "#microsoft.graph.fido2AuthenticationMethod"
    # Authenticator Attestation GUID, an identifier that indicates the type (e.g. make and model) of the authenticator.
    aa_guid: Optional[str] = None
    # The attestation certificate(s) attached to this security key.
    attestation_certificates: Optional[List[str]] = None
    # The attestation level of this FIDO2 security key. Possible values are: attested, or notAttested.
    attestation_level: Optional[attestation_level.AttestationLevel] = None
    # The timestamp when this key was registered to the user.
    created_date_time: Optional[datetime] = None
    # The display name of the key as given by the user.
    display_name: Optional[str] = None
    # The manufacturer-assigned model of the FIDO2 security key.
    model: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Fido2AuthenticationMethod:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Fido2AuthenticationMethod
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Fido2AuthenticationMethod()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import attestation_level, authentication_method

        fields: Dict[str, Callable[[Any], None]] = {
            "aaGuid": lambda n : setattr(self, 'aa_guid', n.get_str_value()),
            "attestationCertificates": lambda n : setattr(self, 'attestation_certificates', n.get_collection_of_primitive_values(str)),
            "attestationLevel": lambda n : setattr(self, 'attestation_level', n.get_enum_value(attestation_level.AttestationLevel)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "model": lambda n : setattr(self, 'model', n.get_str_value()),
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
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("aaGuid", self.aa_guid)
        writer.write_collection_of_primitive_values("attestationCertificates", self.attestation_certificates)
        writer.write_enum_value("attestationLevel", self.attestation_level)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("model", self.model)
    

