from enum import Enum

class Main_options(Enum):
    Elements = 1
    Forms = 2
    Alerts = 3
    Alerts_Frame_Windows = 4
    Widgets = 5
    Interactions = 6
    Book_Store_Application = 7

Main_options_mapping = {
        Main_options.Elements.name: 'Elements',
        Main_options.Forms.name: 'Forms',
        Main_options.Alerts.name: 'Alerts',
        Main_options.Alerts_Frame_Windows.name: 'Alerts, Frame & Windows',
        Main_options.Widgets.name: 'Widgets',
        Main_options.Interactions.name: 'Interactions',
        Main_options.Book_Store_Application.name: 'Book Store Application'
    }

class Elements(Enum):
    Text_box = 1
    Check_box = 2
    Alerts = 3
    Radio_button = 4
    Web_tables = 5
    Buttons = 6
    Links = 7
    Broken_Links_Images = 8
    Upload_and_Download = 9
    Dynamic_Properties = 10

Elements_options_mapping = {
        Elements.Text_box.name: 'Text Box',
        Elements.Check_box.name: 'Check Box',
        Elements.Alerts.name: 'Alerts',
        Elements.Radio_button.name: 'Radio Button',
        Elements.Web_tables.name: 'Web Tables',
        Elements.Buttons.name: 'Buttons',
        Elements.Links.name: 'Links',
        Elements.Broken_Links_Images.name: 'Broken Links - Images',
        Elements.Upload_and_Download.name: 'Upload and Download',
        Elements.Dynamic_Properties.name: 'Dynamic Properties'
    }

class Widgets(Enum):
    Accordian = 1
    Auto_complete = 2
    Date_picker = 3
    Slider = 4
    Progress_Bar = 5
    Tabs = 6
    Tool_tips = 7
    Menu = 8
    Select_menu = 9

Widgets_options_mapping = {
        Widgets.Accordian.name: 'Accordian',
        Widgets.Auto_complete.name: 'Auto Complete',
        Widgets.Date_picker.name: 'Date Picker',
        Widgets.Slider.name: 'Slider',
        Widgets.Progress_Bar.name: 'Progress Bar',
        Widgets.Tabs.name: 'Tabs',
        Widgets.Tool_tips.name: 'Tool Tips',
        Widgets.Menu.name: 'Menu',
        Widgets.Select_menu.name: 'Select Menu',
    }

# its not used.
folders = { "Home" : { "Desktop" : [ "Notes", "Commands" ],
                 "Documents" : { "WorkSpace" : [ "React", "Angular", "Veu" ],
							     "Office" : [ "Public", "Private", "Classified", "General" ] },
			     "Download" : [ "Word File.doc", "Excel File.doc" ] }}

web_table_values = [{ "first_name" : "Toto", "last_name" : "titi", "age" : "33", "email" : "toto@gmail.fr", "salary" : "5000", "department" : "Banking"},
                    { "first_name" : "Toto2", "last_name" : "titi2", "age" : "38", "email" : "toto2@gmail.fr", "salary" : "5100", "department" : "Finance"}]

web_table_updates = [{ "first_name" : None, "last_name" : None, "age" : "35", "email" : "toto2new@gmail.fr", "salary" : None, "department" : None}]