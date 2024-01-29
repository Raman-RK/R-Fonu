class CallPageLocators:
    # main elements
    call_heading_xpath = "//div[@class='flex justify-center items-center group relative '][a[text() = 'Calls']]"
    call_details_xpath = "//div[@class='bg-grey-100 flex  body-height overflow-auto  ']/div/a[text() = 'Call details']"
    call_recordings_xpath = ("//div[@class='bg-grey-100 flex  body-height overflow-auto  ']/div/a[text() = 'Call "
                             "recordings']")
    voicemail_xpath = "//div[@class='bg-grey-100 flex  body-height overflow-auto  ']/div/a[text() = 'Voicemails']"
    set_forwarding_xpath = ("//div[@class='bg-grey-100 flex  body-height overflow-auto  ']/div/a[text() = 'Set "
                            "forwarding']")
    custom_greetings_xpath = ("//div[@class='bg-grey-100 flex  body-height overflow-auto  ']/div/a[text() = 'Custom "
                              "greetings']")
    phone_menu_xpath = "//div[@class='bg-grey-100 flex  body-height overflow-auto  ']/div/a[text() = 'Phone menu']"
    search_box_name = '[name="search"]'

    # text
    manage_call_history_txt = "//div[text()='Manage call history in your workspace']"
    table_header_path = "//th"  # loop elements leave first and last #for all pages(containing tables)
    phone_number_xpath = "//label[text()='Phone number']"
    forward_calls_to_xpath = "//label[text()='Forward calls to']"
    select_member_xpath = "//label[text()='Select Member']"
    forward_how_long_xpath = "//label[text()='Forward how long?']"
    if_no_answer_xpath = "//label[text()='If no answer, then forward call to']"
    note_xpath = ("//div[text() = 'NOTE: When someone calls, attempt to connect the call as a Fonu web call first. If "
                  ""
                  "the call is unable to connect or you do not pick up,']")

    # Call details

    all_details_xpath = '//div[starts-with(@class, "bg-tranparent")][text() = "All"]'
    outgoing_xpath = '//div[starts-with(@class, "bg-tranparent")][text() = "Outgoing"]'
    missed_call_details_xpath = '//div[starts-with(@class, "bg-tranparent")][text() = "Missed"]'
    incoming_call_details_xpath = '//div[starts-with(@class, "bg-tranparent")][text() = "Incoming"]'
    check_box_xpath = "//th[1]"

    # Set forwarding
    number_drpdown_xpath = '//div[label[text()="Phone number"]]//dropdown-caret'
    number_xpath = "//label/div[text()='+234 12054308935']"
    forward_call_drpdwn_x = '//div[label[text()="Forward calls to"]]//dropdown-caret'
    select_member_drpdown_x = '//div[label[text()="Select Member"]]//dropdown-caret'
    forward_duration_drpdwn_x = '//div[label[text()="Forward how long?"]]//dropdown-caret'
    confirm_button_xpath = "//button[text() = 'Confirm']"
    forward_duration_x = '//div[@value="27"]'

    # to member
    member_option_xpath = '//div[@value="EXTENSION"]'
    member_name_option = '//div[starts-with(@class, "w-full h-full flex")]'

    # to team
    team_option_xpath = '//div[@value="TEAM"]'
    team_name_option = '//div[starts-with(@class, "w-full h-full flex")]'

    # to number
    input_field_number_css = '[id=":r2:"]'
    number_option_x = '//div[@value="NUMBER"]'

    # to fonu number
    fonu_number_option_x = '//div[@value="FONU_NUMBER"]'
    input_fonu_css = '[role="textarea"]'

    # to hangup
    hangup_option_x = '//div[@value="HANGUP"]'

    # to voicemail
    voicemail_option_x = '//div[@value="VOICEMAIL"]'

    # to phone menu
    phone_menu_option_x = '//div[@value="IVR"]'
    phone_menu_drpdown_css = '[role="textarea"]'
    phone_menu_list_css = '//label[starts-with(@class, "w-full")]'

    # to SIP
    ip_address_option_x = '//div[@value="IP"]'
    input_ip_address_css = '[id=":r15:"]'
