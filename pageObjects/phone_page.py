from pageObjects.base_page import CommonClass
from locators.phone_page_locators import PhonePageLocators


class PhonePage(CommonClass):
    ppl = PhonePageLocators()

    def click_heading(self):
        self.click_element("XPATH", self.ppl.phone_heading_xpath)

    def click_three_dot_menu(self):
        self.click_element("CSS_SELECTOR", self.ppl.three_dot_menu_css)

    def click_delete_member(self):
        self.click_element('XPATH', self.ppl.delete_number_xpath)

    def click_assign_to(self):
        self.click_element('XPATH', self.ppl.assign_to_xpath)

    def select_members_to_assign(self):
        self.click_element('XPATH', self.ppl.select_member_to_assign_xpath)

    def click_assign_button(self):
        self.click_element('XPATH', self.ppl.assign_btn_xpath)

    def click_set_forwarding(self):
        self.click_element('XPATH', self.ppl.set_forwarding_xpath)

    def click_drpdown_forward_call_to(self):
        self.click_element('XPATH', self.ppl.forward_call_to_dropdown_xpath)

    def forward_call_to_team(self):
        self.click_element('XPATH', self.ppl.forward_call_to_team_xpath)

    def select_drpdown_team_for_forwarding(self):
        self.click_element('XPATH', self.ppl.select_team_dropdown_xpath)

    def select_team(self):
        self.click_element('XPATH', self.ppl.select_team_xpath)

    def update_forwarding(self):
        self.click_element('XPATH', self.ppl.update_forwarding_xpath)

    def select_time_for_ring(self):
        self.click_element('XPATH', self.ppl.value_29_sec_xpath)

    def click_drpdwn_forward_how_long(self):
        self.click_element('XPATH', self.ppl.forward_how_long_xpath)

    def forward_call_to_member(self):
        self.click_element('XPATH', self.ppl.forward_call_to_member_xpath)

    def select_member_from_list(self):
        self.click_element('XPATH', self.ppl.select_dropdown_of_members_xpath)

    def forward_call_to_number(self):
        self.click_element('XPATH', self.ppl.forward_call_to_phone_number_xpath)

    def enter_phone_number(self, text):
        self.send_keys_to_element('XPATH', self.ppl.phone_number_input_id, text)

    def forward_call_to_fonu_number(self):
        self.click_element('XPATH', self.ppl.forward_call_to_fonu_number_xpath)

    def forward_call_to_sip_address(self):
        self.click_element('XPATH', self.ppl.forward_calls_to_sip_address_xpath)

    def select_fonu_number_dropdown(self):
        self.click_element('XPATH', self.ppl.select_fonu_number_drpdown_xpath)

    def click_on_the_fonu_number(self):
        self.click_element('XPATH', self.ppl.select_fonu_number_xpath)

    def forward_call_to_hung_up(self):
        self.click_element('XPATH', self.ppl.forward_call_to_hangup_xpath)

    def forward_call_to_voicemail(self):
        self.click_element('XPATH', self.ppl.forward_call_to_voicemail_xpath)

    def forward_call_to_phone_menu(self):
        self.click_element('XPATH', self.ppl.forward_call_to_phone_menu_xpath)

    def click_on_phone_menu_drpdwn(self):
        self.click_element('XPATH', self.ppl.select_phone_menu_drpdwn_xpath)

    def input_siop_address(self):
        self.click_element('XPATH', self.ppl.sip_address_input_id)

    def click_button_submit_forwarding(self):
        self.click_element('XPATH', self.ppl.button_confirm_set_forwarding_xpath)

    def click_back_submit(self):
        self.click_element('CSS_SELECTOR', self.ppl.button_back_set_forwarding_css)

    def click_settings(self):
        self.click_element('XPATH', self.ppl.settings_xpath)

    def set_default_did(self):
        self.click_element('XPATH', self.ppl.set_default_did_xpath)


