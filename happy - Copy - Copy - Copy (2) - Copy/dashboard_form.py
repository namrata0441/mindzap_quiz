


from PyQt5 import QtCore, QtGui, QtWidgets
import resource_rc

# Import custom widgets
# These imports are now correctly placed within your main application class context.
from profile_widget import ProfileWidget
from aboutUs import AboutUsWidget
from setting import SettingsWidget
from flashcard_page import FlashcardPage
from quiz_form import QuizUiForm

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(832, 629)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.icon_only_widget = QtWidgets.QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName("icon_only_widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.icon_only_widget)
        self.label.setMinimumSize(QtCore.QSize(50, 50))
        self.label.setMaximumSize(QtCore.QSize(60, 60))
        self.label.setText("")

        self.label.setPixmap(QtGui.QPixmap(":/icon/icon/logo_icon.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.home_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.home_btn_1.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon/home_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.home_btn_1.setIcon(icon)
        self.home_btn_1.setIconSize(QtCore.QSize(20, 20))
        self.home_btn_1.setCheckable(True)
        self.home_btn_1.setAutoExclusive(True)
        self.home_btn_1.setObjectName("home_btn_1")
        self.verticalLayout.addWidget(self.home_btn_1)
        self.flash_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.flash_btn_1.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/icon/flashcard_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.flash_btn_1.setIcon(icon1)
        self.flash_btn_1.setIconSize(QtCore.QSize(20, 20))
        self.flash_btn_1.setCheckable(True)
        self.flash_btn_1.setAutoExclusive(True)
        self.flash_btn_1.setObjectName("flash_btn_1")
        self.verticalLayout.addWidget(self.flash_btn_1)
        self.quizze_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.quizze_btn_1.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/icon/quizzes_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.quizze_btn_1.setIcon(icon2)
        self.quizze_btn_1.setIconSize(QtCore.QSize(20, 20))
        self.quizze_btn_1.setCheckable(True)
        self.quizze_btn_1.setAutoExclusive(True)
        self.quizze_btn_1.setObjectName("quizze_btn_1")
        self.verticalLayout.addWidget(self.quizze_btn_1)
        self.about_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.about_btn_1.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/icon/aboutus_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.about_btn_1.setIcon(icon3)
        self.about_btn_1.setIconSize(QtCore.QSize(20, 20))
        self.about_btn_1.setCheckable(True)
        self.about_btn_1.setAutoExclusive(True)
        self.about_btn_1.setObjectName("about_btn_1")
        self.verticalLayout.addWidget(self.about_btn_1)
        self.setting_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.setting_1.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icon/icon/setting_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setting_1.setIcon(icon4)
        self.setting_1.setIconSize(QtCore.QSize(20, 20))
        self.setting_1.setCheckable(True)
        self.setting_1.setAutoExclusive(True)
        self.setting_1.setObjectName("setting_1")
        self.verticalLayout.addWidget(self.setting_1)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 262, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.logout_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.logout_btn_1.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icon/icon/logout_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logout_btn_1.setIcon(icon5)
        self.logout_btn_1.setIconSize(QtCore.QSize(20, 20))
        self.logout_btn_1.setCheckable(True)
        self.logout_btn_1.setAutoExclusive(True)
        self.logout_btn_1.setObjectName("logout_btn_1")
        self.verticalLayout_3.addWidget(self.logout_btn_1)
        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)
        self.full_mwnu_widget = QtWidgets.QWidget(self.centralwidget)
        self.full_mwnu_widget.setObjectName("full_mwnu_widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.full_mwnu_widget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.full_mwnu_widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.home_btn_2 = QtWidgets.QPushButton(self.full_mwnu_widget)
        self.home_btn_2.setCheckable(True)
        self.home_btn_2.setAutoExclusive(True)
        self.home_btn_2.setObjectName("home_btn_2")
        self.verticalLayout_2.addWidget(self.home_btn_2)
        self.flash_btn_2 = QtWidgets.QPushButton(self.full_mwnu_widget)
        self.flash_btn_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/icon/flashcard_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.flash_btn_2.setIcon(icon1)
        self.flash_btn_2.setIconSize(QtCore.QSize(20, 20))
        self.flash_btn_2.setCheckable(True)
        self.flash_btn_2.setAutoExclusive(True)
        self.flash_btn_2.setObjectName("flash_btn_2")
        self.verticalLayout_2.addWidget(self.flash_btn_2)
        self.quizze_btn_2 = QtWidgets.QPushButton(self.full_mwnu_widget)
        self.quizze_btn_2.setCheckable(True)
        self.quizze_btn_2.setAutoExclusive(True)
        self.quizze_btn_2.setObjectName("quizze_btn_2")
        self.verticalLayout_2.addWidget(self.quizze_btn_2)
        self.about_btn_2 = QtWidgets.QPushButton(self.full_mwnu_widget)
        self.about_btn_2.setCheckable(True)
        self.about_btn_2.setAutoExclusive(True)
        self.about_btn_2.setObjectName("about_btn_2")
        self.verticalLayout_2.addWidget(self.about_btn_2)
        self.setting_2 = QtWidgets.QPushButton(self.full_mwnu_widget)
        self.setting_2.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icon/icon/setting_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setting_2.setIcon(icon4)
        self.setting_2.setIconSize(QtCore.QSize(20, 20))
        self.setting_2.setCheckable(True)
        self.setting_2.setAutoExclusive(True)
        self.setting_2.setObjectName("setting_2")
        self.verticalLayout_2.addWidget(self.setting_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 295, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.logout_btn_2 = QtWidgets.QPushButton(self.full_mwnu_widget)
        self.logout_btn_2.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icon/icon/logout_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logout_btn_2.setIcon(icon5)
        self.logout_btn_2.setIconSize(QtCore.QSize(20, 20))
        self.logout_btn_2.setCheckable(True)
        self.logout_btn_2.setAutoExclusive(True)
        self.logout_btn_2.setObjectName("logout_btn_2")
        self.verticalLayout_4.addWidget(self.logout_btn_2)
        self.gridLayout.addWidget(self.full_mwnu_widget, 0, 1, 1, 1)
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget = QtWidgets.QWidget(self.widget_3)
        self.widget.setMinimumSize(QtCore.QSize(0, 40))
        self.widget.setObjectName("widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        # --- Reordered elements to place search at the top-left ---
        self.change_btn = QtWidgets.QPushButton(self.widget)
        self.change_btn.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icon/icon/menu_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.change_btn.setIcon(icon6)
        self.change_btn.setIconSize(QtCore.QSize(25, 25))
        self.change_btn.setCheckable(True)
        self.change_btn.setObjectName("change_btn")
        self.horizontalLayout_4.addWidget(self.change_btn)

        # Search input and button
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.search_input = QtWidgets.QLineEdit(self.widget)
        self.search_input.setObjectName("search_input")
        self.horizontalLayout.addWidget(self.search_input)
        self.search_btn = QtWidgets.QPushButton(self.widget)
        self.search_btn.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icon/icon/search_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_btn.setIcon(icon7)
        self.search_btn.setIconSize(QtCore.QSize(20, 20))
        self.search_btn.setObjectName("search_btn")
        self.horizontalLayout.addWidget(self.search_btn)
        self.horizontalLayout_4.addLayout(self.horizontalLayout)  # Add the search layout here

        # Expanding spacer to push the user button to the right
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)

        # Label to display username
        self.username_display_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.username_display_label.setFont(font)
        self.username_display_label.setStyleSheet("color: #333;")  # Simple styling
        self.username_display_label.setObjectName("username_display_label")
        self.horizontalLayout_4.addWidget(self.username_display_label)

        self.user_btn = QtWidgets.QPushButton(self.widget)
        self.user_btn.setText("")
        icon8 = QtGui.QIcon()
        # FIX: Explicitly name 'mode' and 'state' to resolve TypeError
        icon8.addPixmap(QtGui.QPixmap(":/icon/icon/person_icon.png"), mode=QtGui.QIcon.Normal, state=QtGui.QIcon.Off)
        self.user_btn.setIcon(icon8)
        self.user_btn.setIconSize(QtCore.QSize(25, 25))
        self.user_btn.setObjectName("user_btn")
        self.horizontalLayout_4.addWidget(self.user_btn)
        # --- End of reordered elements ---

        self.verticalLayout_5.addWidget(self.widget)
        self.stackedWidget = QtWidgets.QStackedWidget(self.widget_3)
        self.stackedWidget.setObjectName("stackedWidget")

        # Page 0: Home Page (self.page)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(self.page)
        font = QtGui.QFont()
        font.setPointSize(24) # Increased font size for prominence
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page)

        # Page 1: Profile Page (self.page_7) - Now using ProfileWidget
        self.page_7 = ProfileWidget()  # Instantiate your custom ProfileWidget
        self.page_7.setObjectName("page_7")  # Keep the object name for consistency
        self.stackedWidget.addWidget(self.page_7)

        # Page 2: Flashcard Page (self.page_2) - Now using FlashcardPage
        self.page_2 = FlashcardPage()  # NEW: Instantiate FlashcardPage
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)

        # Page 3: Quizze Page (self.page_3) - NOW USING QUIZUIFORM
        # Remove the generic QWidget and replace it with your QuizUiForm
        self.page_3 = QuizUiForm() # IMPORTANT CHANGE HERE
        self.page_3.setObjectName("page_3")
        # No need for label_6 or gridLayout_4 here, as QuizUiForm manages its own content
        self.stackedWidget.addWidget(self.page_3)


        # Page 4: About us Page (self.page_4) - Now using AboutUsWidget
        self.page_4 = AboutUsWidget()  # Changed from QtWidgets.QWidget() to AboutUsWidget()
        self.page_4.setObjectName("page_4")  # Keep the object name for consistency
        self.stackedWidget.addWidget(self.page_4)

        # Page 5: Settings Page (self.page_5) - Now using SettingsWidget
        self.page_5 = SettingsWidget()  # New: Instantiate your custom SettingsWidget
        self.page_5.setObjectName("page_5")  # Keep the object name for consistency
        self.stackedWidget.addWidget(self.page_5)

        # Page 6: Search Page (self.page_6)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.page_6)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_9 = QtWidgets.QLabel(self.page_6)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_9.setFont(font)
        self.label_9.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.NoContextMenu)
        self.label_9.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_7.addWidget(self.label_9, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_6)

        self.verticalLayout_5.addWidget(self.stackedWidget)
        self.gridLayout.addWidget(self.widget_3, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        # Connect the search button to the search_button_clicked method
        self.search_btn.clicked.connect(self.search_button_clicked)

        # Set initial page. If you want Home to be default, change to 0.
        self.stackedWidget.setCurrentIndex(0)  # Changed to Home Page as default

        # Connect sidebar buttons to switch stackedWidget pages
        self.home_btn_1.toggled['bool'].connect(
            lambda checked: self.stackedWidget.setCurrentIndex(0) if checked else None)
        self.home_btn_2.toggled['bool'].connect(
            lambda checked: self.stackedWidget.setCurrentIndex(0) if checked else None)

        # Flashcard button connections now point to the FlashcardPage (index 2)
        self.flash_btn_1.toggled['bool'].connect(
            lambda checked: self.stackedWidget.setCurrentIndex(2) if checked else None)
        self.flash_btn_2.toggled['bool'].connect(
            lambda checked: self.stackedWidget.setCurrentIndex(2) if checked else None)

        # Quizze button connections now point to QuizUiForm (index 3)
        self.quizze_btn_1.toggled['bool'].connect(
            lambda checked: self.stackedWidget.setCurrentIndex(3) if checked else None)
        self.quizze_btn_2.toggled['bool'].connect(
            lambda checked: self.stackedWidget.setCurrentIndex(3) if checked else None)

        # About Us button connections are now for AboutUsWidget (index 4)
        self.about_btn_1.toggled['bool'].connect(
            lambda checked: self.stackedWidget.setCurrentIndex(4) if checked else None)
        self.about_btn_2.toggled['bool'].connect(
            lambda checked: self.stackedWidget.setCurrentIndex(4) if checked else None)

        # Settings button connections are now for SettingsWidget (index 5)
        self.setting_1.toggled['bool'].connect(
            lambda checked: self.stackedWidget.setCurrentIndex(5) if checked else None)
        self.setting_2.toggled['bool'].connect(
            lambda checked: self.stackedWidget.setCurrentIndex(5) if checked else None)

        # Connect user_btn to Profile Page (index 1)
        self.user_btn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))

        # Connect toggle buttons for sidebar visibility
        self.change_btn.toggled['bool'].connect(self.icon_only_widget.setVisible)
        self.change_btn.toggled['bool'].connect(self.full_mwnu_widget.setHidden)

        # Ensure mutual exclusivity for sidebar buttons (already there, but good to check)
        self.setting_1.toggled['bool'].connect(self.setting_2.setChecked)
        self.about_btn_1.toggled['bool'].connect(self.about_btn_2.setChecked)
        self.quizze_btn_1.toggled['bool'].connect(self.quizze_btn_2.setChecked)
        self.flash_btn_1.toggled['bool'].connect(self.flash_btn_2.setChecked)
        self.home_btn_1.toggled['bool'].connect(self.home_btn_2.setChecked)
        self.flash_btn_2.toggled['bool'].connect(self.flash_btn_1.setChecked)
        self.quizze_btn_2.toggled['bool'].connect(self.quizze_btn_1.setChecked)
        self.about_btn_2.toggled['bool'].connect(self.about_btn_1.setChecked)
        self.setting_2.toggled['bool'].connect(self.setting_1.setChecked)

        self.logout_btn_2.clicked.connect(MainWindow.close)
        self.logout_btn_1.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Set the username display label text to a default. main.py will update this.
        self.username_display_label.setText("Welcome!")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Sidebar"))
        self.home_btn_2.setText(_translate("MainWindow", "Home"))
        self.flash_btn_2.setText(_translate("MainWindow", "Flashcard"))
        self.quizze_btn_2.setText(_translate("MainWindow", "Quizze"))
        self.about_btn_2.setText(_translate("MainWindow", "About Us"))
        self.setting_2.setText(_translate("MainWindow", "Settings"))
        self.logout_btn_2.setText(_translate("MainWindow", "Logout"))
        self.search_input.setPlaceholderText(_translate("MainWindow", "search......."))
        # Labels for pages - these are just text labels, the actual page content is in the stackedWidget
        self.label_4.setText(_translate("MainWindow", "Welcome to MindZap!")) # Changed text here
        # self.label_6.setText(_translate("MainWindow", "Quizze Page")) # This label is no longer needed, QuizUiForm handles its own content
        self.label_9.setText(_translate("MainWindow", "Search Page"))

    # New method to handle search button click - CORRECTLY INDENTED
    def search_button_clicked(self):
        search_query = self.search_input.text().strip().lower()
        print(f"Search button clicked! Query: '{search_query}'")

        # Map search queries to stackedWidget indices based on the order they are added in setupUi
        # Index 0: self.page (Home Page)
        # Index 1: self.page_7 (Profile Page - now ProfileWidget)
        # Index 2: self.page_2 (Flashcard Page - now FlashcardPage)
        # Index 3: self.page_3 (Quizze Page - now QuizUiForm)
        # Index 4: self.page_4 (About us Page - now AboutUsWidget)
        # Index 5: self.page_5 (Settings Page - now SettingsWidget)
        # Index 6: self.page_6 (Search Page)

        if search_query == "home":
            self.stackedWidget.setCurrentIndex(0)  # Home Page
        elif search_query == "profile":
            self.stackedWidget.setCurrentIndex(1)  # Profile Page
        elif search_query == "flashcard" or search_query == "flashcards":
            self.stackedWidget.setCurrentIndex(2)  # Flashcard Page
        elif search_query == "quizze" or search_query == "quizzes":
            self.stackedWidget.setCurrentIndex(3)  # Point Quizze search to QuizUiForm
        elif search_query == "about us" or search_query == "about":
            self.stackedWidget.setCurrentIndex(4)  # About us Page
        elif search_query == "settings" or search_query == "setting":
            self.stackedWidget.setCurrentIndex(5)  # Settings Page
        else:
            # Default to Search Page for any other query
            self.stackedWidget.setCurrentIndex(6)  # Search Page

        self.search_input.clear()  # Clear the search input after searching

    # Added set_username_display method for main.py to call
    def set_username_display(self, username):
        """Sets the text of the username display label."""
        if self.username_display_label:
            self.username_display_label.setText(f"Welcome, {username}!")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow() # Create an instance of your UI class
    ui.setupUi(MainWindow) # Set up the UI on the main window
    MainWindow.show()
    sys.exit(app.exec_())
