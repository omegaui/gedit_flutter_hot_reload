import subprocess
from gi.repository import GObject, Gedit

class HotReloaderPlugin(GObject.Object, Gedit.WindowActivatable):
	__gtype_name__ = "HotReloaderPlugin"

	window = GObject.property(type=Gedit.Window)

	def __init__(self):
		GObject.Object.__init__(self)

	def do_activate(self):
		self.window.connect('tab-added', self.attach_trigger)

	def attach_trigger(self, window, tab):
		doc = tab.get_document()
		doc.connect('saved', self.trigger_hot_reload)

	def trigger_hot_reload(self, doc, data=None):
		lang = doc.get_language()
		if lang.get_name() == 'Dart':
			subprocess.Popen(["./hot_reload_flutter"])

	def do_deactivate(self):
		pass

	def do_update_state(self):
		pass


#silent execute '!kill -SIGUSR1 "$(pgrep -f flutter_tools.snapshot\ run)" &> /dev/null'


