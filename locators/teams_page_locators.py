class TeamsPageLocators:
    teams_heading_xpath = '//div[@class="flex justify-center items-center group relative "]//a[text() = "Teams"]'
    add_member_btn_css = '[class=" w-64"] button'
    f_name_name = "first_name"
    l_name_name = "last_name"
    phone_css = '[name="phone"]'
    email_xpath = "//input[@name= 'email']"
    dropdown_role_xpath = "//span[text()='Select role']"
    role_member_xpath = '//div[@class="text-black font-semibold text-base"][text()= "Member"]'
    add_member_submit_xpath = "//button[text()='Submit']"
    teams_sub_heading_css = '[href="/teams/all-teams"]'
    create_team_btn_css = '[class=" w-64"] button'
    team_name_xpath = '//input[@name="name"]'
    select_members_xpath = '//dialog-body//dropdown-element'
    admin_role_xpath = '//div[@class="text-black font-semibold text-base"][text() = "Admin"]'
    submit_create_team_xpath = "//button[@type='submit']"
    select_members_xpath_list = '//dropdown-menu-item//label'
    heading_text_css = '[class=" text-grey-700 text-sm"]'
    search_placeholder_css = '[name="search"]'
    add_member_btn_txt_css = '[class=" w-64"] button'
    refresh_btn_txt_css = '[class="text-black flex items-center gap-2"]'
    table_heading_name_xpath = "//th/div[contains(text(), 'Name')]"
    table_heading_email_xpath = "//th/div[contains(text(), 'Email')]"
    table_heading_Team_xpath = "//th[contains(text(), 'Team')]"
    table_heading_phone_xpath = "//th[contains(text(), 'Phone number')]"
    table_heading_role_xpath = "//th[contains(text(), 'Role')]"
    table_heading_status_xpath = "//th[contains(text(), 'Status')]"
    name_pankaj_xpath = "//span[text()='Pankaj']"
    dot_menu_xpath = "//td[4]"
    team_name_table_xpath = '//td[2]'
    action_edit_team_xpath = '//span[text() = "Edit team"]'
    name_field_by_name = 'name'
    action_invite_to_team_xpath = "//span[text() = 'Invite to team']"
    btn_send_invite_xpath = "//button[text() ='Send invite']"
    action_dot_menu_member_xpath = '//tr[1]//td[8]//div[@class="cursor-pointer w-1"]'
    member_subheading_xpath = '//*[@class="bg-grey-100 flex  body-height overflow-auto  "]//div//a[text() = "Members"]'
    assign_number_xpath = "//span[text()= 'Assign Number']"
    assign_number_close_btn = '//div[@class="flex justify-between items-start py-4 px-6"]/button'
    assign_team_xpath = "//span[text()= 'Assign Team']"
    delete_member_xpath = "//span[text()= 'Delete Member']"
    select_team = "//*[@class='min-w-[460px]'] //label"
    submit_assign_team_css = '[class=" mt-10 px-6 pb-6"] button'
    select_number_css = '[class="text-xs text-grey-600"]'
    submit_assign_number_css = '[class=" mt-10 px-6 pb-6"]'
    unassign_number_xpath = "//span[text() = 'Unassign Number']"
    unassign_submit_css = "[class='mt-10 pb-14'] button"
    edit_member_xpath = "//span[text() = 'Edit Member']"
    edit_member_name_by_name = "first_name"
    submit_edit_member_css = '[class="px-6 mt-4"] button'
    table_css = 'table[class="w-full table table-auto"]'
    table_members_xpath = '//table'
    select_all_checkbox = '//tr//th[1]//input'
    delete_bulk_xpath = '//*[@class="w-64"] /button'

