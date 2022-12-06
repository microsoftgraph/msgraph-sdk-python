from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

attestation_level = lazy_import('msgraph.generated.models.attestation_level')
authentication_method = lazy_import('msgraph.generated.models.authentication_method')

class Fido2AuthenticationMethod(authentication_method.AuthenticationMethod):
    @property
    def aa_guid(self,) -> Optional[str]:
        """
        Gets the aaGuid property value. Authenticator Attestation GUID, an identifier that indicates the type (e.g. make and model) of the authenticator.
        Returns: Optional[str]
        """
        return self._aa_guid
    
    @aa_guid.setter
    def aa_guid(self,value: Optional[str] = None) -> None:
        """
        Sets the aaGuid property value. Authenticator Attestation GUID, an identifier that indicates the type (e.g. make and model) of the authenticator.
        Args:
            value: Value to set for the aaGuid property.
        """
        self._aa_guid = value
    
    @property
    def attestation_certificates(self,) -> Optional[List[str]]:
        """
        Gets the attestationCertificates property value. The attestation certificate(s) attached to this security key.
        Returns: Optional[List[str]]
        """
        return self._attestation_certificates
    
    @attestation_certificates.setter
    def attestation_certificates(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the attestationCertificates property value. The attestation certificate(s) attached to this security key.
        Args:
            value: Value to set for the attestationCertificates property.
        """
        self._attestation_certificates = value
    
    @property
    def attestation_level(self,) -> Optional[attestation_level.AttestationLevel]:
        """
        Gets the attestationLevel property value. The attestation level of this FIDO2 security key. Possible values are: attested, or notAttested.
        Returns: Optional[attestation_level.AttestationLevel]
        """
        return self._attestation_level
    
    @attestation_level.setter
    def attestation_level(self,value: Optional[attestation_level.AttestationLevel] = None) -> None:
        """
        Sets the attestationLevel property value. The attestation level of this FIDO2 security key. Possible values are: attested, or notAttested.
        Args:
            value: Value to set for the attestationLevel property.
        """
        self._attestation_level = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new Fido2AuthenticationMethod and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.fido2AuthenticationMethod"
        # Authenticator Attestation GUID, an identifier that indicates the type (e.g. make and model) of the authenticator.
        self._aa_guid: Optional[str] = None
        # The attestation certificate(s) attached to this security key.
        self._attestation_certificates: Optional[List[str]] = None
        # The attestation level of this FIDO2 security key. Possible values are: attested, or notAttested.
        self._attestation_level: Optional[attestation_level.AttestationLevel] = None
        # The timestamp when this key was registered to the user.
        self._created_date_time: Optional[datetime] = None
        # The display name of the key as given by the user.
        self._display_name: Optional[str] = None
        # The manufacturer-assigned model of the FIDO2 security key.
        self._model: Optional[str] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The timestamp when this key was registered to the user.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The timestamp when this key was registered to the user.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
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
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name of the key as given by the user.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name of the key as given by the user.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "aa_guid": lambda n : setattr(self, 'aa_guid', n.get_str_value()),
            "attestation_certificates": lambda n : setattr(self, 'attestation_certificates', n.get_collection_of_primitive_values(str)),
            "attestation_level": lambda n : setattr(self, 'attestation_level', n.get_enum_value(attestation_level.AttestationLevel)),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "model": lambda n : setattr(self, 'model', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def model(self,) -> Optional[str]:
        """
        Gets the model property value. The manufacturer-assigned model of the FIDO2 security key.
        Returns: Optional[str]
        """
        return self._model
    
    @model.setter
    def model(self,value: Optional[str] = None) -> None:
        """
        Sets the model property value. The manufacturer-assigned model of the FIDO2 security key.
        Args:
            value: Value to set for the model property.
        """
        self._model = value
    
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
    

