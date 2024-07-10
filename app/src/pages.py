"""
this is where you define your pages (as classes with static "loadPage" functions)
and build your pages with the components you created
"""

from src import components



# HOME PAGE ================================================================================
class HomePage():
    """
    Your Home / Landing Page
    Here you can add your defined components under the loadPage() function
    """
    @staticmethod
    def load_home_page():
        """
        example home page load function
        """
        components.component_say_hello()
        components.component_change_page()
        components.component_input_box()
        components.component_vertical_space(n=2)
        components.component_input_list()
        components.component_recommend_button()
        components.component_recommendations()


