from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

conditional_access_applications = lazy_import('msgraph.generated.models.conditional_access_applications')
conditional_access_client_app = lazy_import('msgraph.generated.models.conditional_access_client_app')
conditional_access_client_applications = lazy_import('msgraph.generated.models.conditional_access_client_applications')
conditional_access_devices = lazy_import('msgraph.generated.models.conditional_access_devices')
conditional_access_locations = lazy_import('msgraph.generated.models.conditional_access_locations')
conditional_access_platforms = lazy_import('msgraph.generated.models.conditional_access_platforms')
conditional_access_users = lazy_import('msgraph.generated.models.conditional_access_users')
risk_level = lazy_import('msgraph.generated.models.risk_level')

class ConditionalAccessConditionSet(AdditionalDataHolder, Parsable):
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
    
    @property
    def applications(self,) -> Optional[conditional_access_applications.ConditionalAccessApplications]:
        """
        Gets the applications property value. Applications and user actions included in and excluded from the policy. Required.
        Returns: Optional[conditional_access_applications.ConditionalAccessApplications]
        """
        return self._applications
    
    @applications.setter
    def applications(self,value: Optional[conditional_access_applications.ConditionalAccessApplications] = None) -> None:
        """
        Sets the applications property value. Applications and user actions included in and excluded from the policy. Required.
        Args:
            value: Value to set for the applications property.
        """
        self._applications = value
    
    @property
    def client_applications(self,) -> Optional[conditional_access_client_applications.ConditionalAccessClientApplications]:
        """
        Gets the clientApplications property value. Client applications (service principals and workload identities) included in and excluded from the policy. Either users or clientApplications is required.
        Returns: Optional[conditional_access_client_applications.ConditionalAccessClientApplications]
        """
        return self._client_applications
    
    @client_applications.setter
    def client_applications(self,value: Optional[conditional_access_client_applications.ConditionalAccessClientApplications] = None) -> None:
        """
        Sets the clientApplications property value. Client applications (service principals and workload identities) included in and excluded from the policy. Either users or clientApplications is required.
        Args:
            value: Value to set for the clientApplications property.
        """
        self._client_applications = value
    
    @property
    def client_app_types(self,) -> Optional[List[conditional_access_client_app.ConditionalAccessClientApp]]:
        """
        Gets the clientAppTypes property value. Client application types included in the policy. Possible values are: all, browser, mobileAppsAndDesktopClients, exchangeActiveSync, easSupported, other. Required.
        Returns: Optional[List[conditional_access_client_app.ConditionalAccessClientApp]]
        """
        return self._client_app_types
    
    @client_app_types.setter
    def client_app_types(self,value: Optional[List[conditional_access_client_app.ConditionalAccessClientApp]] = None) -> None:
        """
        Sets the clientAppTypes property value. Client application types included in the policy. Possible values are: all, browser, mobileAppsAndDesktopClients, exchangeActiveSync, easSupported, other. Required.
        Args:
            value: Value to set for the clientAppTypes property.
        """
        self._client_app_types = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new conditionalAccessConditionSet and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Applications and user actions included in and excluded from the policy. Required.
        self._applications: Optional[conditional_access_applications.ConditionalAccessApplications] = None
        # Client applications (service principals and workload identities) included in and excluded from the policy. Either users or clientApplications is required.
        self._client_applications: Optional[conditional_access_client_applications.ConditionalAccessClientApplications] = None
        # Client application types included in the policy. Possible values are: all, browser, mobileAppsAndDesktopClients, exchangeActiveSync, easSupported, other. Required.
        self._client_app_types: Optional[List[conditional_access_client_app.ConditionalAccessClientApp]] = None
        # Devices in the policy.
        self._devices: Optional[conditional_access_devices.ConditionalAccessDevices] = None
        # Locations included in and excluded from the policy.
        self._locations: Optional[conditional_access_locations.ConditionalAccessLocations] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Platforms included in and excluded from the policy.
        self._platforms: Optional[conditional_access_platforms.ConditionalAccessPlatforms] = None
        # Service principal risk levels included in the policy. Possible values are: low, medium, high, none, unknownFutureValue.
        self._service_principal_risk_levels: Optional[List[risk_level.RiskLevel]] = None
        # Sign-in risk levels included in the policy. Possible values are: low, medium, high, hidden, none, unknownFutureValue. Required.
        self._sign_in_risk_levels: Optional[List[risk_level.RiskLevel]] = None
        # User risk levels included in the policy. Possible values are: low, medium, high, hidden, none, unknownFutureValue. Required.
        self._user_risk_levels: Optional[List[risk_level.RiskLevel]] = None
        # Users, groups, and roles included in and excluded from the policy. Either users or clientApplications is required.
        self._users: Optional[conditional_access_users.ConditionalAccessUsers] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ConditionalAccessConditionSet:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ConditionalAccessConditionSet
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ConditionalAccessConditionSet()
    
    @property
    def devices(self,) -> Optional[conditional_access_devices.ConditionalAccessDevices]:
        """
        Gets the devices property value. Devices in the policy.
        Returns: Optional[conditional_access_devices.ConditionalAccessDevices]
        """
        return self._devices
    
    @devices.setter
    def devices(self,value: Optional[conditional_access_devices.ConditionalAccessDevices] = None) -> None:
        """
        Sets the devices property value. Devices in the policy.
        Args:
            value: Value to set for the devices property.
        """
        self._devices = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "applications": lambda n : setattr(self, 'applications', n.get_object_value(conditional_access_applications.ConditionalAccessApplications)),
            "client_applications": lambda n : setattr(self, 'client_applications', n.get_object_value(conditional_access_client_applications.ConditionalAccessClientApplications)),
            "client_app_types": lambda n : setattr(self, 'client_app_types', n.get_collection_of_enum_values(conditional_access_client_app.ConditionalAccessClientApp)),
            "devices": lambda n : setattr(self, 'devices', n.get_object_value(conditional_access_devices.ConditionalAccessDevices)),
            "locations": lambda n : setattr(self, 'locations', n.get_object_value(conditional_access_locations.ConditionalAccessLocations)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "platforms": lambda n : setattr(self, 'platforms', n.get_object_value(conditional_access_platforms.ConditionalAccessPlatforms)),
            "service_principal_risk_levels": lambda n : setattr(self, 'service_principal_risk_levels', n.get_collection_of_enum_values(risk_level.RiskLevel)),
            "sign_in_risk_levels": lambda n : setattr(self, 'sign_in_risk_levels', n.get_collection_of_enum_values(risk_level.RiskLevel)),
            "user_risk_levels": lambda n : setattr(self, 'user_risk_levels', n.get_collection_of_enum_values(risk_level.RiskLevel)),
            "users": lambda n : setattr(self, 'users', n.get_object_value(conditional_access_users.ConditionalAccessUsers)),
        }
        return fields
    
    @property
    def locations(self,) -> Optional[conditional_access_locations.ConditionalAccessLocations]:
        """
        Gets the locations property value. Locations included in and excluded from the policy.
        Returns: Optional[conditional_access_locations.ConditionalAccessLocations]
        """
        return self._locations
    
    @locations.setter
    def locations(self,value: Optional[conditional_access_locations.ConditionalAccessLocations] = None) -> None:
        """
        Sets the locations property value. Locations included in and excluded from the policy.
        Args:
            value: Value to set for the locations property.
        """
        self._locations = value
    
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
    
    @property
    def platforms(self,) -> Optional[conditional_access_platforms.ConditionalAccessPlatforms]:
        """
        Gets the platforms property value. Platforms included in and excluded from the policy.
        Returns: Optional[conditional_access_platforms.ConditionalAccessPlatforms]
        """
        return self._platforms
    
    @platforms.setter
    def platforms(self,value: Optional[conditional_access_platforms.ConditionalAccessPlatforms] = None) -> None:
        """
        Sets the platforms property value. Platforms included in and excluded from the policy.
        Args:
            value: Value to set for the platforms property.
        """
        self._platforms = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("applications", self.applications)
        writer.write_object_value("clientApplications", self.client_applications)
        writer.write_enum_value("clientAppTypes", self.client_app_types)
        writer.write_object_value("devices", self.devices)
        writer.write_object_value("locations", self.locations)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("platforms", self.platforms)
        writer.write_enum_value("servicePrincipalRiskLevels", self.service_principal_risk_levels)
        writer.write_enum_value("signInRiskLevels", self.sign_in_risk_levels)
        writer.write_enum_value("userRiskLevels", self.user_risk_levels)
        writer.write_object_value("users", self.users)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def service_principal_risk_levels(self,) -> Optional[List[risk_level.RiskLevel]]:
        """
        Gets the servicePrincipalRiskLevels property value. Service principal risk levels included in the policy. Possible values are: low, medium, high, none, unknownFutureValue.
        Returns: Optional[List[risk_level.RiskLevel]]
        """
        return self._service_principal_risk_levels
    
    @service_principal_risk_levels.setter
    def service_principal_risk_levels(self,value: Optional[List[risk_level.RiskLevel]] = None) -> None:
        """
        Sets the servicePrincipalRiskLevels property value. Service principal risk levels included in the policy. Possible values are: low, medium, high, none, unknownFutureValue.
        Args:
            value: Value to set for the servicePrincipalRiskLevels property.
        """
        self._service_principal_risk_levels = value
    
    @property
    def sign_in_risk_levels(self,) -> Optional[List[risk_level.RiskLevel]]:
        """
        Gets the signInRiskLevels property value. Sign-in risk levels included in the policy. Possible values are: low, medium, high, hidden, none, unknownFutureValue. Required.
        Returns: Optional[List[risk_level.RiskLevel]]
        """
        return self._sign_in_risk_levels
    
    @sign_in_risk_levels.setter
    def sign_in_risk_levels(self,value: Optional[List[risk_level.RiskLevel]] = None) -> None:
        """
        Sets the signInRiskLevels property value. Sign-in risk levels included in the policy. Possible values are: low, medium, high, hidden, none, unknownFutureValue. Required.
        Args:
            value: Value to set for the signInRiskLevels property.
        """
        self._sign_in_risk_levels = value
    
    @property
    def user_risk_levels(self,) -> Optional[List[risk_level.RiskLevel]]:
        """
        Gets the userRiskLevels property value. User risk levels included in the policy. Possible values are: low, medium, high, hidden, none, unknownFutureValue. Required.
        Returns: Optional[List[risk_level.RiskLevel]]
        """
        return self._user_risk_levels
    
    @user_risk_levels.setter
    def user_risk_levels(self,value: Optional[List[risk_level.RiskLevel]] = None) -> None:
        """
        Sets the userRiskLevels property value. User risk levels included in the policy. Possible values are: low, medium, high, hidden, none, unknownFutureValue. Required.
        Args:
            value: Value to set for the userRiskLevels property.
        """
        self._user_risk_levels = value
    
    @property
    def users(self,) -> Optional[conditional_access_users.ConditionalAccessUsers]:
        """
        Gets the users property value. Users, groups, and roles included in and excluded from the policy. Either users or clientApplications is required.
        Returns: Optional[conditional_access_users.ConditionalAccessUsers]
        """
        return self._users
    
    @users.setter
    def users(self,value: Optional[conditional_access_users.ConditionalAccessUsers] = None) -> None:
        """
        Sets the users property value. Users, groups, and roles included in and excluded from the policy. Either users or clientApplications is required.
        Args:
            value: Value to set for the users property.
        """
        self._users = value
    

