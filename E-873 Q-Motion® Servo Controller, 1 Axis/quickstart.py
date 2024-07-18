import time
#!/usr/bin/python
# -*- coding: utf-8 -*-
"""This example connects to a PIPython device."""

# (c)2016 Physik Instrumente (PI) GmbH & Co. KG
# Software products that are provided by PI are subject to the
# General Software License Agreement of Physik Instrumente (PI) GmbH & Co. KG
# and may incorporate and/or make use of third-party software components.
# For more information, please read the General Software License Agreement
# and the Third Party Software Note linked below.
# General Software License Agreement:
# http://www.physikinstrumente.com/download/EULA_PhysikInstrumenteGmbH_Co_KG.pdf
# Third Party Software Note:
# http://www.physikinstrumente.com/download/TPSWNote_PhysikInstrumenteGmbH_Co_KG.pdf


from pipython import GCSDevice

__signature__ = 0x8b193828fd914ccc87e2198cb8a30417

def main():
    """Connect to a PIPython device."""

    # We recommend to use GCSDevice as context manager with "with".

    with GCSDevice() as pidevice:
        # Choose the interface which is appropriate to your cabling.

        #   `pidevice.ConnectTCPIP(ipaddress='192.168.178.42')
        pidevice.ConnectUSB(serialnum='124014078')
        # pidevice.ConnectRS232(comport=1, baudrate=115200)

        # Each PI controller supports the qIDN() command which returns an
        # identification string with a trailing line feed character which
        # we "strip" away.

        print('connected: {}'.format(pidevice.qIDN().strip()))

        # Show the version info which is helpful for PI support when there
        # are any issues.

        if pidevice.HasqVER():
            print('version info: {}'.format(pidevice.qVER().strip()))
        exit = False
        while exit == False:
            mode = input("mit 1 bewegen Sie die Axis, mit 2 sehen Sie die Position der Axis, mit 3 beenden Sie das Programm:")
            if mode == "1":
                target = input("Geben Sie die Position ein: ")
                pidevice.MOV(1,target)
                time.sleep(1)
                print("Sie haben die Axis bewegt zu: ", pidevice.qPOS(1))
            if mode == "2":
                print("Die Position der Axis ist: ", pidevice.qPOS(1))
            if mode == "3":
                exit = True



if __name__ == '__main__':
    # To see what is going on in the background you can remove the following
    # two hashtags. Then debug messages are shown. This can be helpful if
    # there are any issues.

    # from pipython import PILogger, DEBUG, INFO, WARNING, ERROR, CRITICAL
    # PILogger.setLevel(DEBUG)

    main()
