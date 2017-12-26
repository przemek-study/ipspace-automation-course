#!/bin/bash
#
# Service VLAN validation unit testing
# 
# Reference:
# https://www.gnu.org/software/bash/manual/bash.html
# https://www.gnu.org/software/bash/manual/bash.html#Bash-Builtins
#
echo "Running VLAN Service model validation unit testing"

# Check inventory file is in the directory from which script was launched
if [ ! -f hosts ]; then
  echo " Inventory file not found in the current directory, aborting."
  echo
  echo " This script must be launched from the project's main directory."
  echo " Like so: testing/validate-data-models.sh"
  exit
fi

echo "-> Validating known correct VLAN Service model"
ansible-playbook validate-vlan-srvc-data-model.yml -e vlsrvc=srvc-vlan-model-correct.yml >/dev/null 2>/dev/null

# ? - holds the exit code
if [ $? -ne 0 ]; then
  echo " .. Arrgh, Something bad happened, initial test failed!"
  exit 1
fi
echo
echo "== Initial test PASS, proceeding =="
echo

exitstatus=0
for vlsrvc in testing/bad-models/*.yml
do
  echo "-> Validating model $vlsrvc"
  ansible-playbook validate-vlan-srvc-data-model.yml -e vlsrvc=$vlsrvc >/dev/null 2>/dev/null
  if [ $? -ne 0 ]; then
    echo " .. model validation failed as expected"
  else
    echo " .. VERY BAD, broken model DID NOT FAIL"
    existatus=1
  fi
done

if [ $exitstatus -ne 0 ]; then
  echo "Data model validation process failed"
else
  echo
  echo "^_^ Validation process completed successfully ^_^"
  echo
fi
exit $exitstatus
