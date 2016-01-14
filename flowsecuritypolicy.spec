{
    "attributes": {
        "action": {
            "description": "The flow action. The action can be either FORWARD or DROP.",
            "allowed_choices": [
                "FORWARD",
                "DROP",
                "REDIRECT"
            ],
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "associatedApplicationServiceID": {
            "description": "The associated service id.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "associatedNetworkObjectID": {
            "description": "The associated network object id.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "associatedNetworkObjectType": {
            "description": "The associated network object type. Refer to API section for supported types.",
            "allowed_choices": [
                "UNSUPPORTED",
                "NETWORK_ELEMENT",
                "NETWORK_LAYOUT",
                "ENTERPRISE",
                "ENTERPRISE_PROFILE",
                "GROUP",
                "USER",
                "DOMAIN_FLOATING_IP_ACL_TEMPLATE",
                "DOMAIN_FLOATING_IP_ACL_TEMPLATE_ENTRY",
                "FLOATING_IP_ACL_TEMPLATE",
                "FLOATING_IP_ACL_TEMPLATE_ENTRY",
                "FLOATINGIP_ACL",
                "FLOATINGIP_ACL_ENTRY",
                "INGRESS_ACL_TEMPLATE",
                "INGRESS_ACL_TEMPLATE_ENTRY",
                "INGRESS_ACL",
                "INGRESS_ACL_ENTRY",
                "INGRESS_ADV_FWD_TEMPLATE",
                "INGRESS_ADV_FWD_TEMPLATE_ENTRY",
                "INGRESS_ADV_FWD",
                "INGRESS_ADV_FWD_ENTRY",
                "INGRESS_EXT_SERVICE_TEMPLATE",
                "INGRESS_EXT_SERVICE_TEMPLATE_ENTRY",
                "INGRESS_EXT_SERVICE",
                "INGRESS_EXT_SERVICE_ENTRY",
                "EGRESS_ACL_TEMPLATE",
                "EGRESS_ACL_TEMPLATE_ENTRY",
                "EGRESS_ACL",
                "EGRESS_ACL_ENTRY",
                "POLICING_POLICY",
                "SHAPING_POLICY",
                "QOS_PRIMITIVE",
                "EGRESS_QOS_PRIMITIVE",
                "EGRESS_QOS_QUEUE_MR",
                "EGRESS_QOS_MR",
                "PORT_MR",
                "RATE_LIMITER",
                "DSCP_FORWARDING_CLASS_MAPPING",
                "DSCP_FORWARDING_CLASS_TABLE",
                "APPLICATION",
                "VIRTUAL_MACHINE",
                "SUBNET",
                "ADDRESS_RANGE",
                "ADDRESS_RANGE_STATE",
                "IP_BINDING",
                "L2DOMAIN",
                "L2DOMAIN_SHARED",
                "L2DOMAIN_TEMPLATE",
                "SUBNET_ENTRY",
                "SUBNET_MAC_ENTRY",
                "ENTERPRISE_NETWORK",
                "NETWORK_MACRO_GROUP",
                "PUBLIC_NETWORK",
                "SUBNET_TEMPLATE",
                "VM_INTERFACE",
                "VM_DESCRIPTION",
                "POLICY_DECISION",
                "CUSTOMER_VRF_SEQUENCENO",
                "SERVICE_VRF_SEQUENCENO",
                "DOMAIN",
                "VPN_CONNECT",
                "ZONE",
                "FLOATINGIP",
                "SUBNET_POOL_ENTRY",
                "DOMAIN_TEMPLATE",
                "ZONE_TEMPLATE",
                "PERMISSION",
                "PERMITTED_ACTION",
                "STATS_TCA",
                "STATS_POLICY",
                "STATS_COLLECTOR",
                "STATISTICS",
                "ALARM",
                "EVENT_LOG",
                "DHCP_OPTION",
                "STATIC_ROUTE",
                "DC_CONFIG",
                "RESYNC",
                "VPRN_LABEL_SEQUENCENO",
                "LDAP_CONFIG",
                "LICENSE",
                "VPORT",
                "VPORT_GATEWAY_RESPONSE",
                "SERVICE_GATEWAY_RESPONSE",
                "SERVICES_GATEWAY_RESPONSE",
                "VPORTTAGTEMPLATE",
                "VPORTTAG",
                "POLICY_GROUP_TEMPLATE",
                "HOSTINTERFACE",
                "BRIDGEINTERFACE",
                "VIRTUAL_IP",
                "VPORT_TAG_BASE",
                "POLICY_GROUP",
                "VNID_SEQUENCENO",
                "ESI_SEQUENCENO",
                "SYSTEM_CONFIG",
                "SYSTEM_CONFIG_REQ",
                "SYSTEM_CONFIG_RESP",
                "SHARED_RESOURCE",
                "RTRD_SEQUENCENO",
                "RD_SEQUENCENO",
                "RTRD_ENTITY",
                "EVPN_BGP_COMMUNITY_TAG_SEQ_NO",
                "EVPN_BGP_COMMUNITY_TAG_ENTRY",
                "VPORT_MEDIATION_REQUEST",
                "NODE_EXECUTION_ERROR",
                "MIRROR_DESTINATION",
                "VPORT_MIRROR",
                "GATEWAY",
                "NSGATEWAY",
                "GATEWAY_TEMPLATE",
                "NSGATEWAY_TEMPLATE",
                "AUTO_DISC_GATEWAY",
                "PORT",
                "NSPORT",
                "NS_REDUNDANT_PORT",
                "VSG_REDUNDANT_PORT",
                "PORT_TEMPLATE",
                "NSPORT_TEMPLATE",
                "VLAN",
                "VLAN_TEMPLATE",
                "VLAN_CONFIG_RESPONSE",
                "REDUNDANT_GW_GRP",
                "NSREDUNDANT_GW_GRP",
                "WAN_SERVICE",
                "GATEWAY_VPORT_CONFIG",
                "GATEWAY_SERVICE_CONFIG",
                "GATEWAY_SERVICE_CONFIG_RESP",
                "GATEWAY_VPORT_CONFIG_RESP",
                "GATEWAY_CONFIG",
                "NSGATEWAY_CONFIG",
                "GATEWAY_CONFIG_RESP",
                "ENTERPRISE_CONFIG",
                "ENTERPRISE_CONFIG_RESP",
                "DHCP_CONFIG_RESP",
                "DHCP_ALLOC_MESSAGE",
                "VSC",
                "HSC",
                "VSD",
                "VRS",
                "STATSSERVER",
                "VSP",
                "VSD_COMPONENT",
                "SYSTEM_MONITORING",
                "DISKSTATS",
                "MONITORING_PORT",
                "BGPPEER",
                "JOB",
                "ENTERPRISE_PERMISSION",
                "VIRTUAL_MACHINE_REPORT",
                "BOOTSTRAP",
                "LOCATION",
                "BOOTSTRAP_ACTIVATION",
                "INFRASTRUCTURE_GATEWAY_PROFILE",
                "INFRASTRUCTURE_PORT_PROFILE",
                "INFRASTRUCTURE_VSC_PROFILE",
                "INFRASTRUCTURE_CONFIG",
                "NSPORT_STATIC_CONFIG",
                "NSG_NOTIFICATION",
                "SITE",
                "SITE_REQ",
                "HEALTH_REQ",
                "SITE_RES",
                "GEO_VM_REQ",
                "GEO_VM_RES",
                "GEO_VM_EVENT",
                "METADATA",
                "METADATA_TAG",
                "ENTITY_METADATA_BINDING",
                "CHILD_ENTITY_POLICY_CHANGE",
                "MULTI_NIC_VPORT",
                "BACK_HAUL_SERVICE_RESP",
                "MC_CHANNEL_MAP",
                "MC_LIST",
                "MC_RANGE",
                "LIBVIRT_INTERFACE",
                "APPD_APPLICATION",
                "APPD_SERVICE",
                "APPD_TIER",
                "APPD_FLOW",
                "APPD_FLOW_SECURITY_POLICY",
                "APPD_FLOW_FORWARDING_POLICY",
                "APPD_EXTERNAL_APP_SERVICE",
                "PATNATPOOL",
                "NATMAPENTRY",
                "PATCONFIG_CONFIG_RESP",
                "NETWORK_POLICY_GROUP",
                "ACLENTRY_LOCATION",
                "EXPORTIMPORT",
                "EXTERNAL_SERVICE",
                "ENDPOINT",
                "DOMAIN_CONFIG",
                "DOMAIN_CONFIG_RESP",
                "STATIC_ROUTE_RESP",
                "NEXT_HOP_RESP",
                "UPLINK_RD",
                "VMWARE_VCENTER_EAM_CONFIG",
                "VMWARE_VCENTER_VRS_CONFIG",
                "VMWARE_VCENTER",
                "VMWARE_VCENTER_DATACENTER",
                "VMWARE_VCENTER_CLUSTER",
                "VMWARE_VCENTER_HYPERVISOR",
                "VMWARE_VRS_ADDRESS_RANGE",
                "VMWARE_VCENTER_VRS_BASE_CONFIG",
                "VMWARE_RELOAD_CONFIG",
                "CLOUD_MGMT_SYSTEM",
                "IKEV2_ENCRYPTION_PROFILE",
                "IKEV2_GATEWAY",
                "GROUPKEY_ENCRYPTION_PROFILE",
                "KEYSERVER_MEMBER",
                "KEYSERVER_MONITOR",
                "KEYSERVER_MONITOR_SEED",
                "KEYSERVER_MONITOR_ENCRYPTED_SEED",
                "KEYSERVER_MONITOR_SEK",
                "KEYSERVER_NOTIFICATION",
                "ENTERPRISE_SECURITY",
                "ENTERPRISE_SECURED_DATA",
                "GATEWAY_SECURITY",
                "GATEWAY_SECURITY_REQUEST",
                "GATEWAY_SECURITY_RESPONSE",
                "GATEWAY_SECURITY_PROFILE",
                "GATEWAY_SECURITY_PROFILE_REQUEST",
                "GATEWAY_SECURITY_PROFILE_RESPONSE",
                "GATEWAY_SECURED_DATA",
                "CERTIFICATE",
                "BGP_PROFILE",
                "ROUTING_POLICY",
                "BGP_NEIGHBOR",
                "BGP_PROFILE_MED_RESPONSE",
                "ROUTING_POL_MED_RESPONSE",
                "BGP_NEIGHBOR_MED_RESPONSE"
            ],
            "exposed": true,
            "filterable": true,
            "orderable": true,
            "type": "enum",
            "uniqueScope": "no"
        },
        "destinationAddressOverwrite": {
            "description": "The destination address overwrite. Needs to be in CIDR format x.x.x.x/n",
            "exposed": true,
            "filterable": true,
            "format": "CIDR",
            "orderable": true,
            "type": "string",
            "min_length": 1,
            "max_length": 50,
            "uniqueScope": "no"
        },
        "flowID": {
            "description": "The associated service id.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "orderable": false,
            "type": "string",
            "uniqueScope": "no"
        },
        "priority": {
            "description": "The priority of the flow security policy that determines the order of entries.",
            "exposed": true,
            "filterable": true,
            "orderable": false,
            "type": "integer",
            "min_value": 0,
            "uniqueScope": "no"
        },
        "sourceAddressOverwrite": {
            "description": "The source address overwrite. Needs to be in CIDR format x.x.x.x/n",
            "exposed": true,
            "filterable": true,
            "format": "CIDR",
            "orderable": true,
            "type": "string",
            "min_length": 1,
            "max_length": 50,
            "uniqueScope": "no"
        }
    },
    "children": {
        "eventlog": {
            "get": true,
            "relationship": "child"
        }
    },
    "model": {
        "delete": true,
        "description": "The security policy on the flow.",
        "entity_name": "FlowSecurityPolicy",
        "extends": [
            "@base",
            "@metadata"
        ],
        "get": true,
        "package": "appd",
        "resource_name": "flowsecuritypolicies",
        "rest_name": "flowsecuritypolicy",
        "update": true
    }
}