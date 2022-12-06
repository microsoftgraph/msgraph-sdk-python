from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

data_source = lazy_import('msgraph.generated.models.security.data_source')
source_type = lazy_import('msgraph.generated.models.security.source_type')

class UserSource(data_source.DataSource):
    def __init__(self,) -> None:
        """
        Instantiates a new UserSource and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.security.userSource"
        # Email address of the user's mailbox.
        self._email: Optional[str] = None
        # Specifies which sources are included in this group. Possible values are: mailbox, site.
        self._included_sources: Optional[source_type.SourceType] = None
        # The URL of the user's OneDrive for Business site. Read-only.
        self._site_web_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserSource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserSource
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserSource()
    
    @property
    def email(self,) -> Optional[str]:
        """
        Gets the email property value. Email address of the user's mailbox.
        Returns: Optional[str]
        """
        return self._email
    
    @email.setter
    def email(self,value: Optional[str] = None) -> None:
        """
        Sets the email property value. Email address of the user's mailbox.
        Args:
            value: Value to set for the email property.
        """
        self._email = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "included_sources": lambda n : setattr(self, 'included_sources', n.get_enum_value(source_type.SourceType)),
            "site_web_url": lambda n : setattr(self, 'site_web_url', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def included_sources(self,) -> Optional[source_type.SourceType]:
        """
        Gets the includedSources property value. Specifies which sources are included in this group. Possible values are: mailbox, site.
        Returns: Optional[source_type.SourceType]
        """
        return self._included_sources
    
    @included_sources.setter
    def included_sources(self,value: Optional[source_type.SourceType] = None) -> None:
        """
        Sets the includedSources property value. Specifies which sources are included in this group. Possible values are: mailbox, site.
        Args:
            value: Value to set for the includedSources property.
        """
        self._included_sources = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("email", self.email)
        writer.write_enum_value("includedSources", self.included_sources)
        writer.write_str_value("siteWebUrl", self.site_web_url)
    
    @property
    def site_web_url(self,) -> Optional[str]:
        """
        Gets the siteWebUrl property value. The URL of the user's OneDrive for Business site. Read-only.
        Returns: Optional[str]
        """
        return self._site_web_url
    
    @site_web_url.setter
    def site_web_url(self,value: Optional[str] = None) -> None:
        """
        Sets the siteWebUrl property value. The URL of the user's OneDrive for Business site. Read-only.
        Args:
            value: Value to set for the siteWebUrl property.
        """
        self._site_web_url = value
    

