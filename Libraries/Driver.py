from robot.libraries.BuiltIn import BuiltIn
from selenium import webdriver

Instance = None


def open_browser(browser):
    global Instance
    if browser == 'gc':
        Instance = webdriver.Chrome()
        Instance.maximize_window()
        BuiltIn().log('Chrome is opened', console=True)
        BuiltIn().set_global_variable('${BROWSER}', Instance)

    elif browser == 'ff':
        Instance = webdriver.Firefox()
        Instance.maximize_window()
        BuiltIn().log('Firefox is opened', console=True)
        BuiltIn().set_global_variable('${BROWSER}', Instance)

    elif browser == 'ph':
        Instance = webdriver.PhantomJS()
        BuiltIn().log('PhantomJS is opened', console=True)
        BuiltIn().set_global_variable('${BROWSER}', Instance)

    else:
        BuiltIn().fail('ERROR: Please input correct name for browser')


def close_driver():
    global Instance
    if Instance is not None:
        driver = BuiltIn().get_variable_value('${BROWSER}')
        driver.close()
        driver.quit()
