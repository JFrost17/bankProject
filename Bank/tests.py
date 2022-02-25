from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.utils import timezone
from http import HTTPStatus

from .models import Deposit, Withdrawl
# Create your tests here.

class LoginTests(TestCase):
    def test_login_valid_account(self):
        User.objects.create_user("user1", password="1234").save()
        form_data = {"username": "user1", "password": "1234"}
        response = self.client.post(
            "/login", form_data, follow=True
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "Account Balance:")

    def test_login_invalid_account(self):
        form_data = {"username": "user1", "password": "1234"}
        response = self.client.post(
            "/login", form_data, follow=True
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "Invalid login! Please try again.")


class RegisterTests(TestCase):
    def test_register_valid_info(self):
        form_data = {
            "username": "user1",
            "password1": "`(2)zy7H89aL}*X",
            "password2": "`(2)zy7H89aL}*X"
        }
        response = self.client.post(
            "/register", form_data, follow=True
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "Login")

    def test_register_invalid_info(self):
        form_data = {
            "username": "user1",
            "password1": "yo",
            "password2": "yo"
        }
        response = self.client.post(
            "/register", form_data, follow=True
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "Register")


class DepositDisplayTests(TestCase):
    def test_deposit_display(self):
        Deposit.objects.create(depositAmount=100).save()
        Deposit.objects.create(depositAmount=50).save()
        response = self.client.get("/")
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "$50.00")

    def test_withdraw_display(self):
        Withdrawl.objects.create(withdrawlAmount=100).save()
        Withdrawl.objects.create(withdrawlAmount=50).save()
        response = self.client.get("/")
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "$50.00")


class DepositFormTests(TestCase):
    def test_deposit_positive_amount(self):
        form_data = {"depositAmount": 50}
        response = self.client.post(
            "/", form_data, follow=True
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "Account Balance: $50.00")

    def test_deposit_negative_amount(self):
        form_data = {"depositAmount": -50}
        response = self.client.post(
            "/", form_data, follow=True
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "Account Balance: $0.00")


class WithdrawFromTests(TestCase):
    def test_withdraw_positive_amount(self):
        Deposit.objects.create(depositAmount=100).save()
        form_data={"withdrawlAmount": 50}
        response = self.client.post(
            "/", form_data, follow=True
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "Account Balance: $50.00")

    def test_withdraw_negative_amount(self):
        form_data={"withdrawlAmount": -50}
        response = self.client.post(
            "/", form_data, follow=True
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "Account Balance: $0.00")
