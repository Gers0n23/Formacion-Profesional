extends Area2D

# Variables configurables
@export var healing_amount: int = 20
@export var speed_boost: int = 800
@export var speed_duration: float = 5.0

# Estado interno
var is_active: bool = true
var original_speed: int
var player: Node = null

func _ready():
	# Conecta la señal solo si no está ya conectada
	if not is_connected("body_entered", Callable(self, "_on_body_entered")):
		connect("body_entered", Callable(self, "_on_body_entered"))

func _on_body_entered(body):
	if not is_active or not body.is_in_group("player"):
		return

	# Verifica si el jugador ya está en el grupo "HasEscort"
	if body.is_in_group("HasEscort"):
		return

	is_active = false
	player = body

	# Añadir al grupo temporal "HasEscort"
	player.add_to_group("HasEscort")

	# Reproducir el sonido
	$AudioStreamPlayer.play()

	# Aplicar efectos al jugador
	if player.health < 100:
		player.health = min(player.health + healing_amount, 100)

	original_speed = player.speed
	player.speed += speed_boost

	# Ocultar el ítem visualmente de forma diferida
	$Sprite2D.visible = false
	$CollisionShape2D.call_deferred("set_disabled", true)

	# Iniciar el temporizador
	$Timer.start(speed_duration)

func _on_timer_timeout():
	# Restaurar la velocidad del jugador
	if player:
		player.speed = original_speed
		player.remove_from_group("HasEscort")  # Sacar al jugador del grupo

	# Eliminar el nodo del ítem de forma diferida
	call_deferred("queue_free")
