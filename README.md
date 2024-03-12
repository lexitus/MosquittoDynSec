# MosquittoDynSec 

A Python interface for interacting with the Mosquitto MQTT broker's Dynamic Security Plugin.
This class abstracts the MQTT communication and command sending to the Dynamic Security Plugin,
facilitating the management of ACLs, clients, groups, and roles within the broker.

The class provides setter and getter functions for various configurations supported by the
Dynamic Security Plugin. Setter functions are used to configure or modify settings, while
getter functions are used to retrieve current configurations from the broker.

SETTER functions return a tuple of (success, response), where 'success' is a boolean indicating
the operation's success, and 'response' is a dictionary containing the broker's response.

GETTER functions similarly return a tuple of (success, response) where 'response' in this case
contains the requested configuration data.

Example usage:
    mosquitto_dyn_sec = MosquittoDynSec(dynsec_user, dynsec_user_password)
    success, response = mosquitto_dyn_sec.set_default_acl_access(False, False, False, False)

Attributes:
    username (str): Username used to interact with the Mosquitto Dynamic Security Plugin.
    password (str): Password used for above user.
    host (str): Hostname or IP address of the MQTT broker.
    port (int): Network port of the MQTT broker.

Based on commands at https://github.com/eclipse/mosquitto/blob/master/plugins/dynamic-security/README.md

## Setup and how to use Mosquitto with Dynamic Security Plugin: 
    https://mosquitto.org/documentation/dynamic-security/
