from unittest import TestCase
from unittest.mock import patch, Mock
from main import BaseShopper, Visit
from mixpanel import Mixpanel


class Tests(TestCase):
    """
    Tests.
    """

    def test_visit(self):
        mock_project = Mock(spec=Mixpanel)
        mxp_mock = [mock_project, ]
        END_POINT = "test_endpoint"
        with patch('main.ACTIVE_PROJECTS', mxp_mock):
            new_shopper = BaseShopper()
            new_shopper.visit(end_point=END_POINT)
        self.assertIn(
            END_POINT, mock_project.track.call_args[0]
        )

    def test_a_visit(self):
        mock_project = Mock(spec=Mixpanel)
        mxp_mock = [mock_project, ]
        END_POINT = "test_endpoint"
        with patch('main.ACTIVE_PROJECTS', mxp_mock):
            new_shopper = BaseShopper()

            new_shopper.visit(end_point=END_POINT)
        self.assertIn(
            END_POINT, mock_project.track.call_args[0]
        )

    def test_new_paths(self):
        mock_project = Mock(spec=Mixpanel)
        mxp_mock = [mock_project, ]
        END_POINT = "test_endpoint"
        with patch('main.ACTIVE_PROJECTS', mxp_mock):
            new_shopper = BaseShopper()
            for item in range(20):
                visit = Visit()
                visit.commence()
        for item in mock_project.track.call_args_list:
            if 'Register' in item:
                pass
        call_args = mock_project.track.call_args_list
        import ipdb
        ipdb.set_trace()
