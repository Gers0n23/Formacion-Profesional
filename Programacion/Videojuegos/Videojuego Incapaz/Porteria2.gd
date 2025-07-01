extends Node2D

signal minigame_completed
signal minigame_failed

@onready var minigame = PackedScene
@export var pasillo_exterior_scene: PackedScene
@export var exterior_scene: PackedScene

func _ready():
	# Obtener la instancia de "Pruebapresicion" desde la escena
	minigame = get_node("Pruebapresicion")
	
	# Conectar las señales del mini-juego a las funciones correspondientes
	minigame.connect("game_won", Callable(self, "_on_game_won"))
	minigame.connect("game_lost", Callable(self, "_on_game_lost"))

func _on_game_won():
	# Emitir la señal de que el mini-juego ha sido completado con éxito
	emit_signal("minigame_completed")
	# Cambiar a la escena "pasillo_exterior" si el jugador gana
	_change_scene(pasillo_exterior_scene)

func _on_game_lost():
	# Emitir la señal de que el mini-juego ha fallado
	emit_signal("minigame_failed")
	# Cambiar a la escena "Exterior" si el jugador pierde
	_change_scene(exterior_scene)

# Función para cambiar de escena
func _change_scene(scene: PackedScene):
	if scene:
		# Instanciar la nueva escena
		var scene_instance = scene.instantiate()
		if scene_instance:
			# Eliminar la escena actual antes de cambiar a la nueva
			get_tree().current_scene.queue_free()
			# Cambiar la escena actual a la nueva escena instanciada
			get_tree().current_scene = scene_instance
		else:
			push_error("No se pudo instanciar la escena.")
	else:
		push_error("Referencia a escena no válida.")
