from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .x509_certificate_affinity_level import X509CertificateAffinityLevel

@dataclass
class X509CertificateUserBinding(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The OdataType property
    odata_type: Optional[str] = None
    # The priority of the binding. Microsoft Entra ID uses the binding with the highest priority. This value must be a non-negative integer and unique in the collection of objects in the certificateUserBindings property of an x509CertificateAuthenticationMethodConfiguration object. Required
    priority: Optional[int] = None
    # The trustAffinityLevel property
    trust_affinity_level: Optional[X509CertificateAffinityLevel] = None
    # Defines the Microsoft Entra user property of the user object to use for the binding. The possible values are: userPrincipalName, onPremisesUserPrincipalName, certificateUserIds. Required.
    user_property: Optional[str] = None
    # The field on the X.509 certificate to use for the binding. The possible values are: PrincipalName, RFC822Name, SubjectKeyIdentifier, SHA1PublicKey.
    x509_certificate_field: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> X509CertificateUserBinding:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: X509CertificateUserBinding
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return X509CertificateUserBinding()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .x509_certificate_affinity_level import X509CertificateAffinityLevel

        from .x509_certificate_affinity_level import X509CertificateAffinityLevel

        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "priority": lambda n : setattr(self, 'priority', n.get_int_value()),
            "trustAffinityLevel": lambda n : setattr(self, 'trust_affinity_level', n.get_enum_value(X509CertificateAffinityLevel)),
            "userProperty": lambda n : setattr(self, 'user_property', n.get_str_value()),
            "x509CertificateField": lambda n : setattr(self, 'x509_certificate_field', n.get_str_value()),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("priority", self.priority)
        writer.write_enum_value("trustAffinityLevel", self.trust_affinity_level)
        writer.write_str_value("userProperty", self.user_property)
        writer.write_str_value("x509CertificateField", self.x509_certificate_field)
        writer.write_additional_data_value(self.additional_data)
    

