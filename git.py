questions = [
    {"question": "¿Cuál de los siguientes es un beneficio de usar Git?",
    "options": ["Facilitar la escritura de código más rápido.",
                "Trabajo colaborativo.",
                "Mejorar el diseño visual de una aplicación.",
                "Crear bases de datos más eficientes."],
    "answer": "b"},
    {"question": "¿Qué es un conflicto de merge?",
    "options": ["Cuando el repositorio remoto no coincide con el local.",
                "Cuando dos ramas tienen cambios en la misma línea de un archivo y no se pueden fusionar automáticamente.",
                "Cuando no se ha hecho un commit en el repositorio local.",
                "Cuando los cambios en la rama principal se pierden al fusionarse."],
    "answer": "b"},
    {"question": "¿Qué es un fork?",
    "options": ["Un mecanismo para fusionar cambios entre ramas.",
                "Un método para copiar un repositorio y trabajar en una versión separada.",
                "Una técnica para eliminar ramas antiguas.",
                "Un comando para revertir cambios en el historial de commits."],
    "answer": "b"},
    {"question": "¿Qué es Git?",
    "options": ["Un lenguaje de programación orientado a objetos.",
                "Una herramienta para compilar código fuente.",
                "Un sistema para el control de versiones del código fuente.",
                "Un editor de texto avanzado para desarrolladores."],
    "answer": "c"},
    {"question": "¿Qué comando inicializa un repositorio Git?",
    "options": ["git init",
                "git start",
                "git create",
                "git repo"],
    "answer": "a"},
    {"question": "¿Qué comando se usa para clonar un repositorio?",
    "options": ["git fork",
                "git download",
                "git clone",
                "git branch"],
    "answer": "c"},
    {"question": "¿Qué es un commit?",
    "options": ["Un mensaje descriptivo de los cambios realizados.",
                "Un comando para fusionar ramas.",
                "Un registro de los cambios realizados en el código.",
                "Una versión en vivo del repositorio remoto."],
    "answer": "c"},
    {"question": "¿Qué significa la opción -m en el comando git commit?",
    "options": ["Mover archivos.",
                "Añadir un mensaje.",
                "Mejorar cambios.",
                "Mostrar historial."],
    "answer": "b"},
    {"question": "¿Qué comando muestra el historial de commits?",
    "options": ["git show",
                "git history",
                "git log",
                "git status"],
    "answer": "c"},
    {"question": "¿Qué significa 'stash' en Git?",
    "options": ["Un comando para guardar cambios pendientes sin hacer commit.",
                "Un método para eliminar commits antiguos.",
                "Un comando para revertir el estado actual del repositorio.",
                "Un sistema para trabajar con múltiples ramas."],
    "answer": "a"},
    {"question": "¿Qué hace el comando git status?",
    "options": ["Muestra el historial de commits.", 
                "Verifica el estado actual del repositorio.",
                "Guarda cambios en un archivo específico.",
                "Clona un repositorio remoto."],
    "answer": "b"},
    {"question": "¿Cómo se crea una nueva rama en Git?",
    "options": ["git branch nueva-rama", "git checkout nueva-rama",
                "git create nueva-rama", "git new nueva-rama"],
    "answer": "a"},
    {"question": "¿Qué comando se usa para cambiar de rama?",
    "options": ["git checkout [nombre-rama]", "git branch [nombre-rama]",
                "git change [nombre-rama]", "git switch [nombre-rama]"],
    "answer": "d"},
    {"question": "¿Qué comando se utiliza para fusionar ramas?",
    "options": ["git commit", "git merge", "git branch", "git pull"],
    "answer": "b"},
    {"question": "¿Qué comando sube los cambios al repositorio remoto?",
    "options": ["git push", "git upload", "git commit", "git send"],
    "answer": "a"},
    {"question": "¿Qué comando baja los cambios del repositorio remoto?",
    "options": ["git pull", "git fetch", "git clone", "git download"],
    "answer": "a"},
    {"question": "¿Qué significa HEAD en Git?",
    "options": ["El primer commit en un repositorio.",
                "La rama principal del repositorio.",
                "Un puntero a la última confirmación del estado actual.",
                "Un alias para el repositorio remoto."],
    "answer": "c"},
    {"question": "¿Qué es un tag en Git?",
    "options": ["Un mecanismo para marcar commits específicos.",
                "Un tipo especial de rama para colaboración.",
                "Un archivo temporal para guardar cambios.",
                "Un comando para realizar cambios rápidos."],
    "answer": "a"},
    {"question": "¿Qué hace el comando git diff?",
    "options": ["Muestra los cambios entre el estado actual y el último commit.",
                "Crea una nueva rama para cambios.",
                "Combina los cambios entre dos ramas.",
                "Crea una copia exacta del repositorio remoto."],
    "answer": "a"},
    {"question": "¿Cómo se elimina un archivo del repositorio pero no del disco?",
    "options": ["git rm", "git delete", "git ignore", "git rm --cached"],
    "answer": "d"},
    {"question": "¿Cuál es el flujo típico de trabajo en Git?",
    "options": ["init -> status -> push -> merge",
                "add -> commit -> push",
                "status -> pull -> add -> init",
                "merge -> add -> log"],
    "answer": "b"},
    {"question": "¿Qué herramienta proporciona interfaces gráficas para usar Git?",
    "options": ["GitHub Desktop", "GitVisual", "Branch Manager", "RepoSync"],
    "answer": "a"},
            {"question": "¿Qué significa 'origin' en Git?",
    "options": ["El repositorio local por defecto.",
                "El repositorio remoto por defecto.",
                "La rama principal del repositorio.", 
                "Un archivo temporal para cambios no confirmados."],
    "answer": "b"},
    {"question": "¿Cómo se soluciona un conflicto de merge en Git?",
    "options": ["Ignorando los cambios conflictivos.",
                "Editando manualmente las partes conflictivas y haciendo un commit.",
                "Ejecutando el comando git fix.",
                "Borrando la rama conflictiva."],
    "answer": "b"},
    {"question": "¿Qué comando devuelve el repositorio a un estado anterior?",
    "options": ["git revert", "git reset", "git rollback", "git checkout"],
    "answer": "b"},
    {"question": "¿Qué comando muestra los cambios en los archivos no confirmados?",
    "options": ["git show", "git diff", "git log", "git status"],
    "answer": "b"},
    {"question": "¿Qué es un pull request?",
    "options": ["Un comando para solicitar cambios en un repositorio remoto.",
                "Una solicitud para fusionar cambios en un repositorio remoto.",
                "Un método para clonar un repositorio privado.",
                "Un comando para sincronizar ramas locales con remotas."],
    "answer": "b"},
    {"question": "¿Qué sucede al usar el comando git rm archivo.txt?",
    "options": ["Se elimina el archivo del repositorio y del disco.", 
                "Se elimina el archivo del disco pero no del repositorio.",
                "Se elimina el archivo del repositorio pero no del disco.", 
                "Se guarda el archivo en una nueva rama temporal."],
    "answer": "a"},
    {"question": "¿Qué hace el comando git add .?",
    "options": ["Confirma todos los cambios en el repositorio.",
                "Agrega todos los cambios pendientes al área de preparación.",
                "Muestra los cambios realizados en todos los archivos.",
                "Crea una nueva rama para los cambios actuales."],
    "answer": "b"},
    {"question": "¿Qué significa 'checkout' en Git?",
    "options": ["Cambiar a una rama o commit específico.",
                "Fusionar cambios entre dos ramas.",
                "Actualizar el repositorio remoto.", 
                "Revertir cambios en un archivo local."],
    "answer": "a"},
    {"question": "¿Qué diferencia hay entre git pull y git fetch?",
    "options": ["git pull clona el repositorio, git fetch no.",
                "git fetch actualiza cambios remotos sin fusionarlos, git pull fusiona los cambios directamente.",
                "git fetch elimina conflictos de fusión, git pull no lo hace.",
                "git pull guarda los cambios en stash automáticamente, git fetch no."],
    "answer": "b"},
    {"question": "¿Cómo se deshace un commit sin eliminar los cambios?",
    "options": ["git reset --soft", "git revert", "git restore", "git stash"],
    "answer": "a"},
    {"question": "¿Cuál es el propósito de un archivo .gitignore?",
    "options": ["Indicar qué archivos deben ser eliminados del repositorio.",
                "Especificar qué archivos deben ser ignorados por Git.",
                "Definir qué archivos deben fusionarse automáticamente.",
                "Listar las ramas protegidas del repositorio."],
    "answer": "b"},
    {"question": "¿Qué es un submódulo en Git?",
    "options": ["Un repositorio independiente incluido dentro de otro repositorio.",
                "Una rama secundaria en el repositorio principal.",
                "Un archivo temporal para cambios no confirmados.", 
                "Un mecanismo para clonar múltiples repositorios a la vez."],
    "answer": "a"},
    {"question": "¿Qué comando enumera las ramas existentes?",
    "options": ["git list", "git show-branches", "git branch", "git branches"],
    "answer": "c"},
    {"question": "¿Qué sucede al usar git stash pop?",
    "options": ["Aplica los cambios guardados en el stash y elimina el stash.",
                "Crea un nuevo commit con los cambios guardados.",
                "Descarta los cambios guardados en el stash.",
                "Combina los cambios del stash con los cambios actuales sin eliminarlos."],
    "answer": "a"},
    {"question": "¿Qué significa hacer un 'squash' en Git?",
    "options": ["Eliminar commits antiguos.",
                "Fusionar varios commits en uno solo.",
                "Ignorar cambios pendientes en el área de preparación.",
                "Fusionar dos ramas en una sola."],
    "answer": "b"},
    {"question": "¿Qué comando elimina una rama local?",
    "options": ["git remove", "git delete", "git branch -d", "git branch --delete"],
    "answer": "c"},
    {"question": "¿Qué comando se utiliza para comparar ramas en Git?",
    "options": ["git branch -c", "git diff", "git compare", "git log --branches"],
    "answer": "b"},
    {"question": "¿Qué significa hacer un 'rebase' en Git?",
    "options": ["Reescribir el historial de commits aplicando los cambios en una nueva base.",
                "Combinar cambios de diferentes ramas en un solo commit.",
                "Eliminar commits antiguos en una rama secundaria.",
                "Crear una copia exacta del repositorio remoto."],
    "answer": "a"},
    {"question": "¿Qué comando muestra un resumen de las operaciones de fusión?",
    "options": ["git show", "git merge --stat", "git log --merges", "git diff --summary"],
    "answer": "b"},
    {"question": "¿Qué opción del comando git diff permite comparar ramas?",
    "options": ["--compare", "--branches", "--summary", "--name-only"],
    "answer": "d"},
    {"question": "¿Qué comando lista los archivos modificados en el último commit?",
    "options": ["git log --name-only", "git show --name-only", "git diff --cached", "git status --last"],
    "answer": "b"},
    {"question": "¿Qué significa 'detached HEAD' en Git?",
    "options": ["El repositorio no tiene commits.",
                "El puntero HEAD no apunta a ninguna rama, sino a un commit específico.",
                "La rama principal ha sido eliminada.",
                "Los cambios locales no se han sincronizado con el remoto."],
    "answer": "b"},
    {"question": "¿Qué significa 'fast-forward' en Git?",
    "options": ["Un tipo de fusión que actualiza directamente el puntero de la rama sin crear un nuevo commit.",
                "Una opción para eliminar conflictos en merges.",
                "Un método para actualizar ramas sin cambiar el historial.",
                "Un comando para revertir cambios rápidamente."],
    "answer": "a"},
    {"question": "¿Qué comando elimina un archivo del área de preparación?",
    "options": ["git restore --staged", "git unstage", "git rm --cached", "git delete --staged"],
    "answer": "a"},
    {"question": "¿Qué opción del comando git log muestra un historial gráfico de ramas?",
    "options": ["--oneline", "--graph", "--pretty=graph", "--decorate"],
    "answer": "b"},
    {"question": "¿Qué hace el comando git config?",
    "options": ["Configura opciones globales o locales para Git.",
                "Inicializa un repositorio.",
                "Fusiona cambios en un archivo de configuración.",
                "Crea un commit con opciones personalizadas."],
    "answer": "a"},
    {"question": "¿Qué es un cherry-pick en Git?",
    "options": ["Seleccionar un commit específico y aplicarlo a la rama actual.",
                "Fusionar dos commits en uno solo.",
                "Eliminar commits antiguos de una rama secundaria.",
                "Mover cambios a un nuevo stash."],
    "answer": "a"},
    {"question": "¿Qué sucede si ejecutas git commit --amend?",
    "options": ["Se confirma un nuevo commit.",
                "Se modifica el mensaje o contenido del último commit.",
                "Se crea una copia exacta del último commit.",
                "Se descartan los cambios en el área de preparación."],
    "answer": "b"},
    {"question": "¿Qué comando sube una rama específica al repositorio remoto?",
    "options": ["git push origin nombre-rama",
                "git commit origin nombre-rama",
                "git branch push nombre-rama",
                "git upload nombre-rama"],
    "answer": "a"},
    {"question": "¿Qué es Git y para qué se utiliza?",
    "options": ["Control de versiones",
                "Compilador de código",
                "Sistema de bases de datos",
                "Editor de texto"],
    "answer": "a"},
    {"question": "¿Cuáles son las principales ventajas de usar Git en proyectos de software?",
    "options": ["Permite colaboración en tiempo real",
                "Hace copias de seguridad automáticas",
                "Realiza pruebas de rendimiento",
                "Controla el historial de versiones"],
    "answer": "d"},
    {"question": "Explica la diferencia entre Git y GitHub.",
    "options": ["Git es un servicio en la nube, y GitHub es un sistema de control de versiones",
                "Git es un sistema de control de versiones, y GitHub es una plataforma para alojar repositorios",
                "Git es un repositorio, y GitHub es un tipo de código fuente",
                "Git es un lenguaje de programación, y GitHub es un repositorio local"],
    "answer": "b"},
    {"question": "¿Qué hace el comando `git init` y en qué momento se utiliza?",
    "options": ["Inicializa un repositorio vacío",
                "Inicia un archivo de configuración",
                "Revisa el historial de cambios",
                "Crea una rama nueva"],
    "answer": "a"},
    {"question": "¿Cómo se añaden archivos al área de preparación (staging area)?",
    "options": ["git commit",
                "git push",
                "git add",
                "git status"],
    "answer": "c"},
    {"question": "¿Qué comando se usa para guardar los cambios en el repositorio local?",
    "options": ["git log",
                "git commit",
                "git status",
                "git add"],
    "answer": "b"},
    {"question": "¿Cómo se visualiza el historial de cambios en un repositorio?",
    "options": ["git show",
                "git log",
                "git diff",
                "git status"],
    "answer": "b"},
    {"question": "¿Qué es una rama en Git y por qué es útil?",
    "options": ["Una herramienta para hacer copias de seguridad",
                "Una función para fusionar cambios",
                "Una línea de desarrollo independiente",
                "Un historial de commits"],
    "answer": "c"},
    {"question": "¿Cómo se crea una nueva rama en Git?",
    "options": ["git create branch",
                "git branch new",
                "git branch <nombre-rama>",
                "git switch <nombre-rama>"],
    "answer": "c"},
    {"question": "Explica cómo se cambian entre ramas existentes.",
    "options": ["git checkout <nombre-rama>",
                "git merge <nombre-rama>",
                "git switch <nombre-rama>",
                "Ambas opciones a y c"],
    "answer": "d"},
    {"question": "¿Qué comando se utiliza para cambiar el nombre de una rama en Git?",
    "options": ["git rename [nuevo-nombre]",
        "git branch -m [nuevo-nombre]",
        "git change [nuevo-nombre]",
        "git branch --rename [nuevo-nombre]"],
    "answer": "b"},
    {"question": "¿Qué sucede durante un `git merge` y cómo se resuelven los conflictos que puedan surgir?",
    "options": ["Git combina los cambios automáticamente sin intervención",
                "Git descarta cambios incompatibles sin avisar",
                "Git fusiona los cambios y puede requerir intervención manual en caso de conflicto",
                "Git solo fusiona si las ramas son idénticas"],
    "answer": "c"},
    {"question": "¿Qué sucede si intentas fusionar dos ramas con cambios incompatibles?",
    "options": ["Git genera un nuevo commit de conflicto",
                "Git reemplaza los archivos conflictivos",
                "Git elimina la rama",
                "Git deshace automáticamente los cambios"],
    "answer": "a"},
    {"question": "¿Qué es un mensaje de commit bien estructurado y por qué es importante?",
    "options": ["Describe detalladamente cada línea de código",
                "Explica los cambios realizados en el proyecto de manera clara y concisa",
                "Solo incluye fechas de modificación",
                "Describe solo el propósito de la rama"],
    "answer": "b"},
    {"question": "Explica el propósito de Conventional Commits y da ejemplos de etiquetas comunes como `:art:` y `:zap:`.",
    "options": ["Estandariza los mensajes de commit para mayor claridad en el historial",
                "Describe exclusivamente los errores en el código",
                "Usa una convención personalizada para el equipo",
                "No tiene ninguna utilidad"],
    "answer": "a"},
    {"question": "¿Qué pasos debes seguir para subir un repositorio local a GitHub por primera vez?",
    "options": ["git push origin master",
                "git init && git push",
                "git commit && git push",
                "git remote add origin <URL> && git push -u origin master"],
    "answer": "d"},
    {"question": "Explica el flujo básico de trabajo al colaborar con otros en un proyecto de GitHub.",
    "options": ["Clonar el repositorio, hacer cambios, crear un pull request",
                "Clonar el repositorio, subir cambios, realizar un push sin revisión",
                "Hacer commits y fusionarlos sin pasar por GitHub",
                "Hacer fork y esperar la revisión de los cambios"],
    "answer": "a"},
    {"question": "¿Qué es un Fork y cómo se utiliza en la colaboración?",
    "options": ["Es una copia del repositorio original para hacer cambios sin afectar al proyecto principal",
                "Es una rama dentro del mismo repositorio",
                "Es un tipo de merge que se realiza automáticamente",
                "Es una forma de respaldar el proyecto en GitHub"],
    "answer": "a"},
    {"question": "¿Cuál es la diferencia entre un Push y un Pull?",
    "options": ["Push es enviar cambios a un repositorio remoto, y Pull es obtener cambios desde el remoto",
                "Push es obtener cambios desde el remoto, y Pull es enviar cambios a un repositorio remoto",
                "Push es fusionar ramas locales, y Pull es hacer commits",
                "Ambos se refieren a operaciones locales de Git"],
    "answer": "a"},
    {"question": "¿Qué información debe incluir la sección de 'Título y Descripción' de un README?",
    "options": ["El nombre del autor y el año de creación",
                "Una breve descripción del proyecto, su propósito y objetivo",
                "Una lista de todos los comandos del proyecto",
                "Solo una descripción técnica del código"],
    "answer": "b"},
    {"question": "¿Qué función cumple una tabla de contenidos en un README?",
    "options": ["Mejorar el SEO del proyecto",
                "Facilitar la navegación dentro del archivo si es largo",
                "Incluir enlaces a otros repositorios",
                "Describir las dependencias del proyecto"],
    "answer": "b"},
    {"question": "¿Cómo se presentan las instrucciones de instalación en un README?",
    "options": ["Solo se coloca el enlace de descarga",
                "Se incluye un conjunto de comandos que permiten instalar y configurar el proyecto",
                "Solo se describen las dependencias",
                "Se añaden detalles sobre el código fuente"],
    "answer": "b"},
    {"question": "Da un ejemplo práctico de un comando que podría incluirse en una sección de instalación.",
    "options": ["git status",
                "sudo apt install <nombre-paquete>",
                "git branch",
                "git push"],
    "answer": "b"},
    {"question": "¿Por qué es importante mantener el archivo README actualizado?",
    "options": ["Para que el proyecto se vea atractivo",
                "Porque describe el estado del proyecto y ayuda a los colaboradores",
                "Para fines de seguridad",
                "Para cumplir con los requisitos de licencias"],
    "answer": "b"},
    {"question": "¿Qué pasos debes seguir para resolver un conflicto de fusión en Git?",
    "options": ["Editar los archivos en conflicto, marcar como resueltos, hacer commit",
                "Eliminar las ramas en conflicto",
                "Usar `git pull` para resolver automáticamente el conflicto",
                "Rehacer el commit sin los cambios en conflicto"],
    "answer": "a"},
    {"question": "Describe cómo organizarías un proyecto con varias ramas y commits incrementales.",
    "options": ["Mantener una rama principal y hacer commits en cada rama nueva según la funcionalidad",
                "Hacer todos los commits directamente en la rama principal",
                "Crear una rama por cada commit realizado",
                "Usar solo una rama para todas las funcionalidades del proyecto"],
    "answer": "a"},
    {"question": "Explica cómo utilizarías la herramienta de visualización `Git Graph` en Visual Studio Code.",
    "options": ["Para realizar un seguimiento visual de los commits y las ramas",
                "Para editar el código directamente",
                "Para hacer merge de ramas automáticamente",
                "Para eliminar ramas obsoletas"],
    "answer": "a"},
    {"question": "¿Qué beneficios aporta el uso de Markdown para crear un archivo README?",
    "options": ["Facilita la creación de texto formateado y la inclusión de enlaces y código",
                "Hace que el archivo sea más pesado",
                "Permite solo texto plano",
                "Limita el tipo de contenido que puedes agregar"],
    "answer": "a"},
        {"question": "¿Qué buenas prácticas recomendarías al documentar un proyecto en GitHub?",
    "options": ["Incluir un archivo README claro y detallado, y hacer commits descriptivos",
                "Usar comentarios solo en los archivos de código",
                "Evitar escribir detalles sobre el proyecto en el README",
                "Nunca usar GitHub para almacenar proyectos privados"],
    "answer": "a"},
    ]

# Mensajes decorativos
correct_msg = "¡Correcto!"
incorrect_msg = "Incorrecto. La respuesta correcta es: "

# Contador de aciertos
correct_answers = 0

print("\nBienvenido al cuestionario de validación de preguntas.\n")

for i, q in enumerate(questions, 1):
    print(f"{i}. {q['question']}")
    for index, option in enumerate(q["options"], start=97):  # 97 es el código ASCII para 'a'
        print(f"   {chr(index)}) {option}")
    answer = input("\nTu respuesta (a, b, c, d): ").lower()

    if answer == q["answer"]:
        print(correct_msg)
        correct_answers += 1
    else:
        print(f"{incorrect_msg}{q['answer']}.\n")
    print("-" * 50)

# Mostrar puntaje final
total_questions = len(questions)
percentage = (correct_answers / total_questions) * 100
print(f"\nHas completado el cuestionario.")
print(f"Puntaje final: {correct_answers} de {total_questions} ({percentage:.2f}%)")

# Mensaje según el puntaje
if percentage < 65:
    print("No eres de nadie.")
elif 65 <= percentage <= 79:
    print("Eres de Campus.")
else:
    print("Eres de Miguel.")