# Explorando Duolingo

Hasta la fecha actual (26/08/2023), Duolingo pone a disposición un conjunto de puntos de conexión abiertos que permiten acceder a información relacionada con los estudiantes de su plataforma, utilizando tanto el nombre de usuario como la dirección de correo electrónico como parámetros de búsqueda.

## Puntos de Conexión Disponibles

Los endpoints que se encuentran disponibles son los siguientes:

- Información del usuario a través del nombre de usuario: [https://www.duolingo.com/2017-06-30/users?username=nombre_usuario](https://www.duolingo.com/2017-06-30/users?username=nombre_usuario)
- Información del usuario a través del correo electrónico: [https://www.duolingo.com/2017-06-30/users?mail=email@gmail.com](https://www.duolingo.com/2017-06-30/users?mail=email@gmail.com)

## Desafíos en la Obtención de Datos

La tarea de obtener información de un gran número de usuarios plantea desafíos significativos debido a la inmensa cantidad de personas que utilizan la plataforma de Duolingo. Incluso obtener el nombre de usuario de al menos un centenar de individuos puede resultar complicado. La opción de utilizar correos electrónicos tampoco es viable a menos que se cuente con una extensa base de datos de direcciones.

Es relevante aclarar que la obtención de estos datos se enmarca en un contexto de aprendizaje, donde se busca familiarizarse con el uso de una API, el web scraping y el análisis de datos. En consecuencia, el código utilizado con esta finalidad es de carácter público. Es importante destacar que los datos específicos obtenidos no serán divulgados.

## Estrategias para Obtener Nombres de Usuario

Una estrategia para obtener nombres de usuario se deriva del propio diseño de la página de Duolingo:

![Imagen de Duolingo](/img/Screenshot_38.png)

Al explorar tu perfil y la lista de seguidores, si inspeccionas las URL al mover el cursor sobre los perfiles de los seguidores, notarás que siguen el formato: [https://www.duolingo.com/u/numeracion](https://www.duolingo.com/u/numeracion). Resulta que esta numeración es correlativa. Además, si introduces esta URL en un navegador, serás redirigido al perfil del usuario correspondiente, lo que revela su nombre de usuario.

## Archivos "obtener.py" y "obtener.js"

En los archivos mencionados se encuentran las funciones esenciales para explorar un rango de URLs y detectar redirecciones en caso de que estas existan. El archivo "obtener.js" ofrece mayor velocidad, pero debido a las respuestas y restricciones del servidor, su eficacia disminuye en análisis de gran escala. "obtener.py", por su parte, utiliza la librería Selenium para verificar cada URL, incorporando intervalos de espera adecuados para garantizar respuestas correctas. La capacidad de configurar el almacenamiento de datos ayuda a evitar pérdidas, y se han establecido varios agentes para prevenir la detección por parte del servidor al ejecutar múltiples solicitudes.

## Uso del Archivo "app.py"

Una vez obtenidos los nombres de usuario, el archivo "app.py" se encarga de extraer información a través de los puntos de conexión mencionados. Los resultados se almacenan en un dataframe, lo cual facilita análisis posteriores.

# Conclusiones

Es fundamental resaltar que el enfoque utilizado para este propósito es con fines educativos y formativos. La divulgación de datos obtenidos de manera específica está sujeta a restricciones éticas y legales, por lo que se ha tomado precaución en garantizar la privacidad y la integridad de los datos de los usuarios.
