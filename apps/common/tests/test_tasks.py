from unittest.mock import patch

from django.test import TestCase

from apps.common import tasks


class TestTasks(TestCase):
    @patch('django.core.mail.EmailMultiAlternatives.send')
    def test_send_email(self, mock_send):
        tasks.send_email('someone@example.com', 'Subj', 'Message')
        mock_send.assert_called_once()

    @patch('django.core.mail.EmailMultiAlternatives.send')
    def test_broadcast_email(self, mock_send):
        tasks.broadcast_email(['1@example.com', '2@example.com'], 'Subj', 'Message')
        mock_send.assert_called_once()

    @patch('django.template.loader.render_to_string')
    @patch('django.core.mail.EmailMultiAlternatives.send')
    def test_template_email(self, mock_send, mock_render):
        mock_render.return_value = 'Spam'
        tasks.send_template_email('1@example.com', 'subj_template.txt', 'email_template.txt',
                                  {}, 'html_template.html')
        self.assertEqual(mock_render.call_count, 3)
        mock_send.assert_called_once()
