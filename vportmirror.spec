{
    "apis": {
        "children": {}, 
        "parents": {
            "/mirrordestinations/{id}/vportmirrors": {
                "RESTName": "mirrordestination", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "GET"
                    }
                ], 
                "resourceName": "mirrordestinations"
            }, 
            "/vports/{id}/vportmirrors": {
                "RESTName": "vport", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "GET"
                    }, 
                    {
                        "availability": null, 
                        "method": "POST"
                    }
                ], 
                "resourceName": "vports"
            }
        }, 
        "self": {
            "/vportmirrors/{id}": {
                "RESTName": "vportmirror", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "PUT"
                    }, 
                    {
                        "availability": null, 
                        "method": "DELETE"
                    }, 
                    {
                        "availability": null, 
                        "method": "GET"
                    }
                ], 
                "resourceName": "vportmirrors"
            }
        }
    }, 
    "model": {
        "RESTName": "vportmirror", 
        "attributes": {
            "VPortName": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "channel": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "Name of the vport to which the mirror destination is associated with.", 
                "exposed": true, 
                "filterable": false, 
                "format": null, 
                "maxLength": null, 
                "maxValue": null, 
                "minLength": null, 
                "minValue": null, 
                "orderable": false, 
                "readOnly": false, 
                "required": false, 
                "transient": false, 
                "type": "string", 
                "unique": false
            }, 
            "attachedNetworkType": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "channel": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "Type of the network attached - L2/L3", 
                "exposed": true, 
                "filterable": false, 
                "format": null, 
                "maxLength": null, 
                "maxValue": null, 
                "minLength": null, 
                "minValue": null, 
                "orderable": false, 
                "readOnly": false, 
                "required": false, 
                "transient": false, 
                "type": "string", 
                "unique": false
            }, 
            "domainName": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "channel": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "Domain name of the vport associated with the mirror destination", 
                "exposed": true, 
                "filterable": false, 
                "format": null, 
                "maxLength": null, 
                "maxValue": null, 
                "minLength": null, 
                "minValue": null, 
                "orderable": false, 
                "readOnly": false, 
                "required": false, 
                "transient": false, 
                "type": "string", 
                "unique": false
            }, 
            "enterpiseName": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "channel": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "Enterprise to which the vport associated with the mirror destination belongs to.", 
                "exposed": true, 
                "filterable": false, 
                "format": null, 
                "maxLength": null, 
                "maxValue": null, 
                "minLength": null, 
                "minValue": null, 
                "orderable": false, 
                "readOnly": false, 
                "required": false, 
                "transient": false, 
                "type": "string", 
                "unique": false
            }, 
            "mirrorDestinationID": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "channel": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "Destination ID of the mirror destination object.", 
                "exposed": true, 
                "filterable": false, 
                "format": null, 
                "maxLength": null, 
                "maxValue": null, 
                "minLength": null, 
                "minValue": null, 
                "orderable": false, 
                "readOnly": false, 
                "required": false, 
                "transient": false, 
                "type": "string", 
                "unique": false
            }, 
            "mirrorDestinationName": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "channel": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "Name of the mirror destination", 
                "exposed": true, 
                "filterable": false, 
                "format": null, 
                "maxLength": null, 
                "maxValue": null, 
                "minLength": null, 
                "minValue": null, 
                "orderable": false, 
                "readOnly": false, 
                "required": false, 
                "transient": false, 
                "type": "string", 
                "unique": false
            }, 
            "mirrorDirection": {
                "allowedChars": null, 
                "allowedChoices": [
                    "BOTH", 
                    "EGRESS", 
                    "INGRESS"
                ], 
                "autogenerated": false, 
                "availability": null, 
                "channel": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "Describes what type of traffic needs to be mirrors - ingress/egress/both Possible values are BOTH, INGRESS, EGRESS, .", 
                "exposed": true, 
                "filterable": false, 
                "format": null, 
                "maxLength": null, 
                "maxValue": null, 
                "minLength": null, 
                "minValue": null, 
                "orderable": false, 
                "readOnly": false, 
                "required": false, 
                "transient": false, 
                "type": "enum", 
                "unique": false
            }, 
            "networkName": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "channel": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "Name of the network to which the vport belongs to", 
                "exposed": true, 
                "filterable": false, 
                "format": null, 
                "maxLength": null, 
                "maxValue": null, 
                "minLength": null, 
                "minValue": null, 
                "orderable": false, 
                "readOnly": false, 
                "required": false, 
                "transient": false, 
                "type": "string", 
                "unique": false
            }, 
            "vportId": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "channel": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "Id of the vport to which the mirror destination is associated with.", 
                "exposed": true, 
                "filterable": false, 
                "format": null, 
                "maxLength": null, 
                "maxValue": null, 
                "minLength": null, 
                "minValue": null, 
                "orderable": false, 
                "readOnly": false, 
                "required": false, 
                "transient": false, 
                "type": "string", 
                "unique": false
            }
        }, 
        "description": "VPort Mirror Object represents the relationship between a vport and a mirror destination.", 
        "entityName": "VPortMirror", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "package": "/vport", 
        "resourceName": "vportmirrors"
    }
}