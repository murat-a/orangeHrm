import time

from helpers.api import Api

# Test Steps:
# 1. Open the application
# 2. Login
# 3. Go to Attendance Sheets section
# 4. TODO - Verify that the Attendance Sheets table is displayed with correct columns
# Expected Result: The Attendance Sheets table is displayed with columns for Employee Id, Employee Name, Supervisor(s),
# Regular Time, Extra Time, and Total Leave.
def test_verify_attendance_sheets_display(app):
    app.orangeHrm.openUrl()
    app.orangeHrm.login_to_the_application()
    app.orangeHrm.sideMenu.click_on_side_menu_button('Attendance')
    app.orangeHrm.attendance.get_table_headers()
    time.sleep(10)