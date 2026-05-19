from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .include_target import IncludeTarget

@dataclass
class X509CertificateAuthorityScope(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # A collection of groups that are enabled to be in scope to use certificates issued by specific certificate authority.
    include_targets: Optional[list[IncludeTarget]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Public Key Infrastructure container object under which the certificate authorities are stored in the Entra PKI based trust store.
    public_key_infrastructure_identifier: Optional[str] = None
    # Subject Key Identifier that identifies the certificate authority uniquely.
    subject_key_identifier: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> X509CertificateAuthorityScope:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: X509CertificateAuthorityScope
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return X509CertificateAuthorityScope()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .include_target import IncludeTarget

        from .include_target import IncludeTarget

        fields: dict[str, Callable[[Any], None]] = {
            "includeTargets": lambda n : setattr(self, 'include_targets', n.get_collection_of_object_values(IncludeTarget)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "publicKeyInfrastructureIdentifier": lambda n : setattr(self, 'public_key_infrastructure_identifier', n.get_str_value()),
            "subjectKeyIdentifier": lambda n : setattr(self, 'subject_key_identifier', n.get_str_value()),
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
        writer.write_collection_of_object_values("includeTargets", self.include_targets)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("publicKeyInfrastructureIdentifier", self.public_key_infrastructure_identifier)
        writer.write_str_value("subjectKeyIdentifier", self.subject_key_identifier)
        writer.write_additional_data_value(self.additional_data)
    

