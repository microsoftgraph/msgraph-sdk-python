from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import aad_user_conversation_member, access_package, access_package_assignment, access_package_assignment_policy, access_package_assignment_request, access_package_catalog, access_package_multiple_choice_question, access_package_question, access_package_subject, access_package_text_input_question, access_review_history_definition, access_review_history_instance, access_review_instance, access_review_instance_decision_item, access_review_reviewer, access_review_schedule_definition, access_review_set, access_review_stage, activity_based_timeout_policy, activity_history_item, add_large_gallery_view_operation, administrative_unit, admin_consent_request_policy, agreement, agreement_acceptance, agreement_file, agreement_file_localization, agreement_file_properties, agreement_file_version, alert, allowed_value, android_compliance_policy, android_custom_configuration, android_general_device_configuration, android_lob_app, android_managed_app_protection, android_managed_app_registration, android_store_app, android_work_profile_compliance_policy, android_work_profile_custom_configuration, android_work_profile_general_device_configuration, anonymous_guest_conversation_member, apple_device_features_configuration_base, apple_managed_identity_provider, apple_push_notification_certificate, application, application_template, approval, approval_stage, app_catalogs, app_consent_approval_route, app_consent_request, app_management_policy, app_role_assignment, app_scope, associated_team_info, attachment, attachment_base, attachment_session, attack_simulation_root, attendance_record, attribute_set, audio_routing_group, audit_event, audit_log_root, authentication, authentication_combination_configuration, authentication_context_class_reference, authentication_flows_policy, authentication_method, authentication_methods_policy, authentication_method_configuration, authentication_method_mode_detail, authentication_method_target, authentication_strength_policy, authentication_strength_root, authored_note, authorization_policy, azure_communication_services_user_conversation_member, b2x_identity_user_flow, base_item, base_item_version, bitlocker, bitlocker_recovery_key, booking_appointment, booking_business, booking_currency, booking_customer, booking_customer_base, booking_custom_question, booking_service, booking_staff_member, booking_staff_member_base, browser_shared_cookie, browser_site, browser_site_list, built_in_identity_provider, calendar, calendar_group, calendar_permission, calendar_sharing_message, call, cancel_media_processing_operation, certificate_based_auth_configuration, change_tracked_entity, channel, chat, chat_message, chat_message_hosted_content, chat_message_info, checklist_item, claims_mapping_policy, column_definition, column_link, comms_operation, compliance_management_partner, conditional_access_policy, conditional_access_root, conditional_access_template, connected_organization, contact, contact_folder, content_sharing_session, content_type, contract, conversation, conversation_member, conversation_thread, country_named_location, cross_tenant_access_policy, cross_tenant_access_policy_configuration_default, custom_security_attribute_definition, data_policy_operation, default_managed_app_protection, delegated_admin_access_assignment, delegated_admin_customer, delegated_admin_relationship, delegated_admin_relationship_operation, delegated_admin_relationship_request, delegated_admin_service_management_detail, delegated_permission_classification, deleted_team, detected_app, device, device_and_app_management_role_assignment, device_and_app_management_role_definition, device_app_management, device_category, device_compliance_action_item, device_compliance_device_overview, device_compliance_device_status, device_compliance_policy, device_compliance_policy_assignment, device_compliance_policy_device_state_summary, device_compliance_policy_setting_state_summary, device_compliance_policy_state, device_compliance_scheduled_action_for_rule, device_compliance_setting_state, device_compliance_user_overview, device_compliance_user_status, device_configuration, device_configuration_assignment, device_configuration_device_overview, device_configuration_device_state_summary, device_configuration_device_status, device_configuration_state, device_configuration_user_overview, device_configuration_user_status, device_enrollment_configuration, device_enrollment_limit_configuration, device_enrollment_platform_restrictions_configuration, device_enrollment_windows_hello_for_business_configuration, device_install_state, device_management, device_management_exchange_connector, device_management_export_job, device_management_partner, device_management_reports, device_management_troubleshooting_event, directory, directory_audit, directory_object, directory_object_partner_reference, directory_role, directory_role_template, document_set_version, domain, domain_dns_cname_record, domain_dns_mx_record, domain_dns_record, domain_dns_srv_record, domain_dns_txt_record, domain_dns_unavailable_record, drive, drive_item, drive_item_version, edge, edition_upgrade_configuration, education_assignment, education_assignment_defaults, education_assignment_resource, education_assignment_settings, education_category, education_class, education_feedback_outcome, education_feedback_resource_outcome, education_organization, education_outcome, education_points_outcome, education_rubric, education_rubric_outcome, education_school, education_submission, education_submission_resource, education_user, email_authentication_method, email_authentication_method_configuration, email_file_assessment_request, endpoint, enrollment_configuration_assignment, enrollment_troubleshooting_event, enterprise_code_signing_certificate, entitlement_management, entitlement_management_settings, event, event_message, event_message_request, event_message_response, extension, extension_property, external_domain_name, e_book_install_summary, feature_rollout_policy, federated_identity_credential, fido2_authentication_method, fido2_authentication_method_configuration, fido2_combination_configuration, field_value_set, file_assessment_request, file_attachment, group, group_lifecycle_policy, group_setting, group_setting_template, home_realm_discovery_policy, identity_api_connector, identity_built_in_user_flow_attribute, identity_container, identity_custom_user_flow_attribute, identity_provider, identity_provider_base, identity_security_defaults_enforcement_policy, identity_user_flow, identity_user_flow_attribute, identity_user_flow_attribute_assignment, imported_windows_autopilot_device_identity, imported_windows_autopilot_device_identity_upload, inference_classification, inference_classification_override, internal_domain_federation, internet_explorer_mode, invitation, invite_participants_operation, iosi_pad_o_s_web_clip, ios_certificate_profile, ios_compliance_policy, ios_custom_configuration, ios_device_features_configuration, ios_general_device_configuration, ios_lob_app, ios_lob_app_provisioning_configuration_assignment, ios_managed_app_protection, ios_managed_app_registration, ios_mobile_app_configuration, ios_store_app, ios_update_configuration, ios_update_device_status, ios_vpp_app, ios_vpp_e_book, ios_vpp_e_book_assignment, ip_named_location, item_activity, item_activity_stat, item_analytics, item_attachment, learning_content, learning_provider, license_details, linked_resource, list, list_item, list_item_version, localized_notification_message, long_running_operation, mac_o_s_compliance_policy, mac_o_s_custom_configuration, mac_o_s_device_features_configuration, mac_o_s_general_device_configuration, mac_o_s_lob_app, mac_o_s_microsoft_edge_app, mac_o_s_office_suite_app, mail_assessment_request, mail_folder, mail_search_folder, managed_android_lob_app, managed_android_store_app, managed_app, managed_app_configuration, managed_app_operation, managed_app_policy, managed_app_policy_deployment_summary, managed_app_protection, managed_app_registration, managed_app_status, managed_app_status_raw, managed_device, managed_device_mobile_app_configuration, managed_device_mobile_app_configuration_assignment, managed_device_mobile_app_configuration_device_status, managed_device_mobile_app_configuration_device_summary, managed_device_mobile_app_configuration_user_status, managed_device_mobile_app_configuration_user_summary, managed_device_overview, managed_e_book, managed_e_book_assignment, managed_i_o_s_lob_app, managed_i_o_s_store_app, managed_mobile_app, managed_mobile_lob_app, mdm_windows_information_protection_policy, meeting_attendance_report, message, message_rule, microsoft_account_user_conversation_member, microsoft_authenticator_authentication_method, microsoft_authenticator_authentication_method_configuration, microsoft_authenticator_authentication_method_target, microsoft_store_for_business_app, mobile_app, mobile_app_assignment, mobile_app_category, mobile_app_content, mobile_app_content_file, mobile_contained_app, mobile_lob_app, mobile_threat_defense_connector, multi_value_legacy_extended_property, mute_participant_operation, named_location, notebook, notification_message_template, offer_shift_request, office_graph_insights, onenote, onenote_entity_base_model, onenote_entity_hierarchy_model, onenote_entity_schema_object_model, onenote_operation, onenote_page, onenote_resource, onenote_section, online_meeting, on_premises_conditional_access_settings, on_premises_directory_synchronization, open_shift, open_shift_change_request, open_type_extension, operation, organization, organizational_branding, organizational_branding_localization, organizational_branding_properties, org_contact, outlook_category, outlook_item, outlook_user, o_auth2_permission_grant, participant, participant_joining_notification, participant_left_notification, password_authentication_method, permission, permission_grant_condition_set, permission_grant_policy, person, phone_authentication_method, pinned_chat_message_info, place, planner, planner_assigned_to_task_board_task_format, planner_bucket, planner_bucket_task_board_task_format, planner_group, planner_plan, planner_plan_details, planner_progress_task_board_task_format, planner_task, planner_task_details, planner_user, play_prompt_operation, policy_base, policy_root, post, presence, printer, printer_base, printer_create_operation, printer_share, print_connector, print_document, print_job, print_operation, print_service, print_service_endpoint, print_task, print_task_definition, print_task_trigger, print_usage, print_usage_by_printer, print_usage_by_user, profile_photo, provisioning_object_summary, rbac_application, record_operation, reference_attachment, remote_assistance_partner, request, resource_operation, resource_specific_permission_grant, rich_long_running_operation, risky_service_principal, risky_service_principal_history_item, risky_user, risky_user_history_item, risk_detection, role_assignment, role_definition, room, room_list, saml_or_ws_fed_external_domain_federation, saml_or_ws_fed_provider, schedule, schedule_change_request, scheduling_group, schema_extension, scoped_role_membership, search_entity, section_group, secure_score, secure_score_control_profile, security_reports_root, service_announcement, service_announcement_attachment, service_announcement_base, service_health, service_health_issue, service_principal, service_principal_risk_detection, service_update_message, setting_state_device_summary, shared_drive_item, shared_insight, shared_p_c_configuration, shared_with_channel_team_info, sharepoint, sharepoint_settings, shift, shift_preferences, sign_in, simulation, simulation_automation, simulation_automation_run, single_value_legacy_extended_property, site, skype_for_business_user_conversation_member, skype_user_conversation_member, sms_authentication_method_configuration, sms_authentication_method_target, social_identity_provider, software_oath_authentication_method, software_oath_authentication_method_configuration, software_update_status_summary, start_hold_music_operation, stop_hold_music_operation, sts_policy, subject_rights_request, subscribed_sku, subscribe_to_tone_operation, subscription, swap_shifts_change_request, targeted_managed_app_configuration, targeted_managed_app_policy_assignment, targeted_managed_app_protection, task_file_attachment, team, teams_app, teams_app_definition, teams_app_installation, teams_async_operation, teams_tab, teams_template, teamwork, teamwork_bot, teamwork_hosted_content, teamwork_tag, teamwork_tag_member, team_info, telecom_expense_management_partner, temporary_access_pass_authentication_method, temporary_access_pass_authentication_method_configuration, tenant_app_management_policy, terms_and_conditions, terms_and_conditions_acceptance_status, terms_and_conditions_assignment, terms_of_use_container, threat_assessment_request, threat_assessment_result, thumbnail_set, time_off, time_off_reason, time_off_request, todo, todo_task, todo_task_list, token_issuance_policy, token_lifetime_policy, trending, unified_rbac_resource_action, unified_rbac_resource_namespace, unified_role_assignment, unified_role_assignment_schedule, unified_role_assignment_schedule_instance, unified_role_assignment_schedule_request, unified_role_definition, unified_role_eligibility_schedule, unified_role_eligibility_schedule_instance, unified_role_eligibility_schedule_request, unified_role_management_policy, unified_role_management_policy_approval_rule, unified_role_management_policy_assignment, unified_role_management_policy_authentication_context_rule, unified_role_management_policy_enablement_rule, unified_role_management_policy_expiration_rule, unified_role_management_policy_notification_rule, unified_role_management_policy_rule, unified_role_schedule_base, unified_role_schedule_instance_base, unmute_participant_operation, update_recording_status_operation, url_assessment_request, used_insight, user, user_activity, user_consent_request, user_experience_analytics_device_performance, user_flow_language_configuration, user_flow_language_page, user_install_state_summary, user_scope_teams_app_installation, user_settings, user_teamwork, voice_authentication_method_configuration, vpp_token, web_app, win32_lob_app, windows10_compliance_policy, windows10_custom_configuration, windows10_endpoint_protection_configuration, windows10_enterprise_modern_app_management_configuration, windows10_general_configuration, windows10_mobile_compliance_policy, windows10_secure_assessment_configuration, windows10_team_general_configuration, windows81_compliance_policy, windows81_general_configuration, windows_app_x, windows_autopilot_device_identity, windows_defender_advanced_threat_protection_configuration, windows_hello_for_business_authentication_method, windows_information_protection, windows_information_protection_app_learning_summary, windows_information_protection_app_locker_file, windows_information_protection_network_learning_summary, windows_information_protection_policy, windows_microsoft_edge_app, windows_mobile_m_s_i, windows_phone81_compliance_policy, windows_phone81_custom_configuration, windows_phone81_general_configuration, windows_universal_app_x, windows_universal_app_x_contained_app, windows_update_for_business_configuration, windows_web_app, workbook, workbook_application, workbook_chart, workbook_chart_area_format, workbook_chart_axes, workbook_chart_axis, workbook_chart_axis_format, workbook_chart_axis_title, workbook_chart_axis_title_format, workbook_chart_data_labels, workbook_chart_data_label_format, workbook_chart_fill, workbook_chart_font, workbook_chart_gridlines, workbook_chart_gridlines_format, workbook_chart_legend, workbook_chart_legend_format, workbook_chart_line_format, workbook_chart_point, workbook_chart_point_format, workbook_chart_series, workbook_chart_series_format, workbook_chart_title, workbook_chart_title_format, workbook_comment, workbook_comment_reply, workbook_filter, workbook_format_protection, workbook_functions, workbook_function_result, workbook_named_item, workbook_operation, workbook_pivot_table, workbook_range, workbook_range_border, workbook_range_fill, workbook_range_font, workbook_range_format, workbook_range_sort, workbook_range_view, workbook_table, workbook_table_column, workbook_table_row, workbook_table_sort, workbook_worksheet, workbook_worksheet_protection, workforce_integration, x509_certificate_authentication_method_configuration
    from .call_records import call_record, segment, session
    from .external_connectors import connection_operation, external_connection, external_group, external_item, identity, schema
    from .security import alert, case, cases_root, case_operation, data_set, data_source, data_source_container, ediscovery_add_to_review_set_operation, ediscovery_case, ediscovery_case_settings, ediscovery_custodian, ediscovery_estimate_operation, ediscovery_hold_operation, ediscovery_index_operation, ediscovery_noncustodial_data_source, ediscovery_purge_data_operation, ediscovery_review_set, ediscovery_review_set_query, ediscovery_review_tag, ediscovery_search, ediscovery_tag_operation, incident, retention_event, retention_event_type, search, security, site_source, tag, triggers_root, trigger_types_root, unified_group_source, user_source
    from .term_store import group, relation, set, store, term

class Entity(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new entity and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The unique idenfier for an entity. Read-only.
        self._id: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Entity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Entity
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.aadUserConversationMember":
                from . import aad_user_conversation_member

                return aad_user_conversation_member.AadUserConversationMember()
            if mapping_value == "#microsoft.graph.accessPackage":
                from . import access_package

                return access_package.AccessPackage()
            if mapping_value == "#microsoft.graph.accessPackageAssignment":
                from . import access_package_assignment

                return access_package_assignment.AccessPackageAssignment()
            if mapping_value == "#microsoft.graph.accessPackageAssignmentPolicy":
                from . import access_package_assignment_policy

                return access_package_assignment_policy.AccessPackageAssignmentPolicy()
            if mapping_value == "#microsoft.graph.accessPackageAssignmentRequest":
                from . import access_package_assignment_request

                return access_package_assignment_request.AccessPackageAssignmentRequest()
            if mapping_value == "#microsoft.graph.accessPackageCatalog":
                from . import access_package_catalog

                return access_package_catalog.AccessPackageCatalog()
            if mapping_value == "#microsoft.graph.accessPackageMultipleChoiceQuestion":
                from . import access_package_multiple_choice_question

                return access_package_multiple_choice_question.AccessPackageMultipleChoiceQuestion()
            if mapping_value == "#microsoft.graph.accessPackageQuestion":
                from . import access_package_question

                return access_package_question.AccessPackageQuestion()
            if mapping_value == "#microsoft.graph.accessPackageSubject":
                from . import access_package_subject

                return access_package_subject.AccessPackageSubject()
            if mapping_value == "#microsoft.graph.accessPackageTextInputQuestion":
                from . import access_package_text_input_question

                return access_package_text_input_question.AccessPackageTextInputQuestion()
            if mapping_value == "#microsoft.graph.accessReviewHistoryDefinition":
                from . import access_review_history_definition

                return access_review_history_definition.AccessReviewHistoryDefinition()
            if mapping_value == "#microsoft.graph.accessReviewHistoryInstance":
                from . import access_review_history_instance

                return access_review_history_instance.AccessReviewHistoryInstance()
            if mapping_value == "#microsoft.graph.accessReviewInstance":
                from . import access_review_instance

                return access_review_instance.AccessReviewInstance()
            if mapping_value == "#microsoft.graph.accessReviewInstanceDecisionItem":
                from . import access_review_instance_decision_item

                return access_review_instance_decision_item.AccessReviewInstanceDecisionItem()
            if mapping_value == "#microsoft.graph.accessReviewReviewer":
                from . import access_review_reviewer

                return access_review_reviewer.AccessReviewReviewer()
            if mapping_value == "#microsoft.graph.accessReviewScheduleDefinition":
                from . import access_review_schedule_definition

                return access_review_schedule_definition.AccessReviewScheduleDefinition()
            if mapping_value == "#microsoft.graph.accessReviewSet":
                from . import access_review_set

                return access_review_set.AccessReviewSet()
            if mapping_value == "#microsoft.graph.accessReviewStage":
                from . import access_review_stage

                return access_review_stage.AccessReviewStage()
            if mapping_value == "#microsoft.graph.activityBasedTimeoutPolicy":
                from . import activity_based_timeout_policy

                return activity_based_timeout_policy.ActivityBasedTimeoutPolicy()
            if mapping_value == "#microsoft.graph.activityHistoryItem":
                from . import activity_history_item

                return activity_history_item.ActivityHistoryItem()
            if mapping_value == "#microsoft.graph.addLargeGalleryViewOperation":
                from . import add_large_gallery_view_operation

                return add_large_gallery_view_operation.AddLargeGalleryViewOperation()
            if mapping_value == "#microsoft.graph.adminConsentRequestPolicy":
                from . import admin_consent_request_policy

                return admin_consent_request_policy.AdminConsentRequestPolicy()
            if mapping_value == "#microsoft.graph.administrativeUnit":
                from . import administrative_unit

                return administrative_unit.AdministrativeUnit()
            if mapping_value == "#microsoft.graph.agreement":
                from . import agreement

                return agreement.Agreement()
            if mapping_value == "#microsoft.graph.agreementAcceptance":
                from . import agreement_acceptance

                return agreement_acceptance.AgreementAcceptance()
            if mapping_value == "#microsoft.graph.agreementFile":
                from . import agreement_file

                return agreement_file.AgreementFile()
            if mapping_value == "#microsoft.graph.agreementFileLocalization":
                from . import agreement_file_localization

                return agreement_file_localization.AgreementFileLocalization()
            if mapping_value == "#microsoft.graph.agreementFileProperties":
                from . import agreement_file_properties

                return agreement_file_properties.AgreementFileProperties()
            if mapping_value == "#microsoft.graph.agreementFileVersion":
                from . import agreement_file_version

                return agreement_file_version.AgreementFileVersion()
            if mapping_value == "#microsoft.graph.alert":
                from . import alert
                from .security import alert

                return alert.Alert()
            if mapping_value == "#microsoft.graph.allowedValue":
                from . import allowed_value

                return allowed_value.AllowedValue()
            if mapping_value == "#microsoft.graph.androidCompliancePolicy":
                from . import android_compliance_policy

                return android_compliance_policy.AndroidCompliancePolicy()
            if mapping_value == "#microsoft.graph.androidCustomConfiguration":
                from . import android_custom_configuration

                return android_custom_configuration.AndroidCustomConfiguration()
            if mapping_value == "#microsoft.graph.androidGeneralDeviceConfiguration":
                from . import android_general_device_configuration

                return android_general_device_configuration.AndroidGeneralDeviceConfiguration()
            if mapping_value == "#microsoft.graph.androidLobApp":
                from . import android_lob_app

                return android_lob_app.AndroidLobApp()
            if mapping_value == "#microsoft.graph.androidManagedAppProtection":
                from . import android_managed_app_protection

                return android_managed_app_protection.AndroidManagedAppProtection()
            if mapping_value == "#microsoft.graph.androidManagedAppRegistration":
                from . import android_managed_app_registration

                return android_managed_app_registration.AndroidManagedAppRegistration()
            if mapping_value == "#microsoft.graph.androidStoreApp":
                from . import android_store_app

                return android_store_app.AndroidStoreApp()
            if mapping_value == "#microsoft.graph.androidWorkProfileCompliancePolicy":
                from . import android_work_profile_compliance_policy

                return android_work_profile_compliance_policy.AndroidWorkProfileCompliancePolicy()
            if mapping_value == "#microsoft.graph.androidWorkProfileCustomConfiguration":
                from . import android_work_profile_custom_configuration

                return android_work_profile_custom_configuration.AndroidWorkProfileCustomConfiguration()
            if mapping_value == "#microsoft.graph.androidWorkProfileGeneralDeviceConfiguration":
                from . import android_work_profile_general_device_configuration

                return android_work_profile_general_device_configuration.AndroidWorkProfileGeneralDeviceConfiguration()
            if mapping_value == "#microsoft.graph.anonymousGuestConversationMember":
                from . import anonymous_guest_conversation_member

                return anonymous_guest_conversation_member.AnonymousGuestConversationMember()
            if mapping_value == "#microsoft.graph.appCatalogs":
                from . import app_catalogs

                return app_catalogs.AppCatalogs()
            if mapping_value == "#microsoft.graph.appConsentApprovalRoute":
                from . import app_consent_approval_route

                return app_consent_approval_route.AppConsentApprovalRoute()
            if mapping_value == "#microsoft.graph.appConsentRequest":
                from . import app_consent_request

                return app_consent_request.AppConsentRequest()
            if mapping_value == "#microsoft.graph.appleDeviceFeaturesConfigurationBase":
                from . import apple_device_features_configuration_base

                return apple_device_features_configuration_base.AppleDeviceFeaturesConfigurationBase()
            if mapping_value == "#microsoft.graph.appleManagedIdentityProvider":
                from . import apple_managed_identity_provider

                return apple_managed_identity_provider.AppleManagedIdentityProvider()
            if mapping_value == "#microsoft.graph.applePushNotificationCertificate":
                from . import apple_push_notification_certificate

                return apple_push_notification_certificate.ApplePushNotificationCertificate()
            if mapping_value == "#microsoft.graph.application":
                from . import application

                return application.Application()
            if mapping_value == "#microsoft.graph.applicationTemplate":
                from . import application_template

                return application_template.ApplicationTemplate()
            if mapping_value == "#microsoft.graph.appManagementPolicy":
                from . import app_management_policy

                return app_management_policy.AppManagementPolicy()
            if mapping_value == "#microsoft.graph.appRoleAssignment":
                from . import app_role_assignment

                return app_role_assignment.AppRoleAssignment()
            if mapping_value == "#microsoft.graph.approval":
                from . import approval

                return approval.Approval()
            if mapping_value == "#microsoft.graph.approvalStage":
                from . import approval_stage

                return approval_stage.ApprovalStage()
            if mapping_value == "#microsoft.graph.appScope":
                from . import app_scope

                return app_scope.AppScope()
            if mapping_value == "#microsoft.graph.associatedTeamInfo":
                from . import associated_team_info

                return associated_team_info.AssociatedTeamInfo()
            if mapping_value == "#microsoft.graph.attachment":
                from . import attachment

                return attachment.Attachment()
            if mapping_value == "#microsoft.graph.attachmentBase":
                from . import attachment_base

                return attachment_base.AttachmentBase()
            if mapping_value == "#microsoft.graph.attachmentSession":
                from . import attachment_session

                return attachment_session.AttachmentSession()
            if mapping_value == "#microsoft.graph.attackSimulationRoot":
                from . import attack_simulation_root

                return attack_simulation_root.AttackSimulationRoot()
            if mapping_value == "#microsoft.graph.attendanceRecord":
                from . import attendance_record

                return attendance_record.AttendanceRecord()
            if mapping_value == "#microsoft.graph.attributeSet":
                from . import attribute_set

                return attribute_set.AttributeSet()
            if mapping_value == "#microsoft.graph.audioRoutingGroup":
                from . import audio_routing_group

                return audio_routing_group.AudioRoutingGroup()
            if mapping_value == "#microsoft.graph.auditEvent":
                from . import audit_event

                return audit_event.AuditEvent()
            if mapping_value == "#microsoft.graph.auditLogRoot":
                from . import audit_log_root

                return audit_log_root.AuditLogRoot()
            if mapping_value == "#microsoft.graph.authentication":
                from . import authentication

                return authentication.Authentication()
            if mapping_value == "#microsoft.graph.authenticationCombinationConfiguration":
                from . import authentication_combination_configuration

                return authentication_combination_configuration.AuthenticationCombinationConfiguration()
            if mapping_value == "#microsoft.graph.authenticationContextClassReference":
                from . import authentication_context_class_reference

                return authentication_context_class_reference.AuthenticationContextClassReference()
            if mapping_value == "#microsoft.graph.authenticationFlowsPolicy":
                from . import authentication_flows_policy

                return authentication_flows_policy.AuthenticationFlowsPolicy()
            if mapping_value == "#microsoft.graph.authenticationMethod":
                from . import authentication_method

                return authentication_method.AuthenticationMethod()
            if mapping_value == "#microsoft.graph.authenticationMethodConfiguration":
                from . import authentication_method_configuration

                return authentication_method_configuration.AuthenticationMethodConfiguration()
            if mapping_value == "#microsoft.graph.authenticationMethodModeDetail":
                from . import authentication_method_mode_detail

                return authentication_method_mode_detail.AuthenticationMethodModeDetail()
            if mapping_value == "#microsoft.graph.authenticationMethodsPolicy":
                from . import authentication_methods_policy

                return authentication_methods_policy.AuthenticationMethodsPolicy()
            if mapping_value == "#microsoft.graph.authenticationMethodTarget":
                from . import authentication_method_target

                return authentication_method_target.AuthenticationMethodTarget()
            if mapping_value == "#microsoft.graph.authenticationStrengthPolicy":
                from . import authentication_strength_policy

                return authentication_strength_policy.AuthenticationStrengthPolicy()
            if mapping_value == "#microsoft.graph.authenticationStrengthRoot":
                from . import authentication_strength_root

                return authentication_strength_root.AuthenticationStrengthRoot()
            if mapping_value == "#microsoft.graph.authoredNote":
                from . import authored_note

                return authored_note.AuthoredNote()
            if mapping_value == "#microsoft.graph.authorizationPolicy":
                from . import authorization_policy

                return authorization_policy.AuthorizationPolicy()
            if mapping_value == "#microsoft.graph.azureCommunicationServicesUserConversationMember":
                from . import azure_communication_services_user_conversation_member

                return azure_communication_services_user_conversation_member.AzureCommunicationServicesUserConversationMember()
            if mapping_value == "#microsoft.graph.b2xIdentityUserFlow":
                from . import b2x_identity_user_flow

                return b2x_identity_user_flow.B2xIdentityUserFlow()
            if mapping_value == "#microsoft.graph.baseItem":
                from . import base_item

                return base_item.BaseItem()
            if mapping_value == "#microsoft.graph.baseItemVersion":
                from . import base_item_version

                return base_item_version.BaseItemVersion()
            if mapping_value == "#microsoft.graph.bitlocker":
                from . import bitlocker

                return bitlocker.Bitlocker()
            if mapping_value == "#microsoft.graph.bitlockerRecoveryKey":
                from . import bitlocker_recovery_key

                return bitlocker_recovery_key.BitlockerRecoveryKey()
            if mapping_value == "#microsoft.graph.bookingAppointment":
                from . import booking_appointment

                return booking_appointment.BookingAppointment()
            if mapping_value == "#microsoft.graph.bookingBusiness":
                from . import booking_business

                return booking_business.BookingBusiness()
            if mapping_value == "#microsoft.graph.bookingCurrency":
                from . import booking_currency

                return booking_currency.BookingCurrency()
            if mapping_value == "#microsoft.graph.bookingCustomer":
                from . import booking_customer

                return booking_customer.BookingCustomer()
            if mapping_value == "#microsoft.graph.bookingCustomerBase":
                from . import booking_customer_base

                return booking_customer_base.BookingCustomerBase()
            if mapping_value == "#microsoft.graph.bookingCustomQuestion":
                from . import booking_custom_question

                return booking_custom_question.BookingCustomQuestion()
            if mapping_value == "#microsoft.graph.bookingService":
                from . import booking_service

                return booking_service.BookingService()
            if mapping_value == "#microsoft.graph.bookingStaffMember":
                from . import booking_staff_member

                return booking_staff_member.BookingStaffMember()
            if mapping_value == "#microsoft.graph.bookingStaffMemberBase":
                from . import booking_staff_member_base

                return booking_staff_member_base.BookingStaffMemberBase()
            if mapping_value == "#microsoft.graph.browserSharedCookie":
                from . import browser_shared_cookie

                return browser_shared_cookie.BrowserSharedCookie()
            if mapping_value == "#microsoft.graph.browserSite":
                from . import browser_site

                return browser_site.BrowserSite()
            if mapping_value == "#microsoft.graph.browserSiteList":
                from . import browser_site_list

                return browser_site_list.BrowserSiteList()
            if mapping_value == "#microsoft.graph.builtInIdentityProvider":
                from . import built_in_identity_provider

                return built_in_identity_provider.BuiltInIdentityProvider()
            if mapping_value == "#microsoft.graph.calendar":
                from . import calendar

                return calendar.Calendar()
            if mapping_value == "#microsoft.graph.calendarGroup":
                from . import calendar_group

                return calendar_group.CalendarGroup()
            if mapping_value == "#microsoft.graph.calendarPermission":
                from . import calendar_permission

                return calendar_permission.CalendarPermission()
            if mapping_value == "#microsoft.graph.calendarSharingMessage":
                from . import calendar_sharing_message

                return calendar_sharing_message.CalendarSharingMessage()
            if mapping_value == "#microsoft.graph.call":
                from . import call

                return call.Call()
            if mapping_value == "#microsoft.graph.callRecords.callRecord":
                from .call_records import call_record

                return call_record.CallRecord()
            if mapping_value == "#microsoft.graph.callRecords.segment":
                from .call_records import segment

                return segment.Segment()
            if mapping_value == "#microsoft.graph.callRecords.session":
                from .call_records import session

                return session.Session()
            if mapping_value == "#microsoft.graph.cancelMediaProcessingOperation":
                from . import cancel_media_processing_operation

                return cancel_media_processing_operation.CancelMediaProcessingOperation()
            if mapping_value == "#microsoft.graph.certificateBasedAuthConfiguration":
                from . import certificate_based_auth_configuration

                return certificate_based_auth_configuration.CertificateBasedAuthConfiguration()
            if mapping_value == "#microsoft.graph.changeTrackedEntity":
                from . import change_tracked_entity

                return change_tracked_entity.ChangeTrackedEntity()
            if mapping_value == "#microsoft.graph.channel":
                from . import channel

                return channel.Channel()
            if mapping_value == "#microsoft.graph.chat":
                from . import chat

                return chat.Chat()
            if mapping_value == "#microsoft.graph.chatMessage":
                from . import chat_message

                return chat_message.ChatMessage()
            if mapping_value == "#microsoft.graph.chatMessageHostedContent":
                from . import chat_message_hosted_content

                return chat_message_hosted_content.ChatMessageHostedContent()
            if mapping_value == "#microsoft.graph.chatMessageInfo":
                from . import chat_message_info

                return chat_message_info.ChatMessageInfo()
            if mapping_value == "#microsoft.graph.checklistItem":
                from . import checklist_item

                return checklist_item.ChecklistItem()
            if mapping_value == "#microsoft.graph.claimsMappingPolicy":
                from . import claims_mapping_policy

                return claims_mapping_policy.ClaimsMappingPolicy()
            if mapping_value == "#microsoft.graph.columnDefinition":
                from . import column_definition

                return column_definition.ColumnDefinition()
            if mapping_value == "#microsoft.graph.columnLink":
                from . import column_link

                return column_link.ColumnLink()
            if mapping_value == "#microsoft.graph.commsOperation":
                from . import comms_operation

                return comms_operation.CommsOperation()
            if mapping_value == "#microsoft.graph.complianceManagementPartner":
                from . import compliance_management_partner

                return compliance_management_partner.ComplianceManagementPartner()
            if mapping_value == "#microsoft.graph.conditionalAccessPolicy":
                from . import conditional_access_policy

                return conditional_access_policy.ConditionalAccessPolicy()
            if mapping_value == "#microsoft.graph.conditionalAccessRoot":
                from . import conditional_access_root

                return conditional_access_root.ConditionalAccessRoot()
            if mapping_value == "#microsoft.graph.conditionalAccessTemplate":
                from . import conditional_access_template

                return conditional_access_template.ConditionalAccessTemplate()
            if mapping_value == "#microsoft.graph.connectedOrganization":
                from . import connected_organization

                return connected_organization.ConnectedOrganization()
            if mapping_value == "#microsoft.graph.contact":
                from . import contact

                return contact.Contact()
            if mapping_value == "#microsoft.graph.contactFolder":
                from . import contact_folder

                return contact_folder.ContactFolder()
            if mapping_value == "#microsoft.graph.contentSharingSession":
                from . import content_sharing_session

                return content_sharing_session.ContentSharingSession()
            if mapping_value == "#microsoft.graph.contentType":
                from . import content_type

                return content_type.ContentType()
            if mapping_value == "#microsoft.graph.contract":
                from . import contract

                return contract.Contract()
            if mapping_value == "#microsoft.graph.conversation":
                from . import conversation

                return conversation.Conversation()
            if mapping_value == "#microsoft.graph.conversationMember":
                from . import conversation_member

                return conversation_member.ConversationMember()
            if mapping_value == "#microsoft.graph.conversationThread":
                from . import conversation_thread

                return conversation_thread.ConversationThread()
            if mapping_value == "#microsoft.graph.countryNamedLocation":
                from . import country_named_location

                return country_named_location.CountryNamedLocation()
            if mapping_value == "#microsoft.graph.crossTenantAccessPolicy":
                from . import cross_tenant_access_policy

                return cross_tenant_access_policy.CrossTenantAccessPolicy()
            if mapping_value == "#microsoft.graph.crossTenantAccessPolicyConfigurationDefault":
                from . import cross_tenant_access_policy_configuration_default

                return cross_tenant_access_policy_configuration_default.CrossTenantAccessPolicyConfigurationDefault()
            if mapping_value == "#microsoft.graph.customSecurityAttributeDefinition":
                from . import custom_security_attribute_definition

                return custom_security_attribute_definition.CustomSecurityAttributeDefinition()
            if mapping_value == "#microsoft.graph.dataPolicyOperation":
                from . import data_policy_operation

                return data_policy_operation.DataPolicyOperation()
            if mapping_value == "#microsoft.graph.defaultManagedAppProtection":
                from . import default_managed_app_protection

                return default_managed_app_protection.DefaultManagedAppProtection()
            if mapping_value == "#microsoft.graph.delegatedAdminAccessAssignment":
                from . import delegated_admin_access_assignment

                return delegated_admin_access_assignment.DelegatedAdminAccessAssignment()
            if mapping_value == "#microsoft.graph.delegatedAdminCustomer":
                from . import delegated_admin_customer

                return delegated_admin_customer.DelegatedAdminCustomer()
            if mapping_value == "#microsoft.graph.delegatedAdminRelationship":
                from . import delegated_admin_relationship

                return delegated_admin_relationship.DelegatedAdminRelationship()
            if mapping_value == "#microsoft.graph.delegatedAdminRelationshipOperation":
                from . import delegated_admin_relationship_operation

                return delegated_admin_relationship_operation.DelegatedAdminRelationshipOperation()
            if mapping_value == "#microsoft.graph.delegatedAdminRelationshipRequest":
                from . import delegated_admin_relationship_request

                return delegated_admin_relationship_request.DelegatedAdminRelationshipRequest()
            if mapping_value == "#microsoft.graph.delegatedAdminServiceManagementDetail":
                from . import delegated_admin_service_management_detail

                return delegated_admin_service_management_detail.DelegatedAdminServiceManagementDetail()
            if mapping_value == "#microsoft.graph.delegatedPermissionClassification":
                from . import delegated_permission_classification

                return delegated_permission_classification.DelegatedPermissionClassification()
            if mapping_value == "#microsoft.graph.deletedTeam":
                from . import deleted_team

                return deleted_team.DeletedTeam()
            if mapping_value == "#microsoft.graph.detectedApp":
                from . import detected_app

                return detected_app.DetectedApp()
            if mapping_value == "#microsoft.graph.device":
                from . import device

                return device.Device()
            if mapping_value == "#microsoft.graph.deviceAndAppManagementRoleAssignment":
                from . import device_and_app_management_role_assignment

                return device_and_app_management_role_assignment.DeviceAndAppManagementRoleAssignment()
            if mapping_value == "#microsoft.graph.deviceAndAppManagementRoleDefinition":
                from . import device_and_app_management_role_definition

                return device_and_app_management_role_definition.DeviceAndAppManagementRoleDefinition()
            if mapping_value == "#microsoft.graph.deviceAppManagement":
                from . import device_app_management

                return device_app_management.DeviceAppManagement()
            if mapping_value == "#microsoft.graph.deviceCategory":
                from . import device_category

                return device_category.DeviceCategory()
            if mapping_value == "#microsoft.graph.deviceComplianceActionItem":
                from . import device_compliance_action_item

                return device_compliance_action_item.DeviceComplianceActionItem()
            if mapping_value == "#microsoft.graph.deviceComplianceDeviceOverview":
                from . import device_compliance_device_overview

                return device_compliance_device_overview.DeviceComplianceDeviceOverview()
            if mapping_value == "#microsoft.graph.deviceComplianceDeviceStatus":
                from . import device_compliance_device_status

                return device_compliance_device_status.DeviceComplianceDeviceStatus()
            if mapping_value == "#microsoft.graph.deviceCompliancePolicy":
                from . import device_compliance_policy

                return device_compliance_policy.DeviceCompliancePolicy()
            if mapping_value == "#microsoft.graph.deviceCompliancePolicyAssignment":
                from . import device_compliance_policy_assignment

                return device_compliance_policy_assignment.DeviceCompliancePolicyAssignment()
            if mapping_value == "#microsoft.graph.deviceCompliancePolicyDeviceStateSummary":
                from . import device_compliance_policy_device_state_summary

                return device_compliance_policy_device_state_summary.DeviceCompliancePolicyDeviceStateSummary()
            if mapping_value == "#microsoft.graph.deviceCompliancePolicySettingStateSummary":
                from . import device_compliance_policy_setting_state_summary

                return device_compliance_policy_setting_state_summary.DeviceCompliancePolicySettingStateSummary()
            if mapping_value == "#microsoft.graph.deviceCompliancePolicyState":
                from . import device_compliance_policy_state

                return device_compliance_policy_state.DeviceCompliancePolicyState()
            if mapping_value == "#microsoft.graph.deviceComplianceScheduledActionForRule":
                from . import device_compliance_scheduled_action_for_rule

                return device_compliance_scheduled_action_for_rule.DeviceComplianceScheduledActionForRule()
            if mapping_value == "#microsoft.graph.deviceComplianceSettingState":
                from . import device_compliance_setting_state

                return device_compliance_setting_state.DeviceComplianceSettingState()
            if mapping_value == "#microsoft.graph.deviceComplianceUserOverview":
                from . import device_compliance_user_overview

                return device_compliance_user_overview.DeviceComplianceUserOverview()
            if mapping_value == "#microsoft.graph.deviceComplianceUserStatus":
                from . import device_compliance_user_status

                return device_compliance_user_status.DeviceComplianceUserStatus()
            if mapping_value == "#microsoft.graph.deviceConfiguration":
                from . import device_configuration

                return device_configuration.DeviceConfiguration()
            if mapping_value == "#microsoft.graph.deviceConfigurationAssignment":
                from . import device_configuration_assignment

                return device_configuration_assignment.DeviceConfigurationAssignment()
            if mapping_value == "#microsoft.graph.deviceConfigurationDeviceOverview":
                from . import device_configuration_device_overview

                return device_configuration_device_overview.DeviceConfigurationDeviceOverview()
            if mapping_value == "#microsoft.graph.deviceConfigurationDeviceStateSummary":
                from . import device_configuration_device_state_summary

                return device_configuration_device_state_summary.DeviceConfigurationDeviceStateSummary()
            if mapping_value == "#microsoft.graph.deviceConfigurationDeviceStatus":
                from . import device_configuration_device_status

                return device_configuration_device_status.DeviceConfigurationDeviceStatus()
            if mapping_value == "#microsoft.graph.deviceConfigurationState":
                from . import device_configuration_state

                return device_configuration_state.DeviceConfigurationState()
            if mapping_value == "#microsoft.graph.deviceConfigurationUserOverview":
                from . import device_configuration_user_overview

                return device_configuration_user_overview.DeviceConfigurationUserOverview()
            if mapping_value == "#microsoft.graph.deviceConfigurationUserStatus":
                from . import device_configuration_user_status

                return device_configuration_user_status.DeviceConfigurationUserStatus()
            if mapping_value == "#microsoft.graph.deviceEnrollmentConfiguration":
                from . import device_enrollment_configuration

                return device_enrollment_configuration.DeviceEnrollmentConfiguration()
            if mapping_value == "#microsoft.graph.deviceEnrollmentLimitConfiguration":
                from . import device_enrollment_limit_configuration

                return device_enrollment_limit_configuration.DeviceEnrollmentLimitConfiguration()
            if mapping_value == "#microsoft.graph.deviceEnrollmentPlatformRestrictionsConfiguration":
                from . import device_enrollment_platform_restrictions_configuration

                return device_enrollment_platform_restrictions_configuration.DeviceEnrollmentPlatformRestrictionsConfiguration()
            if mapping_value == "#microsoft.graph.deviceEnrollmentWindowsHelloForBusinessConfiguration":
                from . import device_enrollment_windows_hello_for_business_configuration

                return device_enrollment_windows_hello_for_business_configuration.DeviceEnrollmentWindowsHelloForBusinessConfiguration()
            if mapping_value == "#microsoft.graph.deviceInstallState":
                from . import device_install_state

                return device_install_state.DeviceInstallState()
            if mapping_value == "#microsoft.graph.deviceManagement":
                from . import device_management

                return device_management.DeviceManagement()
            if mapping_value == "#microsoft.graph.deviceManagementExchangeConnector":
                from . import device_management_exchange_connector

                return device_management_exchange_connector.DeviceManagementExchangeConnector()
            if mapping_value == "#microsoft.graph.deviceManagementExportJob":
                from . import device_management_export_job

                return device_management_export_job.DeviceManagementExportJob()
            if mapping_value == "#microsoft.graph.deviceManagementPartner":
                from . import device_management_partner

                return device_management_partner.DeviceManagementPartner()
            if mapping_value == "#microsoft.graph.deviceManagementReports":
                from . import device_management_reports

                return device_management_reports.DeviceManagementReports()
            if mapping_value == "#microsoft.graph.deviceManagementTroubleshootingEvent":
                from . import device_management_troubleshooting_event

                return device_management_troubleshooting_event.DeviceManagementTroubleshootingEvent()
            if mapping_value == "#microsoft.graph.directory":
                from . import directory

                return directory.Directory()
            if mapping_value == "#microsoft.graph.directoryAudit":
                from . import directory_audit

                return directory_audit.DirectoryAudit()
            if mapping_value == "#microsoft.graph.directoryObject":
                from . import directory_object

                return directory_object.DirectoryObject()
            if mapping_value == "#microsoft.graph.directoryObjectPartnerReference":
                from . import directory_object_partner_reference

                return directory_object_partner_reference.DirectoryObjectPartnerReference()
            if mapping_value == "#microsoft.graph.directoryRole":
                from . import directory_role

                return directory_role.DirectoryRole()
            if mapping_value == "#microsoft.graph.directoryRoleTemplate":
                from . import directory_role_template

                return directory_role_template.DirectoryRoleTemplate()
            if mapping_value == "#microsoft.graph.documentSetVersion":
                from . import document_set_version

                return document_set_version.DocumentSetVersion()
            if mapping_value == "#microsoft.graph.domain":
                from . import domain

                return domain.Domain()
            if mapping_value == "#microsoft.graph.domainDnsCnameRecord":
                from . import domain_dns_cname_record

                return domain_dns_cname_record.DomainDnsCnameRecord()
            if mapping_value == "#microsoft.graph.domainDnsMxRecord":
                from . import domain_dns_mx_record

                return domain_dns_mx_record.DomainDnsMxRecord()
            if mapping_value == "#microsoft.graph.domainDnsRecord":
                from . import domain_dns_record

                return domain_dns_record.DomainDnsRecord()
            if mapping_value == "#microsoft.graph.domainDnsSrvRecord":
                from . import domain_dns_srv_record

                return domain_dns_srv_record.DomainDnsSrvRecord()
            if mapping_value == "#microsoft.graph.domainDnsTxtRecord":
                from . import domain_dns_txt_record

                return domain_dns_txt_record.DomainDnsTxtRecord()
            if mapping_value == "#microsoft.graph.domainDnsUnavailableRecord":
                from . import domain_dns_unavailable_record

                return domain_dns_unavailable_record.DomainDnsUnavailableRecord()
            if mapping_value == "#microsoft.graph.drive":
                from . import drive

                return drive.Drive()
            if mapping_value == "#microsoft.graph.driveItem":
                from . import drive_item

                return drive_item.DriveItem()
            if mapping_value == "#microsoft.graph.driveItemVersion":
                from . import drive_item_version

                return drive_item_version.DriveItemVersion()
            if mapping_value == "#microsoft.graph.eBookInstallSummary":
                from . import e_book_install_summary

                return e_book_install_summary.EBookInstallSummary()
            if mapping_value == "#microsoft.graph.edge":
                from . import edge

                return edge.Edge()
            if mapping_value == "#microsoft.graph.editionUpgradeConfiguration":
                from . import edition_upgrade_configuration

                return edition_upgrade_configuration.EditionUpgradeConfiguration()
            if mapping_value == "#microsoft.graph.educationAssignment":
                from . import education_assignment

                return education_assignment.EducationAssignment()
            if mapping_value == "#microsoft.graph.educationAssignmentDefaults":
                from . import education_assignment_defaults

                return education_assignment_defaults.EducationAssignmentDefaults()
            if mapping_value == "#microsoft.graph.educationAssignmentResource":
                from . import education_assignment_resource

                return education_assignment_resource.EducationAssignmentResource()
            if mapping_value == "#microsoft.graph.educationAssignmentSettings":
                from . import education_assignment_settings

                return education_assignment_settings.EducationAssignmentSettings()
            if mapping_value == "#microsoft.graph.educationCategory":
                from . import education_category

                return education_category.EducationCategory()
            if mapping_value == "#microsoft.graph.educationClass":
                from . import education_class

                return education_class.EducationClass()
            if mapping_value == "#microsoft.graph.educationFeedbackOutcome":
                from . import education_feedback_outcome

                return education_feedback_outcome.EducationFeedbackOutcome()
            if mapping_value == "#microsoft.graph.educationFeedbackResourceOutcome":
                from . import education_feedback_resource_outcome

                return education_feedback_resource_outcome.EducationFeedbackResourceOutcome()
            if mapping_value == "#microsoft.graph.educationOrganization":
                from . import education_organization

                return education_organization.EducationOrganization()
            if mapping_value == "#microsoft.graph.educationOutcome":
                from . import education_outcome

                return education_outcome.EducationOutcome()
            if mapping_value == "#microsoft.graph.educationPointsOutcome":
                from . import education_points_outcome

                return education_points_outcome.EducationPointsOutcome()
            if mapping_value == "#microsoft.graph.educationRubric":
                from . import education_rubric

                return education_rubric.EducationRubric()
            if mapping_value == "#microsoft.graph.educationRubricOutcome":
                from . import education_rubric_outcome

                return education_rubric_outcome.EducationRubricOutcome()
            if mapping_value == "#microsoft.graph.educationSchool":
                from . import education_school

                return education_school.EducationSchool()
            if mapping_value == "#microsoft.graph.educationSubmission":
                from . import education_submission

                return education_submission.EducationSubmission()
            if mapping_value == "#microsoft.graph.educationSubmissionResource":
                from . import education_submission_resource

                return education_submission_resource.EducationSubmissionResource()
            if mapping_value == "#microsoft.graph.educationUser":
                from . import education_user

                return education_user.EducationUser()
            if mapping_value == "#microsoft.graph.emailAuthenticationMethod":
                from . import email_authentication_method

                return email_authentication_method.EmailAuthenticationMethod()
            if mapping_value == "#microsoft.graph.emailAuthenticationMethodConfiguration":
                from . import email_authentication_method_configuration

                return email_authentication_method_configuration.EmailAuthenticationMethodConfiguration()
            if mapping_value == "#microsoft.graph.emailFileAssessmentRequest":
                from . import email_file_assessment_request

                return email_file_assessment_request.EmailFileAssessmentRequest()
            if mapping_value == "#microsoft.graph.endpoint":
                from . import endpoint

                return endpoint.Endpoint()
            if mapping_value == "#microsoft.graph.enrollmentConfigurationAssignment":
                from . import enrollment_configuration_assignment

                return enrollment_configuration_assignment.EnrollmentConfigurationAssignment()
            if mapping_value == "#microsoft.graph.enrollmentTroubleshootingEvent":
                from . import enrollment_troubleshooting_event

                return enrollment_troubleshooting_event.EnrollmentTroubleshootingEvent()
            if mapping_value == "#microsoft.graph.enterpriseCodeSigningCertificate":
                from . import enterprise_code_signing_certificate

                return enterprise_code_signing_certificate.EnterpriseCodeSigningCertificate()
            if mapping_value == "#microsoft.graph.entitlementManagement":
                from . import entitlement_management

                return entitlement_management.EntitlementManagement()
            if mapping_value == "#microsoft.graph.entitlementManagementSettings":
                from . import entitlement_management_settings

                return entitlement_management_settings.EntitlementManagementSettings()
            if mapping_value == "#microsoft.graph.event":
                from . import event

                return event.Event()
            if mapping_value == "#microsoft.graph.eventMessage":
                from . import event_message

                return event_message.EventMessage()
            if mapping_value == "#microsoft.graph.eventMessageRequest":
                from . import event_message_request

                return event_message_request.EventMessageRequest()
            if mapping_value == "#microsoft.graph.eventMessageResponse":
                from . import event_message_response

                return event_message_response.EventMessageResponse()
            if mapping_value == "#microsoft.graph.extension":
                from . import extension

                return extension.Extension()
            if mapping_value == "#microsoft.graph.extensionProperty":
                from . import extension_property

                return extension_property.ExtensionProperty()
            if mapping_value == "#microsoft.graph.externalConnectors.connectionOperation":
                from .external_connectors import connection_operation

                return connection_operation.ConnectionOperation()
            if mapping_value == "#microsoft.graph.externalConnectors.externalConnection":
                from .external_connectors import external_connection

                return external_connection.ExternalConnection()
            if mapping_value == "#microsoft.graph.externalConnectors.externalGroup":
                from .external_connectors import external_group

                return external_group.ExternalGroup()
            if mapping_value == "#microsoft.graph.externalConnectors.externalItem":
                from .external_connectors import external_item

                return external_item.ExternalItem()
            if mapping_value == "#microsoft.graph.externalConnectors.identity":
                from .external_connectors import identity

                return identity.Identity()
            if mapping_value == "#microsoft.graph.externalConnectors.schema":
                from .external_connectors import schema

                return schema.Schema()
            if mapping_value == "#microsoft.graph.externalDomainName":
                from . import external_domain_name

                return external_domain_name.ExternalDomainName()
            if mapping_value == "#microsoft.graph.featureRolloutPolicy":
                from . import feature_rollout_policy

                return feature_rollout_policy.FeatureRolloutPolicy()
            if mapping_value == "#microsoft.graph.federatedIdentityCredential":
                from . import federated_identity_credential

                return federated_identity_credential.FederatedIdentityCredential()
            if mapping_value == "#microsoft.graph.fido2AuthenticationMethod":
                from . import fido2_authentication_method

                return fido2_authentication_method.Fido2AuthenticationMethod()
            if mapping_value == "#microsoft.graph.fido2AuthenticationMethodConfiguration":
                from . import fido2_authentication_method_configuration

                return fido2_authentication_method_configuration.Fido2AuthenticationMethodConfiguration()
            if mapping_value == "#microsoft.graph.fido2CombinationConfiguration":
                from . import fido2_combination_configuration

                return fido2_combination_configuration.Fido2CombinationConfiguration()
            if mapping_value == "#microsoft.graph.fieldValueSet":
                from . import field_value_set

                return field_value_set.FieldValueSet()
            if mapping_value == "#microsoft.graph.fileAssessmentRequest":
                from . import file_assessment_request

                return file_assessment_request.FileAssessmentRequest()
            if mapping_value == "#microsoft.graph.fileAttachment":
                from . import file_attachment

                return file_attachment.FileAttachment()
            if mapping_value == "#microsoft.graph.group":
                from . import group
                from .term_store import group

                return group.Group()
            if mapping_value == "#microsoft.graph.groupLifecyclePolicy":
                from . import group_lifecycle_policy

                return group_lifecycle_policy.GroupLifecyclePolicy()
            if mapping_value == "#microsoft.graph.groupSetting":
                from . import group_setting

                return group_setting.GroupSetting()
            if mapping_value == "#microsoft.graph.groupSettingTemplate":
                from . import group_setting_template

                return group_setting_template.GroupSettingTemplate()
            if mapping_value == "#microsoft.graph.homeRealmDiscoveryPolicy":
                from . import home_realm_discovery_policy

                return home_realm_discovery_policy.HomeRealmDiscoveryPolicy()
            if mapping_value == "#microsoft.graph.identityApiConnector":
                from . import identity_api_connector

                return identity_api_connector.IdentityApiConnector()
            if mapping_value == "#microsoft.graph.identityBuiltInUserFlowAttribute":
                from . import identity_built_in_user_flow_attribute

                return identity_built_in_user_flow_attribute.IdentityBuiltInUserFlowAttribute()
            if mapping_value == "#microsoft.graph.identityContainer":
                from . import identity_container

                return identity_container.IdentityContainer()
            if mapping_value == "#microsoft.graph.identityCustomUserFlowAttribute":
                from . import identity_custom_user_flow_attribute

                return identity_custom_user_flow_attribute.IdentityCustomUserFlowAttribute()
            if mapping_value == "#microsoft.graph.identityProvider":
                from . import identity_provider

                return identity_provider.IdentityProvider()
            if mapping_value == "#microsoft.graph.identityProviderBase":
                from . import identity_provider_base

                return identity_provider_base.IdentityProviderBase()
            if mapping_value == "#microsoft.graph.identitySecurityDefaultsEnforcementPolicy":
                from . import identity_security_defaults_enforcement_policy

                return identity_security_defaults_enforcement_policy.IdentitySecurityDefaultsEnforcementPolicy()
            if mapping_value == "#microsoft.graph.identityUserFlow":
                from . import identity_user_flow

                return identity_user_flow.IdentityUserFlow()
            if mapping_value == "#microsoft.graph.identityUserFlowAttribute":
                from . import identity_user_flow_attribute

                return identity_user_flow_attribute.IdentityUserFlowAttribute()
            if mapping_value == "#microsoft.graph.identityUserFlowAttributeAssignment":
                from . import identity_user_flow_attribute_assignment

                return identity_user_flow_attribute_assignment.IdentityUserFlowAttributeAssignment()
            if mapping_value == "#microsoft.graph.importedWindowsAutopilotDeviceIdentity":
                from . import imported_windows_autopilot_device_identity

                return imported_windows_autopilot_device_identity.ImportedWindowsAutopilotDeviceIdentity()
            if mapping_value == "#microsoft.graph.importedWindowsAutopilotDeviceIdentityUpload":
                from . import imported_windows_autopilot_device_identity_upload

                return imported_windows_autopilot_device_identity_upload.ImportedWindowsAutopilotDeviceIdentityUpload()
            if mapping_value == "#microsoft.graph.inferenceClassification":
                from . import inference_classification

                return inference_classification.InferenceClassification()
            if mapping_value == "#microsoft.graph.inferenceClassificationOverride":
                from . import inference_classification_override

                return inference_classification_override.InferenceClassificationOverride()
            if mapping_value == "#microsoft.graph.internalDomainFederation":
                from . import internal_domain_federation

                return internal_domain_federation.InternalDomainFederation()
            if mapping_value == "#microsoft.graph.internetExplorerMode":
                from . import internet_explorer_mode

                return internet_explorer_mode.InternetExplorerMode()
            if mapping_value == "#microsoft.graph.invitation":
                from . import invitation

                return invitation.Invitation()
            if mapping_value == "#microsoft.graph.inviteParticipantsOperation":
                from . import invite_participants_operation

                return invite_participants_operation.InviteParticipantsOperation()
            if mapping_value == "#microsoft.graph.iosCertificateProfile":
                from . import ios_certificate_profile

                return ios_certificate_profile.IosCertificateProfile()
            if mapping_value == "#microsoft.graph.iosCompliancePolicy":
                from . import ios_compliance_policy

                return ios_compliance_policy.IosCompliancePolicy()
            if mapping_value == "#microsoft.graph.iosCustomConfiguration":
                from . import ios_custom_configuration

                return ios_custom_configuration.IosCustomConfiguration()
            if mapping_value == "#microsoft.graph.iosDeviceFeaturesConfiguration":
                from . import ios_device_features_configuration

                return ios_device_features_configuration.IosDeviceFeaturesConfiguration()
            if mapping_value == "#microsoft.graph.iosGeneralDeviceConfiguration":
                from . import ios_general_device_configuration

                return ios_general_device_configuration.IosGeneralDeviceConfiguration()
            if mapping_value == "#microsoft.graph.iosiPadOSWebClip":
                from . import iosi_pad_o_s_web_clip

                return iosi_pad_o_s_web_clip.IosiPadOSWebClip()
            if mapping_value == "#microsoft.graph.iosLobApp":
                from . import ios_lob_app

                return ios_lob_app.IosLobApp()
            if mapping_value == "#microsoft.graph.iosLobAppProvisioningConfigurationAssignment":
                from . import ios_lob_app_provisioning_configuration_assignment

                return ios_lob_app_provisioning_configuration_assignment.IosLobAppProvisioningConfigurationAssignment()
            if mapping_value == "#microsoft.graph.iosManagedAppProtection":
                from . import ios_managed_app_protection

                return ios_managed_app_protection.IosManagedAppProtection()
            if mapping_value == "#microsoft.graph.iosManagedAppRegistration":
                from . import ios_managed_app_registration

                return ios_managed_app_registration.IosManagedAppRegistration()
            if mapping_value == "#microsoft.graph.iosMobileAppConfiguration":
                from . import ios_mobile_app_configuration

                return ios_mobile_app_configuration.IosMobileAppConfiguration()
            if mapping_value == "#microsoft.graph.iosStoreApp":
                from . import ios_store_app

                return ios_store_app.IosStoreApp()
            if mapping_value == "#microsoft.graph.iosUpdateConfiguration":
                from . import ios_update_configuration

                return ios_update_configuration.IosUpdateConfiguration()
            if mapping_value == "#microsoft.graph.iosUpdateDeviceStatus":
                from . import ios_update_device_status

                return ios_update_device_status.IosUpdateDeviceStatus()
            if mapping_value == "#microsoft.graph.iosVppApp":
                from . import ios_vpp_app

                return ios_vpp_app.IosVppApp()
            if mapping_value == "#microsoft.graph.iosVppEBook":
                from . import ios_vpp_e_book

                return ios_vpp_e_book.IosVppEBook()
            if mapping_value == "#microsoft.graph.iosVppEBookAssignment":
                from . import ios_vpp_e_book_assignment

                return ios_vpp_e_book_assignment.IosVppEBookAssignment()
            if mapping_value == "#microsoft.graph.ipNamedLocation":
                from . import ip_named_location

                return ip_named_location.IpNamedLocation()
            if mapping_value == "#microsoft.graph.itemActivity":
                from . import item_activity

                return item_activity.ItemActivity()
            if mapping_value == "#microsoft.graph.itemActivityStat":
                from . import item_activity_stat

                return item_activity_stat.ItemActivityStat()
            if mapping_value == "#microsoft.graph.itemAnalytics":
                from . import item_analytics

                return item_analytics.ItemAnalytics()
            if mapping_value == "#microsoft.graph.itemAttachment":
                from . import item_attachment

                return item_attachment.ItemAttachment()
            if mapping_value == "#microsoft.graph.learningContent":
                from . import learning_content

                return learning_content.LearningContent()
            if mapping_value == "#microsoft.graph.learningProvider":
                from . import learning_provider

                return learning_provider.LearningProvider()
            if mapping_value == "#microsoft.graph.licenseDetails":
                from . import license_details

                return license_details.LicenseDetails()
            if mapping_value == "#microsoft.graph.linkedResource":
                from . import linked_resource

                return linked_resource.LinkedResource()
            if mapping_value == "#microsoft.graph.list":
                from . import list

                return list.List()
            if mapping_value == "#microsoft.graph.listItem":
                from . import list_item

                return list_item.ListItem()
            if mapping_value == "#microsoft.graph.listItemVersion":
                from . import list_item_version

                return list_item_version.ListItemVersion()
            if mapping_value == "#microsoft.graph.localizedNotificationMessage":
                from . import localized_notification_message

                return localized_notification_message.LocalizedNotificationMessage()
            if mapping_value == "#microsoft.graph.longRunningOperation":
                from . import long_running_operation

                return long_running_operation.LongRunningOperation()
            if mapping_value == "#microsoft.graph.macOSCompliancePolicy":
                from . import mac_o_s_compliance_policy

                return mac_o_s_compliance_policy.MacOSCompliancePolicy()
            if mapping_value == "#microsoft.graph.macOSCustomConfiguration":
                from . import mac_o_s_custom_configuration

                return mac_o_s_custom_configuration.MacOSCustomConfiguration()
            if mapping_value == "#microsoft.graph.macOSDeviceFeaturesConfiguration":
                from . import mac_o_s_device_features_configuration

                return mac_o_s_device_features_configuration.MacOSDeviceFeaturesConfiguration()
            if mapping_value == "#microsoft.graph.macOSGeneralDeviceConfiguration":
                from . import mac_o_s_general_device_configuration

                return mac_o_s_general_device_configuration.MacOSGeneralDeviceConfiguration()
            if mapping_value == "#microsoft.graph.macOSLobApp":
                from . import mac_o_s_lob_app

                return mac_o_s_lob_app.MacOSLobApp()
            if mapping_value == "#microsoft.graph.macOSMicrosoftEdgeApp":
                from . import mac_o_s_microsoft_edge_app

                return mac_o_s_microsoft_edge_app.MacOSMicrosoftEdgeApp()
            if mapping_value == "#microsoft.graph.macOSOfficeSuiteApp":
                from . import mac_o_s_office_suite_app

                return mac_o_s_office_suite_app.MacOSOfficeSuiteApp()
            if mapping_value == "#microsoft.graph.mailAssessmentRequest":
                from . import mail_assessment_request

                return mail_assessment_request.MailAssessmentRequest()
            if mapping_value == "#microsoft.graph.mailFolder":
                from . import mail_folder

                return mail_folder.MailFolder()
            if mapping_value == "#microsoft.graph.mailSearchFolder":
                from . import mail_search_folder

                return mail_search_folder.MailSearchFolder()
            if mapping_value == "#microsoft.graph.managedAndroidLobApp":
                from . import managed_android_lob_app

                return managed_android_lob_app.ManagedAndroidLobApp()
            if mapping_value == "#microsoft.graph.managedAndroidStoreApp":
                from . import managed_android_store_app

                return managed_android_store_app.ManagedAndroidStoreApp()
            if mapping_value == "#microsoft.graph.managedApp":
                from . import managed_app

                return managed_app.ManagedApp()
            if mapping_value == "#microsoft.graph.managedAppConfiguration":
                from . import managed_app_configuration

                return managed_app_configuration.ManagedAppConfiguration()
            if mapping_value == "#microsoft.graph.managedAppOperation":
                from . import managed_app_operation

                return managed_app_operation.ManagedAppOperation()
            if mapping_value == "#microsoft.graph.managedAppPolicy":
                from . import managed_app_policy

                return managed_app_policy.ManagedAppPolicy()
            if mapping_value == "#microsoft.graph.managedAppPolicyDeploymentSummary":
                from . import managed_app_policy_deployment_summary

                return managed_app_policy_deployment_summary.ManagedAppPolicyDeploymentSummary()
            if mapping_value == "#microsoft.graph.managedAppProtection":
                from . import managed_app_protection

                return managed_app_protection.ManagedAppProtection()
            if mapping_value == "#microsoft.graph.managedAppRegistration":
                from . import managed_app_registration

                return managed_app_registration.ManagedAppRegistration()
            if mapping_value == "#microsoft.graph.managedAppStatus":
                from . import managed_app_status

                return managed_app_status.ManagedAppStatus()
            if mapping_value == "#microsoft.graph.managedAppStatusRaw":
                from . import managed_app_status_raw

                return managed_app_status_raw.ManagedAppStatusRaw()
            if mapping_value == "#microsoft.graph.managedDevice":
                from . import managed_device

                return managed_device.ManagedDevice()
            if mapping_value == "#microsoft.graph.managedDeviceMobileAppConfiguration":
                from . import managed_device_mobile_app_configuration

                return managed_device_mobile_app_configuration.ManagedDeviceMobileAppConfiguration()
            if mapping_value == "#microsoft.graph.managedDeviceMobileAppConfigurationAssignment":
                from . import managed_device_mobile_app_configuration_assignment

                return managed_device_mobile_app_configuration_assignment.ManagedDeviceMobileAppConfigurationAssignment()
            if mapping_value == "#microsoft.graph.managedDeviceMobileAppConfigurationDeviceStatus":
                from . import managed_device_mobile_app_configuration_device_status

                return managed_device_mobile_app_configuration_device_status.ManagedDeviceMobileAppConfigurationDeviceStatus()
            if mapping_value == "#microsoft.graph.managedDeviceMobileAppConfigurationDeviceSummary":
                from . import managed_device_mobile_app_configuration_device_summary

                return managed_device_mobile_app_configuration_device_summary.ManagedDeviceMobileAppConfigurationDeviceSummary()
            if mapping_value == "#microsoft.graph.managedDeviceMobileAppConfigurationUserStatus":
                from . import managed_device_mobile_app_configuration_user_status

                return managed_device_mobile_app_configuration_user_status.ManagedDeviceMobileAppConfigurationUserStatus()
            if mapping_value == "#microsoft.graph.managedDeviceMobileAppConfigurationUserSummary":
                from . import managed_device_mobile_app_configuration_user_summary

                return managed_device_mobile_app_configuration_user_summary.ManagedDeviceMobileAppConfigurationUserSummary()
            if mapping_value == "#microsoft.graph.managedDeviceOverview":
                from . import managed_device_overview

                return managed_device_overview.ManagedDeviceOverview()
            if mapping_value == "#microsoft.graph.managedEBook":
                from . import managed_e_book

                return managed_e_book.ManagedEBook()
            if mapping_value == "#microsoft.graph.managedEBookAssignment":
                from . import managed_e_book_assignment

                return managed_e_book_assignment.ManagedEBookAssignment()
            if mapping_value == "#microsoft.graph.managedIOSLobApp":
                from . import managed_i_o_s_lob_app

                return managed_i_o_s_lob_app.ManagedIOSLobApp()
            if mapping_value == "#microsoft.graph.managedIOSStoreApp":
                from . import managed_i_o_s_store_app

                return managed_i_o_s_store_app.ManagedIOSStoreApp()
            if mapping_value == "#microsoft.graph.managedMobileApp":
                from . import managed_mobile_app

                return managed_mobile_app.ManagedMobileApp()
            if mapping_value == "#microsoft.graph.managedMobileLobApp":
                from . import managed_mobile_lob_app

                return managed_mobile_lob_app.ManagedMobileLobApp()
            if mapping_value == "#microsoft.graph.mdmWindowsInformationProtectionPolicy":
                from . import mdm_windows_information_protection_policy

                return mdm_windows_information_protection_policy.MdmWindowsInformationProtectionPolicy()
            if mapping_value == "#microsoft.graph.meetingAttendanceReport":
                from . import meeting_attendance_report

                return meeting_attendance_report.MeetingAttendanceReport()
            if mapping_value == "#microsoft.graph.message":
                from . import message

                return message.Message()
            if mapping_value == "#microsoft.graph.messageRule":
                from . import message_rule

                return message_rule.MessageRule()
            if mapping_value == "#microsoft.graph.microsoftAccountUserConversationMember":
                from . import microsoft_account_user_conversation_member

                return microsoft_account_user_conversation_member.MicrosoftAccountUserConversationMember()
            if mapping_value == "#microsoft.graph.microsoftAuthenticatorAuthenticationMethod":
                from . import microsoft_authenticator_authentication_method

                return microsoft_authenticator_authentication_method.MicrosoftAuthenticatorAuthenticationMethod()
            if mapping_value == "#microsoft.graph.microsoftAuthenticatorAuthenticationMethodConfiguration":
                from . import microsoft_authenticator_authentication_method_configuration

                return microsoft_authenticator_authentication_method_configuration.MicrosoftAuthenticatorAuthenticationMethodConfiguration()
            if mapping_value == "#microsoft.graph.microsoftAuthenticatorAuthenticationMethodTarget":
                from . import microsoft_authenticator_authentication_method_target

                return microsoft_authenticator_authentication_method_target.MicrosoftAuthenticatorAuthenticationMethodTarget()
            if mapping_value == "#microsoft.graph.microsoftStoreForBusinessApp":
                from . import microsoft_store_for_business_app

                return microsoft_store_for_business_app.MicrosoftStoreForBusinessApp()
            if mapping_value == "#microsoft.graph.mobileApp":
                from . import mobile_app

                return mobile_app.MobileApp()
            if mapping_value == "#microsoft.graph.mobileAppAssignment":
                from . import mobile_app_assignment

                return mobile_app_assignment.MobileAppAssignment()
            if mapping_value == "#microsoft.graph.mobileAppCategory":
                from . import mobile_app_category

                return mobile_app_category.MobileAppCategory()
            if mapping_value == "#microsoft.graph.mobileAppContent":
                from . import mobile_app_content

                return mobile_app_content.MobileAppContent()
            if mapping_value == "#microsoft.graph.mobileAppContentFile":
                from . import mobile_app_content_file

                return mobile_app_content_file.MobileAppContentFile()
            if mapping_value == "#microsoft.graph.mobileContainedApp":
                from . import mobile_contained_app

                return mobile_contained_app.MobileContainedApp()
            if mapping_value == "#microsoft.graph.mobileLobApp":
                from . import mobile_lob_app

                return mobile_lob_app.MobileLobApp()
            if mapping_value == "#microsoft.graph.mobileThreatDefenseConnector":
                from . import mobile_threat_defense_connector

                return mobile_threat_defense_connector.MobileThreatDefenseConnector()
            if mapping_value == "#microsoft.graph.multiValueLegacyExtendedProperty":
                from . import multi_value_legacy_extended_property

                return multi_value_legacy_extended_property.MultiValueLegacyExtendedProperty()
            if mapping_value == "#microsoft.graph.muteParticipantOperation":
                from . import mute_participant_operation

                return mute_participant_operation.MuteParticipantOperation()
            if mapping_value == "#microsoft.graph.namedLocation":
                from . import named_location

                return named_location.NamedLocation()
            if mapping_value == "#microsoft.graph.notebook":
                from . import notebook

                return notebook.Notebook()
            if mapping_value == "#microsoft.graph.notificationMessageTemplate":
                from . import notification_message_template

                return notification_message_template.NotificationMessageTemplate()
            if mapping_value == "#microsoft.graph.oAuth2PermissionGrant":
                from . import o_auth2_permission_grant

                return o_auth2_permission_grant.OAuth2PermissionGrant()
            if mapping_value == "#microsoft.graph.offerShiftRequest":
                from . import offer_shift_request

                return offer_shift_request.OfferShiftRequest()
            if mapping_value == "#microsoft.graph.officeGraphInsights":
                from . import office_graph_insights

                return office_graph_insights.OfficeGraphInsights()
            if mapping_value == "#microsoft.graph.onenote":
                from . import onenote

                return onenote.Onenote()
            if mapping_value == "#microsoft.graph.onenoteEntityBaseModel":
                from . import onenote_entity_base_model

                return onenote_entity_base_model.OnenoteEntityBaseModel()
            if mapping_value == "#microsoft.graph.onenoteEntityHierarchyModel":
                from . import onenote_entity_hierarchy_model

                return onenote_entity_hierarchy_model.OnenoteEntityHierarchyModel()
            if mapping_value == "#microsoft.graph.onenoteEntitySchemaObjectModel":
                from . import onenote_entity_schema_object_model

                return onenote_entity_schema_object_model.OnenoteEntitySchemaObjectModel()
            if mapping_value == "#microsoft.graph.onenoteOperation":
                from . import onenote_operation

                return onenote_operation.OnenoteOperation()
            if mapping_value == "#microsoft.graph.onenotePage":
                from . import onenote_page

                return onenote_page.OnenotePage()
            if mapping_value == "#microsoft.graph.onenoteResource":
                from . import onenote_resource

                return onenote_resource.OnenoteResource()
            if mapping_value == "#microsoft.graph.onenoteSection":
                from . import onenote_section

                return onenote_section.OnenoteSection()
            if mapping_value == "#microsoft.graph.onlineMeeting":
                from . import online_meeting

                return online_meeting.OnlineMeeting()
            if mapping_value == "#microsoft.graph.onPremisesConditionalAccessSettings":
                from . import on_premises_conditional_access_settings

                return on_premises_conditional_access_settings.OnPremisesConditionalAccessSettings()
            if mapping_value == "#microsoft.graph.onPremisesDirectorySynchronization":
                from . import on_premises_directory_synchronization

                return on_premises_directory_synchronization.OnPremisesDirectorySynchronization()
            if mapping_value == "#microsoft.graph.openShift":
                from . import open_shift

                return open_shift.OpenShift()
            if mapping_value == "#microsoft.graph.openShiftChangeRequest":
                from . import open_shift_change_request

                return open_shift_change_request.OpenShiftChangeRequest()
            if mapping_value == "#microsoft.graph.openTypeExtension":
                from . import open_type_extension

                return open_type_extension.OpenTypeExtension()
            if mapping_value == "#microsoft.graph.operation":
                from . import operation

                return operation.Operation()
            if mapping_value == "#microsoft.graph.organization":
                from . import organization

                return organization.Organization()
            if mapping_value == "#microsoft.graph.organizationalBranding":
                from . import organizational_branding

                return organizational_branding.OrganizationalBranding()
            if mapping_value == "#microsoft.graph.organizationalBrandingLocalization":
                from . import organizational_branding_localization

                return organizational_branding_localization.OrganizationalBrandingLocalization()
            if mapping_value == "#microsoft.graph.organizationalBrandingProperties":
                from . import organizational_branding_properties

                return organizational_branding_properties.OrganizationalBrandingProperties()
            if mapping_value == "#microsoft.graph.orgContact":
                from . import org_contact

                return org_contact.OrgContact()
            if mapping_value == "#microsoft.graph.outlookCategory":
                from . import outlook_category

                return outlook_category.OutlookCategory()
            if mapping_value == "#microsoft.graph.outlookItem":
                from . import outlook_item

                return outlook_item.OutlookItem()
            if mapping_value == "#microsoft.graph.outlookUser":
                from . import outlook_user

                return outlook_user.OutlookUser()
            if mapping_value == "#microsoft.graph.participant":
                from . import participant

                return participant.Participant()
            if mapping_value == "#microsoft.graph.participantJoiningNotification":
                from . import participant_joining_notification

                return participant_joining_notification.ParticipantJoiningNotification()
            if mapping_value == "#microsoft.graph.participantLeftNotification":
                from . import participant_left_notification

                return participant_left_notification.ParticipantLeftNotification()
            if mapping_value == "#microsoft.graph.passwordAuthenticationMethod":
                from . import password_authentication_method

                return password_authentication_method.PasswordAuthenticationMethod()
            if mapping_value == "#microsoft.graph.permission":
                from . import permission

                return permission.Permission()
            if mapping_value == "#microsoft.graph.permissionGrantConditionSet":
                from . import permission_grant_condition_set

                return permission_grant_condition_set.PermissionGrantConditionSet()
            if mapping_value == "#microsoft.graph.permissionGrantPolicy":
                from . import permission_grant_policy

                return permission_grant_policy.PermissionGrantPolicy()
            if mapping_value == "#microsoft.graph.person":
                from . import person

                return person.Person()
            if mapping_value == "#microsoft.graph.phoneAuthenticationMethod":
                from . import phone_authentication_method

                return phone_authentication_method.PhoneAuthenticationMethod()
            if mapping_value == "#microsoft.graph.pinnedChatMessageInfo":
                from . import pinned_chat_message_info

                return pinned_chat_message_info.PinnedChatMessageInfo()
            if mapping_value == "#microsoft.graph.place":
                from . import place

                return place.Place()
            if mapping_value == "#microsoft.graph.planner":
                from . import planner

                return planner.Planner()
            if mapping_value == "#microsoft.graph.plannerAssignedToTaskBoardTaskFormat":
                from . import planner_assigned_to_task_board_task_format

                return planner_assigned_to_task_board_task_format.PlannerAssignedToTaskBoardTaskFormat()
            if mapping_value == "#microsoft.graph.plannerBucket":
                from . import planner_bucket

                return planner_bucket.PlannerBucket()
            if mapping_value == "#microsoft.graph.plannerBucketTaskBoardTaskFormat":
                from . import planner_bucket_task_board_task_format

                return planner_bucket_task_board_task_format.PlannerBucketTaskBoardTaskFormat()
            if mapping_value == "#microsoft.graph.plannerGroup":
                from . import planner_group

                return planner_group.PlannerGroup()
            if mapping_value == "#microsoft.graph.plannerPlan":
                from . import planner_plan

                return planner_plan.PlannerPlan()
            if mapping_value == "#microsoft.graph.plannerPlanDetails":
                from . import planner_plan_details

                return planner_plan_details.PlannerPlanDetails()
            if mapping_value == "#microsoft.graph.plannerProgressTaskBoardTaskFormat":
                from . import planner_progress_task_board_task_format

                return planner_progress_task_board_task_format.PlannerProgressTaskBoardTaskFormat()
            if mapping_value == "#microsoft.graph.plannerTask":
                from . import planner_task

                return planner_task.PlannerTask()
            if mapping_value == "#microsoft.graph.plannerTaskDetails":
                from . import planner_task_details

                return planner_task_details.PlannerTaskDetails()
            if mapping_value == "#microsoft.graph.plannerUser":
                from . import planner_user

                return planner_user.PlannerUser()
            if mapping_value == "#microsoft.graph.playPromptOperation":
                from . import play_prompt_operation

                return play_prompt_operation.PlayPromptOperation()
            if mapping_value == "#microsoft.graph.policyBase":
                from . import policy_base

                return policy_base.PolicyBase()
            if mapping_value == "#microsoft.graph.policyRoot":
                from . import policy_root

                return policy_root.PolicyRoot()
            if mapping_value == "#microsoft.graph.post":
                from . import post

                return post.Post()
            if mapping_value == "#microsoft.graph.presence":
                from . import presence

                return presence.Presence()
            if mapping_value == "#microsoft.graph.printConnector":
                from . import print_connector

                return print_connector.PrintConnector()
            if mapping_value == "#microsoft.graph.printDocument":
                from . import print_document

                return print_document.PrintDocument()
            if mapping_value == "#microsoft.graph.printer":
                from . import printer

                return printer.Printer()
            if mapping_value == "#microsoft.graph.printerBase":
                from . import printer_base

                return printer_base.PrinterBase()
            if mapping_value == "#microsoft.graph.printerCreateOperation":
                from . import printer_create_operation

                return printer_create_operation.PrinterCreateOperation()
            if mapping_value == "#microsoft.graph.printerShare":
                from . import printer_share

                return printer_share.PrinterShare()
            if mapping_value == "#microsoft.graph.printJob":
                from . import print_job

                return print_job.PrintJob()
            if mapping_value == "#microsoft.graph.printOperation":
                from . import print_operation

                return print_operation.PrintOperation()
            if mapping_value == "#microsoft.graph.printService":
                from . import print_service

                return print_service.PrintService()
            if mapping_value == "#microsoft.graph.printServiceEndpoint":
                from . import print_service_endpoint

                return print_service_endpoint.PrintServiceEndpoint()
            if mapping_value == "#microsoft.graph.printTask":
                from . import print_task

                return print_task.PrintTask()
            if mapping_value == "#microsoft.graph.printTaskDefinition":
                from . import print_task_definition

                return print_task_definition.PrintTaskDefinition()
            if mapping_value == "#microsoft.graph.printTaskTrigger":
                from . import print_task_trigger

                return print_task_trigger.PrintTaskTrigger()
            if mapping_value == "#microsoft.graph.printUsage":
                from . import print_usage

                return print_usage.PrintUsage()
            if mapping_value == "#microsoft.graph.printUsageByPrinter":
                from . import print_usage_by_printer

                return print_usage_by_printer.PrintUsageByPrinter()
            if mapping_value == "#microsoft.graph.printUsageByUser":
                from . import print_usage_by_user

                return print_usage_by_user.PrintUsageByUser()
            if mapping_value == "#microsoft.graph.profilePhoto":
                from . import profile_photo

                return profile_photo.ProfilePhoto()
            if mapping_value == "#microsoft.graph.provisioningObjectSummary":
                from . import provisioning_object_summary

                return provisioning_object_summary.ProvisioningObjectSummary()
            if mapping_value == "#microsoft.graph.rbacApplication":
                from . import rbac_application

                return rbac_application.RbacApplication()
            if mapping_value == "#microsoft.graph.recordOperation":
                from . import record_operation

                return record_operation.RecordOperation()
            if mapping_value == "#microsoft.graph.referenceAttachment":
                from . import reference_attachment

                return reference_attachment.ReferenceAttachment()
            if mapping_value == "#microsoft.graph.remoteAssistancePartner":
                from . import remote_assistance_partner

                return remote_assistance_partner.RemoteAssistancePartner()
            if mapping_value == "#microsoft.graph.request":
                from . import request

                return request.Request()
            if mapping_value == "#microsoft.graph.resourceOperation":
                from . import resource_operation

                return resource_operation.ResourceOperation()
            if mapping_value == "#microsoft.graph.resourceSpecificPermissionGrant":
                from . import resource_specific_permission_grant

                return resource_specific_permission_grant.ResourceSpecificPermissionGrant()
            if mapping_value == "#microsoft.graph.richLongRunningOperation":
                from . import rich_long_running_operation

                return rich_long_running_operation.RichLongRunningOperation()
            if mapping_value == "#microsoft.graph.riskDetection":
                from . import risk_detection

                return risk_detection.RiskDetection()
            if mapping_value == "#microsoft.graph.riskyServicePrincipal":
                from . import risky_service_principal

                return risky_service_principal.RiskyServicePrincipal()
            if mapping_value == "#microsoft.graph.riskyServicePrincipalHistoryItem":
                from . import risky_service_principal_history_item

                return risky_service_principal_history_item.RiskyServicePrincipalHistoryItem()
            if mapping_value == "#microsoft.graph.riskyUser":
                from . import risky_user

                return risky_user.RiskyUser()
            if mapping_value == "#microsoft.graph.riskyUserHistoryItem":
                from . import risky_user_history_item

                return risky_user_history_item.RiskyUserHistoryItem()
            if mapping_value == "#microsoft.graph.roleAssignment":
                from . import role_assignment

                return role_assignment.RoleAssignment()
            if mapping_value == "#microsoft.graph.roleDefinition":
                from . import role_definition

                return role_definition.RoleDefinition()
            if mapping_value == "#microsoft.graph.room":
                from . import room

                return room.Room()
            if mapping_value == "#microsoft.graph.roomList":
                from . import room_list

                return room_list.RoomList()
            if mapping_value == "#microsoft.graph.samlOrWsFedExternalDomainFederation":
                from . import saml_or_ws_fed_external_domain_federation

                return saml_or_ws_fed_external_domain_federation.SamlOrWsFedExternalDomainFederation()
            if mapping_value == "#microsoft.graph.samlOrWsFedProvider":
                from . import saml_or_ws_fed_provider

                return saml_or_ws_fed_provider.SamlOrWsFedProvider()
            if mapping_value == "#microsoft.graph.schedule":
                from . import schedule

                return schedule.Schedule()
            if mapping_value == "#microsoft.graph.scheduleChangeRequest":
                from . import schedule_change_request

                return schedule_change_request.ScheduleChangeRequest()
            if mapping_value == "#microsoft.graph.schedulingGroup":
                from . import scheduling_group

                return scheduling_group.SchedulingGroup()
            if mapping_value == "#microsoft.graph.schemaExtension":
                from . import schema_extension

                return schema_extension.SchemaExtension()
            if mapping_value == "#microsoft.graph.scopedRoleMembership":
                from . import scoped_role_membership

                return scoped_role_membership.ScopedRoleMembership()
            if mapping_value == "#microsoft.graph.searchEntity":
                from . import search_entity

                return search_entity.SearchEntity()
            if mapping_value == "#microsoft.graph.sectionGroup":
                from . import section_group

                return section_group.SectionGroup()
            if mapping_value == "#microsoft.graph.secureScore":
                from . import secure_score

                return secure_score.SecureScore()
            if mapping_value == "#microsoft.graph.secureScoreControlProfile":
                from . import secure_score_control_profile

                return secure_score_control_profile.SecureScoreControlProfile()
            if mapping_value == "#microsoft.graph.security":
                from .security import security

                return security.Security()
            if mapping_value == "#microsoft.graph.security.alert":
                from . import alert
                from .security import alert

                return alert.Alert()
            if mapping_value == "#microsoft.graph.security.case":
                from .security import case

                return case.Case()
            if mapping_value == "#microsoft.graph.security.caseOperation":
                from .security import case_operation

                return case_operation.CaseOperation()
            if mapping_value == "#microsoft.graph.security.casesRoot":
                from .security import cases_root

                return cases_root.CasesRoot()
            if mapping_value == "#microsoft.graph.security.dataSet":
                from .security import data_set

                return data_set.DataSet()
            if mapping_value == "#microsoft.graph.security.dataSource":
                from .security import data_source

                return data_source.DataSource()
            if mapping_value == "#microsoft.graph.security.dataSourceContainer":
                from .security import data_source_container

                return data_source_container.DataSourceContainer()
            if mapping_value == "#microsoft.graph.security.ediscoveryAddToReviewSetOperation":
                from .security import ediscovery_add_to_review_set_operation

                return ediscovery_add_to_review_set_operation.EdiscoveryAddToReviewSetOperation()
            if mapping_value == "#microsoft.graph.security.ediscoveryCase":
                from .security import ediscovery_case

                return ediscovery_case.EdiscoveryCase()
            if mapping_value == "#microsoft.graph.security.ediscoveryCaseSettings":
                from .security import ediscovery_case_settings

                return ediscovery_case_settings.EdiscoveryCaseSettings()
            if mapping_value == "#microsoft.graph.security.ediscoveryCustodian":
                from .security import ediscovery_custodian

                return ediscovery_custodian.EdiscoveryCustodian()
            if mapping_value == "#microsoft.graph.security.ediscoveryEstimateOperation":
                from .security import ediscovery_estimate_operation

                return ediscovery_estimate_operation.EdiscoveryEstimateOperation()
            if mapping_value == "#microsoft.graph.security.ediscoveryHoldOperation":
                from .security import ediscovery_hold_operation

                return ediscovery_hold_operation.EdiscoveryHoldOperation()
            if mapping_value == "#microsoft.graph.security.ediscoveryIndexOperation":
                from .security import ediscovery_index_operation

                return ediscovery_index_operation.EdiscoveryIndexOperation()
            if mapping_value == "#microsoft.graph.security.ediscoveryNoncustodialDataSource":
                from .security import ediscovery_noncustodial_data_source

                return ediscovery_noncustodial_data_source.EdiscoveryNoncustodialDataSource()
            if mapping_value == "#microsoft.graph.security.ediscoveryPurgeDataOperation":
                from .security import ediscovery_purge_data_operation

                return ediscovery_purge_data_operation.EdiscoveryPurgeDataOperation()
            if mapping_value == "#microsoft.graph.security.ediscoveryReviewSet":
                from .security import ediscovery_review_set

                return ediscovery_review_set.EdiscoveryReviewSet()
            if mapping_value == "#microsoft.graph.security.ediscoveryReviewSetQuery":
                from .security import ediscovery_review_set_query

                return ediscovery_review_set_query.EdiscoveryReviewSetQuery()
            if mapping_value == "#microsoft.graph.security.ediscoveryReviewTag":
                from .security import ediscovery_review_tag

                return ediscovery_review_tag.EdiscoveryReviewTag()
            if mapping_value == "#microsoft.graph.security.ediscoverySearch":
                from .security import ediscovery_search

                return ediscovery_search.EdiscoverySearch()
            if mapping_value == "#microsoft.graph.security.ediscoveryTagOperation":
                from .security import ediscovery_tag_operation

                return ediscovery_tag_operation.EdiscoveryTagOperation()
            if mapping_value == "#microsoft.graph.security.incident":
                from .security import incident

                return incident.Incident()
            if mapping_value == "#microsoft.graph.security.retentionEvent":
                from .security import retention_event

                return retention_event.RetentionEvent()
            if mapping_value == "#microsoft.graph.security.retentionEventType":
                from .security import retention_event_type

                return retention_event_type.RetentionEventType()
            if mapping_value == "#microsoft.graph.security.search":
                from .security import search

                return search.Search()
            if mapping_value == "#microsoft.graph.security.siteSource":
                from .security import site_source

                return site_source.SiteSource()
            if mapping_value == "#microsoft.graph.security.tag":
                from .security import tag

                return tag.Tag()
            if mapping_value == "#microsoft.graph.security.triggersRoot":
                from .security import triggers_root

                return triggers_root.TriggersRoot()
            if mapping_value == "#microsoft.graph.security.triggerTypesRoot":
                from .security import trigger_types_root

                return trigger_types_root.TriggerTypesRoot()
            if mapping_value == "#microsoft.graph.security.unifiedGroupSource":
                from .security import unified_group_source

                return unified_group_source.UnifiedGroupSource()
            if mapping_value == "#microsoft.graph.security.userSource":
                from .security import user_source

                return user_source.UserSource()
            if mapping_value == "#microsoft.graph.securityReportsRoot":
                from . import security_reports_root

                return security_reports_root.SecurityReportsRoot()
            if mapping_value == "#microsoft.graph.serviceAnnouncement":
                from . import service_announcement

                return service_announcement.ServiceAnnouncement()
            if mapping_value == "#microsoft.graph.serviceAnnouncementAttachment":
                from . import service_announcement_attachment

                return service_announcement_attachment.ServiceAnnouncementAttachment()
            if mapping_value == "#microsoft.graph.serviceAnnouncementBase":
                from . import service_announcement_base

                return service_announcement_base.ServiceAnnouncementBase()
            if mapping_value == "#microsoft.graph.serviceHealth":
                from . import service_health

                return service_health.ServiceHealth()
            if mapping_value == "#microsoft.graph.serviceHealthIssue":
                from . import service_health_issue

                return service_health_issue.ServiceHealthIssue()
            if mapping_value == "#microsoft.graph.servicePrincipal":
                from . import service_principal

                return service_principal.ServicePrincipal()
            if mapping_value == "#microsoft.graph.servicePrincipalRiskDetection":
                from . import service_principal_risk_detection

                return service_principal_risk_detection.ServicePrincipalRiskDetection()
            if mapping_value == "#microsoft.graph.serviceUpdateMessage":
                from . import service_update_message

                return service_update_message.ServiceUpdateMessage()
            if mapping_value == "#microsoft.graph.settingStateDeviceSummary":
                from . import setting_state_device_summary

                return setting_state_device_summary.SettingStateDeviceSummary()
            if mapping_value == "#microsoft.graph.sharedDriveItem":
                from . import shared_drive_item

                return shared_drive_item.SharedDriveItem()
            if mapping_value == "#microsoft.graph.sharedInsight":
                from . import shared_insight

                return shared_insight.SharedInsight()
            if mapping_value == "#microsoft.graph.sharedPCConfiguration":
                from . import shared_p_c_configuration

                return shared_p_c_configuration.SharedPCConfiguration()
            if mapping_value == "#microsoft.graph.sharedWithChannelTeamInfo":
                from . import shared_with_channel_team_info

                return shared_with_channel_team_info.SharedWithChannelTeamInfo()
            if mapping_value == "#microsoft.graph.sharepoint":
                from . import sharepoint

                return sharepoint.Sharepoint()
            if mapping_value == "#microsoft.graph.sharepointSettings":
                from . import sharepoint_settings

                return sharepoint_settings.SharepointSettings()
            if mapping_value == "#microsoft.graph.shift":
                from . import shift

                return shift.Shift()
            if mapping_value == "#microsoft.graph.shiftPreferences":
                from . import shift_preferences

                return shift_preferences.ShiftPreferences()
            if mapping_value == "#microsoft.graph.signIn":
                from . import sign_in

                return sign_in.SignIn()
            if mapping_value == "#microsoft.graph.simulation":
                from . import simulation

                return simulation.Simulation()
            if mapping_value == "#microsoft.graph.simulationAutomation":
                from . import simulation_automation

                return simulation_automation.SimulationAutomation()
            if mapping_value == "#microsoft.graph.simulationAutomationRun":
                from . import simulation_automation_run

                return simulation_automation_run.SimulationAutomationRun()
            if mapping_value == "#microsoft.graph.singleValueLegacyExtendedProperty":
                from . import single_value_legacy_extended_property

                return single_value_legacy_extended_property.SingleValueLegacyExtendedProperty()
            if mapping_value == "#microsoft.graph.site":
                from . import site

                return site.Site()
            if mapping_value == "#microsoft.graph.skypeForBusinessUserConversationMember":
                from . import skype_for_business_user_conversation_member

                return skype_for_business_user_conversation_member.SkypeForBusinessUserConversationMember()
            if mapping_value == "#microsoft.graph.skypeUserConversationMember":
                from . import skype_user_conversation_member

                return skype_user_conversation_member.SkypeUserConversationMember()
            if mapping_value == "#microsoft.graph.smsAuthenticationMethodConfiguration":
                from . import sms_authentication_method_configuration

                return sms_authentication_method_configuration.SmsAuthenticationMethodConfiguration()
            if mapping_value == "#microsoft.graph.smsAuthenticationMethodTarget":
                from . import sms_authentication_method_target

                return sms_authentication_method_target.SmsAuthenticationMethodTarget()
            if mapping_value == "#microsoft.graph.socialIdentityProvider":
                from . import social_identity_provider

                return social_identity_provider.SocialIdentityProvider()
            if mapping_value == "#microsoft.graph.softwareOathAuthenticationMethod":
                from . import software_oath_authentication_method

                return software_oath_authentication_method.SoftwareOathAuthenticationMethod()
            if mapping_value == "#microsoft.graph.softwareOathAuthenticationMethodConfiguration":
                from . import software_oath_authentication_method_configuration

                return software_oath_authentication_method_configuration.SoftwareOathAuthenticationMethodConfiguration()
            if mapping_value == "#microsoft.graph.softwareUpdateStatusSummary":
                from . import software_update_status_summary

                return software_update_status_summary.SoftwareUpdateStatusSummary()
            if mapping_value == "#microsoft.graph.startHoldMusicOperation":
                from . import start_hold_music_operation

                return start_hold_music_operation.StartHoldMusicOperation()
            if mapping_value == "#microsoft.graph.stopHoldMusicOperation":
                from . import stop_hold_music_operation

                return stop_hold_music_operation.StopHoldMusicOperation()
            if mapping_value == "#microsoft.graph.stsPolicy":
                from . import sts_policy

                return sts_policy.StsPolicy()
            if mapping_value == "#microsoft.graph.subjectRightsRequest":
                from . import subject_rights_request

                return subject_rights_request.SubjectRightsRequest()
            if mapping_value == "#microsoft.graph.subscribedSku":
                from . import subscribed_sku

                return subscribed_sku.SubscribedSku()
            if mapping_value == "#microsoft.graph.subscribeToToneOperation":
                from . import subscribe_to_tone_operation

                return subscribe_to_tone_operation.SubscribeToToneOperation()
            if mapping_value == "#microsoft.graph.subscription":
                from . import subscription

                return subscription.Subscription()
            if mapping_value == "#microsoft.graph.swapShiftsChangeRequest":
                from . import swap_shifts_change_request

                return swap_shifts_change_request.SwapShiftsChangeRequest()
            if mapping_value == "#microsoft.graph.targetedManagedAppConfiguration":
                from . import targeted_managed_app_configuration

                return targeted_managed_app_configuration.TargetedManagedAppConfiguration()
            if mapping_value == "#microsoft.graph.targetedManagedAppPolicyAssignment":
                from . import targeted_managed_app_policy_assignment

                return targeted_managed_app_policy_assignment.TargetedManagedAppPolicyAssignment()
            if mapping_value == "#microsoft.graph.targetedManagedAppProtection":
                from . import targeted_managed_app_protection

                return targeted_managed_app_protection.TargetedManagedAppProtection()
            if mapping_value == "#microsoft.graph.taskFileAttachment":
                from . import task_file_attachment

                return task_file_attachment.TaskFileAttachment()
            if mapping_value == "#microsoft.graph.team":
                from . import team

                return team.Team()
            if mapping_value == "#microsoft.graph.teamInfo":
                from . import team_info

                return team_info.TeamInfo()
            if mapping_value == "#microsoft.graph.teamsApp":
                from . import teams_app

                return teams_app.TeamsApp()
            if mapping_value == "#microsoft.graph.teamsAppDefinition":
                from . import teams_app_definition

                return teams_app_definition.TeamsAppDefinition()
            if mapping_value == "#microsoft.graph.teamsAppInstallation":
                from . import teams_app_installation

                return teams_app_installation.TeamsAppInstallation()
            if mapping_value == "#microsoft.graph.teamsAsyncOperation":
                from . import teams_async_operation

                return teams_async_operation.TeamsAsyncOperation()
            if mapping_value == "#microsoft.graph.teamsTab":
                from . import teams_tab

                return teams_tab.TeamsTab()
            if mapping_value == "#microsoft.graph.teamsTemplate":
                from . import teams_template

                return teams_template.TeamsTemplate()
            if mapping_value == "#microsoft.graph.teamwork":
                from . import teamwork

                return teamwork.Teamwork()
            if mapping_value == "#microsoft.graph.teamworkBot":
                from . import teamwork_bot

                return teamwork_bot.TeamworkBot()
            if mapping_value == "#microsoft.graph.teamworkHostedContent":
                from . import teamwork_hosted_content

                return teamwork_hosted_content.TeamworkHostedContent()
            if mapping_value == "#microsoft.graph.teamworkTag":
                from . import teamwork_tag

                return teamwork_tag.TeamworkTag()
            if mapping_value == "#microsoft.graph.teamworkTagMember":
                from . import teamwork_tag_member

                return teamwork_tag_member.TeamworkTagMember()
            if mapping_value == "#microsoft.graph.telecomExpenseManagementPartner":
                from . import telecom_expense_management_partner

                return telecom_expense_management_partner.TelecomExpenseManagementPartner()
            if mapping_value == "#microsoft.graph.temporaryAccessPassAuthenticationMethod":
                from . import temporary_access_pass_authentication_method

                return temporary_access_pass_authentication_method.TemporaryAccessPassAuthenticationMethod()
            if mapping_value == "#microsoft.graph.temporaryAccessPassAuthenticationMethodConfiguration":
                from . import temporary_access_pass_authentication_method_configuration

                return temporary_access_pass_authentication_method_configuration.TemporaryAccessPassAuthenticationMethodConfiguration()
            if mapping_value == "#microsoft.graph.tenantAppManagementPolicy":
                from . import tenant_app_management_policy

                return tenant_app_management_policy.TenantAppManagementPolicy()
            if mapping_value == "#microsoft.graph.termsAndConditions":
                from . import terms_and_conditions

                return terms_and_conditions.TermsAndConditions()
            if mapping_value == "#microsoft.graph.termsAndConditionsAcceptanceStatus":
                from . import terms_and_conditions_acceptance_status

                return terms_and_conditions_acceptance_status.TermsAndConditionsAcceptanceStatus()
            if mapping_value == "#microsoft.graph.termsAndConditionsAssignment":
                from . import terms_and_conditions_assignment

                return terms_and_conditions_assignment.TermsAndConditionsAssignment()
            if mapping_value == "#microsoft.graph.termsOfUseContainer":
                from . import terms_of_use_container

                return terms_of_use_container.TermsOfUseContainer()
            if mapping_value == "#microsoft.graph.termStore.group":
                from . import group
                from .term_store import group

                return group.Group()
            if mapping_value == "#microsoft.graph.termStore.relation":
                from .term_store import relation

                return relation.Relation()
            if mapping_value == "#microsoft.graph.termStore.set":
                from .term_store import set

                return set.Set()
            if mapping_value == "#microsoft.graph.termStore.store":
                from .term_store import store

                return store.Store()
            if mapping_value == "#microsoft.graph.termStore.term":
                from .term_store import term

                return term.Term()
            if mapping_value == "#microsoft.graph.threatAssessmentRequest":
                from . import threat_assessment_request

                return threat_assessment_request.ThreatAssessmentRequest()
            if mapping_value == "#microsoft.graph.threatAssessmentResult":
                from . import threat_assessment_result

                return threat_assessment_result.ThreatAssessmentResult()
            if mapping_value == "#microsoft.graph.thumbnailSet":
                from . import thumbnail_set

                return thumbnail_set.ThumbnailSet()
            if mapping_value == "#microsoft.graph.timeOff":
                from . import time_off

                return time_off.TimeOff()
            if mapping_value == "#microsoft.graph.timeOffReason":
                from . import time_off_reason

                return time_off_reason.TimeOffReason()
            if mapping_value == "#microsoft.graph.timeOffRequest":
                from . import time_off_request

                return time_off_request.TimeOffRequest()
            if mapping_value == "#microsoft.graph.todo":
                from . import todo

                return todo.Todo()
            if mapping_value == "#microsoft.graph.todoTask":
                from . import todo_task

                return todo_task.TodoTask()
            if mapping_value == "#microsoft.graph.todoTaskList":
                from . import todo_task_list

                return todo_task_list.TodoTaskList()
            if mapping_value == "#microsoft.graph.tokenIssuancePolicy":
                from . import token_issuance_policy

                return token_issuance_policy.TokenIssuancePolicy()
            if mapping_value == "#microsoft.graph.tokenLifetimePolicy":
                from . import token_lifetime_policy

                return token_lifetime_policy.TokenLifetimePolicy()
            if mapping_value == "#microsoft.graph.trending":
                from . import trending

                return trending.Trending()
            if mapping_value == "#microsoft.graph.unifiedRbacResourceAction":
                from . import unified_rbac_resource_action

                return unified_rbac_resource_action.UnifiedRbacResourceAction()
            if mapping_value == "#microsoft.graph.unifiedRbacResourceNamespace":
                from . import unified_rbac_resource_namespace

                return unified_rbac_resource_namespace.UnifiedRbacResourceNamespace()
            if mapping_value == "#microsoft.graph.unifiedRoleAssignment":
                from . import unified_role_assignment

                return unified_role_assignment.UnifiedRoleAssignment()
            if mapping_value == "#microsoft.graph.unifiedRoleAssignmentSchedule":
                from . import unified_role_assignment_schedule

                return unified_role_assignment_schedule.UnifiedRoleAssignmentSchedule()
            if mapping_value == "#microsoft.graph.unifiedRoleAssignmentScheduleInstance":
                from . import unified_role_assignment_schedule_instance

                return unified_role_assignment_schedule_instance.UnifiedRoleAssignmentScheduleInstance()
            if mapping_value == "#microsoft.graph.unifiedRoleAssignmentScheduleRequest":
                from . import unified_role_assignment_schedule_request

                return unified_role_assignment_schedule_request.UnifiedRoleAssignmentScheduleRequest()
            if mapping_value == "#microsoft.graph.unifiedRoleDefinition":
                from . import unified_role_definition

                return unified_role_definition.UnifiedRoleDefinition()
            if mapping_value == "#microsoft.graph.unifiedRoleEligibilitySchedule":
                from . import unified_role_eligibility_schedule

                return unified_role_eligibility_schedule.UnifiedRoleEligibilitySchedule()
            if mapping_value == "#microsoft.graph.unifiedRoleEligibilityScheduleInstance":
                from . import unified_role_eligibility_schedule_instance

                return unified_role_eligibility_schedule_instance.UnifiedRoleEligibilityScheduleInstance()
            if mapping_value == "#microsoft.graph.unifiedRoleEligibilityScheduleRequest":
                from . import unified_role_eligibility_schedule_request

                return unified_role_eligibility_schedule_request.UnifiedRoleEligibilityScheduleRequest()
            if mapping_value == "#microsoft.graph.unifiedRoleManagementPolicy":
                from . import unified_role_management_policy

                return unified_role_management_policy.UnifiedRoleManagementPolicy()
            if mapping_value == "#microsoft.graph.unifiedRoleManagementPolicyApprovalRule":
                from . import unified_role_management_policy_approval_rule

                return unified_role_management_policy_approval_rule.UnifiedRoleManagementPolicyApprovalRule()
            if mapping_value == "#microsoft.graph.unifiedRoleManagementPolicyAssignment":
                from . import unified_role_management_policy_assignment

                return unified_role_management_policy_assignment.UnifiedRoleManagementPolicyAssignment()
            if mapping_value == "#microsoft.graph.unifiedRoleManagementPolicyAuthenticationContextRule":
                from . import unified_role_management_policy_authentication_context_rule

                return unified_role_management_policy_authentication_context_rule.UnifiedRoleManagementPolicyAuthenticationContextRule()
            if mapping_value == "#microsoft.graph.unifiedRoleManagementPolicyEnablementRule":
                from . import unified_role_management_policy_enablement_rule

                return unified_role_management_policy_enablement_rule.UnifiedRoleManagementPolicyEnablementRule()
            if mapping_value == "#microsoft.graph.unifiedRoleManagementPolicyExpirationRule":
                from . import unified_role_management_policy_expiration_rule

                return unified_role_management_policy_expiration_rule.UnifiedRoleManagementPolicyExpirationRule()
            if mapping_value == "#microsoft.graph.unifiedRoleManagementPolicyNotificationRule":
                from . import unified_role_management_policy_notification_rule

                return unified_role_management_policy_notification_rule.UnifiedRoleManagementPolicyNotificationRule()
            if mapping_value == "#microsoft.graph.unifiedRoleManagementPolicyRule":
                from . import unified_role_management_policy_rule

                return unified_role_management_policy_rule.UnifiedRoleManagementPolicyRule()
            if mapping_value == "#microsoft.graph.unifiedRoleScheduleBase":
                from . import unified_role_schedule_base

                return unified_role_schedule_base.UnifiedRoleScheduleBase()
            if mapping_value == "#microsoft.graph.unifiedRoleScheduleInstanceBase":
                from . import unified_role_schedule_instance_base

                return unified_role_schedule_instance_base.UnifiedRoleScheduleInstanceBase()
            if mapping_value == "#microsoft.graph.unmuteParticipantOperation":
                from . import unmute_participant_operation

                return unmute_participant_operation.UnmuteParticipantOperation()
            if mapping_value == "#microsoft.graph.updateRecordingStatusOperation":
                from . import update_recording_status_operation

                return update_recording_status_operation.UpdateRecordingStatusOperation()
            if mapping_value == "#microsoft.graph.urlAssessmentRequest":
                from . import url_assessment_request

                return url_assessment_request.UrlAssessmentRequest()
            if mapping_value == "#microsoft.graph.usedInsight":
                from . import used_insight

                return used_insight.UsedInsight()
            if mapping_value == "#microsoft.graph.user":
                from . import user

                return user.User()
            if mapping_value == "#microsoft.graph.userActivity":
                from . import user_activity

                return user_activity.UserActivity()
            if mapping_value == "#microsoft.graph.userConsentRequest":
                from . import user_consent_request

                return user_consent_request.UserConsentRequest()
            if mapping_value == "#microsoft.graph.userExperienceAnalyticsDevicePerformance":
                from . import user_experience_analytics_device_performance

                return user_experience_analytics_device_performance.UserExperienceAnalyticsDevicePerformance()
            if mapping_value == "#microsoft.graph.userFlowLanguageConfiguration":
                from . import user_flow_language_configuration

                return user_flow_language_configuration.UserFlowLanguageConfiguration()
            if mapping_value == "#microsoft.graph.userFlowLanguagePage":
                from . import user_flow_language_page

                return user_flow_language_page.UserFlowLanguagePage()
            if mapping_value == "#microsoft.graph.userInstallStateSummary":
                from . import user_install_state_summary

                return user_install_state_summary.UserInstallStateSummary()
            if mapping_value == "#microsoft.graph.userScopeTeamsAppInstallation":
                from . import user_scope_teams_app_installation

                return user_scope_teams_app_installation.UserScopeTeamsAppInstallation()
            if mapping_value == "#microsoft.graph.userSettings":
                from . import user_settings

                return user_settings.UserSettings()
            if mapping_value == "#microsoft.graph.userTeamwork":
                from . import user_teamwork

                return user_teamwork.UserTeamwork()
            if mapping_value == "#microsoft.graph.voiceAuthenticationMethodConfiguration":
                from . import voice_authentication_method_configuration

                return voice_authentication_method_configuration.VoiceAuthenticationMethodConfiguration()
            if mapping_value == "#microsoft.graph.vppToken":
                from . import vpp_token

                return vpp_token.VppToken()
            if mapping_value == "#microsoft.graph.webApp":
                from . import web_app

                return web_app.WebApp()
            if mapping_value == "#microsoft.graph.win32LobApp":
                from . import win32_lob_app

                return win32_lob_app.Win32LobApp()
            if mapping_value == "#microsoft.graph.windows10CompliancePolicy":
                from . import windows10_compliance_policy

                return windows10_compliance_policy.Windows10CompliancePolicy()
            if mapping_value == "#microsoft.graph.windows10CustomConfiguration":
                from . import windows10_custom_configuration

                return windows10_custom_configuration.Windows10CustomConfiguration()
            if mapping_value == "#microsoft.graph.windows10EndpointProtectionConfiguration":
                from . import windows10_endpoint_protection_configuration

                return windows10_endpoint_protection_configuration.Windows10EndpointProtectionConfiguration()
            if mapping_value == "#microsoft.graph.windows10EnterpriseModernAppManagementConfiguration":
                from . import windows10_enterprise_modern_app_management_configuration

                return windows10_enterprise_modern_app_management_configuration.Windows10EnterpriseModernAppManagementConfiguration()
            if mapping_value == "#microsoft.graph.windows10GeneralConfiguration":
                from . import windows10_general_configuration

                return windows10_general_configuration.Windows10GeneralConfiguration()
            if mapping_value == "#microsoft.graph.windows10MobileCompliancePolicy":
                from . import windows10_mobile_compliance_policy

                return windows10_mobile_compliance_policy.Windows10MobileCompliancePolicy()
            if mapping_value == "#microsoft.graph.windows10SecureAssessmentConfiguration":
                from . import windows10_secure_assessment_configuration

                return windows10_secure_assessment_configuration.Windows10SecureAssessmentConfiguration()
            if mapping_value == "#microsoft.graph.windows10TeamGeneralConfiguration":
                from . import windows10_team_general_configuration

                return windows10_team_general_configuration.Windows10TeamGeneralConfiguration()
            if mapping_value == "#microsoft.graph.windows81CompliancePolicy":
                from . import windows81_compliance_policy

                return windows81_compliance_policy.Windows81CompliancePolicy()
            if mapping_value == "#microsoft.graph.windows81GeneralConfiguration":
                from . import windows81_general_configuration

                return windows81_general_configuration.Windows81GeneralConfiguration()
            if mapping_value == "#microsoft.graph.windowsAppX":
                from . import windows_app_x

                return windows_app_x.WindowsAppX()
            if mapping_value == "#microsoft.graph.windowsAutopilotDeviceIdentity":
                from . import windows_autopilot_device_identity

                return windows_autopilot_device_identity.WindowsAutopilotDeviceIdentity()
            if mapping_value == "#microsoft.graph.windowsDefenderAdvancedThreatProtectionConfiguration":
                from . import windows_defender_advanced_threat_protection_configuration

                return windows_defender_advanced_threat_protection_configuration.WindowsDefenderAdvancedThreatProtectionConfiguration()
            if mapping_value == "#microsoft.graph.windowsHelloForBusinessAuthenticationMethod":
                from . import windows_hello_for_business_authentication_method

                return windows_hello_for_business_authentication_method.WindowsHelloForBusinessAuthenticationMethod()
            if mapping_value == "#microsoft.graph.windowsInformationProtection":
                from . import windows_information_protection

                return windows_information_protection.WindowsInformationProtection()
            if mapping_value == "#microsoft.graph.windowsInformationProtectionAppLearningSummary":
                from . import windows_information_protection_app_learning_summary

                return windows_information_protection_app_learning_summary.WindowsInformationProtectionAppLearningSummary()
            if mapping_value == "#microsoft.graph.windowsInformationProtectionAppLockerFile":
                from . import windows_information_protection_app_locker_file

                return windows_information_protection_app_locker_file.WindowsInformationProtectionAppLockerFile()
            if mapping_value == "#microsoft.graph.windowsInformationProtectionNetworkLearningSummary":
                from . import windows_information_protection_network_learning_summary

                return windows_information_protection_network_learning_summary.WindowsInformationProtectionNetworkLearningSummary()
            if mapping_value == "#microsoft.graph.windowsInformationProtectionPolicy":
                from . import windows_information_protection_policy

                return windows_information_protection_policy.WindowsInformationProtectionPolicy()
            if mapping_value == "#microsoft.graph.windowsMicrosoftEdgeApp":
                from . import windows_microsoft_edge_app

                return windows_microsoft_edge_app.WindowsMicrosoftEdgeApp()
            if mapping_value == "#microsoft.graph.windowsMobileMSI":
                from . import windows_mobile_m_s_i

                return windows_mobile_m_s_i.WindowsMobileMSI()
            if mapping_value == "#microsoft.graph.windowsPhone81CompliancePolicy":
                from . import windows_phone81_compliance_policy

                return windows_phone81_compliance_policy.WindowsPhone81CompliancePolicy()
            if mapping_value == "#microsoft.graph.windowsPhone81CustomConfiguration":
                from . import windows_phone81_custom_configuration

                return windows_phone81_custom_configuration.WindowsPhone81CustomConfiguration()
            if mapping_value == "#microsoft.graph.windowsPhone81GeneralConfiguration":
                from . import windows_phone81_general_configuration

                return windows_phone81_general_configuration.WindowsPhone81GeneralConfiguration()
            if mapping_value == "#microsoft.graph.windowsUniversalAppX":
                from . import windows_universal_app_x

                return windows_universal_app_x.WindowsUniversalAppX()
            if mapping_value == "#microsoft.graph.windowsUniversalAppXContainedApp":
                from . import windows_universal_app_x_contained_app

                return windows_universal_app_x_contained_app.WindowsUniversalAppXContainedApp()
            if mapping_value == "#microsoft.graph.windowsUpdateForBusinessConfiguration":
                from . import windows_update_for_business_configuration

                return windows_update_for_business_configuration.WindowsUpdateForBusinessConfiguration()
            if mapping_value == "#microsoft.graph.windowsWebApp":
                from . import windows_web_app

                return windows_web_app.WindowsWebApp()
            if mapping_value == "#microsoft.graph.workbook":
                from . import workbook

                return workbook.Workbook()
            if mapping_value == "#microsoft.graph.workbookApplication":
                from . import workbook_application

                return workbook_application.WorkbookApplication()
            if mapping_value == "#microsoft.graph.workbookChart":
                from . import workbook_chart

                return workbook_chart.WorkbookChart()
            if mapping_value == "#microsoft.graph.workbookChartAreaFormat":
                from . import workbook_chart_area_format

                return workbook_chart_area_format.WorkbookChartAreaFormat()
            if mapping_value == "#microsoft.graph.workbookChartAxes":
                from . import workbook_chart_axes

                return workbook_chart_axes.WorkbookChartAxes()
            if mapping_value == "#microsoft.graph.workbookChartAxis":
                from . import workbook_chart_axis

                return workbook_chart_axis.WorkbookChartAxis()
            if mapping_value == "#microsoft.graph.workbookChartAxisFormat":
                from . import workbook_chart_axis_format

                return workbook_chart_axis_format.WorkbookChartAxisFormat()
            if mapping_value == "#microsoft.graph.workbookChartAxisTitle":
                from . import workbook_chart_axis_title

                return workbook_chart_axis_title.WorkbookChartAxisTitle()
            if mapping_value == "#microsoft.graph.workbookChartAxisTitleFormat":
                from . import workbook_chart_axis_title_format

                return workbook_chart_axis_title_format.WorkbookChartAxisTitleFormat()
            if mapping_value == "#microsoft.graph.workbookChartDataLabelFormat":
                from . import workbook_chart_data_label_format

                return workbook_chart_data_label_format.WorkbookChartDataLabelFormat()
            if mapping_value == "#microsoft.graph.workbookChartDataLabels":
                from . import workbook_chart_data_labels

                return workbook_chart_data_labels.WorkbookChartDataLabels()
            if mapping_value == "#microsoft.graph.workbookChartFill":
                from . import workbook_chart_fill

                return workbook_chart_fill.WorkbookChartFill()
            if mapping_value == "#microsoft.graph.workbookChartFont":
                from . import workbook_chart_font

                return workbook_chart_font.WorkbookChartFont()
            if mapping_value == "#microsoft.graph.workbookChartGridlines":
                from . import workbook_chart_gridlines

                return workbook_chart_gridlines.WorkbookChartGridlines()
            if mapping_value == "#microsoft.graph.workbookChartGridlinesFormat":
                from . import workbook_chart_gridlines_format

                return workbook_chart_gridlines_format.WorkbookChartGridlinesFormat()
            if mapping_value == "#microsoft.graph.workbookChartLegend":
                from . import workbook_chart_legend

                return workbook_chart_legend.WorkbookChartLegend()
            if mapping_value == "#microsoft.graph.workbookChartLegendFormat":
                from . import workbook_chart_legend_format

                return workbook_chart_legend_format.WorkbookChartLegendFormat()
            if mapping_value == "#microsoft.graph.workbookChartLineFormat":
                from . import workbook_chart_line_format

                return workbook_chart_line_format.WorkbookChartLineFormat()
            if mapping_value == "#microsoft.graph.workbookChartPoint":
                from . import workbook_chart_point

                return workbook_chart_point.WorkbookChartPoint()
            if mapping_value == "#microsoft.graph.workbookChartPointFormat":
                from . import workbook_chart_point_format

                return workbook_chart_point_format.WorkbookChartPointFormat()
            if mapping_value == "#microsoft.graph.workbookChartSeries":
                from . import workbook_chart_series

                return workbook_chart_series.WorkbookChartSeries()
            if mapping_value == "#microsoft.graph.workbookChartSeriesFormat":
                from . import workbook_chart_series_format

                return workbook_chart_series_format.WorkbookChartSeriesFormat()
            if mapping_value == "#microsoft.graph.workbookChartTitle":
                from . import workbook_chart_title

                return workbook_chart_title.WorkbookChartTitle()
            if mapping_value == "#microsoft.graph.workbookChartTitleFormat":
                from . import workbook_chart_title_format

                return workbook_chart_title_format.WorkbookChartTitleFormat()
            if mapping_value == "#microsoft.graph.workbookComment":
                from . import workbook_comment

                return workbook_comment.WorkbookComment()
            if mapping_value == "#microsoft.graph.workbookCommentReply":
                from . import workbook_comment_reply

                return workbook_comment_reply.WorkbookCommentReply()
            if mapping_value == "#microsoft.graph.workbookFilter":
                from . import workbook_filter

                return workbook_filter.WorkbookFilter()
            if mapping_value == "#microsoft.graph.workbookFormatProtection":
                from . import workbook_format_protection

                return workbook_format_protection.WorkbookFormatProtection()
            if mapping_value == "#microsoft.graph.workbookFunctionResult":
                from . import workbook_function_result

                return workbook_function_result.WorkbookFunctionResult()
            if mapping_value == "#microsoft.graph.workbookFunctions":
                from . import workbook_functions

                return workbook_functions.WorkbookFunctions()
            if mapping_value == "#microsoft.graph.workbookNamedItem":
                from . import workbook_named_item

                return workbook_named_item.WorkbookNamedItem()
            if mapping_value == "#microsoft.graph.workbookOperation":
                from . import workbook_operation

                return workbook_operation.WorkbookOperation()
            if mapping_value == "#microsoft.graph.workbookPivotTable":
                from . import workbook_pivot_table

                return workbook_pivot_table.WorkbookPivotTable()
            if mapping_value == "#microsoft.graph.workbookRange":
                from . import workbook_range

                return workbook_range.WorkbookRange()
            if mapping_value == "#microsoft.graph.workbookRangeBorder":
                from . import workbook_range_border

                return workbook_range_border.WorkbookRangeBorder()
            if mapping_value == "#microsoft.graph.workbookRangeFill":
                from . import workbook_range_fill

                return workbook_range_fill.WorkbookRangeFill()
            if mapping_value == "#microsoft.graph.workbookRangeFont":
                from . import workbook_range_font

                return workbook_range_font.WorkbookRangeFont()
            if mapping_value == "#microsoft.graph.workbookRangeFormat":
                from . import workbook_range_format

                return workbook_range_format.WorkbookRangeFormat()
            if mapping_value == "#microsoft.graph.workbookRangeSort":
                from . import workbook_range_sort

                return workbook_range_sort.WorkbookRangeSort()
            if mapping_value == "#microsoft.graph.workbookRangeView":
                from . import workbook_range_view

                return workbook_range_view.WorkbookRangeView()
            if mapping_value == "#microsoft.graph.workbookTable":
                from . import workbook_table

                return workbook_table.WorkbookTable()
            if mapping_value == "#microsoft.graph.workbookTableColumn":
                from . import workbook_table_column

                return workbook_table_column.WorkbookTableColumn()
            if mapping_value == "#microsoft.graph.workbookTableRow":
                from . import workbook_table_row

                return workbook_table_row.WorkbookTableRow()
            if mapping_value == "#microsoft.graph.workbookTableSort":
                from . import workbook_table_sort

                return workbook_table_sort.WorkbookTableSort()
            if mapping_value == "#microsoft.graph.workbookWorksheet":
                from . import workbook_worksheet

                return workbook_worksheet.WorkbookWorksheet()
            if mapping_value == "#microsoft.graph.workbookWorksheetProtection":
                from . import workbook_worksheet_protection

                return workbook_worksheet_protection.WorkbookWorksheetProtection()
            if mapping_value == "#microsoft.graph.workforceIntegration":
                from . import workforce_integration

                return workforce_integration.WorkforceIntegration()
            if mapping_value == "#microsoft.graph.x509CertificateAuthenticationMethodConfiguration":
                from . import x509_certificate_authentication_method_configuration

                return x509_certificate_authentication_method_configuration.X509CertificateAuthenticationMethodConfiguration()
        return Entity()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import aad_user_conversation_member, access_package, access_package_assignment, access_package_assignment_policy, access_package_assignment_request, access_package_catalog, access_package_multiple_choice_question, access_package_question, access_package_subject, access_package_text_input_question, access_review_history_definition, access_review_history_instance, access_review_instance, access_review_instance_decision_item, access_review_reviewer, access_review_schedule_definition, access_review_set, access_review_stage, activity_based_timeout_policy, activity_history_item, add_large_gallery_view_operation, administrative_unit, admin_consent_request_policy, agreement, agreement_acceptance, agreement_file, agreement_file_localization, agreement_file_properties, agreement_file_version, alert, allowed_value, android_compliance_policy, android_custom_configuration, android_general_device_configuration, android_lob_app, android_managed_app_protection, android_managed_app_registration, android_store_app, android_work_profile_compliance_policy, android_work_profile_custom_configuration, android_work_profile_general_device_configuration, anonymous_guest_conversation_member, apple_device_features_configuration_base, apple_managed_identity_provider, apple_push_notification_certificate, application, application_template, approval, approval_stage, app_catalogs, app_consent_approval_route, app_consent_request, app_management_policy, app_role_assignment, app_scope, associated_team_info, attachment, attachment_base, attachment_session, attack_simulation_root, attendance_record, attribute_set, audio_routing_group, audit_event, audit_log_root, authentication, authentication_combination_configuration, authentication_context_class_reference, authentication_flows_policy, authentication_method, authentication_methods_policy, authentication_method_configuration, authentication_method_mode_detail, authentication_method_target, authentication_strength_policy, authentication_strength_root, authored_note, authorization_policy, azure_communication_services_user_conversation_member, b2x_identity_user_flow, base_item, base_item_version, bitlocker, bitlocker_recovery_key, booking_appointment, booking_business, booking_currency, booking_customer, booking_customer_base, booking_custom_question, booking_service, booking_staff_member, booking_staff_member_base, browser_shared_cookie, browser_site, browser_site_list, built_in_identity_provider, calendar, calendar_group, calendar_permission, calendar_sharing_message, call, cancel_media_processing_operation, certificate_based_auth_configuration, change_tracked_entity, channel, chat, chat_message, chat_message_hosted_content, chat_message_info, checklist_item, claims_mapping_policy, column_definition, column_link, comms_operation, compliance_management_partner, conditional_access_policy, conditional_access_root, conditional_access_template, connected_organization, contact, contact_folder, content_sharing_session, content_type, contract, conversation, conversation_member, conversation_thread, country_named_location, cross_tenant_access_policy, cross_tenant_access_policy_configuration_default, custom_security_attribute_definition, data_policy_operation, default_managed_app_protection, delegated_admin_access_assignment, delegated_admin_customer, delegated_admin_relationship, delegated_admin_relationship_operation, delegated_admin_relationship_request, delegated_admin_service_management_detail, delegated_permission_classification, deleted_team, detected_app, device, device_and_app_management_role_assignment, device_and_app_management_role_definition, device_app_management, device_category, device_compliance_action_item, device_compliance_device_overview, device_compliance_device_status, device_compliance_policy, device_compliance_policy_assignment, device_compliance_policy_device_state_summary, device_compliance_policy_setting_state_summary, device_compliance_policy_state, device_compliance_scheduled_action_for_rule, device_compliance_setting_state, device_compliance_user_overview, device_compliance_user_status, device_configuration, device_configuration_assignment, device_configuration_device_overview, device_configuration_device_state_summary, device_configuration_device_status, device_configuration_state, device_configuration_user_overview, device_configuration_user_status, device_enrollment_configuration, device_enrollment_limit_configuration, device_enrollment_platform_restrictions_configuration, device_enrollment_windows_hello_for_business_configuration, device_install_state, device_management, device_management_exchange_connector, device_management_export_job, device_management_partner, device_management_reports, device_management_troubleshooting_event, directory, directory_audit, directory_object, directory_object_partner_reference, directory_role, directory_role_template, document_set_version, domain, domain_dns_cname_record, domain_dns_mx_record, domain_dns_record, domain_dns_srv_record, domain_dns_txt_record, domain_dns_unavailable_record, drive, drive_item, drive_item_version, edge, edition_upgrade_configuration, education_assignment, education_assignment_defaults, education_assignment_resource, education_assignment_settings, education_category, education_class, education_feedback_outcome, education_feedback_resource_outcome, education_organization, education_outcome, education_points_outcome, education_rubric, education_rubric_outcome, education_school, education_submission, education_submission_resource, education_user, email_authentication_method, email_authentication_method_configuration, email_file_assessment_request, endpoint, enrollment_configuration_assignment, enrollment_troubleshooting_event, enterprise_code_signing_certificate, entitlement_management, entitlement_management_settings, event, event_message, event_message_request, event_message_response, extension, extension_property, external_domain_name, e_book_install_summary, feature_rollout_policy, federated_identity_credential, fido2_authentication_method, fido2_authentication_method_configuration, fido2_combination_configuration, field_value_set, file_assessment_request, file_attachment, group, group_lifecycle_policy, group_setting, group_setting_template, home_realm_discovery_policy, identity_api_connector, identity_built_in_user_flow_attribute, identity_container, identity_custom_user_flow_attribute, identity_provider, identity_provider_base, identity_security_defaults_enforcement_policy, identity_user_flow, identity_user_flow_attribute, identity_user_flow_attribute_assignment, imported_windows_autopilot_device_identity, imported_windows_autopilot_device_identity_upload, inference_classification, inference_classification_override, internal_domain_federation, internet_explorer_mode, invitation, invite_participants_operation, iosi_pad_o_s_web_clip, ios_certificate_profile, ios_compliance_policy, ios_custom_configuration, ios_device_features_configuration, ios_general_device_configuration, ios_lob_app, ios_lob_app_provisioning_configuration_assignment, ios_managed_app_protection, ios_managed_app_registration, ios_mobile_app_configuration, ios_store_app, ios_update_configuration, ios_update_device_status, ios_vpp_app, ios_vpp_e_book, ios_vpp_e_book_assignment, ip_named_location, item_activity, item_activity_stat, item_analytics, item_attachment, learning_content, learning_provider, license_details, linked_resource, list, list_item, list_item_version, localized_notification_message, long_running_operation, mac_o_s_compliance_policy, mac_o_s_custom_configuration, mac_o_s_device_features_configuration, mac_o_s_general_device_configuration, mac_o_s_lob_app, mac_o_s_microsoft_edge_app, mac_o_s_office_suite_app, mail_assessment_request, mail_folder, mail_search_folder, managed_android_lob_app, managed_android_store_app, managed_app, managed_app_configuration, managed_app_operation, managed_app_policy, managed_app_policy_deployment_summary, managed_app_protection, managed_app_registration, managed_app_status, managed_app_status_raw, managed_device, managed_device_mobile_app_configuration, managed_device_mobile_app_configuration_assignment, managed_device_mobile_app_configuration_device_status, managed_device_mobile_app_configuration_device_summary, managed_device_mobile_app_configuration_user_status, managed_device_mobile_app_configuration_user_summary, managed_device_overview, managed_e_book, managed_e_book_assignment, managed_i_o_s_lob_app, managed_i_o_s_store_app, managed_mobile_app, managed_mobile_lob_app, mdm_windows_information_protection_policy, meeting_attendance_report, message, message_rule, microsoft_account_user_conversation_member, microsoft_authenticator_authentication_method, microsoft_authenticator_authentication_method_configuration, microsoft_authenticator_authentication_method_target, microsoft_store_for_business_app, mobile_app, mobile_app_assignment, mobile_app_category, mobile_app_content, mobile_app_content_file, mobile_contained_app, mobile_lob_app, mobile_threat_defense_connector, multi_value_legacy_extended_property, mute_participant_operation, named_location, notebook, notification_message_template, offer_shift_request, office_graph_insights, onenote, onenote_entity_base_model, onenote_entity_hierarchy_model, onenote_entity_schema_object_model, onenote_operation, onenote_page, onenote_resource, onenote_section, online_meeting, on_premises_conditional_access_settings, on_premises_directory_synchronization, open_shift, open_shift_change_request, open_type_extension, operation, organization, organizational_branding, organizational_branding_localization, organizational_branding_properties, org_contact, outlook_category, outlook_item, outlook_user, o_auth2_permission_grant, participant, participant_joining_notification, participant_left_notification, password_authentication_method, permission, permission_grant_condition_set, permission_grant_policy, person, phone_authentication_method, pinned_chat_message_info, place, planner, planner_assigned_to_task_board_task_format, planner_bucket, planner_bucket_task_board_task_format, planner_group, planner_plan, planner_plan_details, planner_progress_task_board_task_format, planner_task, planner_task_details, planner_user, play_prompt_operation, policy_base, policy_root, post, presence, printer, printer_base, printer_create_operation, printer_share, print_connector, print_document, print_job, print_operation, print_service, print_service_endpoint, print_task, print_task_definition, print_task_trigger, print_usage, print_usage_by_printer, print_usage_by_user, profile_photo, provisioning_object_summary, rbac_application, record_operation, reference_attachment, remote_assistance_partner, request, resource_operation, resource_specific_permission_grant, rich_long_running_operation, risky_service_principal, risky_service_principal_history_item, risky_user, risky_user_history_item, risk_detection, role_assignment, role_definition, room, room_list, saml_or_ws_fed_external_domain_federation, saml_or_ws_fed_provider, schedule, schedule_change_request, scheduling_group, schema_extension, scoped_role_membership, search_entity, section_group, secure_score, secure_score_control_profile, security_reports_root, service_announcement, service_announcement_attachment, service_announcement_base, service_health, service_health_issue, service_principal, service_principal_risk_detection, service_update_message, setting_state_device_summary, shared_drive_item, shared_insight, shared_p_c_configuration, shared_with_channel_team_info, sharepoint, sharepoint_settings, shift, shift_preferences, sign_in, simulation, simulation_automation, simulation_automation_run, single_value_legacy_extended_property, site, skype_for_business_user_conversation_member, skype_user_conversation_member, sms_authentication_method_configuration, sms_authentication_method_target, social_identity_provider, software_oath_authentication_method, software_oath_authentication_method_configuration, software_update_status_summary, start_hold_music_operation, stop_hold_music_operation, sts_policy, subject_rights_request, subscribed_sku, subscribe_to_tone_operation, subscription, swap_shifts_change_request, targeted_managed_app_configuration, targeted_managed_app_policy_assignment, targeted_managed_app_protection, task_file_attachment, team, teams_app, teams_app_definition, teams_app_installation, teams_async_operation, teams_tab, teams_template, teamwork, teamwork_bot, teamwork_hosted_content, teamwork_tag, teamwork_tag_member, team_info, telecom_expense_management_partner, temporary_access_pass_authentication_method, temporary_access_pass_authentication_method_configuration, tenant_app_management_policy, terms_and_conditions, terms_and_conditions_acceptance_status, terms_and_conditions_assignment, terms_of_use_container, threat_assessment_request, threat_assessment_result, thumbnail_set, time_off, time_off_reason, time_off_request, todo, todo_task, todo_task_list, token_issuance_policy, token_lifetime_policy, trending, unified_rbac_resource_action, unified_rbac_resource_namespace, unified_role_assignment, unified_role_assignment_schedule, unified_role_assignment_schedule_instance, unified_role_assignment_schedule_request, unified_role_definition, unified_role_eligibility_schedule, unified_role_eligibility_schedule_instance, unified_role_eligibility_schedule_request, unified_role_management_policy, unified_role_management_policy_approval_rule, unified_role_management_policy_assignment, unified_role_management_policy_authentication_context_rule, unified_role_management_policy_enablement_rule, unified_role_management_policy_expiration_rule, unified_role_management_policy_notification_rule, unified_role_management_policy_rule, unified_role_schedule_base, unified_role_schedule_instance_base, unmute_participant_operation, update_recording_status_operation, url_assessment_request, used_insight, user, user_activity, user_consent_request, user_experience_analytics_device_performance, user_flow_language_configuration, user_flow_language_page, user_install_state_summary, user_scope_teams_app_installation, user_settings, user_teamwork, voice_authentication_method_configuration, vpp_token, web_app, win32_lob_app, windows10_compliance_policy, windows10_custom_configuration, windows10_endpoint_protection_configuration, windows10_enterprise_modern_app_management_configuration, windows10_general_configuration, windows10_mobile_compliance_policy, windows10_secure_assessment_configuration, windows10_team_general_configuration, windows81_compliance_policy, windows81_general_configuration, windows_app_x, windows_autopilot_device_identity, windows_defender_advanced_threat_protection_configuration, windows_hello_for_business_authentication_method, windows_information_protection, windows_information_protection_app_learning_summary, windows_information_protection_app_locker_file, windows_information_protection_network_learning_summary, windows_information_protection_policy, windows_microsoft_edge_app, windows_mobile_m_s_i, windows_phone81_compliance_policy, windows_phone81_custom_configuration, windows_phone81_general_configuration, windows_universal_app_x, windows_universal_app_x_contained_app, windows_update_for_business_configuration, windows_web_app, workbook, workbook_application, workbook_chart, workbook_chart_area_format, workbook_chart_axes, workbook_chart_axis, workbook_chart_axis_format, workbook_chart_axis_title, workbook_chart_axis_title_format, workbook_chart_data_labels, workbook_chart_data_label_format, workbook_chart_fill, workbook_chart_font, workbook_chart_gridlines, workbook_chart_gridlines_format, workbook_chart_legend, workbook_chart_legend_format, workbook_chart_line_format, workbook_chart_point, workbook_chart_point_format, workbook_chart_series, workbook_chart_series_format, workbook_chart_title, workbook_chart_title_format, workbook_comment, workbook_comment_reply, workbook_filter, workbook_format_protection, workbook_functions, workbook_function_result, workbook_named_item, workbook_operation, workbook_pivot_table, workbook_range, workbook_range_border, workbook_range_fill, workbook_range_font, workbook_range_format, workbook_range_sort, workbook_range_view, workbook_table, workbook_table_column, workbook_table_row, workbook_table_sort, workbook_worksheet, workbook_worksheet_protection, workforce_integration, x509_certificate_authentication_method_configuration
        from .call_records import call_record, segment, session
        from .external_connectors import connection_operation, external_connection, external_group, external_item, identity, schema
        from .security import alert, case, cases_root, case_operation, data_set, data_source, data_source_container, ediscovery_add_to_review_set_operation, ediscovery_case, ediscovery_case_settings, ediscovery_custodian, ediscovery_estimate_operation, ediscovery_hold_operation, ediscovery_index_operation, ediscovery_noncustodial_data_source, ediscovery_purge_data_operation, ediscovery_review_set, ediscovery_review_set_query, ediscovery_review_tag, ediscovery_search, ediscovery_tag_operation, incident, retention_event, retention_event_type, search, security, site_source, tag, triggers_root, trigger_types_root, unified_group_source, user_source
        from .term_store import group, relation, set, store, term

        fields: Dict[str, Callable[[Any], None]] = {
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def id(self,) -> Optional[str]:
        """
        Gets the id property value. The unique idenfier for an entity. Read-only.
        Returns: Optional[str]
        """
        return self._id
    
    @id.setter
    def id(self,value: Optional[str] = None) -> None:
        """
        Sets the id property value. The unique idenfier for an entity. Read-only.
        Args:
            value: Value to set for the id property.
        """
        self._id = value
    
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
            value: Value to set for the odata_type property.
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
        writer.write_str_value("id", self.id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

