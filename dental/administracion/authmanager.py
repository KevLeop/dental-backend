from django.contrib.auth.models import BaseUserManager  
# Base user te permite modificar todo el modelo interno de Usuarios de django

class UsuarioManager(BaseUserManager):
  def create_user(self, email, nombre, apellido, tipo, password=None):
    if not email:
      raise ValueError("El usuario debe tener obligatoriamente un correo")
    email = self.normalize_email(email)
    usuario = self.model(personalCorreo = email, personalNombre= nombre, 
                        personalApellido=apellido, personalTipo=tipo)
    usuario.set_password(password)
    usuario.save(using=self._db) # para referenciar a la BD
    return usuario
  
  def create_superuser(self, personalCorreo, personalNombre, personalApellido, personalTipo, password):
    usuario = self.create_user(personalCorreo, personalNombre, personalApellido, personalTipo, password)
    # esste campo se crea automaticamente por la herencia del userModel
    usuario.is_superuser = True
    usuario.is_staff = True
    usuario.save(using=self._db)

      
