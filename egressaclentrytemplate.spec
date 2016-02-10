{
    "attributes": {
        "DSCP": {
            "description": "DSCP match condition to be set in the rule. It is either * or from 0-63",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "action": {
            "allowed_choices": [
                "FORWARD",
                "REDIRECT",
                "DROP"
            ],
            "description": "The action of the ACL entry DROP or FORWARD or REDIRECT. Action REDIRECT is allowed only for IngressAdvancedForwardingEntry Possible values are DROP, FORWARD, REDIRECT, .",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "enum",
            "uniqueScope": "no"
        },
        "addressOverride": {
            "description": "Overrides the source IP for Ingress and destination IP for Egress, macentries will use this adress as the match criteria.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "associatedApplicationID": {
            "description": "The associated application ID",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "associatedApplicationObjectID": {
            "description": "The associated application object ID",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "associatedApplicationObjectType": {
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
            "description": "The associated application object type Refer to API section for supported types.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "enum",
            "uniqueScope": "no"
        },
        "associatedLiveEntityID": {
            "description": "In the draft mode, the ACL entry refers to this LiveEntity. In non-drafted mode, this is null.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "description": {
            "description": "Description of the ACL entry",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "destinationPort": {
            "description": "The destination port to be matched if protocol is UDP or TCP. Value should be either * or single port number or a port range",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "etherType": {
            "description": "Ether type of the packet to be matched. etherType can be * or a valid hexadecimal value",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "flowLoggingEnabled": {
            "description": "Is flow logging enabled for this particular template",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "boolean",
            "uniqueScope": "no"
        },
        "icmpCode": {
            "description": "The ICMP Code when protocol selected is ICMP.",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "icmpType": {
            "description": "The ICMP Type when protocol selected is ICMP.",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "locationID": {
            "description": "The ID of the location entity (Subnet/Zone/VportTag)",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "locationType": {
            "allowed_choices": [
                "VPORTTAG",
                "SUBNET",
                "ANY",
                "POLICYGROUP",
                "REDIRECTIONTARGET",
                "ZONE"
            ],
            "description": "Type of the location entity - ANY or SUBNET or ZONE or VPORTTAG Possible values are ANY, SUBNET, ZONE, POLICYGROUP, REDIRECTIONTARGET, VPORTTAG, .",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "enum",
            "uniqueScope": "no"
        },
        "mirrorDestinationID": {
            "description": "Destination ID of the mirror destination object.",
            "exposed": true,
            "format": "free",
            "type": "string",
            "uniqueScope": "no"
        },
        "networkID": {
            "description": "The destination network entity that is referenced(subnet/zone/macro)",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "networkType": {
            "allowed_choices": [
                "SUBNET",
                "NETWORK_MACRO_GROUP",
                "ANY",
                "PUBLIC_NETWORK",
                "INTERNET_POLICYGROUP",
                "ENTERPRISE_NETWORK",
                "POLICYGROUP",
                "ENDPOINT_SUBNET",
                "ENDPOINT_DOMAIN",
                "ENDPOINT_ZONE",
                "ZONE"
            ],
            "description": "Type of the source network -  VM_SUBNET or VM_ZONE or VM_DOMAIN or SUBNET or ZONE or ENTERPRISE_NETWORK or PUBLIC_NETWORK or ANY Possible values are ENDPOINT_SUBNET, ENDPOINT_ZONE, ENDPOINT_DOMAIN, SUBNET, ZONE, ENTERPRISE_NETWORK, PUBLIC_NETWORK, POLICYGROUP, NETWORK_MACRO_GROUP, ANY, INTERNET_POLICYGROUP, .",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "enum",
            "uniqueScope": "no"
        },
        "policyState": {
            "allowed_choices": [
                "DRAFT",
                "LIVE"
            ],
            "description": "State of the policy.  Possible values are DRAFT, LIVE, .",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "enum",
            "uniqueScope": "no"
        },
        "priority": {
            "default_value": "0",
            "description": "The priority of the ACL entry that determines the order of entries",
            "exposed": true,
            "type": "integer",
            "uniqueScope": "no"
        },
        "protocol": {
            "description": "Protocol number that must be matched",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "sourcePort": {
            "description": "Source port to be matched if protocol is UDP or TCP. Value can be either * or single port number or a port range",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "required": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "stateful": {
            "description": "True means that this ACL entry is reflexive, so there will be a corresponding egress rule that will be created by OVS in the network. false means that there is no corresponding egress rule created by OVS in the network.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "boolean",
            "uniqueScope": "no"
        },
        "statsID": {
            "description": "The statsID that is created in the VSD and identifies this ACL Template Entry. This is auto-generated by VSD",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string",
            "uniqueScope": "no"
        },
        "statsLoggingEnabled": {
            "description": "Is stats logging enabled for this particular template",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "boolean",
            "uniqueScope": "no"
        }
    },
    "children": {
        "job": {
            "create": true,
            "relationship": "child"
        },
        "statistics": {
            "get": true,
            "relationship": "child"
        }
    },
    "model": {
        "delete": true,
        "description": "Defines the template of Egress ACL Template entries",
        "entity_name": "EgressACLEntryTemplate",
        "extends": [
            "@audited",
            "@base",
            "@metadata"
        ],
        "get": true,
        "package": "policy/acl",
        "resource_name": "egressaclentrytemplates",
        "rest_name": "egressaclentrytemplate",
        "update": true
    }
}