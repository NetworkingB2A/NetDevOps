import logging
logger = logging.getLogger(__name__)

#You would use this next part if you want to customize your logger a bit more. This will allow you to change the root logger info.
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
file_handler = logging.FileHandler('runbook_logging/testlog2.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


# adding this statement creates a log file and  changes the default logging
#logging.basicConfig(filename='runbook_logging/testlog.log', level=logging.INFO, format='%(asctime)s:%(name)s:%(levelname)s:%(message)s')


def uname_creator(first_name, last_name):
    return (first_name + '.' + last_name)

def email_creator(first_name, last_name):
    return (first_name + '.' + last_name + '@networkingb2a.com')


#by default this will not output to the screen
logger.debug(uname_creator('sam', 'gamgee'))
logger.debug(email_creator('sam', 'gamgee'))

#by default this will not output to the screen
logger.info(uname_creator('bilbo', 'baggins'))
logger.info(email_creator('bilbo', 'baggins'))

#by default this will output to the screen
logger.warning(uname_creator('frodo', 'baggins'))
logger.warning(email_creator('frodo', 'baggins'))

#by default this will output to the screen
logger.error(uname_creator('aragorn', 'strider'))
logger.error(email_creator('aragorn', 'strider'))

#by default this will output to the screen
logger.critical(uname_creator('gandalf', 'gray'))
logger.critical(email_creator('gandalf', 'gray'))
