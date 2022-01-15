## Desarrollo y Personalización módulo Lista de tareas

El primer paso que tenemos que hacer introducir el siguiente comando en la terminal del usuario odoo

./odoo14/odoo-bin scaffold Ejemplo02-scaffold odoo14-custom-addons/

Ahora tenemos que modifcar los ficheros __manifest.py models.py y views.xml que se encuentran dentro de la estructura del modulo que acabamos de crear(antes de eso es recomendable renombrar la carpeta con el nombre "lista de tareas",con el objetivo que en el momento de actualizar las aplicaciones en nuestro odoo podamos visualizar la aplicación con el nombre que queremos).

## Desarrollo de los ficheros __manifest.py models.py y views.xml

### __manifest.py

