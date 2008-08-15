#!/usr/bin/python

import gobject
import dbus
import sys
import time
from random import randint

from optparse import OptionParser
from pasytest import PasyTest

from dbus.mainloop.glib import DBusGMainLoop

DBusGMainLoop(set_as_default=True)

def run_test_app(module_name, dbus_name=None):
	import os
	from subprocess import Popen

	test_data_directory = os.environ["TEST_DATA_DIRECTORY"]
	test_modules_directory = os.environ["TEST_MODULES_DIRECTORY"]
	test_atspi_library = os.environ["TEST_ATSPI_LIBRARY"]
	test_application = os.environ["TEST_APPLICATION"]

	test_module = os.path.join(test_modules_directory, module_name)

	if (dbus_name):
		print " ".join([test_application,
			"--atspi-dbus-name", dbus_name,
			"--test-atspi-library", test_atspi_library,
			"--test-module", test_module,
			"--test-data-directory", test_data_directory,])
		pop = Popen([test_application,
			"--atspi-dbus-name", dbus_name,
			"--test-atspi-library", test_atspi_library,
			"--test-module", test_module,
			"--test-data-directory", test_data_directory,])
	else:
		print " ".join([test_application,
			"--test-atspi-library", test_atspi_library,
			"--test-module", test_module,
			"--test-data-directory", test_data_directory,])
		pop = Popen([test_application,
			"--test-atspi-library", test_atspi_library,
			"--test-module", test_module,
			"--test-data-directory", test_data_directory,])

	wait_message = """
	The test application %s has been started with PID %d.
	
	To continue the test press ENTER.\n\n
	"""
	if ("TEST_APP_WAIT_FOR_DEBUG" in os.environ.keys()):
		raw_input(wait_message % (module_name, pop.pid))

def main(argv):
	parser = OptionParser()
	parser.add_option("-l", "--library", dest="test_library")
	parser.add_option("-m", "--module", dest="test_module")
	parser.add_option("-n", "--name", dest="test_name")
	(options, args) = parser.parse_args()

	bus = dbus.SessionBus()
	name = "test.atspi.R" + str(randint(1, 1000)) 

	app = run_test_app(options.test_library, name)
	time.sleep(1)
	print "Started test app on bus name %s" % (name,)

	to = bus.get_object(name, "/org/codethink/atspi/test")
	test = dbus.Interface(to, "org.codethink.atspi.test")

	# Run the test script here
	module = __import__(options.test_module)
	test_class = getattr(module, options.test_name)
	test_object = test_class(bus, name)
	test_object.run()

	loop = gobject.MainLoop()

	def finished_handler():
		loop.quit()
		print "\n" + test_object.report() + "\n"
		test.finish()

	test_object.events.finished += finished_handler

	loop.run()

if __name__=="__main__":
	sys.exit(main(sys.argv))
