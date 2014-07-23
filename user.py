import sublime, sublime_plugin
import re

class TransformPlugin(sublime_plugin.TextCommand):
    def transform(self, s):
        return s

    def run(self, edit):
        for region in self.view.sel():
            if not region.empty():
                # Get the selected text
                s = self.view.substr(region)
                # Transform it
                result = self.transform(s)
                # Replace the selection with transformed text
                self.view.replace(edit, region, result)

class RailsErbifyCommand(TransformPlugin):
    def transform(self, s):
        s = '<%= ' + s + ' %>'
        return s

class RailsI18nifyCommand(TransformPlugin):
    def transform(self, s):
        s = re.sub(r'^[\'\"]', '', s)
        s = re.sub(r'[\'\"]$', '', s)
        key = re.sub('[^\w]', '_', s.strip()).lower()
        key = re.sub('^_*', '', key)
        key = re.sub('_*$', '', key)
        s = "t('."+key+"', default: '"+s+"')"
        return s

class FileNameOnStatusBar(sublime_plugin.EventListener):
    def on_activated(self, view):
        path = view.file_name()
        if path:
            for folder in view.window().folders():
                path = path.replace(folder + '/', '', 1)
            view.set_status('zz_file_name', path)
        else:
            view.set_status('zz_file_name', 'untitled')

