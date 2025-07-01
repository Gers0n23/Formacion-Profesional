extends Node2D

# Rutas de las escenas
@export var pasillo_exterior_scene: String = "res://Escenas/pasillo_exterior.tscn"
@export var exterior_scene: String = "res://Escenas/Exterior.tscn"

# Referencia al minijuego
@onready var minigame = $Pruebapresicion

func _ready():
	if minigame:
		print("Nodo Pruebapresicion encontrado.")
		
		# Verificar que las señales no estén conectadas previamente
		if not minigame.is_connected("game_won", Callable(self, "_on_pruebapresicion_game_won")):
			minigame.connect("game_won", Callable(self, "_on_pruebapresicion_game_won"))
		
		if not minigame.is_connected("game_lost", Callable(self, "_on_pruebapresicion_game_lost")):
			minigame.connect("game_lost", Callable(self, "_on_pruebapresicion_game_lost"))
	else:
		print("No se encontró el nodo Pruebapresicion.")

func _on_pruebapresicion_game_won():
	print("Prueba ganada. Avanzando al siguiente nivel.")
	if pasillo_exterior_scene != "":
		get_tree().change_scene_to_file(pasillo_exterior_scene)
	else:
		print("La ruta para 'pasillo_exterior_scene' no está configurada.")

func _on_pruebapresicion_game_lost():
	print("Prueba perdida. Volviendo a la escena exterior.")
	if exterior_scene != "":
		get_tree().change_scene_to_file(exterior_scene)
	else:
		print("La ruta para 'exterior_scene' no está configurada.")
