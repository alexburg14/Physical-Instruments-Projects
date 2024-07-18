# simple script to get the ID of the device

from pipython import GCSDevice
pidevice = GCSDevice('C-873')
pidevice.InterfaceSetupDlg()
print(pidevice.qIDN())
print(pidevice.qPOS(1))
pidevice.CloseConnection()