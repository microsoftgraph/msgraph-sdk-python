from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

average_comparative_score = lazy_import('msgraph.generated.models.average_comparative_score')
control_score = lazy_import('msgraph.generated.models.control_score')
entity = lazy_import('msgraph.generated.models.entity')
security_vendor_information = lazy_import('msgraph.generated.models.security_vendor_information')

class SecureScore(entity.Entity):
    """
    Provides operations to manage the admin singleton.
    """
    @property
    def active_user_count(self,) -> Optional[int]:
        """
        Gets the activeUserCount property value. Active user count of the given tenant.
        Returns: Optional[int]
        """
        return self._active_user_count
    
    @active_user_count.setter
    def active_user_count(self,value: Optional[int] = None) -> None:
        """
        Sets the activeUserCount property value. Active user count of the given tenant.
        Args:
            value: Value to set for the activeUserCount property.
        """
        self._active_user_count = value
    
    @property
    def average_comparative_scores(self,) -> Optional[List[average_comparative_score.AverageComparativeScore]]:
        """
        Gets the averageComparativeScores property value. Average score by different scopes (for example, average by industry, average by seating) and control category (Identity, Data, Device, Apps, Infrastructure) within the scope.
        Returns: Optional[List[average_comparative_score.AverageComparativeScore]]
        """
        return self._average_comparative_scores
    
    @average_comparative_scores.setter
    def average_comparative_scores(self,value: Optional[List[average_comparative_score.AverageComparativeScore]] = None) -> None:
        """
        Sets the averageComparativeScores property value. Average score by different scopes (for example, average by industry, average by seating) and control category (Identity, Data, Device, Apps, Infrastructure) within the scope.
        Args:
            value: Value to set for the averageComparativeScores property.
        """
        self._average_comparative_scores = value
    
    @property
    def azure_tenant_id(self,) -> Optional[str]:
        """
        Gets the azureTenantId property value. GUID string for tenant ID.
        Returns: Optional[str]
        """
        return self._azure_tenant_id
    
    @azure_tenant_id.setter
    def azure_tenant_id(self,value: Optional[str] = None) -> None:
        """
        Sets the azureTenantId property value. GUID string for tenant ID.
        Args:
            value: Value to set for the azureTenantId property.
        """
        self._azure_tenant_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new secureScore and sets the default values.
        """
        super().__init__()
        # Active user count of the given tenant.
        self._active_user_count: Optional[int] = None
        # Average score by different scopes (for example, average by industry, average by seating) and control category (Identity, Data, Device, Apps, Infrastructure) within the scope.
        self._average_comparative_scores: Optional[List[average_comparative_score.AverageComparativeScore]] = None
        # GUID string for tenant ID.
        self._azure_tenant_id: Optional[str] = None
        # Contains tenant scores for a set of controls.
        self._control_scores: Optional[List[control_score.ControlScore]] = None
        # The date when the entity is created.
        self._created_date_time: Optional[datetime] = None
        # Tenant current attained score on specified date.
        self._current_score: Optional[float] = None
        # Microsoft-provided services for the tenant (for example, Exchange online, Skype, Sharepoint).
        self._enabled_services: Optional[List[str]] = None
        # Licensed user count of the given tenant.
        self._licensed_user_count: Optional[int] = None
        # Tenant maximum possible score on specified date.
        self._max_score: Optional[float] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Complex type containing details about the security product/service vendor, provider, and subprovider (for example, vendor=Microsoft; provider=SecureScore). Required.
        self._vendor_information: Optional[security_vendor_information.SecurityVendorInformation] = None
    
    @property
    def control_scores(self,) -> Optional[List[control_score.ControlScore]]:
        """
        Gets the controlScores property value. Contains tenant scores for a set of controls.
        Returns: Optional[List[control_score.ControlScore]]
        """
        return self._control_scores
    
    @control_scores.setter
    def control_scores(self,value: Optional[List[control_score.ControlScore]] = None) -> None:
        """
        Sets the controlScores property value. Contains tenant scores for a set of controls.
        Args:
            value: Value to set for the controlScores property.
        """
        self._control_scores = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The date when the entity is created.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The date when the entity is created.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SecureScore:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SecureScore
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SecureScore()
    
    @property
    def current_score(self,) -> Optional[float]:
        """
        Gets the currentScore property value. Tenant current attained score on specified date.
        Returns: Optional[float]
        """
        return self._current_score
    
    @current_score.setter
    def current_score(self,value: Optional[float] = None) -> None:
        """
        Sets the currentScore property value. Tenant current attained score on specified date.
        Args:
            value: Value to set for the currentScore property.
        """
        self._current_score = value
    
    @property
    def enabled_services(self,) -> Optional[List[str]]:
        """
        Gets the enabledServices property value. Microsoft-provided services for the tenant (for example, Exchange online, Skype, Sharepoint).
        Returns: Optional[List[str]]
        """
        return self._enabled_services
    
    @enabled_services.setter
    def enabled_services(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the enabledServices property value. Microsoft-provided services for the tenant (for example, Exchange online, Skype, Sharepoint).
        Args:
            value: Value to set for the enabledServices property.
        """
        self._enabled_services = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "active_user_count": lambda n : setattr(self, 'active_user_count', n.get_int_value()),
            "average_comparative_scores": lambda n : setattr(self, 'average_comparative_scores', n.get_collection_of_object_values(average_comparative_score.AverageComparativeScore)),
            "azure_tenant_id": lambda n : setattr(self, 'azure_tenant_id', n.get_str_value()),
            "control_scores": lambda n : setattr(self, 'control_scores', n.get_collection_of_object_values(control_score.ControlScore)),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "current_score": lambda n : setattr(self, 'current_score', n.get_float_value()),
            "enabled_services": lambda n : setattr(self, 'enabled_services', n.get_collection_of_primitive_values(str)),
            "licensed_user_count": lambda n : setattr(self, 'licensed_user_count', n.get_int_value()),
            "max_score": lambda n : setattr(self, 'max_score', n.get_float_value()),
            "vendor_information": lambda n : setattr(self, 'vendor_information', n.get_object_value(security_vendor_information.SecurityVendorInformation)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def licensed_user_count(self,) -> Optional[int]:
        """
        Gets the licensedUserCount property value. Licensed user count of the given tenant.
        Returns: Optional[int]
        """
        return self._licensed_user_count
    
    @licensed_user_count.setter
    def licensed_user_count(self,value: Optional[int] = None) -> None:
        """
        Sets the licensedUserCount property value. Licensed user count of the given tenant.
        Args:
            value: Value to set for the licensedUserCount property.
        """
        self._licensed_user_count = value
    
    @property
    def max_score(self,) -> Optional[float]:
        """
        Gets the maxScore property value. Tenant maximum possible score on specified date.
        Returns: Optional[float]
        """
        return self._max_score
    
    @max_score.setter
    def max_score(self,value: Optional[float] = None) -> None:
        """
        Sets the maxScore property value. Tenant maximum possible score on specified date.
        Args:
            value: Value to set for the maxScore property.
        """
        self._max_score = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("activeUserCount", self.active_user_count)
        writer.write_collection_of_object_values("averageComparativeScores", self.average_comparative_scores)
        writer.write_str_value("azureTenantId", self.azure_tenant_id)
        writer.write_collection_of_object_values("controlScores", self.control_scores)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_float_value("currentScore", self.current_score)
        writer.write_collection_of_primitive_values("enabledServices", self.enabled_services)
        writer.write_int_value("licensedUserCount", self.licensed_user_count)
        writer.write_float_value("maxScore", self.max_score)
        writer.write_object_value("vendorInformation", self.vendor_information)
    
    @property
    def vendor_information(self,) -> Optional[security_vendor_information.SecurityVendorInformation]:
        """
        Gets the vendorInformation property value. Complex type containing details about the security product/service vendor, provider, and subprovider (for example, vendor=Microsoft; provider=SecureScore). Required.
        Returns: Optional[security_vendor_information.SecurityVendorInformation]
        """
        return self._vendor_information
    
    @vendor_information.setter
    def vendor_information(self,value: Optional[security_vendor_information.SecurityVendorInformation] = None) -> None:
        """
        Sets the vendorInformation property value. Complex type containing details about the security product/service vendor, provider, and subprovider (for example, vendor=Microsoft; provider=SecureScore). Required.
        Args:
            value: Value to set for the vendorInformation property.
        """
        self._vendor_information = value
    

