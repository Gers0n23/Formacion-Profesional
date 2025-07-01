extends Node

func _ready():
	var exterior_scene = preload("res://Escenas/Exterior.tscn")
	var lugar_interaccion_scene = preload("res://Escenas/lugar_interaccion.tscn")
	var porteria_scene = preload("res://Escenas/Porteria.tscn")
	
	if not exterior_scene or not lugar_interaccion_scene or not porteria_scene:
		print_error("No se pudieron cargar una o más escenas. Verifica las rutas y la integridad de los archivos.")
	else:
		print("Todas las escenas se han cargado correctamente.")
