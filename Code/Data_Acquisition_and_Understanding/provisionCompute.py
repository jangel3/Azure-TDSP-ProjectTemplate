from azureml.core import Workspace
from azureml.core.compute import AmlCompute, ComputeInstance
from azureml.core.compute_target import ComputeTargetException

# Get a reference to our workspace
ws = Workspace.get(name='ps-ml-workspace-eastus', 
                   subscription_id='5e9f0e7f-b386-4a7e-85d1-c986fb94e5c7',
                   resource_group='pluralsight')    

# Create a name for our new cluster
cpu_cluster_name = 'tdsp-cluster'

# Compute Instance
jyputer_compute_name = 'azml-jupyter-compute'


# Verify that cluster does not already exist

try:
    cpu_cluster = AmlCompute(workspace=ws, name=cpu_cluster_name)
    print('Cluster already exists')
except ComputeTargetException:
    compute_config = AmlCompute.provisioning_configuration(vm_size='Standard_NC6',
                                                           max_nodes=4)
    cpu_cluster = AmlCompute.create(ws, cpu_cluster_name, compute_config)
    
cpu_cluster.wait_for_completion(show_output=True)

try: 
    jupyter_compute = ComputeInstance(workspace=ws, name=jyputer_compute_name)
    print('Instance already exists')
except ComputeTargetException:
    compute_config = ComputeInstance.provisioning_configuration(vm_size='Standard_DS11_v2')
    jupyter_compute = ComputeInstance.create(ws, jyputer_compute_name, compute_config)

jupyter_compute.wait_for_completion(show_output=True)