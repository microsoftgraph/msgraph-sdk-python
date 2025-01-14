from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .agreement_file import AgreementFile
    from .agreement_file_data import AgreementFileData
    from .agreement_file_localization import AgreementFileLocalization
    from .agreement_file_version import AgreementFileVersion
    from .entity import Entity

from .entity import Entity

@dataclass
class AgreementFileProperties(Entity, Parsable):
    # The date time representing when the file was created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    created_date_time: Optional[datetime.datetime] = None
    # Localized display name of the policy file of an agreement. The localized display name is shown to end users who view the agreement.
    display_name: Optional[str] = None
    # Data that represents the terms of use PDF document. Read-only.
    file_data: Optional[AgreementFileData] = None
    # Name of the agreement file (for example, TOU.pdf). Read-only.
    file_name: Optional[str] = None
    # If none of the languages matches the client preference, indicates whether this is the default agreement file. If none of the files are marked as default, the first one is treated as the default. Read-only.
    is_default: Optional[bool] = None
    # Indicates whether the agreement file is a major version update. Major version updates invalidate the agreement's acceptances on the corresponding language.
    is_major_version: Optional[bool] = None
    # The language of the agreement file in the format 'languagecode2-country/regioncode2'. 'languagecode2' is a lowercase two-letter code derived from ISO 639-1, while 'country/regioncode2' is derived from ISO 3166 and usually consists of two uppercase letters, or a BCP-47 language tag. For example, U.S. English is en-US. Read-only.
    language: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
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
        from .agreement_file_data import AgreementFileData
        from .agreement_file_localization import AgreementFileLocalization
        from .agreement_file_version import AgreementFileVersion
        from .entity import Entity

        from .agreement_file import AgreementFile
        from .agreement_file_data import AgreementFileData
        from .agreement_file_localization import AgreementFileLocalization
        from .agreement_file_version import AgreementFileVersion
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "fileData": lambda n : setattr(self, 'file_data', n.get_object_value(AgreementFileData)),
            "fileName": lambda n : setattr(self, 'file_name', n.get_str_value()),
            "isDefault": lambda n : setattr(self, 'is_default', n.get_bool_value()),
            "isMajorVersion": lambda n : setattr(self, 'is_major_version', n.get_bool_value()),
            "language": lambda n : setattr(self, 'language', n.get_str_value()),
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
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("fileData", self.file_data)
        writer.write_str_value("fileName", self.file_name)
        writer.write_bool_value("isDefault", self.is_default)
        writer.write_bool_value("isMajorVersion", self.is_major_version)
        writer.write_str_value("language", self.language)
    

