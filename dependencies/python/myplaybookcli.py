from ansible.cli.playbook import PlaybookCLI
from ansible import context
from ansible.executor.playbook_executor import PlaybookExecutor


class MyPlaybookCLI(PlaybookCLI):
    def run(self, extra_vars):
        super(PlaybookCLI, self).run()
        print(context.CLIARGS)
        loader, inventory, variable_manager = self._play_prereqs()
        variable_manager._extra_vars = extra_vars
        passwords = {}
        pbex = PlaybookExecutor(playbooks=context.CLIARGS['args'], inventory=inventory,
                                variable_manager=variable_manager, loader=loader,
                                passwords=passwords)

        print(pbex.run())