from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

app_consent_request_scope = lazy_import('msgraph.generated.models.app_consent_request_scope')
entity = lazy_import('msgraph.generated.models.entity')
user_consent_request = lazy_import('msgraph.generated.models.user_consent_request')

class AppConsentRequest(entity.Entity):
    """
    Provides operations to manage the admin singleton.
    """
    @property
    def app_display_name(self,) -> Optional[str]:
        """
        Gets the appDisplayName property value. The display name of the app for which consent is requested. Required. Supports $filter (eq only) and $orderby.
        Returns: Optional[str]
        """
        return self._app_display_name
    
    @app_display_name.setter
    def app_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the appDisplayName property value. The display name of the app for which consent is requested. Required. Supports $filter (eq only) and $orderby.
        Args:
            value: Value to set for the appDisplayName property.
        """
        self._app_display_name = value
    
    @property
    def app_id(self,) -> Optional[str]:
        """
        Gets the appId property value. The identifier of the application. Required. Supports $filter (eq only) and $orderby.
        Returns: Optional[str]
        """
        return self._app_id
    
    @app_id.setter
    def app_id(self,value: Optional[str] = None) -> None:
        """
        Sets the appId property value. The identifier of the application. Required. Supports $filter (eq only) and $orderby.
        Args:
            value: Value to set for the appId property.
        """
        self._app_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new appConsentRequest and sets the default values.
        """
        super().__init__()
        # The display name of the app for which consent is requested. Required. Supports $filter (eq only) and $orderby.
        self._app_display_name: Optional[str] = None
        # The identifier of the application. Required. Supports $filter (eq only) and $orderby.
        self._app_id: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # A list of pending scopes waiting for approval. Required.
        self._pending_scopes: Optional[List[app_consent_request_scope.AppConsentRequestScope]] = None
        # A list of pending user consent requests. Supports $filter (eq).
        self._user_consent_requests: Optional[List[user_consent_request.UserConsentRequest]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AppConsentRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AppConsentRequest
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AppConsentRequest()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "app_display_name": lambda n : setattr(self, 'app_display_name', n.get_str_value()),
            "app_id": lambda n : setattr(self, 'app_id', n.get_str_value()),
            "pending_scopes": lambda n : setattr(self, 'pending_scopes', n.get_collection_of_object_values(app_consent_request_scope.AppConsentRequestScope)),
            "user_consent_requests": lambda n : setattr(self, 'user_consent_requests', n.get_collection_of_object_values(user_consent_request.UserConsentRequest)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def pending_scopes(self,) -> Optional[List[app_consent_request_scope.AppConsentRequestScope]]:
        """
        Gets the pendingScopes property value. A list of pending scopes waiting for approval. Required.
        Returns: Optional[List[app_consent_request_scope.AppConsentRequestScope]]
        """
        return self._pending_scopes
    
    @pending_scopes.setter
    def pending_scopes(self,value: Optional[List[app_consent_request_scope.AppConsentRequestScope]] = None) -> None:
        """
        Sets the pendingScopes property value. A list of pending scopes waiting for approval. Required.
        Args:
            value: Value to set for the pendingScopes property.
        """
        self._pending_scopes = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("appDisplayName", self.app_display_name)
        writer.write_str_value("appId", self.app_id)
        writer.write_collection_of_object_values("pendingScopes", self.pending_scopes)
        writer.write_collection_of_object_values("userConsentRequests", self.user_consent_requests)
    
    @property
    def user_consent_requests(self,) -> Optional[List[user_consent_request.UserConsentRequest]]:
        """
        Gets the userConsentRequests property value. A list of pending user consent requests. Supports $filter (eq).
        Returns: Optional[List[user_consent_request.UserConsentRequest]]
        """
        return self._user_consent_requests
    
    @user_consent_requests.setter
    def user_consent_requests(self,value: Optional[List[user_consent_request.UserConsentRequest]] = None) -> None:
        """
        Sets the userConsentRequests property value. A list of pending user consent requests. Supports $filter (eq).
        Args:
            value: Value to set for the userConsentRequests property.
        """
        self._user_consent_requests = value
    

