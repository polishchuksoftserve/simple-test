import random , requests
import subprocess , pytest

def test_persistent_storage_name():
    value = subprocess.check_output("kubectl get pod |grep \'persistent-storage*\'|cut -d: -f2| awk \'{print $1}\'",shell=True)
    assert value.rstrip() =='persistent-storage-wg6i4'

def test_persistent_storage_is_ready():
    value = subprocess.check_output("kubectl get pod |grep \'persistent-storage*\'|cut -d: -f2| awk \'{print $2}\'",shell=True)
    assert '2/2' == value.rstrip()

def test_persistent_storage_status():
    value = subprocess.check_output("kubectl get pod |grep \'persistent-storage*\'|cut -d: -f2| awk \'{print $3}\'",shell=True)
    assert 'Running' == value.rstrip()

def test_persistent_storage_restars():
    value = subprocess.check_output("kubectl get pod |grep \'persistent-storage*\'|cut -d: -f2| awk \'{print $4}\'",shell=True)
    assert int(value.rstrip()) <= 4


