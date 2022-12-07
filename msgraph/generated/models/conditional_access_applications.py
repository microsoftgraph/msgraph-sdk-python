from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class ConditionalAccessApplications(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new conditionalAccessApplications and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Can be one of the following:  The list of client IDs (appId) explicitly excluded from the policy. Office365 - For the list of apps included in Office365, see Conditional Access target apps: Office 365
        self._exclude_applications: Optional[List[str]] = None
        # Can be one of the following:  The list of client IDs (appId) the policy applies to, unless explicitly excluded (in excludeApplications)  All  Office365 - For the list of apps included in Office365, see Conditional Access target apps: Office 365
        self._include_applications: Optional[List[str]] = None
        # The includeAuthenticationContextClassReferences property
        self._include_authentication_context_class_references: Optional[List[str]] = None
        # User actions to include. Supported values are urn:user:registersecurityinfo and urn:user:registerdevice
        self._include_user_actions: Optional[List[str]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ConditionalAccessApplications:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ConditionalAccessApplications
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ConditionalAccessApplications()
    
    @property
    def exclude_applications(self,) -> Optional[List[str]]:
        """
        Gets the excludeApplications property value. Can be one of the following:  The list of client IDs (appId) explicitly excluded from the policy. Office365 - For the list of apps included in Office365, see Conditional Access target apps: Office 365
        Returns: Optional[List[str]]
        """
        return self._exclude_applications
    
    @exclude_applications.setter
    def exclude_applications(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the excludeApplications property value. Can be one of the following:  The list of client IDs (appId) explicitly excluded from the policy. Office365 - For the list of apps included in Office365, see Conditional Access target apps: Office 365
        Args:
            value: Value to set for the excludeApplications property.
        """
        self._exclude_applications = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "exclude_applications": lambda n : setattr(self, 'exclude_applications', n.get_collection_of_primitive_values(str)),
            "include_applications": lambda n : setattr(self, 'include_applications', n.get_collection_of_primitive_values(str)),
            "include_authentication_context_class_references": lambda n : setattr(self, 'include_authentication_context_class_references', n.get_collection_of_primitive_values(str)),
            "include_user_actions": lambda n : setattr(self, 'include_user_actions', n.get_collection_of_primitive_values(str)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def include_applications(self,) -> Optional[List[str]]:
        """
        Gets the includeApplications property value. Can be one of the following:  The list of client IDs (appId) the policy applies to, unless explicitly excluded (in excludeApplications)  All  Office365 - For the list of apps included in Office365, see Conditional Access target apps: Office 365
        Returns: Optional[List[str]]
        """
        return self._include_applications
    
    @include_applications.setter
    def include_applications(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the includeApplications property value. Can be one of the following:  The list of client IDs (appId) the policy applies to, unless explicitly excluded (in excludeApplications)  All  Office365 - For the list of apps included in Office365, see Conditional Access target apps: Office 365
        Args:
            value: Value to set for the includeApplications property.
        """
        self._include_applications = value
    
    @property
    def include_authentication_context_class_references(self,) -> Optional[List[str]]:
        """
        Gets the includeAuthenticationContextClassReferences property value. The includeAuthenticationContextClassReferences property
        Returns: Optional[List[str]]
        """
        return self._include_authentication_context_class_references
    
    @include_authentication_context_class_references.setter
    def include_authentication_context_class_references(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the includeAuthenticationContextClassReferences property value. The includeAuthenticationContextClassReferences property
        Args:
            value: Value to set for the includeAuthenticationContextClassReferences property.
        """
        self._include_authentication_context_class_references = value
    
    @property
    def include_user_actions(self,) -> Optional[List[str]]:
        """
        Gets the includeUserActions property value. User actions to include. Supported values are urn:user:registersecurityinfo and urn:user:registerdevice
        Returns: Optional[List[str]]
        """
        return self._include_user_actions
    
    @include_user_actions.setter
    def include_user_actions(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the includeUserActions property value. User actions to include. Supported values are urn:user:registersecurityinfo and urn:user:registerdevice
        Args:
            value: Value to set for the includeUserActions property.
        """
        self._include_user_actions = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_primitive_values("excludeApplications", self.exclude_applications)
        writer.write_collection_of_primitive_values("includeApplications", self.include_applications)
        writer.write_collection_of_primitive_values("includeAuthenticationContextClassReferences", self.include_authentication_context_class_references)
        writer.write_collection_of_primitive_values("includeUserActions", self.include_user_actions)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

