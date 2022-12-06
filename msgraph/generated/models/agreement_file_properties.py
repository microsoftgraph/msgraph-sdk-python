from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

agreement_file_data = lazy_import('msgraph.generated.models.agreement_file_data')
entity = lazy_import('msgraph.generated.models.entity')

class AgreementFileProperties(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new agreementFileProperties and sets the default values.
        """
        super().__init__()
        # The date time representing when the file was created.The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._created_date_time: Optional[datetime] = None
        # Localized display name of the policy file of an agreement. The localized display name is shown to end users who view the agreement.
        self._display_name: Optional[str] = None
        # Data that represents the terms of use PDF document. Read-only.
        self._file_data: Optional[agreement_file_data.AgreementFileData] = None
        # Name of the agreement file (for example, TOU.pdf). Read-only.
        self._file_name: Optional[str] = None
        # If none of the languages matches the client preference, indicates whether this is the default agreement file . If none of the files are marked as default, the first one is treated as the default. Read-only.
        self._is_default: Optional[bool] = None
        # Indicates whether the agreement file is a major version update. Major version updates invalidate the agreement's acceptances on the corresponding language.
        self._is_major_version: Optional[bool] = None
        # The language of the agreement file in the format 'languagecode2-country/regioncode2'. 'languagecode2' is a lowercase two-letter code derived from ISO 639-1, while 'country/regioncode2' is derived from ISO 3166 and usually consists of two uppercase letters, or a BCP-47 language tag. For example, U.S. English is en-US. Read-only.
        self._language: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The date time representing when the file was created.The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The date time representing when the file was created.The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AgreementFileProperties:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AgreementFileProperties
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AgreementFileProperties()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Localized display name of the policy file of an agreement. The localized display name is shown to end users who view the agreement.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Localized display name of the policy file of an agreement. The localized display name is shown to end users who view the agreement.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def file_data(self,) -> Optional[agreement_file_data.AgreementFileData]:
        """
        Gets the fileData property value. Data that represents the terms of use PDF document. Read-only.
        Returns: Optional[agreement_file_data.AgreementFileData]
        """
        return self._file_data
    
    @file_data.setter
    def file_data(self,value: Optional[agreement_file_data.AgreementFileData] = None) -> None:
        """
        Sets the fileData property value. Data that represents the terms of use PDF document. Read-only.
        Args:
            value: Value to set for the fileData property.
        """
        self._file_data = value
    
    @property
    def file_name(self,) -> Optional[str]:
        """
        Gets the fileName property value. Name of the agreement file (for example, TOU.pdf). Read-only.
        Returns: Optional[str]
        """
        return self._file_name
    
    @file_name.setter
    def file_name(self,value: Optional[str] = None) -> None:
        """
        Sets the fileName property value. Name of the agreement file (for example, TOU.pdf). Read-only.
        Args:
            value: Value to set for the fileName property.
        """
        self._file_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "file_data": lambda n : setattr(self, 'file_data', n.get_object_value(agreement_file_data.AgreementFileData)),
            "file_name": lambda n : setattr(self, 'file_name', n.get_str_value()),
            "is_default": lambda n : setattr(self, 'is_default', n.get_bool_value()),
            "is_major_version": lambda n : setattr(self, 'is_major_version', n.get_bool_value()),
            "language": lambda n : setattr(self, 'language', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_default(self,) -> Optional[bool]:
        """
        Gets the isDefault property value. If none of the languages matches the client preference, indicates whether this is the default agreement file . If none of the files are marked as default, the first one is treated as the default. Read-only.
        Returns: Optional[bool]
        """
        return self._is_default
    
    @is_default.setter
    def is_default(self,value: Optional[bool] = None) -> None:
        """
        Sets the isDefault property value. If none of the languages matches the client preference, indicates whether this is the default agreement file . If none of the files are marked as default, the first one is treated as the default. Read-only.
        Args:
            value: Value to set for the isDefault property.
        """
        self._is_default = value
    
    @property
    def is_major_version(self,) -> Optional[bool]:
        """
        Gets the isMajorVersion property value. Indicates whether the agreement file is a major version update. Major version updates invalidate the agreement's acceptances on the corresponding language.
        Returns: Optional[bool]
        """
        return self._is_major_version
    
    @is_major_version.setter
    def is_major_version(self,value: Optional[bool] = None) -> None:
        """
        Sets the isMajorVersion property value. Indicates whether the agreement file is a major version update. Major version updates invalidate the agreement's acceptances on the corresponding language.
        Args:
            value: Value to set for the isMajorVersion property.
        """
        self._is_major_version = value
    
    @property
    def language(self,) -> Optional[str]:
        """
        Gets the language property value. The language of the agreement file in the format 'languagecode2-country/regioncode2'. 'languagecode2' is a lowercase two-letter code derived from ISO 639-1, while 'country/regioncode2' is derived from ISO 3166 and usually consists of two uppercase letters, or a BCP-47 language tag. For example, U.S. English is en-US. Read-only.
        Returns: Optional[str]
        """
        return self._language
    
    @language.setter
    def language(self,value: Optional[str] = None) -> None:
        """
        Sets the language property value. The language of the agreement file in the format 'languagecode2-country/regioncode2'. 'languagecode2' is a lowercase two-letter code derived from ISO 639-1, while 'country/regioncode2' is derived from ISO 3166 and usually consists of two uppercase letters, or a BCP-47 language tag. For example, U.S. English is en-US. Read-only.
        Args:
            value: Value to set for the language property.
        """
        self._language = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("fileData", self.file_data)
        writer.write_str_value("fileName", self.file_name)
        writer.write_bool_value("isDefault", self.is_default)
        writer.write_bool_value("isMajorVersion", self.is_major_version)
        writer.write_str_value("language", self.language)
    

