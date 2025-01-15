from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .agreement_file_properties import AgreementFileProperties
    from .agreement_file_version import AgreementFileVersion

from .agreement_file_properties import AgreementFileProperties

@dataclass
class AgreementFileLocalization(AgreementFileProperties, Parsable):
    # The OdataType property
    odata_type: Optional[str] = None
    # Read-only. Customized versions of the terms of use agreement in the Microsoft Entra tenant.
    versions: Optional[list[AgreementFileVersion]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AgreementFileLocalization:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AgreementFileLocalization
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AgreementFileLocalization()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .agreement_file_properties import AgreementFileProperties
        from .agreement_file_version import AgreementFileVersion

        from .agreement_file_properties import AgreementFileProperties
        from .agreement_file_version import AgreementFileVersion

        fields: dict[str, Callable[[Any], None]] = {
            "versions": lambda n : setattr(self, 'versions', n.get_collection_of_object_values(AgreementFileVersion)),
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
        writer.write_collection_of_object_values("versions", self.versions)
    

