# Copyright (C) 2015 Synapse Wireless, Inc.
# Subject to your agreement of the disclaimer set forth below, permission is given by Synapse Wireless, Inc. ("Synapse") to you to freely modify, redistribute or include this SNAPpy code in any program. The purpose of this code is to help you understand and learn about SNAPpy by code examples.
# BY USING ALL OR ANY PORTION OF THIS SNAPPY CODE, YOU ACCEPT AND AGREE TO THE BELOW DISCLAIMER. If you do not accept or agree to the below disclaimer, then you may not use, modify, or distribute this SNAPpy code.
# THE CODE IS PROVIDED UNDER THIS LICENSE ON AN "AS IS" BASIS, WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, WITHOUT LIMITATION, WARRANTIES THAT THE COVERED CODE IS FREE OF DEFECTS, MERCHANTABLE, FIT FOR A PARTICULAR PURPOSE OR NON-INFRINGING. THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE COVERED CODE IS WITH YOU. SHOULD ANY COVERED CODE PROVE DEFECTIVE IN ANY RESPECT, YOU (NOT THE INITIAL DEVELOPER OR ANY OTHER CONTRIBUTOR) ASSUME THE COST OF ANY NECESSARY SERVICING, REPAIR OR CORRECTION. UNDER NO CIRCUMSTANCES WILL SYNAPSE BE LIABLE TO YOU, OR ANY OTHER PERSON OR ENTITY, FOR ANY LOSS OF USE, REVENUE OR PROFIT, LOST OR DAMAGED DATA, OR OTHER COMMERCIAL OR ECONOMIC LOSS OR FOR ANY DAMAGES WHATSOEVER RELATED TO YOUR USE OR RELIANCE UPON THE SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGES OR IF SUCH DAMAGES ARE FORESEEABLE. THIS DISCLAIMER OF WARRANTY AND LIABILITY CONSTITUTES AN ESSENTIAL PART OF THIS LICENSE. NO USE OF ANY COVERED CODE IS AUTHORIZED HEREUNDER EXCEPT UNDER THIS DISCLAIMER.

'''SNAPpy Button Demo
    Sample SNAPpy script to demonstrate one method of invoking an action based on an input toggle.
    This script is intended to be used with the SN173 evaluation boards.
'''
from SN173 import *

# Run start-up function
@setHook(HOOK_STARTUP)
def start_up():
    # Set pin direction as input
    setPinDir(S1, False)
    setPinDir(S2, False)
    
    # Enable internal pull-up resistor
    setPinPullup(S1, True)
    setPinPullup(S2, True)
    
    # Setup pin to be monitored
    monitorPin(S1, True)
    monitorPin(S2, True)
    
    # Set pin direction as output
    setPinDir(LED1, True)
    setPinDir(LED2, True)
    
    # Set LED default state to off
    writePin(LED1, False)
    writePin(LED2, False)
    
# Monitor pin event hook
@setHook(HOOK_GPIN)
def button_event(pin, set):
    
    # If Switch1 is pressed, turn on LED2
    if pin == S1:
        if not set:
            writePin(LED1, True)
        else:
            writePin(LED1, False)
    
    # If Switch2 is pressed, turn on LED2
    if pin == S2:
        if not set:
            writePin(LED2, True)
        else:
            writePin(LED2, False)
            