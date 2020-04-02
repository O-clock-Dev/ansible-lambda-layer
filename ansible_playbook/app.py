# coding: utf8
import json
from myplaybookcli import MyPlaybookCLI

data = {}

def lambda_handler(event, context):
    a = MyPlaybookCLI(["", "playbooks/mon-playbook.yml"])
    a.run({'slot_name': self._slot_name[0], 'slot_hostname': self._hostname, 'slot_port': self._port})

