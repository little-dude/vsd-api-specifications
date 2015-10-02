{
    "apis": {
        "children": {
            "/endpoints/{id}/eventlogs": {
                "RESTName": "eventlog", 
                "entityName": "EventLog", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "GET"
                    }
                ], 
                "resourceName": "eventlogs"
            }
        }, 
        "parents": {
            "/externalservices/{id}/endpoints": {
                "RESTName": "externalservice", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "GET"
                    }
                ], 
                "resourceName": "externalservices"
            }
        }, 
        "self": {
            "/endpoints/{id}": {
                "RESTName": "endpoint", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "GET"
                    }
                ], 
                "resourceName": "endpoints"
            }
        }
    }, 
    "model": {
        "RESTName": "endpoint", 
        "attributes": {
            "description": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "channel": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "Description of the External Service.", 
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
            "name": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "channel": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "unique name of the External Service. ", 
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
        "description": "Representation of End Point", 
        "entityName": "EndPoint", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "package": "/policy", 
        "resourceName": "endpoints"
    }
}