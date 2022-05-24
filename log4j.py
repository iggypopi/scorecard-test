from org.apache.log4j import * 

class logtest:
    def __init__(self):

  log.info("start of Logtest")
  log.debug('just before file read')
  try:
   log.warn('file read proceding to processing')
   xmlStringData = open('example.xml').read()
  except:       
   #yes, more could have been done here but this is just an example
   log.error('file read FAILURE')
  log.info('file read proceding to processing') 
  # since this is just an example processing would go here.
  #
  #you can also log variables
  log.warn('its just an example, OK?')
  pi = 3.141592681
  msg = 'do you like?' + str(pi)
  log.info(msg)
  log.debug('lets try to parse the string')
  if '[CDATA' in xmlStringData:
   log.warn('No CDATA section.')                        
  #say good bye and close the log file.
  log.info('That all. The End. Good Bye')
  log.shutdown()


if __name__ == '__main__':
    # loggingTest is just a string that identifies this log.
    log = Logger.getLogger("loggingTest")
    #use the config data in the properties file
    PropertyConfigurator.configure('log4j.properties')
    log.info('This is the start of the log file')
    logit = logtest()
    print '\n\nif you change the log level in the properties'
    print "file you'll get varing amouts of log data."
