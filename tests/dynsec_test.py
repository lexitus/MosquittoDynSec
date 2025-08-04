# Test for correct implementation of the mosquitto_dynsec module
import time
import csv
from mosquitto_dynsec import MosquittoDynSec


admin_username = "MOSQUITTO_DYNSEC_USER_NAME"
admin_password = "MOSQUITTO_DYNSEC_USER_PASSWORD"

dynsec = MosquittoDynSec(admin_username, admin_password)

# Test-Client
client_username = 'client_username'
client_password = 'client_password'
client_id = 'client_id'
client_textname = 'client_textname'
client_textdescription = 'client_textdescription'

# Test-Role
role_name = 'role_name'
alternative_role_name = 'alternative_role_name'
role_textname = 'role_textname'
role_textdescription = 'role_textdescription'
role_acls = [{"acltype": "subscribePattern", "topic": "role_topic", "priority": -1, "allow": True}]
{ "acltype": "subscribe", "allow": False }
# Test-Role-ACLs
role_acltype = 'subscribePattern'
role_topic = 'role_topic'

# Test-Group
group_name = 'group_name'
alternative_group_name = 'alternative_group_name'
group_textname = 'group_textname'
group_textdescription = 'group_textdescription'
group_roles = [{"rolename": "role_name", "priority": 1}]
group_clients = [{"username": "client_username", "priority": 1}]

# Test-Client
client_username = 'client_username'
client_password = 'client_password'
client_id = 'client_id'
client_textname = 'client_textname'
client_textdescription = 'client_textdescription'
client_groups = [{"groupname": group_name, "priority": 1}]
client_roles = [{"rolename": role_name, "priority": 1}]

start_time = time.time()

# Initialize a list to store tuples of 'function', 'send_code', 'success' and 'response'
results = []

# List of function calls with function names
function_calls = [
    ("set_default_acl_access", dynsec.set_default_acl_access(False, False, False, False)),
    ("get_default_acl_access", dynsec.get_default_acl_access()),
    ("create_role", dynsec.create_role(role_name, textname=role_textname, textdescription=role_textdescription, acls=role_acls)),
    ("get_role", dynsec.get_role(role_name)),
    ("list_roles", dynsec.list_roles(verbose=False, count=-1, offset=0)),
    ("add_role_acl", dynsec.add_role_acl(role_name, role_acltype, role_topic, priority=-1, allow=True)),
    ("modify_role", dynsec.modify_role(role_name, textname=role_textname, textdescription=role_textdescription, acls=role_acls)),
    ("create_group", dynsec.create_group(group_name, roles=group_roles)),
    ("get_group", dynsec.get_group(group_name)),
    ("list_groups", dynsec.list_groups(verbose=False, count=-1, offset=0)),
    ("modify_group", dynsec.modify_group(group_name, textname=group_textname, textdescription=group_textdescription, roles=group_roles, clients=group_clients)),
    ("create_client", dynsec.create_client(client_username, client_password, clientid=client_id, textname=client_textname, textdescription=client_textdescription, groups=client_groups)), #, roles=client_roles)),
    ("add_group_client", dynsec.add_group_client(group_name, client_username, priority=-1)),
    ("add_group_role", dynsec.add_group_role(group_name, role_name, priority=-1)),
    ("set_client_id", dynsec.set_client_id(client_username, clientid=client_id)),
    ("set_client_password", dynsec.set_client_password(client_username, client_password)),
    ("add_client_role", dynsec.add_client_role(client_username, role_name, priority=-1)),
    ("disable_client", dynsec.disable_client(client_username)),
    ("enable_client", dynsec.enable_client(client_username)),
    ("get_client", dynsec.get_client(client_username)),
    ("list_clients", dynsec.list_clients(verbose=False, count=-1, offset=0)),
    ("modify_client", dynsec.modify_client(client_username, clientid=client_id, password=client_password, textname=client_textname, textdescription=client_textdescription, roles=client_roles, groups=client_groups)),
    ("remove_client_role", dynsec.remove_client_role(client_username, role_name)),
    ("remove_group_client", dynsec.remove_group_client(group_name, client_username)),
    ("remove_group_role", dynsec.remove_group_role(group_name, role_name)),
    ("delete_client", dynsec.delete_client(client_username)),
    ("remove_role_acl", dynsec.remove_role_acl(role_name, role_acltype, role_topic)),
    ("delete_role", dynsec.delete_role(role_name)), 
    ("create_role", dynsec.create_role(role_name, textname=role_textname, textdescription=role_textdescription, acls=role_acls)),
    ("delete_group", dynsec.delete_group(group_name)),  #  Sometimes rror: {'responses': [{'command': 'deleteGroup', 'error': 'Group not found'}]}
    ("create_group", dynsec.create_group(alternative_group_name, roles=group_roles)),  
    ("create_role", dynsec.create_role(alternative_role_name, textname=role_textname, textdescription=role_textdescription, acls=role_acls)),  # Even with this line: 'error': 'Role not found
    ("set_anonymous_group", dynsec.set_anonymous_group(alternative_group_name)),
    ("get_anonymous_group", dynsec.get_anonymous_group())
]

# Open CSV file in write mode
with open('dynsec-test-results.csv', mode='w', newline='') as file:
    writer = csv.writer(file, delimiter='\t')  # Using tab delimiter for TSV format
    writer.writerow(['function', 'send_code', 'success', 'response'])  # Write header row

    # Iterate over each function call, execute it, and write results to file
    for function_name, call in function_calls:
        success, response, send_code = call
        writer.writerow([function_name, send_code, success, response])

end_time = time.time()
duration = end_time - start_time

number_of_functions = len(function_calls)
print(f"Tested {number_of_functions} functions in {duration} seconds.")
