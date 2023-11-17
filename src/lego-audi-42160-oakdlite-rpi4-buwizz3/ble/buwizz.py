# Discovering BuWizz3 device
#
# When active, BuWizz3 device advertises main advertisement data and optional scan response data
# (shown in Figure 1). Main advertisement data contains device name (‘BuWizz3’ by default, but can be
# customized) and short manufacturer information (sequence of 8 bytes - 05:4E:’B’:’W’:’B’:’L’:00:00 in
# bootloader and 05:4E:’B’:’W’:’x’:’y’:<serialLSB>:<serialMSB> in the application, where x and y are
# replaced with firmware version and serial number contains lower 16 bits of device’s serial number).
# Scan response data contains the 128-bit UUID of the device’s main (BuWizz application) service. 
#
# Service UUID
# BuWizz 93:6E:67:B1:19:99:B3:88:81:44:FB:74:D1:92:05:50
#
# There are 6 characteristics in this service, shown in the table below. These have a data exchange
# characteristic with a data exchange descriptor and a Client Characteristic Configuration Descriptor
# (CCCD) controlling the characteristic behavior.
# Characteristic UUID Type
# Application 0x2901 Write + Notify
# Bootloader 0x8000 Write + Notify
# UART ch. 1 0x3901 Write + Notify
# UART ch. 2 0x3902 Write + Notify
# UART ch. 3 0x3903 Write + Notify
# UART ch. 4 0x3904 Write + Notify

# https://buwizz.com/BuWizz_3.0_API_3.6_web.pdf