extends Node2D

signal game_won
signal game_lost

@onready var progress_line = $ProgressLine
@onready var timer = $Timer
@onready var status_label = $StatusLabel
@onready var success_area = $SuccessArea  # Nodo de tipo Polygon2D para el área de éxito

var radius = 90  # Radio del círculo
var divisions = []  # Divisiones del círculo (en grados)
var target_index = 0  # Índice de la división seleccionada
var progress_angle = 0.0  # Ángulo de la línea de progreso
var success_range = 15  # Rango de éxito en grados
var attempts = 3  # Intentos restantes
var is_game_active = true
var speed_multiplier = 1.0  # Velocidad de rotación de la línea
var has_won_once = false  # Bandera para registrar una victoria

func _ready():
	# Inicializar juego
	generate_circle_divisions()
	select_random_target()
	timer.start()
	status_label.text = "Dale apura"
	
	# Asegurar conexión de señales
	connect_signals()

func connect_signals():
	if not is_connected("game_won", Callable(get_parent(), "_on_pruebapresicion_game_won")):
		connect("game_won", Callable(get_parent(), "_on_pruebapresicion_game_won"))
	if not is_connected("game_lost", Callable(get_parent(), "_on_pruebapresicion_game_lost")):
		connect("game_lost", Callable(get_parent(), "_on_pruebapresicion_game_lost"))

# Generar divisiones del círculo en pasos de 10 grados
func generate_circle_divisions():
	divisions.clear()
	for i in range(36):
		divisions.append(i * 10)

# Seleccionar aleatoriamente una división como zona de éxito
func select_random_target():
	target_index = randi() % divisions.size()
	update_success_area_position()

# Actualizar posición de la zona de éxito en el círculo
func update_success_area_position():
	var target_angle = divisions[target_index]
	var radians = deg_to_rad(target_angle)
	success_area.position = Vector2(radius * cos(radians), radius * sin(radians))
	success_area.rotation = radians

# Lógica principal del juego
func _process(delta):
	if is_game_active:
		# Actualizar rotación de la línea de progreso
		progress_angle += 90 * delta * speed_multiplier
		progress_angle = fmod(progress_angle, 360)  # Limitar el ángulo a [0, 360)
		progress_line.rotation = deg_to_rad(progress_angle)

		# Actualizar mensaje según la posición de la línea
		if is_line_in_success_area():
			status_label.text = "Ponele weno ahora!."
		else:
			status_label.text = "Espera que ta pegao."

# Detectar entrada del jugador
func _input(event):
	if is_game_active and event.is_action_pressed("ui_accept"):  # "ui_accept" corresponde a Space por defecto
		check_success()

# Verificar si el jugador acertó
func check_success():
	if is_line_in_success_area():
		status_label.text = "Pasa antes que me arrepienta"
		is_game_active = false
		has_won_once = true
		emit_signal("game_won")
	else:
		attempts -= 1
		if attempts > 0:
			speed_multiplier += 0.5  # Incrementar velocidad en cada intento fallido
			status_label.text = "Na, denuevo intenta, teni: %d" % attempts
			reset_game()
		else:
			status_label.text = "Me aburriste, pajuera!"
			is_game_active = false
			emit_signal("game_lost")

# Comprobar si la línea de progreso está en el área de éxito
func is_line_in_success_area() -> bool:
	var target_angle = divisions[target_index]
	var diff = abs(progress_angle - target_angle)
	diff = min(diff, 360 - diff)  # Manejar casos en que el ángulo cruza 0°
	return diff <= success_range

# Reiniciar el estado del juego tras un fallo
func reset_game():
	progress_angle = 0.0
	select_random_target()
	timer.start()
