import Locators.RegistrationLocators as Locators
import Settings.RegistrationSettings as Settings
from Libraries.Base_methods import Base_methods
from robot.libraries.BuiltIn import BuiltIn

import string
import random

class RegistrationPage():

    ROBOT_LIBRARY_SCOPE = 'TEST_SUITE'
    __version__ = '0.1'

    email = None

    def email_generator(self, size=15, chars=string.ascii_uppercase + string.digits):
        random_part = ''.join(random.choice(chars) for _ in range(size))
        e_mail = '{0}@example.com'.format(random_part)
        BuiltIn().set_global_variable('${EMAIL}', e_mail)
        return e_mail

    def Registration_To_Site(self):
        email = self.email_generator()
        Base_methods().Fill_In_Field(Locators.Surname, Settings.Surname)
        Base_methods().Fill_In_Field(Locators.First_Name, Settings.First_Name)
        Base_methods().Fill_In_Field(Locators.E_mail, email)
        Base_methods().Fill_In_Field(Locators.Confirm_email, email)
        Base_methods().Fill_In_Field(Locators.Postcode, Settings.Postcode)
        Base_methods().Fill_In_Field(Locators.Password, Settings.Password)
        Base_methods().Fill_In_Field(Locators.Confirm_Password, Settings.Password)
        Base_methods().Click_Button(Locators.Agree_policy)
        BuiltIn().sleep(3)
        Base_methods().Click_Button(Locators.Sign_up_button)

    def Verify_user(self):
        email = BuiltIn().get_variable_value('${EMAIL}')
        e_mail = email.lower()
        Base_methods().Verify_Data(Locators.email_in_profile, e_mail)

    def Verify_page(self):
        lurl = Base_methods().get_url()
        if lurl == Settings.DOMAIN:
            BuiltIn().log('Redirect was correct to {0}'.format(lurl))
        else:
            BuiltIn().fail('Redirect was incorrect to {0}'.format(lurl))

    def Verify_message(self):
        Base_methods().get_text_in_message(Locators.success_msg)



