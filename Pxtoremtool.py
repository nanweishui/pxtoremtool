import sublime
import sublime_plugin
class pxtoremtoolCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sz = self.view.find("\d*.\(px\)",sublime.IGNORECASE)
        if sz:
            sc = self.view.find("\d*\.*\d*.\(rem\)",sublime.IGNORECASE)
            c = int(self.view.substr(sz)[:-4])/float(self.view.substr(sc)[:-5])
            t = self.view.find_all("[1-9]\d*px",sublime.IGNORECASE)
            for x in t:
                s = self.view.find("[1-9]\d*px",sublime.IGNORECASE)
                i = float(self.view.substr(s)[:-2])/c
                self.view.replace(edit, s, str(i) + "rem")
