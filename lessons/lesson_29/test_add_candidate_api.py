from helpers.api import Api

def test_add_candidate_api_demo(app):
    Api.add_candidate_recruitment_section("Dimash2", "Test", "2024-05-13", "dimash2.dodsdffdfe@example.com")
    app.orangeHrm.openUrl()
    app.orangeHrm.login_to_the_application()