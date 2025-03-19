from django.test import TestCase
from django.urls import reverse
from .models import Adolescente
from django.contrib.auth.models import User

class AdolescenteViewTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.adolescente = Adolescente.objects.create(
            nome='John',
            sobrenome='Doe',
            data_nascimento='2005-01-01',
            genero='M',
            pg='Test PG'
        )

    def test_login_view(self):
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'testpass'})
        self.assertEqual(response.status_code, 302)  # Should redirect after login

    def test_listar_adolescentes_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('listar_adolescentes'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'John Doe')

    def test_create_adolescente_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('criar_adolescente'), {
            'nome': 'Jane',
            'sobrenome': 'Doe',
            'data_nascimento': '2006-01-01',
            'genero': 'F',
            'pg': 'Test PG'
        })
        self.assertEqual(response.status_code, 302)  # Should redirect after creation
        self.assertEqual(Adolescente.objects.count(), 2)  # Check if the new record was created

    def test_edit_adolescente_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('editar_adolescente', args=[self.adolescente.id]), {
            'nome': 'John',
            'sobrenome': 'Doe',
            'data_nascimento': '2005-01-01',
            'genero': 'M',
            'pg': 'Updated PG'
        })
        self.assertEqual(response.status_code, 302)  # Should redirect after editing
        self.adolescente.refresh_from_db()
        self.assertEqual(self.adolescente.pg, 'Updated PG')  # Check if the record was updated

    def test_delete_adolescente_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('excluir_adolescente', args=[self.adolescente.id]))
        self.assertEqual(response.status_code, 302)  # Should redirect after deletion
        self.assertEqual(Adolescente.objects.count(), 0)  # Check if the record was deleted
