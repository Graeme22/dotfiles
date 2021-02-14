import dbus

from libqtile.log_utils import logger
from libqtile.widget import base

class Bluetooth(base.InLoopPollText):
    """
    Displays bluetooth status or connected device.

    Uses dbus to communicate with the system bus.
    """

    orientations = base.ORIENTATION_HORIZONTAL
    defaults = [
        ('update_interval', 1, 'The update interval.'),
        ('format', '{status}', 'Display format')
    ]

    def __init__(self, **config):
        base.InLoopPollText.__init__(self, **config)
        self.add_defaults(Bluetooth.defaults)

        bus = dbus.SystemBus()
        # set up interface into adapter properties
        adapter = bus.get_object('org.bluez', '/org/bluez/hci0')
        adapter_interface = dbus.Interface(adapter, 'org.bluez.Adapter1')
        self._adapter = dbus.Interface(adapter_interface, 'org.freedesktop.DBus.Properties')
        # set up interface into device properties
        device = bus.get_object('org.bluez', '/org/bluez/hci0/dev_41_42_30_00_18_CD')
        device_interface = dbus.Interface(device, 'org.bluez.Device1')
        self._device = dbus.Interface(device_interface, 'org.freedesktop.DBus.Properties')

    def poll(self):
        try:
            powered = self._adapter.Get('org.bluez.Adapter1', 'Powered')
            if powered == 0:
                status = 'off'
            else:
                connected = self._device.Get('org.bluez.Device1', 'Connected')
                if connected == 0:
                    status = 'on'
                else:
                    status = self._device.Get('org.bluez.Device1', 'Name')

            return self.format.format(status=status)

        except EnvironmentError:
            logger.error('%s: Make sure your hci0 device has the correct address.', self.__class__.__name__)
