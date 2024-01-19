import time
import allure
import pytest

from utilities.readproperties import TeamReadConfig, ReadConfig
from pageObjects.teams_page import TeamPage
from utilities.customlogger import LogGen
from testCases.conf_test import setup
from pageObjects.signin_page import SignInPage
from pageObjects.base_page import Base


class TestTeam:
    config_reader = TeamReadConfig()
    l_name = config_reader.add_member_l_name()
    config_reader1 = ReadConfig()
    otp = config_reader1.get_otp()
    baseURL = config_reader1.get_application_url()
    number1 = config_reader1.get_number()
    number_and_spaces = config_reader.add_member_num_vth_spaces()
    special_char = config_reader.add_member_special_char()
    repeating_char = config_reader.add_member_repeating_char()
    registered_email = config_reader.add_member_registered_email()
    team_name = config_reader.team_name()
    txt_heading = config_reader.txt_heading()
    search_place_holder = config_reader.search_place_holder()
    add_member_txt = config_reader.add_member_text()
    name_heading_txt = config_reader.name_table()
    email_heading_txt = config_reader.email_table()
    teams_heading_txt = config_reader.team_heading()
    phone_heading_txt = config_reader.phone_heading()
    role_heading_txt = config_reader.role_table()
    status_heading_txt = config_reader.status_table()
    logger = LogGen.loggen()
    bp = Base()




    @allure.feature('Adding a member')
    @allure.story('Verify member is added successfully.')
    def test_add_member(self, setup):
        self.random_name = self.bp.generate_random_name()
        self.random_email = self.bp.generate_random_email()
        self.random_number = self.bp.generate_random_10_digit_number()
        self.logger.info("__Test One")
        self.logger.info("__Adding Member")
        self.driver = setup
        self.tp = TeamPage(self.driver)
        self.sp = SignInPage(self.driver)
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.sp.send_phone("+234 1234567890")
        self.sp.send_password("OhMG@123")
        self.sp.click_sign_in_btn()
        self.logger.info("__Successful login")
        time.sleep(2)
        self.tp.click_teams_heading()
        self.logger.info("____________Team on header is clicked.")
        time.sleep(2)

        self.tp.click_add_member_btn()
        self.logger.info("____________Clicked add member.")
        self.tp.send_f_name(self.random_name)
        self.logger.info("____________First name is entered.")
        self.tp.send_l_name(self.l_name)
        self.logger.info("____________Last name is entered.")
        self.tp.send_email(self.random_email)
        self.logger.info("Email is entered.")
        self.tp.send_phone_member(self.random_number)
        self.logger.info("____________Phone number is entered")
        self.tp.select_role_dropdown()
        self.logger.info("____________Clicked on dropdown to select the role")
        self.tp.select_role_member()
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), name="Added_role",
                      attachment_type=allure.attachment_type.PNG)
        self.logger.info("____________Selected the role")
        time.sleep(2)
        self.tp.click_submit_add_member()
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), name="Add member screenshot",
                      attachment_type=allure.attachment_type.PNG)
        self.logger.info("__Member added successfully")
        self.tp.table_data_members()

    def test_create_an_admin(self, setup):
        self.random_name = self.bp.generate_random_name()
        self.random_email = self.bp.generate_random_email()
        self.random_number = self.bp.generate_random_10_digit_number()
        self.driver = setup
        self.tp = TeamPage(self.driver)
        self.tp.click_add_member_btn()
        self.logger.info("____________Clicked add member.")
        self.tp.send_f_name(self.random_name)
        self.logger.info("____________First name is entered.")
        self.tp.send_l_name(self.l_name)
        self.logger.info("____________Last name is entered.")
        self.tp.send_email(self.random_email)
        self.logger.info("Email is entered.")
        self.tp.send_phone_member(self.random_number)
        self.logger.info("____________Phone number is entered")
        self.tp.select_role_dropdown()
        self.logger.info("____________Clicked on dropdown to select the role")
        self.tp.select_role_admin()
        allure.attach(self.driver.get_screenshot_as_png(), name="Added_role",
                      attachment_type=allure.attachment_type.PNG)
        self.logger.info("____________Selected the role as member")
        time.sleep(2)
        self.tp.click_submit_add_member()
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), name="Add member screenshot",
                      attachment_type=allure.attachment_type.PNG)
        self.logger.info("__Member added successfully")
        self.tp.table_data_members()

    @allure.feature('Creating a Team')
    @allure.story('Verify team with member is added successfully.')
    def test_create_team(self, setup):
        self.random_team_name = self.bp.generate_random_name()
        self.random_name = self.bp.generate_random_name()
        self.driver = setup
        self.tp = TeamPage(self.driver)
        self.tp.click_subheading_teams()
        self.logger.info("__Clicked on the teams in sidebar")
        self.tp.click_create_team()
        self.logger.info("__Clicked on the create team.")
        self.tp.send_team_name(self.random_team_name)
        self.logger.info("__Team name is entered.")
        self.tp.select_members_drpdown()
        self.logger.info("__Clicked on 'Select dropdown'")
        time.sleep(2)
        self.tp.dropdown_list_select_members()
        # self.tp.list_select()
        self.logger.info("__Selected on member.")
        self.tp.select_members_drpdown()
        self.tp.click_submit_create_team()
        self.logger.info("Team is created successfully")

    @allure.feature('Create a Team')
    @allure.feature('Verify that a team without a member is created successfully')
    def test_create_empty_team(self, setup):
        self.random_team_name = self.bp.generate_random_name()
        self.driver = setup
        self.tp = TeamPage(self.driver)
        time.sleep(2)
        self.tp.click_create_team()
        self.logger.info("__Clicked on the create team.")
        self.tp.send_team_name(self.team_name)
        self.logger.info("__Team name is entered.")

        self.tp.click_submit_create_team()

        self.logger.info("__Clicked on the submit button")
        self.logger.info("__Team without member is created successfully")

    @allure.feature('Inviting team members to already created teams')
    @allure.feature('Verify that a team members are invited successfully')
    def test_perform_actions_team(self, setup):
        self.driver = setup
        self.tp = TeamPage(self.driver)
        self.random_team_name = self.bp.generate_random_name()
        self.tp.click_subheading_teams()

        self.tp.click_drpdwn_for_first_team()
        self.logger.info("__Three dot menu of First team is selected")
        self.tp.click_edit_team()
        self.logger.info("__Clicked on edit team")
        self.tp.change_team_name(self.random_team_name)
        self.logger.info("__Team name is changed")
        self.tp.select_members_drpdown()
        self.logger.info("__Clicked on the member dropdown")
        self.tp.modify_dropdown_elements()
        self.logger.info("__members from the dropdown are modified")
        self.tp.select_members_drpdown()
        self.logger.info("__Clicked on the member dropdown")
        self.tp.click_submit_create_team()
        self.logger.info("__Clicked on the Create Team")
        time.sleep(2)
        self.tp.click_drpdwn_for_first_team()
        self.logger.info("__Three dot menu of First team is selected")
        self.tp.click_invite_2_team()
        self.logger.info("__Clicked on invite to team")
        time.sleep(2)
        self.tp.select_members_to_send_invite()
        self.logger.info("__Clicked on send invite")
        self.tp.click_send_invite()

    def test_table_data_in_excel(self, setup):
        self.driver = setup
        self.tp = TeamPage(self.driver)
        time.sleep(3)
        self.tp.table_data_teams()

    def test_perform_actions_member(self, setup):
        self.driver = setup
        self.tp = TeamPage(self.driver)
        time.sleep(3)
        self.tp.click_member_subheading()
        time.sleep(3)
        self.tp.click_menu_member()
        self.logger.info("__Clicked three dot menu.")

        self.tp.click_assign_team()
        self.logger.info("__Clicked on assign team.")

        self.tp.select_team_to_assign()
        self.logger.info("__Selected team to assign")

        self.tp.click_submit_assign_team()
        self.logger.info("__Submit.")

        time.sleep(3)
        # self.tp.click_menu_member()
        # self.logger.info("__Clicked three dot menu.")

        # self.tp.click_assign_number()
        # self.logger.info("__Clicked assign number.")

        # self.tp.click_number_from_list()
        # self.logger.info("__Selected number from the list.")
        #
        # self.tp.click_submit_assign_number()
        # self.logger.info("__Submit.")
        #
        # time.sleep(3)
        # self.tp.click_menu_member()
        # self.logger.info("__Clicked three dot menu.")

        # self.tp.click_unassign()
        # self.logger.info("__Click unassign number.")

        # # self.tp.click_unassign_submit()
        # self.logger.info("__Submit.")
        #
        # time.sleep(3)
        # # self.tp.click_menu_member()
        # self.logger.info("__Clicked three dot menu.")

        # time.sleep(3)
        # self.tp.click_edit_member()
        # self.logger.info("__Clicked edit member.")
        #
        # self.tp.change_member_name(self.random_name)
        # self.logger.info("__Clicked three dot menu.")
        #
        # self.tp.click_submit_edit_member()
        time.sleep(2)
        # self.tp.click_menu_member()
        # self.tp.click_delete_member()
        self.tp.click_to_select_all()
        self.tp.delete_in_bulk()


