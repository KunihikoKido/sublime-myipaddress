import sublime
import sublime_plugin


class ShowIpAddressCommand(sublime_plugin.WindowCommand):

    def run(self):
        settings = sublime.load_settings('MyIpAddress.sublime-settings')
        domain = settings.get("ip_lookup_service_domain")
        curl = settings.get("curl_command")
        command = [curl, '-s', domain]
        self.run_command(command)

    def run_command(self, command):
        self.window.run_command("exec", {"cmd": command, "quiet": True})
