from azureml.core import Workspace
from azureml.core.compute import ComputeInstance, AmlCompute
from azureml.core.compute_target import ComputeTargetException

# Get a reference to our workspace
ws = Workspace.get(name='ps-ml-workspace',
                    subscription_id='5e9f0e7f-b386-4a7e-85d1-c986fb94e5c7',
                    resource_group='pluralsight')

# Enter the name of our cluster
cpu_cluster_name = 'tdsp-cluster'

# Compute Instance
jyputer_compute_name = 'azml-jupyter-compute'

# Attempt to delete compute resources
try:
    cpu_cluster = AmlCompute(workspace=ws, name=cpu_cluster_name)
    cpu_cluster.delete()
    print('Deleting cluster...')
    jupyter_compute = ComputeInstance(workspace=ws, name=jyputer_compute_name)
    jupyter_compute.delete()
    print('Deleting Compute instance...')
except ComputeTargetException:
    print('Cluster or Instance does not exist on workspace...')