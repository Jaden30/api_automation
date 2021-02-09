# Device Registry Device 

## usage 

## CRUD Create Read Update Delete 
## Create - POST 
## Read - GET
## Update - PUT & PATCH 
## Delete - DELETE 
All responses will have the form 
```json 
{
 "data" : "Mixed type holding the content of the response"
 "message" : "Description of what happened"


}

Subsequent response definitions will only detail the expected value of the data field 

### List all devices 
**Definition **
`GET /devices` 

**Response**
- `200 OK` on successs 

```json 
[

    {
        "identifier": "floor-lamp",
        "name": "Floor Lamp",
        "device_type": "switch",
        "controller_gateway": "192.1.68.0.2"
        

    
            }


    
    {
        "identifier": "room-light",
        "name": "Room Light",
        "device_type": "Light",
        "controller_gateway": "192.1.60.2.3"
        
            }
]
### Registering a new device 

*** Definition**

`post /devices` 

**ARGUMENTS** 
[
 "IDENTIFIER" : "A global unique identifier for this device, A string"
 "Name" : " A user friendly name for this device, a string"
 "Device type" : " The type of device for the string being used, a string"
 "Controller gateway" : "An ip address for the device to connect to, a string " 

]
If the device with the identifier already exists, the creation overrides the formerly created devices.

**Response**
 
'201 Created' on success 
## on creation , it returns the json created documents 

```json 
{
        "identifier": "room-light",
        "name": "Room Light",
        "device_type": "Light",
        "controller_gateway": "192.1.60.2.3"
        
            }

```
## Lookup devices details 
`GET /devices/<identifier>`

**Response ** 
-- `404 NOT found ` if the device does not exist 
-- `200 OK ` on success 

```json 
## returns an identifier on success 
{
        "identifier": "room-light",
        "name": "Room Light",
        "device_type": "Light",
        "controller_gateway": "192.1.60.2.3"
        
            }
```
 ## Delete a device 
/DELETE/devices/<identifier>

**Response ** 

`404 not found, device does not exist'
204 OK, device has been deleted
## No content
## Does not return anything 

## First step is to create a dockerfile and then copy the docker python image from the website and paste.
## Create a requirements.txt
## Create a docker-compose.yml text
## Create a device_registry folder 
## create a __init__.py  to tell python that it is a package and not just a random folder 
## instead of installing flask with pip, you can automate it by adding it to the requoirements.txt

