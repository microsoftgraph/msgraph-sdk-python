from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .agreement_file import AgreementFile
    from .agreement_file_localization import AgreementFileLocalization
    from .agreement_file_version import AgreementFileVersion
    from .entity import Entity

from .entity import Entity

@dataclass
class AgreementFileProperties(Entity, Parsable):
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AgreementFileProperties:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AgreementFileProperties
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.agreementFile".casefold():
            from .agreement_file import AgreementFile

            return AgreementFile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.agreementFileLocalization".casefold():
            from .agreement_file_localization import AgreementFileLocalization

            return AgreementFileLocalization()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.agreementFileVersion".casefold():
            from .agreement_file_version import AgreementFileVersion

            return AgreementFileVersion()
        return AgreementFileProperties()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .agreement_file import AgreementFile
        from .agreement_file_localization import AgreementFileLocalization
        from .agreement_file_version import AgreementFileVersion
        from .entity import Entity

        from .agreement_file import AgreementFile
        from .agreement_file_localization import AgreementFileLocalization
        from .agreement_file_version import AgreementFileVersion
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
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
    

