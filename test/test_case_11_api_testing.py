import time

from helpers.api import Api

# Step 1: TODO - Open the application
# Step 2: TODO - Login
# Step 3: TODO - Go to Recruitment ATS section
# Step 4: TODO - Find Candidate 1 using the search field
# Step 5: TODO - Verify Candidate 1's data in the table: Name, Email, Date Applied

def test_verify_candidate_one_api_demo(app):
    # Api.add_candidate_recruitment_section("David", "Test", "2024-05-13", "john.dodsdffdfe@example.com")
    app.orangeHrm.openUrl()
    app.orangeHrm.login_to_the_application()
    app.orangeHrm.sideMenu.click_on_side_menu_button('Recruitment (ATS)')
    app.orangeHrm.recruitment.search_candidate_name('Dimash Test')
    time.sleep(3)