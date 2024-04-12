
def test_lesson_17_drag_and_drop(app):
    app.demonstrationAppDemoQa.openUrl()
    app.demonstrationAppDemoQa.go_to_side_menu_section("Interactions", "Droppable",)
    app.demonstrationAppDemoQa.drag_and_drop()

def test_lesson_17_drop_down_select(app):
    app.demonstrationAppDemoQa.openUrl()
    app.demonstrationAppDemoQa.go_to_side_menu_section("Widgets", "Select Menu")
    app.demonstrationAppDemoQa.select_value_from_old_style_drop_down('White')

def test_lesson_17_upload_file(app):
    app.demonstrationAppDemoQa.openUrl()
    app.demonstrationAppDemoQa.go_to_side_menu_section("Elements", "Upload and Download")
    app.demonstrationAppDemoQa.upload_file('/Users/admin/PycharmProjects/orangeHrm/files/test_upload.txt')