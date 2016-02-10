{
    "attributes": {
        "IPType": {
            "allowed_choices": [
                "IPV4",
                "IPV6"
            ],
            "description": null,
            "exposed": true,
            "filterable": true,
            "orderable": true,
            "type": "enum"
        },
        "PATCentralized": {
            "description": null,
            "exposed": true,
            "filterable": true,
            "orderable": true,
            "type": "boolean"
        },
        "domainID": {
            "description": null,
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string"
        },
        "hypervisorID": {
            "description": null,
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string"
        },
        "ipAddress": {
            "description": null,
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string"
        }
    },
    "model": {
        "delete": true,
        "entity_name": "PATIpEntry",
        "get": true,
        "resource_name": "patipentries",
        "rest_name": "patipentry",
        "update": true
    }
}