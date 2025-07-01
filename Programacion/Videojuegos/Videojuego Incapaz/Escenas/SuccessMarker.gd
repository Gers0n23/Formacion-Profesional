extends Node2D

@onready var progress_line = $ProgressLine
@onready var target_zone = $TargetZone
@onready var timer = $Timer
@onready var status_label = $StatusLabel

var radius = 90  # Radio del círculo
var target_angle = 0  # Ángulo donde aparece el TargetZone
var progress_angle = 0  # Ángulo actual de la línea de progreso
var success_range = 0.05  # Rango de éxito (5% de 360 grados)
var is_game_active = true
var success_visual_range = 0.1  # Visualizar un rango mayor para ayudar a la referencia (10%)

func _ready():
	if target_zone:
		# Asegurarse de que el TargetZone esté correctamente inicializado
		target_zone.modulate = Color(1, 0, 0)  # Hacemos que el TargetZone sea rojo
		target_zone.scale = Vector2(0.3, 0.3)  # Ajusta el tamaño del TargetZone
	else:
		print("Error: No se encontró el nodo TargetZone en la escena.")

	# Generar un ángulo aleatorio para el TargetZone dentro del área de éxito
	target_angle = randf_range(0, 360)
	
	# Coloca el TargetZone en el borde del círculo
	update_target_position()

	# Inicia el temporizador para el juego
	timer.start(10.0)  # 10 segundos para ganar o perder

	# Crear el visual de la zona de éxito (esto es opcional para la referencia visual)
	create_success_range_visual()

func _process(delta):
	if is_game_active:
		# Rotar la línea de progreso
		progress_angle += 90 * delta  # Ajusta la velocidad de rotación según sea necesario
		if progress_angle >= 360:
			progress_angle = 0  # Mantener la rotación dentro de 360 grados

		# Actualizar la posición de la línea
		progress_line.rotation = deg_to_rad(progress_angle)

		# Verificar si la línea de progreso está dentro del área de éxito
		if is_line_in_success_area():
			status_label.text = "¡Presiona el botón! Estás dentro del área de éxito."

		# Mostrar estado si la línea pasa exactamente por el target
		if progress_angle == target_angle:
			status_label.text = "¡Ganas! Presiona ahora."

# Función para actualizar la posición del TargetZone dentro del área de éxito
func update_target_position():
	# Calcula un ángulo aleatorio dentro del área de éxito
	var random_angle = target_angle + randf_range(-success_range * 180, success_range * 180)
	# Convertir el ángulo a coordenadas X, Y
	var target_x = radius * cos(deg_to_rad(random_angle))
	var target_y = radius * sin(deg_to_rad(random_angle))
	
	# Actualiza la posición del TargetZone
	if target_zone:
		target_zone.position = Vector2(target_x, target_y)
	else:
		print("Error: No se encontró el nodo TargetZone para actualizar su posición.")

# Función para verificar si la línea está dentro del área de éxito
func is_line_in_success_area() -> bool:
	return abs(progress_angle - target_angle) < success_range * 360

# Función para detectar la presión del botón
func _input(event):
	if is_game_active and event.is_action_pressed("ui_accept"):  # "ui_accept" suele ser Space
		check_success()

# Función para verificar si la presión fue en el momento correcto
func check_success():
	if is_line_in_success_area():
		status_label.text = "¡Acceso concedido!"
		is_game_active = false
		emit_signal("game_won")
	else:
		status_label.text = "¡Fallaste! Vuelve a intentar."
		is_game_active = false
		emit_signal("game_lost")

# Crear el círculo visual que muestra el rango de éxito
# Crear el círculo visual que muestra el rango de éxito
func create_success_range_visual():
	var range_circle = CircleShape2D.new()  # Crea una nueva forma circular
	range_circle.radius = radius + success_range * radius  # Aumenta el radio para visualizar el rango de éxito
	var range_visual = Line2D.new()  # Usamos Line2D para visualizar el círculo
	range_visual.add_point(Vector2(0, 0))  # El centro del círculo
	range_visual.add_point(Vector2(range_circle.radius, 0))  # Un punto en el borde de la zona de éxito

	# Configuración de la visualización
	range_visual.width = 2  # Puedes hacer que el círculo visual sea más grueso si lo deseas
	range_visual.default_color = Color(0, 1, 0)  # Verde para indicar el rango de éxito
	add_child(range_visual)
