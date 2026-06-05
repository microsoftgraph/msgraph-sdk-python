from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .application_risk_factors import ApplicationRiskFactors
    from .application_risk_score import ApplicationRiskScore
    from .entity import Entity

from .entity import Entity

@dataclass
class ApplicationTemplate(Entity, Parsable):
    # The list of categories for the application. Supported values can be: Collaboration, Business Management, Consumer, Content management, CRM, Data services, Developer services, E-commerce, Education, ERP, Finance, Health, Human resources, IT infrastructure, Mail, Management, Marketing, Media, Productivity, Project management, Telecommunications, Tools, Travel, and Web design & hosting.  Supports $filter (contains).
    categories: Optional[list[str]] = None
    # Deprecation date for this application. If specified, the application will be removed from the Microsoft Entra application gallery on this date.
    deprecation_date: Optional[datetime.date] = None
    # A description of the application.
    description: Optional[str] = None
    # The name of the application. Supports $filter (contains).
    display_name: Optional[str] = None
    # A collection of string URLs representing various domains that are used by this application.
    endpoints: Optional[list[str]] = None
    # The home page URL of the application.
    home_page_url: Optional[str] = None
    # Indicates whether the application is integrated with Entra ID (for example, through single sign-on or user provisioning).
    is_entra_integrated: Optional[bool] = None
    # The date and time when the data for the application was last updated, represented using ISO 8601 format and always in UTC time.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The URL to get the logo for this application.
    logo_url: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The name of the publisher for this application.
    publisher: Optional[str] = None
    # A comprehensive set of risk assessment data for the application, including general, security, compliance, and legal dimensions. Returned only when $select is used.
    risk_factors: Optional[ApplicationRiskFactors] = None
    # Represents the Microsoft-generated numerical risk score assessment for the application. Supported $orderby on total (for example, $orderby=riskScore/total desc). Returned only when $select is used.
    risk_score: Optional[ApplicationRiskScore] = None
    # The list of provisioning modes supported by this application. The only valid value is sync.
    supported_provisioning_types: Optional[list[str]] = None
    # The list of single sign-on modes supported by this application. The supported values are oidc, password, saml, and notSupported.
    supported_single_sign_on_modes: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ApplicationTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ApplicationTemplate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ApplicationTemplate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .application_risk_factors import ApplicationRiskFactors
        from .application_risk_score import ApplicationRiskScore
        from .entity import Entity

        from .application_risk_factors import ApplicationRiskFactors
        from .application_risk_score import ApplicationRiskScore
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "categories": lambda n : setattr(self, 'categories', n.get_collection_of_primitive_values(str)),
            "deprecationDate": lambda n : setattr(self, 'deprecation_date', n.get_date_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "endpoints": lambda n : setattr(self, 'endpoints', n.get_collection_of_primitive_values(str)),
            "homePageUrl": lambda n : setattr(self, 'home_page_url', n.get_str_value()),
            "isEntraIntegrated": lambda n : setattr(self, 'is_entra_integrated', n.get_bool_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "logoUrl": lambda n : setattr(self, 'logo_url', n.get_str_value()),
            "publisher": lambda n : setattr(self, 'publisher', n.get_str_value()),
            "riskFactors": lambda n : setattr(self, 'risk_factors', n.get_object_value(ApplicationRiskFactors)),
            "riskScore": lambda n : setattr(self, 'risk_score', n.get_object_value(ApplicationRiskScore)),
            "supportedProvisioningTypes": lambda n : setattr(self, 'supported_provisioning_types', n.get_collection_of_primitive_values(str)),
            "supportedSingleSignOnModes": lambda n : setattr(self, 'supported_single_sign_on_modes', n.get_collection_of_primitive_values(str)),
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
        writer.write_collection_of_primitive_values("categories", self.categories)
        writer.write_date_value("deprecationDate", self.deprecation_date)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_primitive_values("endpoints", self.endpoints)
        writer.write_str_value("homePageUrl", self.home_page_url)
        writer.write_bool_value("isEntraIntegrated", self.is_entra_integrated)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("logoUrl", self.logo_url)
        writer.write_str_value("publisher", self.publisher)
        writer.write_object_value("riskFactors", self.risk_factors)
        writer.write_object_value("riskScore", self.risk_score)
        writer.write_collection_of_primitive_values("supportedProvisioningTypes", self.supported_provisioning_types)
        writer.write_collection_of_primitive_values("supportedSingleSignOnModes", self.supported_single_sign_on_modes)
    

