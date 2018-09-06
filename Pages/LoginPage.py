import Locators.LoginLocators as Locators
import Settings.LoginSettings as Settings
from Libraries.Base_methods import Base_methods

from robot.libraries.BuiltIn import BuiltIn



class LoginPage():

    ROBOT_LIBRARY_SCOPE = 'TEST_SUITE'
    __version__ = '0.1'

    def Login_To_Site(self):
        Base_methods().Fill_In_Field(Locators.user_email, Settings.email)
        Base_methods().Fill_In_Field(Locators.user_password, Settings.password)
        Base_methods().Click_Button(Locators.submit_button)

    def Verify_user(self):
        Base_methods().Verify_Data(Locators.email_in_profile, Settings.email)

    def Verify_page(self):
        lurl = Base_methods().get_url()
        if lurl == Settings.DOMAIN:
            BuiltIn().log('Redirect was correct to {0}'.format(lurl))
        else:
            BuiltIn().fail('Redirect was incorrect to {0}'.format(lurl))
